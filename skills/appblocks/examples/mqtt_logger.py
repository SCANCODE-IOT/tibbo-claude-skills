#!/usr/bin/env python3
"""Пример приёмника MQTT для проекта examples/greenhouse_tpp3.json: телеметрия -> SQLite -> графики.
Не инструмент скилла (нужны paho-mqtt и matplotlib); см. references/mqtt.md §6.

Установка на ноутбук:
    1) брокер Mosquitto (mosquitto.org/download), в mosquitto.conf:  listener 1883  и  allow_anonymous true
    2) pip install paho-mqtt matplotlib

Запуск:
    python greenhouse_logger.py log            # слушать MQTT и писать в greenhouse.db
    python greenhouse_logger.py plot [часы]    # графики за последние N часов (по умолчанию 24) -> greenhouse.png
    python greenhouse_logger.py water1         # команда: порция полива грядки 1 (также water2, stop)

Контроллер публикует в greenhouse/tele строку вида
    soil1=41.2;soil2=38.0;light1=5200;...;fan=0
и в greenhouse/alarm - тревоги (no_water). Команды слушает в greenhouse/cmd.
"""
import sqlite3, sys, time
from datetime import datetime, timedelta

BROKER = "localhost"
DB = "greenhouse.db"
FIELDS = ["soil1", "soil2", "light1", "light2", "air_t", "air_h", "tank_empty", "bus_v", "current_a", "power_w",
          "energy_wh", "water_ml", "water1_today", "water2_today", "pump1", "pump2", "lamp1", "lamp2", "fan"]
# pump1/pump2 приходят как уровень линии реле #06 (активно по LOW): 0 = насос работает, 1 = стоит.
# В базу пишем понятное значение: 1 = работает.
INVERTED = {"pump1", "pump2"}


def db():
    con = sqlite3.connect(DB)
    con.execute("create table if not exists tele (ts text, %s)" % ", ".join(f + " real" for f in FIELDS))
    con.execute("create table if not exists events (ts text, topic text, payload text)")
    return con


def parse(payload: str) -> dict:
    """'a=1.5;b=2' -> {'a': 1.5, 'b': 2.0}; неизвестные ключи и мусор пропускаются."""
    out = {}
    for part in payload.split(";"):
        if "=" not in part:
            continue
        k, v = part.split("=", 1)
        k = k.strip()
        if k in FIELDS:
            try:
                out[k] = float(v)
                if k in INVERTED:
                    out[k] = 1.0 - out[k]
            except ValueError:
                pass
    return out


def save(con, topic: str, payload: str):
    ts = datetime.now().isoformat(timespec="seconds")
    if topic.endswith("/tele"):
        row = parse(payload)
        con.execute("insert into tele values (?, %s)" % ",".join("?" * len(FIELDS)),
                    [ts] + [row.get(f) for f in FIELDS])
    else:
        con.execute("insert into events values (?,?,?)", (ts, topic, payload))
    con.commit()


def run_logger():
    import paho.mqtt.client as mqtt
    con = db()

    def on_connect(c, userdata, flags, rc, *args):
        c.subscribe("greenhouse/#")
        print("подключено к брокеру, жду данные...")

    def on_message(c, userdata, msg):
        payload = msg.payload.decode("utf-8", "replace")
        if msg.topic.endswith("/cmd"):
            return
        save(con, msg.topic, payload)
        print(msg.topic, payload)

    try:
        c = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="greenhouse-logger")
    except AttributeError:  # paho-mqtt 1.x
        c = mqtt.Client(client_id="greenhouse-logger")
    c.on_connect, c.on_message = on_connect, on_message
    c.connect(BROKER, 1883, 60)
    c.loop_forever()


def send(cmd: str):
    import paho.mqtt.publish as publish
    publish.single("greenhouse/cmd", cmd, hostname=BROKER)
    print("отправлено:", cmd)


def plot(hours: float = 24):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    con = db()
    since = (datetime.now() - timedelta(hours=hours)).isoformat(timespec="seconds")
    rows = con.execute("select ts, %s from tele where ts >= ? order by ts" % ",".join(FIELDS), (since,)).fetchall()
    if not rows:
        print("нет данных за период")
        return
    t = [datetime.fromisoformat(r[0]) for r in rows]
    col = {f: [r[i + 1] for r in rows] for i, f in enumerate(FIELDS)}
    fig, ax = plt.subplots(4, 1, figsize=(11, 11), sharex=True)
    ax[0].plot(t, col["soil1"], label="почва, грядка 1, %")
    ax[0].plot(t, col["soil2"], label="почва, грядка 2, %")
    ax[1].plot(t, col["air_t"], label="воздух, °C", color="tab:red")
    ax1b = ax[1].twinx()
    ax[1].plot(t, col["air_h"], label="влажность воздуха, %", color="tab:cyan")
    ax1b.plot(t, col["light1"], label="свет 1, лк", color="tab:olive", alpha=.6)
    ax1b.plot(t, col["light2"], label="свет 2, лк", color="tab:green", alpha=.6)
    ax[2].plot(t, col["current_a"], label="ток нагрузок, А", color="tab:purple")
    ax2b = ax[2].twinx()
    ax2b.plot(t, col["energy_wh"], label="энергия, Вт·ч", color="tab:gray")
    ax[3].plot(t, col["water_ml"], label="вода (по времени работы насосов), мл", color="tab:blue")
    for a in list(ax) + [ax1b, ax2b]:
        a.legend(loc="upper left", fontsize=8)
    for a in ax:
        a.grid(alpha=.3)
    fig.suptitle("Умная теплица: последние %g ч" % hours)
    fig.tight_layout()
    fig.savefig("greenhouse.png", dpi=110)
    print("сохранено greenhouse.png,", len(rows), "точек")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "log"
    if cmd == "log":
        run_logger()
    elif cmd == "plot":
        plot(float(sys.argv[2]) if len(sys.argv) > 2 else 24)
    elif cmd in ("water1", "water2", "stop"):
        send(cmd)
    else:
        print(__doc__)
