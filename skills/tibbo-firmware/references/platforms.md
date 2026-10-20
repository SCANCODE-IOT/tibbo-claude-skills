# Tibbo platforms (auto-extracted from github.com/tibbotech/platforms)

Each platform = one TIDE target. `Object headers` shows which TiOS objects exist on it (see tios-api.md).
I/O line, serial port, ADC enums below are exact constant names for that platform.

| Folder | Description | PLATFORM_ID | ROM | RAM | Objects | Firmware in repo |
|---|---|---|---|---|---|---|
| DS1100 | DS1100 Device | 17 | 327680 | 17920 | io-5xx net pppoe sys-5xx | tios-ds1100-3_60_06.bin |
| DS1101N | DS1101 Device + WA2000 Wi-Fi add-on | 38 | 983040 | 22271 | beep fd io-1xxx lcd net pppoe rtc sys-1xxx wln | tios-ds1101n-3_70_02.bin |
| DS1101W | DS1101 Device + GA1000 Wi-Fi add-on | 18 | 983040 | 22271 | beep fd io-1xxx lcd net pppoe rtc sys-1xxx wln | tios-ds1101w-3_60_06.bin |
| DS1101W2 | DS1101 Device + GA1000 Wi-Fi add-on | 31 | 983040 | 22271 | beep fd io-1xxx lcd net pppoe rtc sys-1xxx wln | tios-ds1101w-3_60_06.bin |
| DS1102N | DS1102 Device + WA2000 Wi-Fi add-on | 39 | 983040 | 22271 | beep fd io-1xxx lcd net pppoe rtc ssi sys-1xxx wln | tios-ds1102n-3_70_02.bin |
| DS1102W | DS1102 Device + GA1000 Wi-Fi add-on | 16 | 983040 | 22271 | beep fd io-1xxx lcd net pppoe rtc ssi sys-1xxx wln | tios-ds1102w-3_60_06.bin |
| DS1202 | DS1202 Device | 5 | 983040 | 22271 | fd io-1xxx net pppoe sys-1xxx | tios-ds1202-3_60_06.bin |
| DS1206 | DS1206 Device | 3 | 983040 | 22271 | fd io-1xxx net pppoe sys-1xxx | tios-ds1206-3_60_06.bin |
| EM1000 | EM1000 Module | 0 | 983040 | 22271 | gen-em1000 | tios-em1000-3_60_06.bin |
| EM1000N | EM1000 Module + WA2000 Wi-Fi add-on | 34 | 983040 | 22271 | gen-em1000 wln | tios-em1000n-3_70_02.bin |
| EM1000W | EM1000 Module + GA1000 Wi-Fi add-on | 11 | 983040 | 22271 | gen-em1000 wln | tios-em1000w-3_60_06.bin |
| EM1001N | EM1001 Module + WA2000 Wi-Fi add-on | 35 | 3080192 | 22271 | beep fd io-1xxx kp lcd net pppoe rtc ssi sys-1xxx wln | tios-em1001n-3_70_02.bin |
| EM1001W | EM1001 Module + GA1000 Wi-Fi add-on | 23 | 3080192 | 22271 | beep fd io-1xxx kp lcd net pppoe rtc ssi sys-1xxx wln | tios-em1001w-3_60_06.bin |
| EM1202 | EM1202 Module | 1 | 983040 | 22271 | gen-em1202 | tios-em1202-3_60_06.bin |
| EM1202N | EM1202 Module + WA2000 Wi-Fi add-on | 36 | 983040 | 22271 | gen-em1202 wln | tios-em1202N-3_70_02.bin |
| EM1202W | EM1202 Module + GA1000 Wi-Fi add-on | 12 | 983040 | 22271 | gen-em1202 wln | tios-em1202w-3_60_06.bin |
| EM1206 | EM1206 Module | 4 | 983040 | 22271 | gen-em1206 | tios-em1206-3_60_06.bin |
| EM1206N | EM1206 Module + WA2000 Wi-Fi add-on | 37 | 983040 | 22271 | gen-em1206 wln | tios-em1206n-3_70_02.bin |
| EM1206W | EM1206 Module + GA1000 Wi-Fi add-on | 13 | 983040 | 22271 | gen-em1206 wln | tios-em1206w-3_60_06.bin |
| EM2000W | EM2000 Module | 24 | 786432 | 66816 | adc beep bt fd i2c io-1xxx kp lcd net pppoe rtc ssi sys-2xxx tls wln | tios-em2000w-4_02_02.bin |
| EM3000W | EM3000 Module | 49 | 1310720 | 132352 | adc beep bt em3000w_sock fd i2c io-2xxx kp lcd net pppoe rtc ssi sys-2xxx tls wln | tios-em3000w-4_01_08.bin |
| EM500W | EM500 Module + GA1000 Wi-Fi add-on | 15 | 327680 | 17920 | fd io-5xx net pppoe sys-5xx wln | tios-em500w-3_60_08.bin |
| EM510W | EM510 Module | 43 | 262144 | 16128 | bt fd io-5xx net pppoe ssi sys-5xx wln | tios-EM510W-3_80_26.bin |
| KLM106_32 | KLM106 platform | 33 | 786432 | 86784 | bt gen-st tls wln | tios-klm106-4_00_01.bin |
| KLM601 | KLM601 platform | 7 | 983040 | 21760 | gen-t1000 wln | tios-klm601-3_60_00.bin |
| KLM601_32 | KLM601 platform | 27 | 786432 | 86784 | bt gen-st tls wln | tios-klm601-4_00_01.bin |
| LKLM601 | LKLM601 Board | 32 | 983040 | 86784 | beep button constants defines fd io io-1xxx kp lcd lfd lsock net pat romfile rtc ser sock ssi stor sys sys-linux syscalls wln |  |
| LTPP3 | LTPP3 Board | 29 | 983040 | 86784 | beep button constants defines fd io io-1xxx lfd lsock net pat ppp romfile rtc ser sock ssi stor sys sys-linux syscalls wln |  |
| NB1010 | NB1010 Board | 9 | 983040 | 22271 | gen-nb1010 | tios-nb1010-3_60_06.bin |
| NB1010N | NB1010N Board | 10 | 983040 | 22271 | gen-nb1010 wln | tios-nb1010n-3_70_02.bin |
| NB1010W | NB1010W Board | 10 | 983040 | 22271 | gen-nb1010 wln | tios-nb1010w-3_60_06.bin |
| SIMULATOR | TiOS Simulator | 28 | 983040 | 86784 | beep button constants defines fd kp lcd net pat romfile rtc sock stor sys sys-2xxx syscalls |  |
| SPACE_AGE | Space Age controller | 30 | 786432 | 66816 | beep fd io-1xxx kp lcd pppoe rtc sled ssi sys-2xxx wln |  |
| T1000W | T1000 IC + GA1000 Wi-Fi add-on | 6 | 983040 | 21760 | gen-t1000 wln | tios-t1000w-3_60_00.bin |
| TPP2N | TPP2 Board + WA2000 Wi-Fi add-on | 40 | 983040 | 22271 | beep fd io-1xxx kp lcd net pppoe rtc ssi sys-1xxx wln | tios-tpp2n-3_70_02.bin |
| TPP2W | TPP2 Board | 19 | 983040 | 22271 | beep fd io-1xxx kp lcd net pppoe rtc ssi sys-1xxx wln | tios-tpp2w-3_60_06.bin |
| TPP2W(G2) | TPP2(G2) Board | 25 | 786432 | 66816 | beep bt fd i2c io-2xxx kp lcd net pppoe rtc ssi sys-2xxx tls wln | tios-tpp2w(g2)-4_02_02.bin |
| TPP2W(G3) | TPP2(G3) Board | 48 | 1310720 | 132352 | adc beep bt fd i2c io-2xxx kp lcd net pppoe rtc ssi sys-2xxx tls tpp2w(g3)_sock tpp2w(g3)_sys wln | tios-tpp2w(g3)-5_00_00.bin |
| TPP3N | TPP3 Board + WA2000 Wi-Fi add on | 41 | 983040 | 22271 | beep fd io-1xxx kp lcd net pppoe rtc ssi sys-1xxx wln | tios-tpp3n-3_70_02.bin |
| TPP3W | TPP3 Board | 20 | 983040 | 22271 | beep fd io-1xxx kp lcd net pppoe rtc ssi sys-1xxx wln | tios-tpp3w-3_60_06.bin |
| TPP3W(G2) | TPP3(G2) Board | 26 | 786432 | 66816 | adc beep bt fd i2c io-2xxx kp net pppoe rtc ssi sys-2xxx tls wln | tios-tpp3w(g2)-4_02_02.bin |
| TPP3W(G3) | TPP3(G3) Board | 47 | 1310720 | 132352 | adc beep bt fd i2c io-2xxx kp net pppoe rtc ssi sys-2xxx tls tpp3w(g3)_sock wln | tios-tpp3w(g3)-4_01_08.bin |
| WM2000 | WM2000 Module | 44 | 1728512 | 59392 | adc beep bt dhcp fd io-1xxx kp pwm rtc ssi sys-2xxx tls wln wm2000_ser wm2000_sock wm2000_sys wm2000_wln | tios-wm2000-4_03_08.bin |
| WS1101 | WS1101 | 45 | 1728512 | 59392 | beep bt dhcp fd io-1xxx rtc ssi sys-2xxx tls wln ws1101_ser ws1101_sys ws1101_wln |  |
| WS1102 | WS1102 | 46 | 1728512 | 59392 | beep bt dhcp fd io-1xxx rtc ssi sys-2xxx tls wln ws1102_ser ws1102_sys ws1102_wln | tios-ws1102-4_03_08.bin |
| em203 | EM203 Module |  | 63488 | 20480 |  | tios-em202-2_05_12.bin |


## Символы PLATFORM_ID (Platforms/defines.tph)

В коде сравнивай с символом, а не с числом: `#if PLATFORM_ID=TPP2WG2 ... #elif PLATFORM_ID=TPP3WG2 ... #else #error ... #endif`.
Символ — имя папки без скобок: `TPP2W(G2)` → `TPP2WG2`, `TPP3W(G3)` → `TPP3WG3`.

| Символ | PLATFORM_ID |
|---|---|
| `EM1000` | 0 |
| `EM1202` | 1 |
| `EM110` | 2 |
| `DS1206` | 3 |
| `EM1206` | 4 |
| `DS1202` | 5 |
| `T1000W` | 6 |
| `KLM601` | 7 |
| `NB1010` | 9 |
| `NB1010W` | 10 |
| `EM1000W` | 11 |
| `EM1202W` | 12 |
| `EM1206W` | 13 |
| `EM202` | 14 |
| `EM500W` | 15 |
| `DS1102W` | 16 |
| `DS1100` | 17 |
| `DS1101W` | 18 |
| `TPP2W` | 19 |
| `TPP3W` | 20 |
| `EM1001` | 22 |
| `EM1001W` | 23 |
| `EM2000W` | 24 |
| `TPP2WG2` | 25 |
| `TPP3WG2` | 26 |
| `KLM601_32` | 27 |
| `SIMULATOR` | 28 |
| `LTPP3` | 29 |
| `SPACE_AGE` | 30 |
| `DS1101W2` | 31 |
| `LKLM601` | 32 |
| `KLM106_32` | 33 |
| `EM1000N` | 34 |
| `EM1001N` | 35 |
| `EM1202N` | 36 |
| `EM1206N` | 37 |
| `DS1101N` | 38 |
| `DS1102N` | 39 |
| `TPP2N` | 40 |
| `TPP3N` | 41 |
| `NB1010N` | 42 |
| `EM510W` | 43 |
| `WM2000` | 44 |
| `WS1101` | 45 |
| `WS1102` | 46 |
| `TPP3WG3` | 47 |
| `TPP2WG3` | 48 |
| `EM3000W` | 49 |
| `KP_DISABLED` | 0 |
| `KP_ENABLED` | 1 |
| `FD_DISABLED` | 0 |
| `FD_ENABLED` | 1 |
| `WLN_DISABLED` | 0 |
| `WLN_ENABLED` | 1 |

## DS1100 — DS1100 Device

- PLATFORM_ID: 17; rom=327680 ram=17920; firmware file(s): tios-ds1100-3_60_06.bin
- Object headers included: gen, sys-5xx, net, pppoe, io-5xx
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0_CTS_INT0 — General-purpose I/O line 0 (P0.0), also the CTS input of the serial port and the interrupt line 0.
- PL_IO_NUM_1_DSR_INT1 — General-purpose I/O line 1 (P0.1), also the DSR input of the serial port and the interrupt line 1.
- PL_IO_NUM_2_RTS — General-purpose I/O line 2 (P0.2), also the RTS output of the serial port.
- PL_IO_NUM_3_DTR — General-purpose I/O line 3 (P0.3), also the DTR output of the serial port.
- PL_IO_NUM_4_DCD — General-purpose I/O line 4 (P0.4), also the DCD input of the serial port.
- PL_IO_NUM_5_EMPTY — Not implemented.
- PL_IO_NUM_6_EMPTY — Not implemented.
- PL_IO_NUM_7_EMPTY — Not implemented.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7. Lines 5-7 are not implemented.

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 0, which serves as the CTS input of the serial port).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 1, which serves as the DSR input of the serial port).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## DS1101N — DS1101 Device + WA2000 Wi-Fi add-on

- PLATFORM_ID: 38; rom=983040 ram=22271; firmware file(s): tios-ds1101n-3_70_02.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, fd, beep, rtc, lcd, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_io_num`:
- PL_IO_NUM_0_RX0_INT0 — General-purpose I/O line 0 (P0.0), also the RX/W1in/din input of the serial port 0 and the interrupt line 0. When this serial port is in the UART mode…
- PL_IO_NUM_1_TX0_INT1 — General-purpose I/O line 1 (P0.1), also the TX/W1out/dout output of the serial port 0 and the interrupt line 1. When this serial port is in the UART m…
- PL_IO_NUM_2_RX1_INT2 — General-purpose I/O line 2 (P0.2), also the RX/W1in/din input of the serial port 1 and the interrupt line 2. When this serial port is in the UART mode…
- PL_IO_NUM_3_TX1_INT3 — General-purpose I/O line 3 (P0.3), also the TX/W1out/dout output of the serial port 1 and the interrupt line 3. When this serial port is in the UART m…
- PL_IO_NUM_4_RX2_INT4 — General-purpose I/O line 4 (P0.4), also the RX/W1in/din input of the serial port 2 and the interrupt line 4. When this serial port is in the UART mode…
- PL_IO_NUM_5_TX2_INT5 — General-purpose I/O line 5 (P0.5), also the TX/W1out/dout output of the serial port 2 and the interrupt line 5. When this serial port is in the UART m…
- PL_IO_NUM_6_RX3_INT6 — General-purpose I/O line 6 (P0.6), also the RX/W1in/din input of the serial port 3 and the interrupt line 6. When this serial port is in the UART mode…
- PL_IO_NUM_7_TX3_INT7 — Not implemented.
- PL_IO_NUM_8_PWROUT — Controls the power output on pin 9 of the DB9M connector. Power will be ON when this output is enabled (io.enabled= 1- YES) and set to LOW (io.state= …
- PL_IO_NUM_9 — Pin 8 on the wireless interface connector.
- PL_IO_NUM_10 — Pin 6 on the wireless interface connector.
- PL_IO_NUM_11 — The RST line of the wireless interface.
- PL_IO_NUM_12 — The DI line of the wireless interface.
- PL_IO_NUM_13 — The DO line of the wireless interface.
- PL_IO_NUM_14 — The CLK line of the wireless interface.
- PL_IO_NUM_15 — The CS line of the wireless interface.
- PL_IO_NUM_16 — Pin 9 on the wireless interface connector.
- PL_IO_NUM_17_EMPTY — Not implemented.
- PL_IO_NUM_18_EMPTY — Not implemented.
- PL_IO_NUM_19_SB1 — LED bar, LED#1 (the "weakest signal" LED).
- PL_IO_NUM_20_SB2 — LED bar, LED#2.
- PL_IO_NUM_21_SB3 — LED bar, LED#3.
- PL_IO_NUM_22_SB4 — LED bar, LED#4.
- PL_IO_NUM_23_SB5 — LED bar, LED#5 (the "strongest signal" LED).
- PL_IO_NUM_24_OLED_D0 — OLED dispay data bus, line 0 (P0.0).
- PL_IO_NUM_25_OLED_D1 — OLED dispay data bus, line 1 (P0.1).
- PL_IO_NUM_26_OLED_D2 — OLED dispay data bus, line 2 (P0.2).
- PL_IO_NUM_27_OLED_D3 — OLED dispay data bus, line 3 (P0.3).
- PL_IO_NUM_28_OLED_D4 — OLED dispay data bus, line 4 (P0.4).
- PL_IO_NUM_29_OLED_D5 — OLED dispay data bus, line 5 (P0.5).
- PL_IO_NUM_30_OLED_D6 — OLED dispay data bus, line 6 (P0.6).
- PL_IO_NUM_31_OLED_D7 — OLED dispay data bus, line 7 (P0.7).
- PL_IO_NUM_32_OLED_CS — OLED display, CS control line.
- PL_IO_NUM_33_OLED_RD — OLED display, RD control line.
- PL_IO_NUM_34_OLED_WR — OLED display, WR control line.
- PL_IO_NUM_35_OLED_DC — OLED display, DC control line.
- PL_IO_NUM_36_OLED_RST — OLED display, RST control line.
- PL_IO_NUM_37_CO — General-purpose I/O line 23 (does not belong to any 8-bit port), also a square wave output controlled by the beep object. This output is driving a buz…
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (the data bus of the OLED display).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 0).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 1).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 2).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 3).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 4).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 5).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 6).
- PL_INT_NUM_7 — Not implemented.
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## DS1101W — DS1101 Device + GA1000 Wi-Fi add-on

- PLATFORM_ID: 18; rom=983040 ram=22271; firmware file(s): tios-ds1101w-3_60_06.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, fd, beep, rtc, lcd, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_io_num`:
- PL_IO_NUM_0_RX0_INT0 — General-purpose I/O line 0 (P0.0), also the RX/W1in/din input of the serial port 0 and the interrupt line 0. When this serial port is in the UART mode…
- PL_IO_NUM_1_TX0_INT1 — General-purpose I/O line 1 (P0.1), also the TX/W1out/dout output of the serial port 0 and the interrupt line 1. When this serial port is in the UART m…
- PL_IO_NUM_2_RX1_INT2 — General-purpose I/O line 2 (P0.2), also the RX/W1in/din input of the serial port 1 and the interrupt line 2. When this serial port is in the UART mode…
- PL_IO_NUM_3_TX1_INT3 — General-purpose I/O line 3 (P0.3), also the TX/W1out/dout output of the serial port 1 and the interrupt line 3. When this serial port is in the UART m…
- PL_IO_NUM_4_RX2_INT4 — General-purpose I/O line 4 (P0.4), also the RX/W1in/din input of the serial port 2 and the interrupt line 4. When this serial port is in the UART mode…
- PL_IO_NUM_5_TX2_INT5 — General-purpose I/O line 5 (P0.5), also the TX/W1out/dout output of the serial port 2 and the interrupt line 5. When this serial port is in the UART m…
- PL_IO_NUM_6_RX3_INT6 — General-purpose I/O line 6 (P0.6), also the RX/W1in/din input of the serial port 3 and the interrupt line 6. When this serial port is in the UART mode…
- PL_IO_NUM_7_TX3_INT7 — Not implemented.
- PL_IO_NUM_8_PWROUT — Controls the power output on pin 9 of the DB9M connector. Power will be ON when this output is enabled (io.enabled= 1- YES) and set to LOW (io.state= …
- PL_IO_NUM_9 — Pin 8 on the wireless interface connector.
- PL_IO_NUM_10 — Pin 6 on the wireless interface connector.
- PL_IO_NUM_11 — The RST line of the wireless interface.
- PL_IO_NUM_12 — The DI line of the wireless interface.
- PL_IO_NUM_13 — The DO line of the wireless interface.
- PL_IO_NUM_14 — The CLK line of the wireless interface.
- PL_IO_NUM_15 — The CS line of the wireless interface.
- PL_IO_NUM_16 — Pin 9 on the wireless interface connector.
- PL_IO_NUM_17_EMPTY — Not implemented.
- PL_IO_NUM_18_EMPTY — Not implemented.
- PL_IO_NUM_19_SB1 — LED bar, LED#1 (the "weakest signal" LED).
- PL_IO_NUM_20_SB2 — LED bar, LED#2.
- PL_IO_NUM_21_SB3 — LED bar, LED#3.
- PL_IO_NUM_22_SB4 — LED bar, LED#4.
- PL_IO_NUM_23_SB5 — LED bar, LED#5 (the "strongest signal" LED).
- PL_IO_NUM_24_OLED_D0 — OLED dispay data bus, line 0 (P0.0).
- PL_IO_NUM_25_OLED_D1 — OLED dispay data bus, line 1 (P0.1).
- PL_IO_NUM_26_OLED_D2 — OLED dispay data bus, line 2 (P0.2).
- PL_IO_NUM_27_OLED_D3 — OLED dispay data bus, line 3 (P0.3).
- PL_IO_NUM_28_OLED_D4 — OLED dispay data bus, line 4 (P0.4).
- PL_IO_NUM_29_OLED_D5 — OLED dispay data bus, line 5 (P0.5).
- PL_IO_NUM_30_OLED_D6 — OLED dispay data bus, line 6 (P0.6).
- PL_IO_NUM_31_OLED_D7 — OLED dispay data bus, line 7 (P0.7).
- PL_IO_NUM_32_OLED_CS — OLED display, CS control line.
- PL_IO_NUM_33_OLED_RD — OLED display, RD control line.
- PL_IO_NUM_34_OLED_WR — OLED display, WR control line.
- PL_IO_NUM_35_OLED_DC — OLED display, DC control line.
- PL_IO_NUM_36_OLED_RST — OLED display, RST control line.
- PL_IO_NUM_37_CO — General-purpose I/O line 23 (does not belong to any 8-bit port), also a square wave output controlled by the beep object. This output is driving a buz…
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (the data bus of the OLED display).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 0).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 1).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 2).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 3).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 4).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 5).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 6).
- PL_INT_NUM_7 — Not implemented.
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## DS1101W2 — DS1101 Device + GA1000 Wi-Fi add-on

- PLATFORM_ID: 31; rom=983040 ram=22271; firmware file(s): tios-ds1101w-3_60_06.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, fd, beep, rtc, lcd, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_io_num`:
- PL_IO_NUM_0_RX0_INT0 — General-purpose I/O line 0 (P0.0), also the RX/W1in/din input of the serial port 0 and the interrupt line 0. When this serial port is in the UART mode…
- PL_IO_NUM_1_TX0_INT1 — General-purpose I/O line 1 (P0.1), also the TX/W1out/dout output of the serial port 0 and the interrupt line 1. When this serial port is in the UART m…
- PL_IO_NUM_2_RX1_INT2 — General-purpose I/O line 2 (P0.2), also the RX/W1in/din input of the serial port 1 and the interrupt line 2. When this serial port is in the UART mode…
- PL_IO_NUM_3_TX1_INT3 — General-purpose I/O line 3 (P0.3), also the TX/W1out/dout output of the serial port 1 and the interrupt line 3. When this serial port is in the UART m…
- PL_IO_NUM_4_RX2_INT4 — General-purpose I/O line 4 (P0.4), also the RX/W1in/din input of the serial port 2 and the interrupt line 4. When this serial port is in the UART mode…
- PL_IO_NUM_5_TX2_INT5 — General-purpose I/O line 5 (P0.5), also the TX/W1out/dout output of the serial port 2 and the interrupt line 5. When this serial port is in the UART m…
- PL_IO_NUM_6_RX3_INT6 — General-purpose I/O line 6 (P0.6), also the RX/W1in/din input of the serial port 3 and the interrupt line 6. When this serial port is in the UART mode…
- PL_IO_NUM_7_TX3_INT7 — Not implemented.
- PL_IO_NUM_8_PWROUT — Controls the power output on pin 9 of the DB9M connector. Power will be ON when this output is enabled (io.enabled= 1- YES) and set to LOW (io.state= …
- PL_IO_NUM_9 — Pin 8 on the wireless interface connector.
- PL_IO_NUM_10 — Pin 6 on the wireless interface connector.
- PL_IO_NUM_11 — The RST line of the wireless interface.
- PL_IO_NUM_12 — The DI line of the wireless interface.
- PL_IO_NUM_13 — The DO line of the wireless interface.
- PL_IO_NUM_14 — The CLK line of the wireless interface.
- PL_IO_NUM_15 — The CS line of the wireless interface.
- PL_IO_NUM_16 — Pin 9 on the wireless interface connector.
- PL_IO_NUM_17_EMPTY — Not implemented.
- PL_IO_NUM_18_EMPTY — Not implemented.
- PL_IO_NUM_19_SB1 — LED bar, LED#1 (the "weakest signal" LED).
- PL_IO_NUM_20_SB2 — LED bar, LED#2.
- PL_IO_NUM_21_SB3 — LED bar, LED#3.
- PL_IO_NUM_22_SB4 — LED bar, LED#4.
- PL_IO_NUM_23_SB5 — LED bar, LED#5 (the "strongest signal" LED).
- PL_IO_NUM_24_OLED_D0 — OLED dispay data bus, line 0 (P0.0).
- PL_IO_NUM_25_OLED_D1 — OLED dispay data bus, line 1 (P0.1).
- PL_IO_NUM_26_OLED_D2 — OLED dispay data bus, line 2 (P0.2).
- PL_IO_NUM_27_OLED_D3 — OLED dispay data bus, line 3 (P0.3).
- PL_IO_NUM_28_OLED_D4 — OLED dispay data bus, line 4 (P0.4).
- PL_IO_NUM_29_OLED_D5 — OLED dispay data bus, line 5 (P0.5).
- PL_IO_NUM_30_OLED_D6 — OLED dispay data bus, line 6 (P0.6).
- PL_IO_NUM_31_OLED_D7 — OLED dispay data bus, line 7 (P0.7).
- PL_IO_NUM_32_OLED_CS — OLED display, CS control line.
- PL_IO_NUM_33_OLED_RD — OLED display, RD control line.
- PL_IO_NUM_34_OLED_WR — OLED display, WR control line.
- PL_IO_NUM_35_OLED_DC — OLED display, DC control line.
- PL_IO_NUM_36_OLED_RST — OLED display, RST control line.
- PL_IO_NUM_37_CO — General-purpose I/O line 23 (does not belong to any 8-bit port), also a square wave output controlled by the beep object. This output is driving a buz…
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (the data bus of the OLED display).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 0).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 1).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 2).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 3).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 4).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 5).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 6).
- PL_INT_NUM_7 — Not implemented.
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## DS1102N — DS1102 Device + WA2000 Wi-Fi add-on

- PLATFORM_ID: 39; rom=983040 ram=22271; firmware file(s): tios-ds1102n-3_70_02.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, fd, beep, rtc, wln, lcd, ssi
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_io_num`:
- PL_IO_NUM_0_RX0_INT0 — General-purpose I/O line 0 (P0.0), also the RX/W1in/din input of the serial port 0 and the interrupt line 0. When this serial port is in the UART mode…
- PL_IO_NUM_1_TX0_INT1 — General-purpose I/O line 1 (P0.1), also the TX/W1out/dout output of the serial port 0 and the interrupt line 1. When this serial port is in the UART m…
- PL_IO_NUM_2_RX1_INT2 — General-purpose I/O line 2 (P0.2), also the RX/W1in/din input of the serial port 1 and the interrupt line 2. When this serial port is in the UART mode…
- PL_IO_NUM_3_TX1_INT3 — General-purpose I/O line 3 (P0.3), also the TX/W1out/dout output of the serial port 1 and the interrupt line 3. When this serial port is in the UART m…
- PL_IO_NUM_4_RX2_INT4 — General-purpose I/O line 4 (P0.4), also the RX/W1in/din input of the serial port 2 and the interrupt line 4. When this serial port is in the UART mode…
- PL_IO_NUM_5_TX2_INT5 — General-purpose I/O line 5 (P0.5), also the TX/W1out/dout output of the serial port 2 and the interrupt line 5. When this serial port is in the UART m…
- PL_IO_NUM_6_RX3_INT6 — Not implemented.
- PL_IO_NUM_7_TX3_INT7 — Not implemented.
- PL_IO_NUM_8 — Not implemented.
- PL_IO_NUM_9 — Pin 8 on the wireless interface connector.
- PL_IO_NUM_10 — Pin 6 on the wireless interface connector.
- PL_IO_NUM_11 — The RST line of the wireless interface.
- PL_IO_NUM_12 — The DI line of the wireless interface.
- PL_IO_NUM_13 — The DO line of the wireless interface.
- PL_IO_NUM_14 — The CLK line of the wireless interface.
- PL_IO_NUM_15 — The CS line of the wireless interface.
- PL_IO_NUM_16 — Pin 9 on the wireless interface connector.
- PL_IO_NUM_17_RSMD — Serial port mode: HIGH for RS422/485, LOW for RS232.
- PL_IO_NUM_18_HDFD — Serial port mode: HIGH for full-duplex, LOW for half-duplex.
- PL_IO_NUM_19_SB1 — LED bar, LED#1 (the "weakest signal" LED).
- PL_IO_NUM_20_SB2 — LED bar, LED#2.
- PL_IO_NUM_21_SB3 — LED bar, LED#3.
- PL_IO_NUM_22_SB4 — LED bar, LED#4.
- PL_IO_NUM_23_SB5 — LED bar, LED#5 (the "strongest signal" LED).
- PL_IO_NUM_24_OLED_D0 — OLED dispay data bus, line 0 (P0.0).
- PL_IO_NUM_25_OLED_D1 — OLED dispay data bus, line 1 (P0.1).
- PL_IO_NUM_26_OLED_D2 — OLED dispay data bus, line 2 (P0.2).
- PL_IO_NUM_27_OLED_D3 — OLED dispay data bus, line 3 (P0.3).
- PL_IO_NUM_28_OLED_D4 — OLED dispay data bus, line 4 (P0.4).
- PL_IO_NUM_29_OLED_D5 — OLED dispay data bus, line 5 (P0.5).
- PL_IO_NUM_30_OLED_D6 — OLED dispay data bus, line 6 (P0.6).
- PL_IO_NUM_31_OLED_D7 — OLED dispay data bus, line 7 (P0.7).
- PL_IO_NUM_32_OLED_CS — OLED display, CS control line.
- PL_IO_NUM_33_OLED_RD — OLED display, RD control line.
- PL_IO_NUM_34_OLED_WR — OLED display, WR control line.
- PL_IO_NUM_35_OLED_DC — OLED display, DC control line.
- PL_IO_NUM_36_OLED_RST — OLED display, RST control line.
- PL_IO_NUM_37_CO — General-purpose I/O line 37 (does not belong to any 8-bit port), also a square wave output controlled by the beep object. This output is driving a buz…
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (the data bus of the OLED display).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 0).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 1).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 2).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 3).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 4).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 5).
- PL_INT_NUM_6 — Not implemented.
- PL_INT_NUM_7 — Not implemented.
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## DS1102W — DS1102 Device + GA1000 Wi-Fi add-on

- PLATFORM_ID: 16; rom=983040 ram=22271; firmware file(s): tios-ds1102w-3_60_06.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, fd, beep, rtc, wln, lcd, ssi
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_io_num`:
- PL_IO_NUM_0_RX0_INT0 — General-purpose I/O line 0 (P0.0), also the RX/W1in/din input of the serial port 0 and the interrupt line 0. When this serial port is in the UART mode…
- PL_IO_NUM_1_TX0_INT1 — General-purpose I/O line 1 (P0.1), also the TX/W1out/dout output of the serial port 0 and the interrupt line 1. When this serial port is in the UART m…
- PL_IO_NUM_2_RX1_INT2 — General-purpose I/O line 2 (P0.2), also the RX/W1in/din input of the serial port 1 and the interrupt line 2. When this serial port is in the UART mode…
- PL_IO_NUM_3_TX1_INT3 — General-purpose I/O line 3 (P0.3), also the TX/W1out/dout output of the serial port 1 and the interrupt line 3. When this serial port is in the UART m…
- PL_IO_NUM_4_RX2_INT4 — General-purpose I/O line 4 (P0.4), also the RX/W1in/din input of the serial port 2 and the interrupt line 4. When this serial port is in the UART mode…
- PL_IO_NUM_5_TX2_INT5 — General-purpose I/O line 5 (P0.5), also the TX/W1out/dout output of the serial port 2 and the interrupt line 5. When this serial port is in the UART m…
- PL_IO_NUM_6_RX3_INT6 — Not implemented.
- PL_IO_NUM_7_TX3_INT7 — Not implemented.
- PL_IO_NUM_8 — Not implemented.
- PL_IO_NUM_9 — Pin 8 on the wireless interface connector.
- PL_IO_NUM_10 — Pin 6 on the wireless interface connector.
- PL_IO_NUM_11 — The RST line of the wireless interface.
- PL_IO_NUM_12 — The DI line of the wireless interface.
- PL_IO_NUM_13 — The DO line of the wireless interface.
- PL_IO_NUM_14 — The CLK line of the wireless interface.
- PL_IO_NUM_15 — The CS line of the wireless interface.
- PL_IO_NUM_16 — Pin 9 on the wireless interface connector.
- PL_IO_NUM_17_RSMD — Serial port mode: HIGH for RS422/485, LOW for RS232.
- PL_IO_NUM_18_HDFD — Serial port mode: HIGH for full-duplex, LOW for half-duplex.
- PL_IO_NUM_19_SB1 — LED bar, LED#1 (the "weakest signal" LED).
- PL_IO_NUM_20_SB2 — LED bar, LED#2.
- PL_IO_NUM_21_SB3 — LED bar, LED#3.
- PL_IO_NUM_22_SB4 — LED bar, LED#4.
- PL_IO_NUM_23_SB5 — LED bar, LED#5 (the "strongest signal" LED).
- PL_IO_NUM_24_OLED_D0 — OLED dispay data bus, line 0 (P0.0).
- PL_IO_NUM_25_OLED_D1 — OLED dispay data bus, line 1 (P0.1).
- PL_IO_NUM_26_OLED_D2 — OLED dispay data bus, line 2 (P0.2).
- PL_IO_NUM_27_OLED_D3 — OLED dispay data bus, line 3 (P0.3).
- PL_IO_NUM_28_OLED_D4 — OLED dispay data bus, line 4 (P0.4).
- PL_IO_NUM_29_OLED_D5 — OLED dispay data bus, line 5 (P0.5).
- PL_IO_NUM_30_OLED_D6 — OLED dispay data bus, line 6 (P0.6).
- PL_IO_NUM_31_OLED_D7 — OLED dispay data bus, line 7 (P0.7).
- PL_IO_NUM_32_OLED_CS — OLED display, CS control line.
- PL_IO_NUM_33_OLED_RD — OLED display, RD control line.
- PL_IO_NUM_34_OLED_WR — OLED display, WR control line.
- PL_IO_NUM_35_OLED_DC — OLED display, DC control line.
- PL_IO_NUM_36_OLED_RST — OLED display, RST control line.
- PL_IO_NUM_37_CO — General-purpose I/O line 37 (does not belong to any 8-bit port), also a square wave output controlled by the beep object. This output is driving a buz…
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (the data bus of the OLED display).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 0).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 1).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 2).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 3).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 4).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 5).
- PL_INT_NUM_6 — Not implemented.
- PL_INT_NUM_7 — Not implemented.
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## DS1202 — DS1202 Device

- PLATFORM_ID: 5; rom=983040 ram=22271; firmware file(s): tios-ds1202-3_60_06.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, fd
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_io_num`:
- PL_IO_NUM_0_RX0_INT0 — General-purpose I/O line 0 (P0.0), also the RX/W1in/din input of the serial port 0 and the interrupt line 0. When this serial port is in the UART mode…
- PL_IO_NUM_1_TX0_INT4 — General-purpose I/O line 1 (P0.1), also the TX/W1out/dout output of the serial port 0 and the interrupt line 4. When this serial port is in the UART m…
- PL_IO_NUM_2_RX1_INT1 — General-purpose I/O line 2 (P0.2), also the RX/W1in/din input of the serial port 1 and the interrupt line 1. When this serial port is in the UART mode…
- PL_IO_NUM_3_TX1_INT5 — General-purpose I/O line 3 (P0.3), also the TX/W1out/dout output of the serial port 1 and the interrupt line 5. When this serial port is in the UART m…
- PL_IO_NUM_4_RX2_INT2 — General-purpose I/O line 4 (P0.4), also the RX/W1in/din input of the serial port 2 and the interrupt line 2. When this serial port is in the UART mode…
- PL_IO_NUM_5_TX2_INT6 — General-purpose I/O line 5 (P0.5), also the TX/W1out/dout output of the serial port 2 and the interrupt line 6. When this serial port is in the UART m…
- PL_IO_NUM_6_RX3_INT3 — General-purpose I/O line 6 (P0.6), also the RX/W1in/din input of the serial port 3 and the interrupt line 3. When this serial port is in the UART mode…
- PL_IO_NUM_7_INT7 — General-purpose I/O line 7 (P0.7), also the interrupt line 7.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7.

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 0).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 2).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 4).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 6).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 1).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 3).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 5).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 7).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## DS1206 — DS1206 Device

- PLATFORM_ID: 3; rom=983040 ram=22271; firmware file(s): tios-ds1206-3_60_06.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, fd
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_io_num`:
- PL_IO_NUM_0_RX0_INT0 — General-purpose I/O line 0 (P0.0), also the RX/W1in/din input of the serial port 0 and the interrupt line 0. When this serial port is in the UART mode…
- PL_IO_NUM_1_TX0_INT1 — General-purpose I/O line 1 (P0.1), also the TX/W1out/dout output of the serial port 0 and the interrupt line 1. When this serial port is in the UART m…
- PL_IO_NUM_2_RX1_INT2 — General-purpose I/O line 2 (P0.2), also the RX/W1in/din input of the serial port 1 and the interrupt line 2. When this serial port is in the UART mode…
- PL_IO_NUM_3_TX1_INT3 — General-purpose I/O line 3 (P0.3), also the TX/W1out/dout output of the serial port 1 and the interrupt line 3. When this serial port is in the UART m…
- PL_IO_NUM_4_RX2_INT4 — General-purpose I/O line 4 (P0.4), also the RX/W1in/din input of the serial port 2 and the interrupt line 4. When this serial port is in the UART mode…
- PL_IO_NUM_5_TX2_INT5 — General-purpose I/O line 5 (P0.5), also the TX/W1out/dout output of the serial port 2 and the interrupt line 5. When this serial port is in the UART m…
- PL_IO_NUM_6_RX3_INT6 — General-purpose I/O line 6 (P0.6), also the RX/W1in/din input of the serial port 3 and the interrupt line 6. When this serial port is in the UART mode…
- PL_IO_NUM_7_EMPTY — This line is not implemented and has no function.
- PL_IO_NUM_8_PWROUT — Controls the power output on pin 9 of the DB9M connector (this applies only to the DS1206 and DS1206N-RS devices). Power will be ON when this output i…
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7.

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 0).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 1).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 2).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 3).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 4).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 5).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 6).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 7).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## EM1000 — EM1000 Module

- PLATFORM_ID: 0; rom=983040 ram=22271; firmware file(s): tios-em1000-3_60_06.bin
- Object headers included: gen-em1000
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## EM1000N — EM1000 Module + WA2000 Wi-Fi add-on

- PLATFORM_ID: 34; rom=983040 ram=22271; firmware file(s): tios-em1000n-3_70_02.bin
- Object headers included: gen-em1000, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## EM1000W — EM1000 Module + GA1000 Wi-Fi add-on

- PLATFORM_ID: 11; rom=983040 ram=22271; firmware file(s): tios-em1000w-3_60_06.bin
- Object headers included: gen-em1000, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## EM1001N — EM1001 Module + WA2000 Wi-Fi add-on

- PLATFORM_ID: 35; rom=3080192 ram=22271; firmware file(s): tios-em1001n-3_70_02.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, beep, rtc, lcd, kp, ssi, fd, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0 — General-purpose I/O line 0 (P0.0).
- PL_IO_NUM_1 — General-purpose I/O line 1 (P0.1).
- PL_IO_NUM_2 — General-purpose I/O line 2 (P0.2).
- PL_IO_NUM_3 — General-purpose I/O line 3 (P0.3).
- PL_IO_NUM_4 — General-purpose I/O line 4 (P0.4).
- PL_IO_NUM_5 — General-purpose I/O line 5 (P0.5).
- PL_IO_NUM_6 — General-purpose I/O line 6 (P0.6).
- PL_IO_NUM_7 — General-purpose I/O line 7 (P0.7).
- PL_IO_NUM_8_RX0 — General-purpose I/O line 8 (P1.0), also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MOD…
- PL_IO_NUM_9_TX0 — General-purpose I/O line 9 (P1.1), also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_…
- PL_IO_NUM_10_RX1 — General-purpose I/O line 10 (P1.2), also the RX/W1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_11_TX1 — General-purpose I/O line 11 (P1.3), also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_12_RX2 — General-purpose I/O line 12 (P1.4), also the RX/W1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_13_TX2 — General-purpose I/O line 13 (P1.5), also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_14_RX3 — General-purpose I/O line 14 (P1.6), also the RX/W1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_15_TX3 — General-purpose I/O line 15 (P1.7), also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_16_INT0 — General-purpose I/O line 16 (P2.0), also the interrupt line 0.
- PL_IO_NUM_17_INT1 — General-purpose I/O line 17 (P2.1), also the interrupt line 1.
- PL_IO_NUM_18_INT2 — General-purpose I/O line 18 (P2.2), also the interrupt line 2.
- PL_IO_NUM_19_INT3 — General-purpose I/O line 19 (P2.3), also the interrupt line 3.
- PL_IO_NUM_20_INT4 — General-purpose I/O line 20 (P2.4), also the interrupt line 4.
- PL_IO_NUM_21_INT5 — General-purpose I/O line 21 (P2.5), also the interrupt line 5.
- PL_IO_NUM_22_INT6 — General-purpose I/O line 22 (P2.6), also the interrupt line 6.
- PL_IO_NUM_23_INT7 — General-purpose I/O line 23 (P2.7), also the interrupt line 7.
- PL_IO_NUM_24 — General-purpose I/O line 24 (P3.0).
- PL_IO_NUM_25 — General-purpose I/O line 25 (P3.1).
- PL_IO_NUM_26 — General-purpose I/O line 26 (P3.2).
- PL_IO_NUM_27 — General-purpose I/O line 27 (P3.3).
- PL_IO_NUM_28 — General-purpose I/O line 28 (P3.4).
- PL_IO_NUM_29 — General-purpose I/O line 29 (P3.5).
- PL_IO_NUM_30 — General-purpose I/O line 30 (P3.6).
- PL_IO_NUM_31 — General-purpose I/O line 31 (P3.7).
- PL_IO_NUM_32 — General-purpose I/O line 32 (P4.0).
- PL_IO_NUM_33 — General-purpose I/O line 33 (P4.1).
- PL_IO_NUM_34 — General-purpose I/O line 34 (P4.2).
- PL_IO_NUM_35 — General-purpose I/O line 35 (P4.3).
- PL_IO_NUM_36 — General-purpose I/O line 36 (P4.4).
- PL_IO_NUM_37 — General-purpose I/O line 37 (P4.5).
- PL_IO_NUM_38 — General-purpose I/O line 38 (P4.6).
- PL_IO_NUM_39 — General-purpose I/O line 39 (P4.7).
- PL_IO_NUM_40 — General-purpose I/O line 40 (does not belong to any 8-bit port).
- PL_IO_NUM_41 — General-purpose I/O line 41 (does not belong to any 8-bit port).
- PL_IO_NUM_42 — General-purpose I/O line 42 (does not belong to any 8-bit port).
- PL_IO_NUM_43 — General-purpose I/O line 43 (does not belong to any 8-bit port).
- PL_IO_NUM_44 — General-purpose I/O line 44 (does not belong to any 8-bit port).
- PL_IO_NUM_45_CO — General-purpose I/O line 45 (does not belong to any 8-bit port), also a square wave output controlled by the beep object. This output is primarily int…
- PL_IO_NUM_46 — General-purpose I/O line 46 (does not belong to any 8-bit port).
- PL_IO_NUM_47 — General-purpose I/O line 47 (does not belong to any 8-bit port).
- PL_IO_NUM_48 — General-purpose I/O line 48 (does not belong to any 8-bit port).
- PL_IO_NUM_49 — General-purpose I/O line 49 (does not belong to any 8-bit port).
- PL_IO_NUM_50 — General-purpose I/O line 50 (does not belong to any 8-bit port).
- PL_IO_NUM_51 — General-purpose I/O line 51 (does not belong to any 8-bit port).
- PL_IO_NUM_52 — General-purpose I/O line 52 (does not belong to any 8-bit port).
- PL_IO_NUM_53 — General-purpose I/O line 53 (does not belong to any 8-bit port).
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7.
- PL_IO_PORT_NUM_1 — 8-bit port 1, contains I/O lines 8-15.
- PL_IO_PORT_NUM_2 — 8-bit port 2, contains I/O lines 16-23.
- PL_IO_PORT_NUM_3 — 8-bit port 3, contains I/O lines 24-31.
- PL_IO_PORT_NUM_4 — 8-bit port 4, contains I/O lines 32-39.

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## EM1001W — EM1001 Module + GA1000 Wi-Fi add-on

- PLATFORM_ID: 23; rom=3080192 ram=22271; firmware file(s): tios-em1001w-3_60_06.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, beep, rtc, lcd, kp, ssi, fd, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0 — General-purpose I/O line 0 (P0.0).
- PL_IO_NUM_1 — General-purpose I/O line 1 (P0.1).
- PL_IO_NUM_2 — General-purpose I/O line 2 (P0.2).
- PL_IO_NUM_3 — General-purpose I/O line 3 (P0.3).
- PL_IO_NUM_4 — General-purpose I/O line 4 (P0.4).
- PL_IO_NUM_5 — General-purpose I/O line 5 (P0.5).
- PL_IO_NUM_6 — General-purpose I/O line 6 (P0.6).
- PL_IO_NUM_7 — General-purpose I/O line 7 (P0.7).
- PL_IO_NUM_8_RX0 — General-purpose I/O line 8 (P1.0), also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MOD…
- PL_IO_NUM_9_TX0 — General-purpose I/O line 9 (P1.1), also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_…
- PL_IO_NUM_10_RX1 — General-purpose I/O line 10 (P1.2), also the RX/W1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_11_TX1 — General-purpose I/O line 11 (P1.3), also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_12_RX2 — General-purpose I/O line 12 (P1.4), also the RX/W1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_13_TX2 — General-purpose I/O line 13 (P1.5), also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_14_RX3 — General-purpose I/O line 14 (P1.6), also the RX/W1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_15_TX3 — General-purpose I/O line 15 (P1.7), also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_16_INT0 — General-purpose I/O line 16 (P2.0), also the interrupt line 0.
- PL_IO_NUM_17_INT1 — General-purpose I/O line 17 (P2.1), also the interrupt line 1.
- PL_IO_NUM_18_INT2 — General-purpose I/O line 18 (P2.2), also the interrupt line 2.
- PL_IO_NUM_19_INT3 — General-purpose I/O line 19 (P2.3), also the interrupt line 3.
- PL_IO_NUM_20_INT4 — General-purpose I/O line 20 (P2.4), also the interrupt line 4.
- PL_IO_NUM_21_INT5 — General-purpose I/O line 21 (P2.5), also the interrupt line 5.
- PL_IO_NUM_22_INT6 — General-purpose I/O line 22 (P2.6), also the interrupt line 6.
- PL_IO_NUM_23_INT7 — General-purpose I/O line 23 (P2.7), also the interrupt line 7.
- PL_IO_NUM_24 — General-purpose I/O line 24 (P3.0).
- PL_IO_NUM_25 — General-purpose I/O line 25 (P3.1).
- PL_IO_NUM_26 — General-purpose I/O line 26 (P3.2).
- PL_IO_NUM_27 — General-purpose I/O line 27 (P3.3).
- PL_IO_NUM_28 — General-purpose I/O line 28 (P3.4).
- PL_IO_NUM_29 — General-purpose I/O line 29 (P3.5).
- PL_IO_NUM_30 — General-purpose I/O line 30 (P3.6).
- PL_IO_NUM_31 — General-purpose I/O line 31 (P3.7).
- PL_IO_NUM_32 — General-purpose I/O line 32 (P4.0).
- PL_IO_NUM_33 — General-purpose I/O line 33 (P4.1).
- PL_IO_NUM_34 — General-purpose I/O line 34 (P4.2).
- PL_IO_NUM_35 — General-purpose I/O line 35 (P4.3).
- PL_IO_NUM_36 — General-purpose I/O line 36 (P4.4).
- PL_IO_NUM_37 — General-purpose I/O line 37 (P4.5).
- PL_IO_NUM_38 — General-purpose I/O line 38 (P4.6).
- PL_IO_NUM_39 — General-purpose I/O line 39 (P4.7).
- PL_IO_NUM_40 — General-purpose I/O line 40 (does not belong to any 8-bit port).
- PL_IO_NUM_41 — General-purpose I/O line 41 (does not belong to any 8-bit port).
- PL_IO_NUM_42 — General-purpose I/O line 42 (does not belong to any 8-bit port).
- PL_IO_NUM_43 — General-purpose I/O line 43 (does not belong to any 8-bit port).
- PL_IO_NUM_44 — General-purpose I/O line 44 (does not belong to any 8-bit port).
- PL_IO_NUM_45_CO — General-purpose I/O line 45 (does not belong to any 8-bit port), also a square wave output controlled by the beep object. This output is primarily int…
- PL_IO_NUM_46 — General-purpose I/O line 46 (does not belong to any 8-bit port).
- PL_IO_NUM_47 — General-purpose I/O line 47 (does not belong to any 8-bit port).
- PL_IO_NUM_48 — General-purpose I/O line 48 (does not belong to any 8-bit port).
- PL_IO_NUM_49 — General-purpose I/O line 49 (does not belong to any 8-bit port).
- PL_IO_NUM_50 — General-purpose I/O line 50 (does not belong to any 8-bit port).
- PL_IO_NUM_51 — General-purpose I/O line 51 (does not belong to any 8-bit port).
- PL_IO_NUM_52 — General-purpose I/O line 52 (does not belong to any 8-bit port).
- PL_IO_NUM_53 — General-purpose I/O line 53 (does not belong to any 8-bit port).
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7.
- PL_IO_PORT_NUM_1 — 8-bit port 1, contains I/O lines 8-15.
- PL_IO_PORT_NUM_2 — 8-bit port 2, contains I/O lines 16-23.
- PL_IO_PORT_NUM_3 — 8-bit port 3, contains I/O lines 24-31.
- PL_IO_PORT_NUM_4 — 8-bit port 4, contains I/O lines 32-39.

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## EM1202 — EM1202 Module

- PLATFORM_ID: 1; rom=983040 ram=22271; firmware file(s): tios-em1202-3_60_06.bin
- Object headers included: gen-em1202
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## EM1202N — EM1202 Module + WA2000 Wi-Fi add-on

- PLATFORM_ID: 36; rom=983040 ram=22271; firmware file(s): tios-em1202N-3_70_02.bin
- Object headers included: gen-em1202, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## EM1202W — EM1202 Module + GA1000 Wi-Fi add-on

- PLATFORM_ID: 12; rom=983040 ram=22271; firmware file(s): tios-em1202w-3_60_06.bin
- Object headers included: gen-em1202, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## EM1206 — EM1206 Module

- PLATFORM_ID: 4; rom=983040 ram=22271; firmware file(s): tios-em1206-3_60_06.bin
- Object headers included: gen-em1206
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## EM1206N — EM1206 Module + WA2000 Wi-Fi add-on

- PLATFORM_ID: 37; rom=983040 ram=22271; firmware file(s): tios-em1206n-3_70_02.bin
- Object headers included: gen-em1206, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## EM1206W — EM1206 Module + GA1000 Wi-Fi add-on

- PLATFORM_ID: 13; rom=983040 ram=22271; firmware file(s): tios-em1206w-3_60_06.bin
- Object headers included: gen-em1206, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## EM2000W — EM2000 Module

- PLATFORM_ID: 24; rom=786432 ram=66816; firmware file(s): tios-em2000w-4_02_02.bin
- Object headers included: gen, sys-2xxx, net, pppoe, io-1xxx, beep, rtc, lcd, kp, ssi, fd, wln, bt, adc, tls, i2c
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, OBJECT_KP KP_ENABLED, OBJECT_FD FD_ENABLED, OBJECT_WLN WLN_ENABLED, OBJECT_BT BT_ENABLED, OBJECT_LCD LCD_ENABLED, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_adc_num`:
- PL_ADC_NUM_0 — ADC channel 0 (mapped to I/O line 40).
- PL_ADC_NUM_1 — ADC channel 1 (mapped to I/O line 41).
- PL_ADC_NUM_2 — ADC channel 2 (mapped to I/O line 42).
- PL_ADC_NUM_3 — ADC channel 3 (mapped to I/O line 43).

`enum pl_io_num`:
- PL_IO_NUM_0 — General-purpose I/O line 0 (P0.0).
- PL_IO_NUM_1 — General-purpose I/O line 1 (P0.1).
- PL_IO_NUM_2 — General-purpose I/O line 2 (P0.2).
- PL_IO_NUM_3 — General-purpose I/O line 3 (P0.3).
- PL_IO_NUM_4 — General-purpose I/O line 4 (P0.4).
- PL_IO_NUM_5 — General-purpose I/O line 5 (P0.5).
- PL_IO_NUM_6 — General-purpose I/O line 6 (P0.6).
- PL_IO_NUM_7 — General-purpose I/O line 7 (P0.7).
- PL_IO_NUM_8_RX0 — General-purpose I/O line 8 (P1.0), also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MOD…
- PL_IO_NUM_9_TX0 — General-purpose I/O line 9 (P1.1), also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_…
- PL_IO_NUM_10_RX1 — General-purpose I/O line 10 (P1.2), also the RX/W1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_11_TX1 — General-purpose I/O line 11 (P1.3), also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_12_RX2 — General-purpose I/O line 12 (P1.4), also the RX/W1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_13_TX2 — General-purpose I/O line 13 (P1.5), also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_14_RX3 — General-purpose I/O line 14 (P1.6), also the RX/W1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_15_TX3 — General-purpose I/O line 15 (P1.7), also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_16_INT0 — General-purpose I/O line 16 (P2.0), also the interrupt line 0.
- PL_IO_NUM_17_INT1 — General-purpose I/O line 17 (P2.1), also the interrupt line 1.
- PL_IO_NUM_18_INT2 — General-purpose I/O line 18 (P2.2), also the interrupt line 2.
- PL_IO_NUM_19_INT3 — General-purpose I/O line 19 (P2.3), also the interrupt line 3.
- PL_IO_NUM_20_INT4 — General-purpose I/O line 20 (P2.4), also the interrupt line 4.
- PL_IO_NUM_21_INT5 — General-purpose I/O line 21 (P2.5), also the interrupt line 5.
- PL_IO_NUM_22_INT6 — General-purpose I/O line 22 (P2.6), also the interrupt line 6.
- PL_IO_NUM_23_INT7 — General-purpose I/O line 23 (P2.7), also the interrupt line 7.
- PL_IO_NUM_24 — General-purpose I/O line 24 (P3.0).
- PL_IO_NUM_25 — General-purpose I/O line 25 (P3.1).
- PL_IO_NUM_26 — General-purpose I/O line 26 (P3.2).
- PL_IO_NUM_27 — General-purpose I/O line 27 (P3.3).
- PL_IO_NUM_28 — General-purpose I/O line 28 (P3.4).
- PL_IO_NUM_29 — General-purpose I/O line 29 (P3.5).
- PL_IO_NUM_30 — General-purpose I/O line 30 (P3.6).
- PL_IO_NUM_31 — General-purpose I/O line 31 (P3.7).
- PL_IO_NUM_32 — General-purpose I/O line 32 (P4.0).
- PL_IO_NUM_33 — General-purpose I/O line 33 (P4.1).
- PL_IO_NUM_34 — General-purpose I/O line 34 (P4.2).
- PL_IO_NUM_35 — General-purpose I/O line 35 (P4.3).
- PL_IO_NUM_36 — General-purpose I/O line 36 (P4.4).
- PL_IO_NUM_37 — General-purpose I/O line 37 (P4.5).
- PL_IO_NUM_38 — General-purpose I/O line 38 (P4.6).
- PL_IO_NUM_39 — General-purpose I/O line 39 (P4.7).
- PL_IO_NUM_40 — General-purpose I/O line 40 (does not belong to any 8-bit port).
- PL_IO_NUM_41 — General-purpose I/O line 41 (does not belong to any 8-bit port).
- PL_IO_NUM_42 — General-purpose I/O line 42 (does not belong to any 8-bit port).
- PL_IO_NUM_43 — General-purpose I/O line 43 (does not belong to any 8-bit port).
- PL_IO_NUM_44 — General-purpose I/O line 44 (does not belong to any 8-bit port).
- PL_IO_NUM_45_CO — General-purpose I/O line 45 (does not belong to any 8-bit port), also a square wave output controlled by the beep object. This output is primarily int…
- PL_IO_NUM_46 — General-purpose I/O line 46 (does not belong to any 8-bit port).
- PL_IO_NUM_47 — General-purpose I/O line 47 (does not belong to any 8-bit port).
- PL_IO_NUM_48 — General-purpose I/O line 48 (does not belong to any 8-bit port).
- PL_IO_NUM_49 — General-purpose I/O line 49 (does not belong to any 8-bit port).
- PL_IO_NUM_50 — General-purpose I/O line 50 (does not belong to any 8-bit port).
- PL_IO_NUM_51 — General-purpose I/O line 51 (does not belong to any 8-bit port).
- PL_IO_NUM_52 — General-purpose I/O line 52 (does not belong to any 8-bit port).
- PL_IO_NUM_53 — General-purpose I/O line 53 (does not belong to any 8-bit port).
- PL_IO_NUM_54 — General-purpose I/O line 54 (does not belong to any 8-bit port). Formerly DBGRX.
- PL_IO_NUM_55 — General-purpose I/O line 55 (does not belong to any 8-bit port). Formerly DBGTX.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7. This is a virtual port. During reads (io.portget, io.portstate(g)) and writes (io.portset, io.portstate(s)) each…
- PL_IO_PORT_NUM_1 — 8-bit port 1, contains I/O lines 8-15. This is a virtual port. During reads (io.portget, io.portstate(g)) and writes (io.portset, io.portstate(s)) eac…
- PL_IO_PORT_NUM_2 — 8-bit port 2, contains I/O lines 16-23. This is a virtual port. During writes (io.portset, io.portstate(s)), all lines with their new value equal to L…
- PL_IO_PORT_NUM_3 — 8-bit port 3, contains I/O lines 24-31. This is a virtual port. During writes (io.portset, io.portstate(s)), all lines with their new value equal to L…
- PL_IO_PORT_NUM_4 — 8-bit port 4, contains I/O lines 32-39. This is a virtual port. During writes (io.portset, io.portstate(s)), all lines with their new value equal to L…

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## EM3000W — EM3000 Module

- PLATFORM_ID: 49; rom=1310720 ram=132352; firmware file(s): tios-em3000w-4_01_08.bin
- Object headers included: gen, sys-2xxx, em3000w_sock, net, pppoe, io-2xxx, beep, rtc, lcd, kp, ssi, fd, wln, bt, adc, tls, i2c
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, OBJECT_KP KP_ENABLED, OBJECT_FD FD_ENABLED, OBJECT_WLN WLN_ENABLED, OBJECT_BT BT_ENABLED, OBJECT_LCD LCD_ENABLED, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_adc_num`:
- PL_ADC_NUM_0 — ADC channel 0 (mapped to I/O line 40).
- PL_ADC_NUM_1 — ADC channel 1 (mapped to I/O line 41).
- PL_ADC_NUM_2 — ADC channel 2 (mapped to I/O line 42).
- PL_ADC_NUM_3 — ADC channel 3 (mapped to I/O line 43).

`enum pl_io_num`:
- PL_IO_NUM_0 — General-purpose I/O line 0 (P0.0).
- PL_IO_NUM_1 — General-purpose I/O line 1 (P0.1).
- PL_IO_NUM_2 — General-purpose I/O line 2 (P0.2).
- PL_IO_NUM_3 — General-purpose I/O line 3 (P0.3).
- PL_IO_NUM_4 — General-purpose I/O line 4 (P0.4).
- PL_IO_NUM_5 — General-purpose I/O line 5 (P0.5).
- PL_IO_NUM_6 — General-purpose I/O line 6 (P0.6).
- PL_IO_NUM_7 — General-purpose I/O line 7 (P0.7).
- PL_IO_NUM_8_RX0 — General-purpose I/O line 8 (P1.0), also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MOD…
- PL_IO_NUM_9_TX0 — General-purpose I/O line 9 (P1.1), also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_…
- PL_IO_NUM_10_RX1 — General-purpose I/O line 10 (P1.2), also the RX/W1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_11_TX1 — General-purpose I/O line 11 (P1.3), also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_12_RX2 — General-purpose I/O line 12 (P1.4), also the RX/W1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_13_TX2 — General-purpose I/O line 13 (P1.5), also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_14_RX3 — General-purpose I/O line 14 (P1.6), also the RX/W1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_15_TX3 — General-purpose I/O line 15 (P1.7), also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_16_INT0 — General-purpose I/O line 16 (P2.0), also the interrupt line 0.
- PL_IO_NUM_17_INT1 — General-purpose I/O line 17 (P2.1), also the interrupt line 1.
- PL_IO_NUM_18_INT2 — General-purpose I/O line 18 (P2.2), also the interrupt line 2.
- PL_IO_NUM_19_INT3 — General-purpose I/O line 19 (P2.3), also the interrupt line 3.
- PL_IO_NUM_20_INT4 — General-purpose I/O line 20 (P2.4), also the interrupt line 4.
- PL_IO_NUM_21_INT5 — General-purpose I/O line 21 (P2.5), also the interrupt line 5.
- PL_IO_NUM_22_INT6 — General-purpose I/O line 22 (P2.6), also the interrupt line 6.
- PL_IO_NUM_23_INT7 — General-purpose I/O line 23 (P2.7), also the interrupt line 7.
- PL_IO_NUM_24 — General-purpose I/O line 24 (P3.0).
- PL_IO_NUM_25 — General-purpose I/O line 25 (P3.1).
- PL_IO_NUM_26 — General-purpose I/O line 26 (P3.2).
- PL_IO_NUM_27 — General-purpose I/O line 27 (P3.3).
- PL_IO_NUM_28 — General-purpose I/O line 28 (P3.4).
- PL_IO_NUM_29 — General-purpose I/O line 29 (P3.5).
- PL_IO_NUM_30 — General-purpose I/O line 30 (P3.6).
- PL_IO_NUM_31 — General-purpose I/O line 31 (P3.7).
- PL_IO_NUM_32 — General-purpose I/O line 32 (P4.0).
- PL_IO_NUM_33 — General-purpose I/O line 33 (P4.1).
- PL_IO_NUM_34 — General-purpose I/O line 34 (P4.2).
- PL_IO_NUM_35 — General-purpose I/O line 35 (P4.3).
- PL_IO_NUM_36 — General-purpose I/O line 36 (P4.4).
- PL_IO_NUM_37 — General-purpose I/O line 37 (P4.5).
- PL_IO_NUM_38 — General-purpose I/O line 38 (P4.6).
- PL_IO_NUM_39 — General-purpose I/O line 39 (P4.7).
- PL_IO_NUM_40 — General-purpose I/O line 40 (does not belong to any 8-bit port).
- PL_IO_NUM_41 — General-purpose I/O line 41 (does not belong to any 8-bit port).
- PL_IO_NUM_42 — General-purpose I/O line 42 (does not belong to any 8-bit port).
- PL_IO_NUM_43 — General-purpose I/O line 43 (does not belong to any 8-bit port).
- PL_IO_NUM_44 — General-purpose I/O line 44 (does not belong to any 8-bit port).
- PL_IO_NUM_45_CO — General-purpose I/O line 45 (does not belong to any 8-bit port), also a square wave output controlled by the beep object. This output is primarily int…
- PL_IO_NUM_46 — General-purpose I/O line 46 (does not belong to any 8-bit port).
- PL_IO_NUM_47 — General-purpose I/O line 47 (does not belong to any 8-bit port).
- PL_IO_NUM_48 — General-purpose I/O line 48 (does not belong to any 8-bit port).
- PL_IO_NUM_49 — General-purpose I/O line 49 (does not belong to any 8-bit port).
- PL_IO_NUM_50 — General-purpose I/O line 50 (does not belong to any 8-bit port).
- PL_IO_NUM_51 — General-purpose I/O line 51 (does not belong to any 8-bit port).
- PL_IO_NUM_52 — General-purpose I/O line 52 (does not belong to any 8-bit port).
- PL_IO_NUM_53 — General-purpose I/O line 53 (does not belong to any 8-bit port).
- PL_IO_NUM_54 — General-purpose I/O line 54 (does not belong to any 8-bit port). Formerly DBGRX.
- PL_IO_NUM_55 — General-purpose I/O line 55 (does not belong to any 8-bit port). Formerly DBGTX.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7. This is a virtual port. During reads (io.portget, io.portstate(g)) and writes (io.portset, io.portstate(s)) each…
- PL_IO_PORT_NUM_1 — 8-bit port 1, contains I/O lines 8-15. This is a virtual port. During reads (io.portget, io.portstate(g)) and writes (io.portset, io.portstate(s)) eac…
- PL_IO_PORT_NUM_2 — 8-bit port 2, contains I/O lines 16-23. This is a virtual port. During writes (io.portset, io.portstate(s)), all lines with their new value equal to L…
- PL_IO_PORT_NUM_3 — 8-bit port 3, contains I/O lines 24-31. This is a virtual port. During writes (io.portset, io.portstate(s)), all lines with their new value equal to L…
- PL_IO_PORT_NUM_4 — 8-bit port 4, contains I/O lines 32-39. This is a virtual port. During writes (io.portset, io.portstate(s)), all lines with their new value equal to L…

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## EM500W — EM500 Module + GA1000 Wi-Fi add-on

- PLATFORM_ID: 15; rom=327680 ram=17920; firmware file(s): tios-em500w-3_60_06.bin, tios-em500w-3_60_08.bin
- Object headers included: gen, sys-5xx, net, pppoe, io-5xx, fd, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0_INT0 — General-purpose I/O line 0 (P0.0), also the interrupt line 0.
- PL_IO_NUM_1_INT1 — General-purpose I/O line 1 (P0.1), also the interrupt line 1.
- PL_IO_NUM_2 — General-purpose I/O line 2 (P0.2).
- PL_IO_NUM_3 — General-purpose I/O line 3 (P0.3).
- PL_IO_NUM_4 — General-purpose I/O line 4 (P0.4).
- PL_IO_NUM_5 — General-purpose I/O line 5 (P0.5).
- PL_IO_NUM_6 — General-purpose I/O line 6 (P0.6).
- PL_IO_NUM_7 — General-purpose I/O line 7 (P0.7).
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7.

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 0).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 1).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## EM510W — EM510 Module

- PLATFORM_ID: 43; rom=262144 ram=16128; firmware file(s): tios-EM510W-3_80_26.bin
- Object headers included: gen, sys-5xx, net, pppoe, io-5xx, fd, wln, bt, ssi
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, OBJECT_KP KP_ENABLED, OBJECT_FD FD_ENABLED, OBJECT_WLN WLN_ENABLED, OBJECT_BT BT_ENABLED, OBJECT_LCD LCD_ENABLED, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0_INT0 — General-purpose I/O line 0 (P0.0), also the interrupt line 0.
- PL_IO_NUM_1_INT1 — General-purpose I/O line 1 (P0.1), also the interrupt line 1.
- PL_IO_NUM_2 — General-purpose I/O line 2 (P0.2).
- PL_IO_NUM_3 — General-purpose I/O line 3 (P0.3).
- PL_IO_NUM_4 — General-purpose I/O line 4 (P0.4).
- PL_IO_NUM_5 — General-purpose I/O line 5 (P0.5).
- PL_IO_NUM_6 — General-purpose I/O line 6 (P0.6).
- PL_IO_NUM_7 — General-purpose I/O line 7 (P0.7).
- PL_IO_NUM_8_RX0 — General-purpose I/O line 8 , also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MODE_UART…
- PL_IO_NUM_9_TX0 — General-purpose I/O line 9 , also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MODE_U…
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7.
- PL_IO_PORT_NUM_1 — 2-bit port 1, contains I/O lines 8-9.

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 0).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 1).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## KLM106_32 — KLM106 platform

- PLATFORM_ID: 33; rom=786432 ram=86784; firmware file(s): tios-klm106-4_00_01.bin
- Object headers included: gen-st, wln, bt, tls
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.

`enum pl_adc_num`:
- PL_ADC_NUM_0 — ADC channel 0 (mapped to I/O line 40).
- PL_ADC_NUM_1 — ADC channel 1 (mapped to I/O line 41).
- PL_ADC_NUM_2 — ADC channel 2 (mapped to I/O line 42).
- PL_ADC_NUM_3 — ADC channel 3 (mapped to I/O line 43).

## KLM601 — KLM601 platform

- PLATFORM_ID: 7; rom=983040 ram=21760; firmware file(s): tios-klm601-3_60_00.bin
- Object headers included: gen-t1000, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.

## KLM601_32 — KLM601 platform

- PLATFORM_ID: 27; rom=786432 ram=86784; firmware file(s): tios-klm601-4_00_01.bin
- Object headers included: gen-st, wln, bt, tls
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.

`enum pl_adc_num`:
- PL_ADC_NUM_0 — ADC channel 0 (mapped to I/O line 40).
- PL_ADC_NUM_1 — ADC channel 1 (mapped to I/O line 41).
- PL_ADC_NUM_2 — ADC channel 2 (mapped to I/O line 42).
- PL_ADC_NUM_3 — ADC channel 3 (mapped to I/O line 43).

## LKLM601 — LKLM601 Board

- PLATFORM_ID: 32; rom=983040 ram=86784; firmware file(s): —
- Object headers included: defines, constants, syscalls, button, fd, io, io-1xxx, kp, lfd, lsock, pat, romfile, rtc, ser, sock, stor, sys, sys-linux, ssi, wln, lcd, beep, net
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.

`enum pl_io_num`:
- PL_IO_NUM_0 — General-purpose I/O line 0 (P0.0).
- PL_IO_NUM_1 — General-purpose I/O line 1 (P0.1).
- PL_IO_NUM_2 — General-purpose I/O line 2 (P0.2).
- PL_IO_NUM_3 — General-purpose I/O line 3 (P0.3).
- PL_IO_NUM_4 — General-purpose I/O line 4 (P0.4).
- PL_IO_NUM_5 — General-purpose I/O line 5 (P0.5).
- PL_IO_NUM_6 — General-purpose I/O line 6 (P0.6).
- PL_IO_NUM_7 — General-purpose I/O line 7 (P0.7).
- PL_IO_NUM_8_RX0 — General-purpose I/O line 8 (P1.0), also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MOD…
- PL_IO_NUM_9_TX0 — General-purpose I/O line 9 (P1.1), also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER_…
- PL_IO_NUM_10_RX1 — General-purpose I/O line 10 (P1.2), also the RX/W1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_11_TX1 — General-purpose I/O line 11 (P1.3), also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_12_RX2 — General-purpose I/O line 12 (P1.4), also the RX/W1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_13_TX2 — General-purpose I/O line 13 (P1.5), also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_14_RX3 — General-purpose I/O line 14 (P1.6), also the RX/W1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_SER_MO…
- PL_IO_NUM_15_TX3 — General-purpose I/O line 15 (P1.7), also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_16_INT0 — General-purpose I/O line 16 (P2.0), also the interrupt line 0.
- PL_IO_NUM_17_INT1 — General-purpose I/O line 17 (P2.1), also the interrupt line 1.
- PL_IO_NUM_18_INT2 — General-purpose I/O line 18 (P2.2), also the interrupt line 2.
- PL_IO_NUM_19_INT3 — General-purpose I/O line 19 (P2.3), also the interrupt line 3.
- PL_IO_NUM_20_INT4 — General-purpose I/O line 20 (P2.4), also the interrupt line 4.
- PL_IO_NUM_21_INT5 — General-purpose I/O line 21 (P2.5), also the interrupt line 5.
- PL_IO_NUM_22_INT6 — General-purpose I/O line 22 (P2.6), also the interrupt line 6.
- PL_IO_NUM_23_INT7 — General-purpose I/O line 23 (P2.7), also the interrupt line 7.
- PL_IO_NUM_24 — General-purpose I/O line 24 (P3.0).
- PL_IO_NUM_25 — General-purpose I/O line 25 (P3.1).
- PL_IO_NUM_26 — General-purpose I/O line 26 (P3.2).
- PL_IO_NUM_27 — General-purpose I/O line 27 (P3.3).
- PL_IO_NUM_28 — General-purpose I/O line 28 (P3.4).
- PL_IO_NUM_29 — General-purpose I/O line 29 (P3.5).
- PL_IO_NUM_30 — General-purpose I/O line 30 (P3.6).
- PL_IO_NUM_31 — General-purpose I/O line 31 (P3.7).
- PL_IO_NUM_32 — General-purpose I/O line 32 (P4.0).
- PL_IO_NUM_33 — General-purpose I/O line 33 (P4.1).
- PL_IO_NUM_34 — General-purpose I/O line 34 (P4.2).
- PL_IO_NUM_35 — General-purpose I/O line 35 (P4.3).
- PL_IO_NUM_36 — General-purpose I/O line 36 (P4.4).
- PL_IO_NUM_37 — General-purpose I/O line 37 (P4.5).
- PL_IO_NUM_38 — General-purpose I/O line 38 (P4.6).
- PL_IO_NUM_39 — General-purpose I/O line 39 (P4.7).
- PL_IO_NUM_40 — General-purpose I/O line 40 (does not belong to any 8-bit port).
- PL_IO_NUM_41 — General-purpose I/O line 41 (does not belong to any 8-bit port).
- PL_IO_NUM_42 — General-purpose I/O line 42 (does not belong to any 8-bit port).
- PL_IO_NUM_43 — General-purpose I/O line 43 (does not belong to any 8-bit port).
- PL_IO_NUM_44 — General-purpose I/O line 44 (does not belong to any 8-bit port).
- PL_IO_NUM_45_CO — General-purpose I/O line 45 (does not belong to any 8-bit port), also a square wave output controlled by the beep object. This output is primarily int…
- PL_IO_NUM_46 — General-purpose I/O line 46 (does not belong to any 8-bit port).
- PL_IO_NUM_47 — General-purpose I/O line 47 (does not belong to any 8-bit port).
- PL_IO_NUM_48 — General-purpose I/O line 48 (does not belong to any 8-bit port).
- PL_IO_NUM_49 — General-purpose I/O line 49 (does not belong to any 8-bit port).
- PL_IO_NUM_50 — General-purpose I/O line 50 (does not belong to any 8-bit port).
- PL_IO_NUM_51 — General-purpose I/O line 51 (does not belong to any 8-bit port).
- PL_IO_NUM_52 — General-purpose I/O line 52 (does not belong to any 8-bit port).
- PL_IO_NUM_53 — General-purpose I/O line 53 (does not belong to any 8-bit port).
- PL_IO_NUM_54 — General-purpose I/O line 54 (does not belong to any 8-bit port).
- PL_IO_NUM_55 — General-purpose I/O line 55 (does not belong to any 8-bit port).
- PL_IO_NUM_56 — General-purpose I/O line 56 (does not belong to any 8-bit port).
- PL_IO_NUM_57 — General-purpose I/O line 57 (does not belong to any 8-bit port).
- PL_IO_NUM_58 — General-purpose I/O line 58 (does not belong to any 8-bit port).
- PL_IO_NUM_59 — General-purpose I/O line 59 (does not belong to any 8-bit port).
- PL_IO_NUM_60 — General-purpose I/O line 60 (does not belong to any 8-bit port).
- PL_IO_NUM_61 — General-purpose I/O line 61 (does not belong to any 8-bit port).
- PL_IO_NUM_62 — General-purpose I/O line 62 (does not belong to any 8-bit port).
- PL_IO_NUM_63 — General-purpose I/O line 63 (does not belong to any 8-bit port).
- PL_IO_NUM_64 — General-purpose I/O line 64 (does not belong to any 8-bit port).
- PL_IO_NUM_65 — General-purpose I/O line 65 (does not belong to any 8-bit port).
- PL_IO_NUM_66 — General-purpose I/O line 66 (does not belong to any 8-bit port).
- PL_IO_NUM_67 — General-purpose I/O line 67 (does not belong to any 8-bit port).
- PL_IO_NUM_68 — General-purpose I/O line 68 (does not belong to any 8-bit port).
- PL_IO_NUM_69 — General-purpose I/O line 69 (does not belong to any 8-bit port).
- PL_IO_NUM_70 — General-purpose I/O line 70 (does not belong to any 8-bit port).
- PL_IO_NUM_71 — General-purpose I/O line 71 (does not belong to any 8-bit port).
- PL_IO_NUM_72 — General-purpose I/O line 72 (does not belong to any 8-bit port).
- PL_IO_NUM_73 — General-purpose I/O line 73 (does not belong to any 8-bit port).
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7.
- PL_IO_PORT_NUM_1 — 8-bit port 1, contains I/O lines 8-15.
- PL_IO_PORT_NUM_2 — 8-bit port 2, contains I/O lines 16-23.
- PL_IO_PORT_NUM_3 — 8-bit port 3, contains I/O lines 24-31.
- PL_IO_PORT_NUM_4 — 8-bit port 4, contains I/O lines 32-39.
- PL_IO_PORT_NUM_5 — 8-bit port 5, contains I/O lines 56-63.
- PL_IO_PORT_NUM_6 — 8-bit port 6, contains I/O lines 64-71.

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## LTPP3 — LTPP3 Board

- PLATFORM_ID: 29; rom=983040 ram=86784; firmware file(s): —
- Object headers included: defines, constants, syscalls, beep, button, fd, io, io-1xxx, lfd, lsock, net, pat, romfile, rtc, ser, sock, stor, sys, sys-linux, ssi, wln, ppp
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.

`enum pl_io_num`:
- PL_IO_NUM_0 — Socket 1, control line C.
- PL_IO_NUM_1 — Socket 5, control line C.
- PL_IO_NUM_2 — Socket 9, control line C.
- PL_IO_NUM_3 — Socket 13, control line C.
- PL_IO_NUM_4 — Socket 3, control line C.
- PL_IO_NUM_5 — Socket 7, control line C.
- PL_IO_NUM_6 — Socket 11, control line C.
- PL_IO_NUM_7 — Socket 15, control line C.
- PL_IO_NUM_8_RX0 — Socket 1, control line B. This line is also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_9_TX0 — Socket 1, control line A. This line is also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_10_RX1 — Socket 5, control line B. This line is also the RX/W0&1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_11_TX1 — Socket 5, control line A. This line is also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_12_RX2 — Socket 9, control line B. This line is also the RX/W0&1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_13_TX2 — Socket 9, control line A. This line is also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_14_RX3 — Socket 13, control line B. This line is also the RX/W0&1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_15_TX3 — Socket 13, control line A. This line is also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL…
- PL_IO_NUM_16_INT0 — Socket 1, control line D. This is also the interrupt line 0.
- PL_IO_NUM_17_INT1 — Socket 5, control line D. This is also the interrupt line 1.
- PL_IO_NUM_18_INT2 — Socket 9, control line D. This is also the interrupt line 2.
- PL_IO_NUM_19_INT3 — Socket 13, control line D. This is also the interrupt line 3.
- PL_IO_NUM_20_INT4 — Socket 3, control line D. This is also the interrupt line 4.
- PL_IO_NUM_21_INT5 — Socket 7, control line D. This is also the interrupt line 5.
- PL_IO_NUM_22_INT6 — Socket 11, control line D. This is also the interrupt line 5.
- PL_IO_NUM_23_INT7 — Socket 15, control line D. This is also the interrupt line 5.
- PL_IO_NUM_24 — Socket 17, control line A.
- PL_IO_NUM_25 — Socket 17, control line B.
- PL_IO_NUM_26 — Socket 17, control line C.
- PL_IO_NUM_27 — Socket 17, control line D.
- PL_IO_NUM_28 — Socket 19, control line A.
- PL_IO_NUM_29 — Socket 19, control line B.
- PL_IO_NUM_30 — Socket 19, control line C.
- PL_IO_NUM_31 — Socket 19, control line D.
- PL_IO_NUM_32 — Socket 3, control line A.
- PL_IO_NUM_33 — Socket 3, control line B.
- PL_IO_NUM_34 — Socket 7, control line A.
- PL_IO_NUM_35 — Socket 7, control line B.
- PL_IO_NUM_36 — Socket 11, control line A.
- PL_IO_NUM_37 — Socket 11, control line B.
- PL_IO_NUM_38 — Socket 13, control line A.
- PL_IO_NUM_39 — Socket 13, control line B.
- PL_IO_NUM_40 — Socket 21, control line A.
- PL_IO_NUM_41 — Socket 21, control line B.
- PL_IO_NUM_42 — Socket 21, control line C.
- PL_IO_NUM_43 — Socket 21, control line D.
- PL_IO_NUM_44 — Socket 25, control line A.
- PL_IO_NUM_45_CO — A square wave output controlled by the beep object. This output is driving a buzzer. When the beeper pattern starts playing, the line is configured as…
- PL_IO_NUM_46 — Signal strength LED bar control circuit, reset line.
- PL_IO_NUM_47 — Signal strength LED bar control circuit, clock line.
- PL_IO_NUM_48 — Signal strength LED bar control circuit, data line.
- PL_IO_NUM_49 — Wireless add-on socket, CS line.
- PL_IO_NUM_50 — Wireless add-on socket, DO line.
- PL_IO_NUM_51 — Wireless add-on socket, RST line.
- PL_IO_NUM_52 — Wireless add-on socket, DI line.
- PL_IO_NUM_53 — Wireless add-on socket, CLK line.
- PL_IO_NUM_54 — Socket 23, control line A.
- PL_IO_NUM_55 — Socket 23, control line B.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (LCD data lines D0-7).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## NB1010 — NB1010 Board

- PLATFORM_ID: 9; rom=983040 ram=22271; firmware file(s): tios-nb1010-3_60_06.bin
- Object headers included: gen-nb1010
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## NB1010N — NB1010N Board

- PLATFORM_ID: 10; rom=983040 ram=22271; firmware file(s): tios-nb1010n-3_70_02.bin
- Object headers included: gen-nb1010, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## NB1010W — NB1010W Board

- PLATFORM_ID: 10; rom=983040 ram=22271; firmware file(s): tios-nb1010w-3_60_06.bin
- Object headers included: gen-nb1010, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

## SIMULATOR — TiOS Simulator

- PLATFORM_ID: 28; rom=983040 ram=86784; firmware file(s): —
- Object headers included: defines, constants, syscalls, beep, button, fd, kp, lcd, net, pat, romfile, rtc, sock, stor, sys, sys-2xxx
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.

`enum pl_io_num`:
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

## SPACE_AGE — Space Age controller

- PLATFORM_ID: 30; rom=786432 ram=66816; firmware file(s): —
- Object headers included: gen, sys-2xxx, pppoe, io-1xxx, beep, rtc, lcd, kp, ssi, fd, wln, sled
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, OBJECT_KP KP_ENABLED, OBJECT_FD FD_ENABLED, OBJECT_WLN WLN_ENABLED, OBJECT_LCD LCD_ENABLED
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0 — Socket 1, control line C.
- PL_IO_NUM_1 — Socket 3, control line C.
- PL_IO_NUM_2 — Socket 5, control line C.
- PL_IO_NUM_3 — Socket 7, control line C.
- PL_IO_NUM_4 — Socket 9, control line C.
- PL_IO_NUM_5 — Socket 11, control line C.
- PL_IO_NUM_6 — Not connected.
- PL_IO_NUM_7 — Not connected.
- PL_IO_NUM_8_RX0 — Socket 1, control line B. This line is also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_9_TX0 — Socket 1, control line A. This line is also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_10_RX1 — Socket 3, control line B. This line is also the RX/W0&1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_11_TX1 — Socket 3, control line A. This line is also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_12_RX2 — Socket 5, control line B. This line is also the RX/W0&1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_13_TX2 — Socket 5, control line A. This line is also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_14_RX3 — Socket 7, control line B. This line is also the RX/W0&1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_15_TX3 — Socket 7, control line A. This line is also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_16_INT0 — Socket 1, control line D. This is also the interrupt line 0.
- PL_IO_NUM_17_INT1 — Socket 3, control line D. This is also the interrupt line 1.
- PL_IO_NUM_18_INT2 — Socket 5, control line D. This is also the interrupt line 2.
- PL_IO_NUM_19_INT3 — Socket 7, control line D. This is also the interrupt line 3.
- PL_IO_NUM_20_INT4 — Socket 9, control line D. This is also the interrupt line 4.
- PL_IO_NUM_21_INT5 — Socket 11, control line D. This is also the interrupt line 5.
- PL_IO_NUM_22_INT6 — Not connected.
- PL_IO_NUM_23_INT7 — Not connected.
- PL_IO_NUM_24 — LCD connector, data bus, line 0 (P0.0).
- PL_IO_NUM_25 — LCD connector, data bus, line 1 (P0.1).
- PL_IO_NUM_26 — LCD connector, data bus, line 2 (P0.2).
- PL_IO_NUM_27 — LCD connector, data bus, line 3 (P0.3).
- PL_IO_NUM_28 — LCD connector, data bus, line 4 (P0.4).
- PL_IO_NUM_29 — LCD connector, data bus, line 5 (P0.5).
- PL_IO_NUM_30 — LCD connector, data bus, line 6 (P0.6).
- PL_IO_NUM_31 — LCD connector, data bus, line 7 (P0.7).
- PL_IO_NUM_32 — Socket 9, control line A.
- PL_IO_NUM_33 — Socket 9, control line B.
- PL_IO_NUM_34 — Socket 11, control line A.
- PL_IO_NUM_35 — Socket 11, control line B.
- PL_IO_NUM_36 — Keypad connector, return line 1 (for the leftmost button, active low).
- PL_IO_NUM_37 — Keypad connector, return line 2 (active low).
- PL_IO_NUM_38 — Keypad connector, return line 3 (active low).
- PL_IO_NUM_39 — Keypad connector, return line 4 (for the rightmost button, active low).
- PL_IO_NUM_40 — LCD connector, CS line (active low).
- PL_IO_NUM_41 — LCD connector, RD line (active low).
- PL_IO_NUM_42 — LCD connector, WR line (active low).
- PL_IO_NUM_43 — LCD connector, DC line.
- PL_IO_NUM_44 — Keypad connector, reset line (for the sensor IC of the keypad, active low).
- PL_IO_NUM_45_CO — A square wave output controlled by the beep object. This output is driving a buzzer. When the beeper pattern starts playing, the line is configured as…
- PL_IO_NUM_46 — Signal strength LED bar control circuit, reset line.
- PL_IO_NUM_47 — Signal strength LED bar control circuit, clock line.
- PL_IO_NUM_48 — Signal strength LED bar control circuit, data line.
- PL_IO_NUM_49 — Wireless add-on socket, CS line.
- PL_IO_NUM_50 — Wireless add-on socket, DO line.
- PL_IO_NUM_51 — Wireless add-on socket, RST line.
- PL_IO_NUM_52 — Wireless add-on socket, DI line.
- PL_IO_NUM_53 — Wireless add-on socket, CLK line.
- PL_IO_NUM_54 — LCD connector, backlight control line (active low).
- PL_IO_NUM_55 — LCD connector, RST line (active low).
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (LCD data lines D0-7).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## T1000W — T1000 IC + GA1000 Wi-Fi add-on

- PLATFORM_ID: 6; rom=983040 ram=21760; firmware file(s): tios-t1000w-3_60_00.bin
- Object headers included: gen-t1000, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.

## TPP2N — TPP2 Board + WA2000 Wi-Fi add-on

- PLATFORM_ID: 40; rom=983040 ram=22271; firmware file(s): tios-tpp2n-3_70_02.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, beep, rtc, lcd, kp, ssi, fd, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0 — Socket 1, control line C.
- PL_IO_NUM_1 — Socket 3, control line C.
- PL_IO_NUM_2 — Socket 5, control line C.
- PL_IO_NUM_3 — Socket 7, control line C.
- PL_IO_NUM_4 — Socket 9, control line C.
- PL_IO_NUM_5 — Socket 11, control line C.
- PL_IO_NUM_6 — Not connected.
- PL_IO_NUM_7 — Not connected.
- PL_IO_NUM_8_RX0 — Socket 1, control line B. This line is also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_9_TX0 — Socket 1, control line A. This line is also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_10_RX1 — Socket 3, control line B. This line is also the RX/W0&1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_11_TX1 — Socket 3, control line A. This line is also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_12_RX2 — Socket 5, control line B. This line is also the RX/W0&1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_13_TX2 — Socket 5, control line A. This line is also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_14_RX3 — Socket 7, control line B. This line is also the RX/W0&1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_15_TX3 — Socket 7, control line A. This line is also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_16_INT0 — Socket 1, control line D. This is also the interrupt line 0.
- PL_IO_NUM_17_INT1 — Socket 3, control line D. This is also the interrupt line 1.
- PL_IO_NUM_18_INT2 — Socket 5, control line D. This is also the interrupt line 2.
- PL_IO_NUM_19_INT3 — Socket 7, control line D. This is also the interrupt line 3.
- PL_IO_NUM_20_INT4 — Socket 9, control line D. This is also the interrupt line 4.
- PL_IO_NUM_21_INT5 — Socket 11, control line D. This is also the interrupt line 5.
- PL_IO_NUM_22_INT6 — Not connected.
- PL_IO_NUM_23_INT7 — Not connected.
- PL_IO_NUM_24 — LCD connector, data bus, line 0 (P0.0).
- PL_IO_NUM_25 — LCD connector, data bus, line 1 (P0.1).
- PL_IO_NUM_26 — LCD connector, data bus, line 2 (P0.2).
- PL_IO_NUM_27 — LCD connector, data bus, line 3 (P0.3).
- PL_IO_NUM_28 — LCD connector, data bus, line 4 (P0.4).
- PL_IO_NUM_29 — LCD connector, data bus, line 5 (P0.5).
- PL_IO_NUM_30 — LCD connector, data bus, line 6 (P0.6).
- PL_IO_NUM_31 — LCD connector, data bus, line 7 (P0.7).
- PL_IO_NUM_32 — Socket 9, control line A.
- PL_IO_NUM_33 — Socket 9, control line B.
- PL_IO_NUM_34 — Socket 11, control line A.
- PL_IO_NUM_35 — Socket 11, control line B.
- PL_IO_NUM_36 — Keypad connector, return line 1 (for the leftmost button, active low).
- PL_IO_NUM_37 — Keypad connector, return line 2 (active low).
- PL_IO_NUM_38 — Keypad connector, return line 3 (active low).
- PL_IO_NUM_39 — Keypad connector, return line 4 (for the rightmost button, active low).
- PL_IO_NUM_40 — LCD connector, CS line (active low).
- PL_IO_NUM_41 — LCD connector, RD line (active low).
- PL_IO_NUM_42 — LCD connector, WR line (active low).
- PL_IO_NUM_43 — LCD connector, DC line.
- PL_IO_NUM_44 — Keypad connector, reset line (for the sensor IC of the keypad, active low).
- PL_IO_NUM_45_CO — A square wave output controlled by the beep object. This output is driving a buzzer. When the beeper pattern starts playing, the line is configured as…
- PL_IO_NUM_46 — Signal strength LED bar control circuit, reset line.
- PL_IO_NUM_47 — Signal strength LED bar control circuit, clock line.
- PL_IO_NUM_48 — Signal strength LED bar control circuit, data line.
- PL_IO_NUM_49 — Wireless add-on socket, CS line.
- PL_IO_NUM_50 — Wireless add-on socket, DO line.
- PL_IO_NUM_51 — Wireless add-on socket, RST line.
- PL_IO_NUM_52 — Wireless add-on socket, DI line.
- PL_IO_NUM_53 — Wireless add-on socket, CLK line.
- PL_IO_NUM_54 — LCD connector, backlight control line (active low).
- PL_IO_NUM_55 — LCD connector, RST line (active low).
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (LCD data lines D0-7).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## TPP2W — TPP2 Board

- PLATFORM_ID: 19; rom=983040 ram=22271; firmware file(s): tios-tpp2w-3_60_06.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, beep, rtc, lcd, kp, ssi, fd, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0 — Socket 1, control line C.
- PL_IO_NUM_1 — Socket 3, control line C.
- PL_IO_NUM_2 — Socket 5, control line C.
- PL_IO_NUM_3 — Socket 7, control line C.
- PL_IO_NUM_4 — Socket 9, control line C.
- PL_IO_NUM_5 — Socket 11, control line C.
- PL_IO_NUM_6 — Not connected.
- PL_IO_NUM_7 — Not connected.
- PL_IO_NUM_8_RX0 — Socket 1, control line B. This line is also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_9_TX0 — Socket 1, control line A. This line is also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_10_RX1 — Socket 3, control line B. This line is also the RX/W0&1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_11_TX1 — Socket 3, control line A. This line is also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_12_RX2 — Socket 5, control line B. This line is also the RX/W0&1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_13_TX2 — Socket 5, control line A. This line is also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_14_RX3 — Socket 7, control line B. This line is also the RX/W0&1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_15_TX3 — Socket 7, control line A. This line is also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_16_INT0 — Socket 1, control line D. This is also the interrupt line 0.
- PL_IO_NUM_17_INT1 — Socket 3, control line D. This is also the interrupt line 1.
- PL_IO_NUM_18_INT2 — Socket 5, control line D. This is also the interrupt line 2.
- PL_IO_NUM_19_INT3 — Socket 7, control line D. This is also the interrupt line 3.
- PL_IO_NUM_20_INT4 — Socket 9, control line D. This is also the interrupt line 4.
- PL_IO_NUM_21_INT5 — Socket 11, control line D. This is also the interrupt line 5.
- PL_IO_NUM_22_INT6 — Not connected.
- PL_IO_NUM_23_INT7 — Not connected.
- PL_IO_NUM_24 — LCD connector, data bus, line 0 (P0.0).
- PL_IO_NUM_25 — LCD connector, data bus, line 1 (P0.1).
- PL_IO_NUM_26 — LCD connector, data bus, line 2 (P0.2).
- PL_IO_NUM_27 — LCD connector, data bus, line 3 (P0.3).
- PL_IO_NUM_28 — LCD connector, data bus, line 4 (P0.4).
- PL_IO_NUM_29 — LCD connector, data bus, line 5 (P0.5).
- PL_IO_NUM_30 — LCD connector, data bus, line 6 (P0.6).
- PL_IO_NUM_31 — LCD connector, data bus, line 7 (P0.7).
- PL_IO_NUM_32 — Socket 9, control line A.
- PL_IO_NUM_33 — Socket 9, control line B.
- PL_IO_NUM_34 — Socket 11, control line A.
- PL_IO_NUM_35 — Socket 11, control line B.
- PL_IO_NUM_36 — Keypad connector, return line 1 (for the leftmost button, active low).
- PL_IO_NUM_37 — Keypad connector, return line 2 (active low).
- PL_IO_NUM_38 — Keypad connector, return line 3 (active low).
- PL_IO_NUM_39 — Keypad connector, return line 4 (for the rightmost button, active low).
- PL_IO_NUM_40 — LCD connector, CS line (active low).
- PL_IO_NUM_41 — LCD connector, RD line (active low).
- PL_IO_NUM_42 — LCD connector, WR line (active low).
- PL_IO_NUM_43 — LCD connector, DC line.
- PL_IO_NUM_44 — Keypad connector, reset line (for the sensor IC of the keypad, active low).
- PL_IO_NUM_45_CO — A square wave output controlled by the beep object. This output is driving a buzzer. When the beeper pattern starts playing, the line is configured as…
- PL_IO_NUM_46 — Signal strength LED bar control circuit, reset line.
- PL_IO_NUM_47 — Signal strength LED bar control circuit, clock line.
- PL_IO_NUM_48 — Signal strength LED bar control circuit, data line.
- PL_IO_NUM_49 — Wireless add-on socket, CS line.
- PL_IO_NUM_50 — Wireless add-on socket, DO line.
- PL_IO_NUM_51 — Wireless add-on socket, RST line.
- PL_IO_NUM_52 — Wireless add-on socket, DI line.
- PL_IO_NUM_53 — Wireless add-on socket, CLK line.
- PL_IO_NUM_54 — LCD connector, backlight control line (active low).
- PL_IO_NUM_55 — LCD connector, RST line (active low).
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (LCD data lines D0-7).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## TPP2W(G2) — TPP2(G2) Board

- PLATFORM_ID: 25; rom=786432 ram=66816; firmware file(s): tios-tpp2w(g2)-4_02_02.bin
- Object headers included: gen, sys-2xxx, net, pppoe, io-2xxx, beep, rtc, lcd, kp, ssi, fd, wln, bt, tls, i2c
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, OBJECT_KP KP_ENABLED, OBJECT_FD FD_ENABLED, OBJECT_WLN WLN_ENABLED, OBJECT_BT BT_ENABLED, OBJECT_LCD LCD_ENABLED, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0 — Socket 1, control line C.
- PL_IO_NUM_1 — Socket 3, control line C.
- PL_IO_NUM_2 — Socket 5, control line C.
- PL_IO_NUM_3 — Socket 7, control line C.
- PL_IO_NUM_4 — Socket 9, control line C.
- PL_IO_NUM_5 — Socket 11, control line C.
- PL_IO_NUM_6 — Not connected.
- PL_IO_NUM_7 — Not connected.
- PL_IO_NUM_8_RX0 — Socket 1, control line B. This line is also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_9_TX0 — Socket 1, control line A. This line is also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_10_RX1 — Socket 3, control line B. This line is also the RX/W0&1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_11_TX1 — Socket 3, control line A. This line is also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_12_RX2 — Socket 5, control line B. This line is also the RX/W0&1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_13_TX2 — Socket 5, control line A. This line is also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_14_RX3 — Socket 7, control line B. This line is also the RX/W0&1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_15_TX3 — Socket 7, control line A. This line is also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_16_INT0 — Socket 1, control line D. This is also the interrupt line 0.
- PL_IO_NUM_17_INT1 — Socket 3, control line D. This is also the interrupt line 1.
- PL_IO_NUM_18_INT2 — Socket 5, control line D. This is also the interrupt line 2.
- PL_IO_NUM_19_INT3 — Socket 7, control line D. This is also the interrupt line 3.
- PL_IO_NUM_20_INT4 — Socket 9, control line D. This is also the interrupt line 4.
- PL_IO_NUM_21_INT5 — Socket 11, control line D. This is also the interrupt line 5.
- PL_IO_NUM_22_INT6 — Not connected.
- PL_IO_NUM_23_INT7 — Not connected.
- PL_IO_NUM_24 — LCD connector, data bus, line 0 (P0.0).
- PL_IO_NUM_25 — LCD connector, data bus, line 1 (P0.1).
- PL_IO_NUM_26 — LCD connector, data bus, line 2 (P0.2).
- PL_IO_NUM_27 — LCD connector, data bus, line 3 (P0.3).
- PL_IO_NUM_28 — LCD connector, data bus, line 4 (P0.4).
- PL_IO_NUM_29 — LCD connector, data bus, line 5 (P0.5).
- PL_IO_NUM_30 — LCD connector, data bus, line 6 (P0.6).
- PL_IO_NUM_31 — LCD connector, data bus, line 7 (P0.7).
- PL_IO_NUM_32 — Socket 9, control line A.
- PL_IO_NUM_33 — Socket 9, control line B.
- PL_IO_NUM_34 — Socket 11, control line A.
- PL_IO_NUM_35 — Socket 11, control line B.
- PL_IO_NUM_36 — Keypad connector, return line 1 (for the leftmost button, active low).
- PL_IO_NUM_37 — Keypad connector, return line 2 (active low).
- PL_IO_NUM_38 — Keypad connector, return line 3 (active low).
- PL_IO_NUM_39 — Keypad connector, return line 4 (for the rightmost button, active low).
- PL_IO_NUM_40 — LCD connector, CS line (active low).
- PL_IO_NUM_41 — LCD connector, RD line (active low).
- PL_IO_NUM_42 — LCD connector, WR line (active low).
- PL_IO_NUM_43 — LCD connector, DC line.
- PL_IO_NUM_44 — Keypad connector, reset line (for the sensor IC of the keypad, active low).
- PL_IO_NUM_45_CO — A square wave output controlled by the beep object. This output is driving a buzzer. When the beeper pattern starts playing, the line is configured as…
- PL_IO_NUM_46 — Signal strength LED bar control circuit, reset line.
- PL_IO_NUM_47 — Signal strength LED bar control circuit, clock line.
- PL_IO_NUM_48 — Signal strength LED bar control circuit, data line.
- PL_IO_NUM_49 — Wireless add-on socket, CS line.
- PL_IO_NUM_50 — Wireless add-on socket, DO line.
- PL_IO_NUM_51 — Wireless add-on socket, RST line.
- PL_IO_NUM_52 — Wireless add-on socket, DI line.
- PL_IO_NUM_53 — Wireless add-on socket, CLK line.
- PL_IO_NUM_54 — LCD connector, backlight control line (active low).
- PL_IO_NUM_55 — LCD connector, RST line (active low).
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (LCD data lines D0-7).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## TPP2W(G3) — TPP2(G3) Board

- PLATFORM_ID: 48; rom=1310720 ram=132352; firmware file(s): tios-tpp2w(g3)-5_00_00.bin
- Object headers included: gen, sys-2xxx, tpp2w(g3)_sys, tpp2w(g3)_sock, net, pppoe, io-2xxx, beep, rtc, lcd, kp, ssi, fd, wln, adc, bt, tls, i2c
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, OBJECT_KP KP_ENABLED, OBJECT_FD FD_ENABLED, OBJECT_WLN WLN_ENABLED, OBJECT_BT BT_ENABLED, OBJECT_LCD LCD_ENABLED, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_adc_num`:
- PL_ADC_NUM_0 — ADC channel 0 (mapped to I/O line 40).
- PL_ADC_NUM_1 — ADC channel 1 (mapped to I/O line 41).
- PL_ADC_NUM_2 — ADC channel 2 (mapped to I/O line 42).
- PL_ADC_NUM_3 — ADC channel 3 (mapped to I/O line 43).

`enum pl_io_num`:
- PL_IO_NUM_0 — Socket 1, control line C.
- PL_IO_NUM_1 — Socket 3, control line C.
- PL_IO_NUM_2 — Socket 5, control line C.
- PL_IO_NUM_3 — Socket 7, control line C.
- PL_IO_NUM_4 — Socket 9, control line C.
- PL_IO_NUM_5 — Socket 11, control line C.
- PL_IO_NUM_6 — Not connected.
- PL_IO_NUM_7 — Not connected.
- PL_IO_NUM_8_RX0 — Socket 1, control line B. This line is also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_9_TX0 — Socket 1, control line A. This line is also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_10_RX1 — Socket 3, control line B. This line is also the RX/W0&1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_11_TX1 — Socket 3, control line A. This line is also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_12_RX2 — Socket 5, control line B. This line is also the RX/W0&1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_13_TX2 — Socket 5, control line A. This line is also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_14_RX3 — Socket 7, control line B. This line is also the RX/W0&1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_15_TX3 — Socket 7, control line A. This line is also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_16_INT0 — Socket 1, control line D. This is also the interrupt line 0.
- PL_IO_NUM_17_INT1 — Socket 3, control line D. This is also the interrupt line 1.
- PL_IO_NUM_18_INT2 — Socket 5, control line D. This is also the interrupt line 2.
- PL_IO_NUM_19_INT3 — Socket 7, control line D. This is also the interrupt line 3.
- PL_IO_NUM_20_INT4 — Socket 9, control line D. This is also the interrupt line 4.
- PL_IO_NUM_21_INT5 — Socket 11, control line D. This is also the interrupt line 5.
- PL_IO_NUM_22_INT6 — Not connected.
- PL_IO_NUM_23_INT7 — Not connected.
- PL_IO_NUM_24 — LCD connector, data bus, line 0 (P0.0).
- PL_IO_NUM_25 — LCD connector, data bus, line 1 (P0.1).
- PL_IO_NUM_26 — LCD connector, data bus, line 2 (P0.2).
- PL_IO_NUM_27 — LCD connector, data bus, line 3 (P0.3).
- PL_IO_NUM_28 — LCD connector, data bus, line 4 (P0.4).
- PL_IO_NUM_29 — LCD connector, data bus, line 5 (P0.5).
- PL_IO_NUM_30 — LCD connector, data bus, line 6 (P0.6).
- PL_IO_NUM_31 — LCD connector, data bus, line 7 (P0.7).
- PL_IO_NUM_32 — Socket 9, control line A.
- PL_IO_NUM_33 — Socket 9, control line B.
- PL_IO_NUM_34 — Socket 11, control line A.
- PL_IO_NUM_35 — Socket 11, control line B.
- PL_IO_NUM_36 — Keypad connector, return line 1 (for the leftmost button, active low).
- PL_IO_NUM_37 — Keypad connector, return line 2 (active low).
- PL_IO_NUM_38 — Keypad connector, return line 3 (active low).
- PL_IO_NUM_39 — Keypad connector, return line 4 (for the rightmost button, active low).
- PL_IO_NUM_40 — LCD connector, CS line (active low).
- PL_IO_NUM_41 — LCD connector, RD line (active low).
- PL_IO_NUM_42 — LCD connector, WR line (active low).
- PL_IO_NUM_43 — LCD connector, DC line.
- PL_IO_NUM_44 — Keypad connector, reset line (for the sensor IC of the keypad, active low).
- PL_IO_NUM_45_CO — A square wave output controlled by the beep object. This output is driving a buzzer. When the beeper pattern starts playing, the line is configured as…
- PL_IO_NUM_46 — Signal strength LED bar control circuit, reset line.
- PL_IO_NUM_47 — Signal strength LED bar control circuit, clock line.
- PL_IO_NUM_48 — Signal strength LED bar control circuit, data line.
- PL_IO_NUM_49 — Wireless add-on socket, CS line.
- PL_IO_NUM_50 — Wireless add-on socket, DO line.
- PL_IO_NUM_51 — Wireless add-on socket, RST line.
- PL_IO_NUM_52 — Wireless add-on socket, DI line.
- PL_IO_NUM_53 — Wireless add-on socket, CLK line.
- PL_IO_NUM_54 — LCD connector, backlight control line (active low).
- PL_IO_NUM_55 — LCD connector, RST line (active low).
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (LCD data lines D0-7).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## TPP3N — TPP3 Board + WA2000 Wi-Fi add on

- PLATFORM_ID: 41; rom=983040 ram=22271; firmware file(s): tios-tpp3n-3_70_02.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, beep, rtc, lcd, kp, ssi, fd, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0 — Socket 1, control line C.
- PL_IO_NUM_1 — Socket 5, control line C.
- PL_IO_NUM_2 — Socket 9, control line C.
- PL_IO_NUM_3 — Socket 13, control line C.
- PL_IO_NUM_4 — Socket 3, control line C.
- PL_IO_NUM_5 — Socket 7, control line C.
- PL_IO_NUM_6 — Socket 11, control line C.
- PL_IO_NUM_7 — Socket 15, control line C.
- PL_IO_NUM_8_RX0 — Socket 1, control line B. This line is also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_9_TX0 — Socket 1, control line A. This line is also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_10_RX1 — Socket 5, control line B. This line is also the RX/W0&1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_11_TX1 — Socket 5, control line A. This line is also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_12_RX2 — Socket 9, control line B. This line is also the RX/W0&1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_13_TX2 — Socket 9, control line A. This line is also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_14_RX3 — Socket 13, control line B. This line is also the RX/W0&1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_15_TX3 — Socket 13, control line A. This line is also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL…
- PL_IO_NUM_16_INT0 — Socket 1, control line D. This is also the interrupt line 0.
- PL_IO_NUM_17_INT1 — Socket 5, control line D. This is also the interrupt line 1.
- PL_IO_NUM_18_INT2 — Socket 9, control line D. This is also the interrupt line 2.
- PL_IO_NUM_19_INT3 — Socket 13, control line D. This is also the interrupt line 3.
- PL_IO_NUM_20_INT4 — Socket 3, control line D. This is also the interrupt line 4.
- PL_IO_NUM_21_INT5 — Socket 7, control line D. This is also the interrupt line 5.
- PL_IO_NUM_22_INT6 — Socket 11, control line D. This is also the interrupt line 5.
- PL_IO_NUM_23_INT7 — Socket 15, control line D. This is also the interrupt line 5.
- PL_IO_NUM_24 — Socket 17, control line A.
- PL_IO_NUM_25 — Socket 17, control line B.
- PL_IO_NUM_26 — Socket 17, control line C.
- PL_IO_NUM_27 — Socket 17, control line D.
- PL_IO_NUM_28 — Socket 19, control line A.
- PL_IO_NUM_29 — Socket 19, control line B.
- PL_IO_NUM_30 — Socket 19, control line C.
- PL_IO_NUM_31 — Socket 19, control line D.
- PL_IO_NUM_32 — Socket 3, control line A.
- PL_IO_NUM_33 — Socket 3, control line B.
- PL_IO_NUM_34 — Socket 7, control line A.
- PL_IO_NUM_35 — Socket 7, control line B.
- PL_IO_NUM_36 — Socket 11, control line A.
- PL_IO_NUM_37 — Socket 11, control line B.
- PL_IO_NUM_38 — Socket 13, control line A.
- PL_IO_NUM_39 — Socket 13, control line B.
- PL_IO_NUM_40 — Socket 21, control line A.
- PL_IO_NUM_41 — Socket 21, control line B.
- PL_IO_NUM_42 — Socket 21, control line C.
- PL_IO_NUM_43 — Socket 21, control line D.
- PL_IO_NUM_44 — Socket 25, control line A.
- PL_IO_NUM_45_CO — A square wave output controlled by the beep object. This output is driving a buzzer. When the beeper pattern starts playing, the line is configured as…
- PL_IO_NUM_46 — Signal strength LED bar control circuit, reset line.
- PL_IO_NUM_47 — Signal strength LED bar control circuit, clock line.
- PL_IO_NUM_48 — Signal strength LED bar control circuit, data line.
- PL_IO_NUM_49 — Wireless add-on socket, CS line.
- PL_IO_NUM_50 — Wireless add-on socket, DO line.
- PL_IO_NUM_51 — Wireless add-on socket, RST line.
- PL_IO_NUM_52 — Wireless add-on socket, DI line.
- PL_IO_NUM_53 — Wireless add-on socket, CLK line.
- PL_IO_NUM_54 — Socket 23, control line A.
- PL_IO_NUM_55 — Socket 23, control line B.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (LCD data lines D0-7).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## TPP3W — TPP3 Board

- PLATFORM_ID: 20; rom=983040 ram=22271; firmware file(s): tios-tpp3w-3_60_06.bin
- Object headers included: gen, sys-1xxx, net, pppoe, io-1xxx, beep, rtc, lcd, kp, ssi, fd, wln
- Feature defines: BUFF_PAGE_TYPE byte, BUFF_SIZE_TYPE word
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0 — Socket 1, control line C.
- PL_IO_NUM_1 — Socket 5, control line C.
- PL_IO_NUM_2 — Socket 9, control line C.
- PL_IO_NUM_3 — Socket 13, control line C.
- PL_IO_NUM_4 — Socket 3, control line C.
- PL_IO_NUM_5 — Socket 7, control line C.
- PL_IO_NUM_6 — Socket 11, control line C.
- PL_IO_NUM_7 — Socket 15, control line C.
- PL_IO_NUM_8_RX0 — Socket 1, control line B. This line is also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_9_TX0 — Socket 1, control line A. This line is also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_10_RX1 — Socket 5, control line B. This line is also the RX/W0&1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_11_TX1 — Socket 5, control line A. This line is also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_12_RX2 — Socket 9, control line B. This line is also the RX/W0&1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_13_TX2 — Socket 9, control line A. This line is also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_14_RX3 — Socket 13, control line B. This line is also the RX/W0&1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_15_TX3 — Socket 13, control line A. This line is also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL…
- PL_IO_NUM_16_INT0 — Socket 1, control line D. This is also the interrupt line 0.
- PL_IO_NUM_17_INT1 — Socket 5, control line D. This is also the interrupt line 1.
- PL_IO_NUM_18_INT2 — Socket 9, control line D. This is also the interrupt line 2.
- PL_IO_NUM_19_INT3 — Socket 13, control line D. This is also the interrupt line 3.
- PL_IO_NUM_20_INT4 — Socket 3, control line D. This is also the interrupt line 4.
- PL_IO_NUM_21_INT5 — Socket 7, control line D. This is also the interrupt line 5.
- PL_IO_NUM_22_INT6 — Socket 11, control line D. This is also the interrupt line 5.
- PL_IO_NUM_23_INT7 — Socket 15, control line D. This is also the interrupt line 5.
- PL_IO_NUM_24 — Socket 17, control line A.
- PL_IO_NUM_25 — Socket 17, control line B.
- PL_IO_NUM_26 — Socket 17, control line C.
- PL_IO_NUM_27 — Socket 17, control line D.
- PL_IO_NUM_28 — Socket 19, control line A.
- PL_IO_NUM_29 — Socket 19, control line B.
- PL_IO_NUM_30 — Socket 19, control line C.
- PL_IO_NUM_31 — Socket 19, control line D.
- PL_IO_NUM_32 — Socket 3, control line A.
- PL_IO_NUM_33 — Socket 3, control line B.
- PL_IO_NUM_34 — Socket 7, control line A.
- PL_IO_NUM_35 — Socket 7, control line B.
- PL_IO_NUM_36 — Socket 11, control line A.
- PL_IO_NUM_37 — Socket 11, control line B.
- PL_IO_NUM_38 — Socket 13, control line A.
- PL_IO_NUM_39 — Socket 13, control line B.
- PL_IO_NUM_40 — Socket 21, control line A.
- PL_IO_NUM_41 — Socket 21, control line B.
- PL_IO_NUM_42 — Socket 21, control line C.
- PL_IO_NUM_43 — Socket 21, control line D.
- PL_IO_NUM_44 — Socket 25, control line A.
- PL_IO_NUM_45_CO — A square wave output controlled by the beep object. This output is driving a buzzer. When the beeper pattern starts playing, the line is configured as…
- PL_IO_NUM_46 — Signal strength LED bar control circuit, reset line.
- PL_IO_NUM_47 — Signal strength LED bar control circuit, clock line.
- PL_IO_NUM_48 — Signal strength LED bar control circuit, data line.
- PL_IO_NUM_49 — Wireless add-on socket, CS line.
- PL_IO_NUM_50 — Wireless add-on socket, DO line.
- PL_IO_NUM_51 — Wireless add-on socket, RST line.
- PL_IO_NUM_52 — Wireless add-on socket, DI line.
- PL_IO_NUM_53 — Wireless add-on socket, CLK line.
- PL_IO_NUM_54 — Socket 23, control line A.
- PL_IO_NUM_55 — Socket 23, control line B.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (LCD data lines D0-7).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## TPP3W(G2) — TPP3(G2) Board

- PLATFORM_ID: 26; rom=786432 ram=66816; firmware file(s): tios-tpp3w(g2)-4_02_02.bin
- Object headers included: gen, sys-2xxx, net, pppoe, io-2xxx, beep, rtc, kp, ssi, fd, wln, adc, bt, tls, i2c
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, OBJECT_KP KP_ENABLED, OBJECT_FD FD_ENABLED, OBJECT_WLN WLN_ENABLED, OBJECT_BT BT_ENABLED, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_adc_num`:
- PL_ADC_NUM_0 — ADC channel 0 (mapped to I/O line 40).
- PL_ADC_NUM_1 — ADC channel 1 (mapped to I/O line 41).
- PL_ADC_NUM_2 — ADC channel 2 (mapped to I/O line 42).
- PL_ADC_NUM_3 — ADC channel 3 (mapped to I/O line 43).

`enum pl_io_num`:
- PL_IO_NUM_0 — Socket 1, control line C.
- PL_IO_NUM_1 — Socket 5, control line C.
- PL_IO_NUM_2 — Socket 9, control line C.
- PL_IO_NUM_3 — Socket 13, control line C.
- PL_IO_NUM_4 — Socket 3, control line C.
- PL_IO_NUM_5 — Socket 7, control line C.
- PL_IO_NUM_6 — Socket 11, control line C.
- PL_IO_NUM_7 — Socket 15, control line C.
- PL_IO_NUM_8_RX0 — Socket 1, control line B. This line is also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_9_TX0 — Socket 1, control line A. This line is also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_10_RX1 — Socket 5, control line B. This line is also the RX/W0&1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_11_TX1 — Socket 5, control line A. This line is also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_12_RX2 — Socket 9, control line B. This line is also the RX/W0&1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_13_TX2 — Socket 9, control line A. This line is also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_14_RX3 — Socket 13, control line B. This line is also the RX/W0&1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_15_TX3 — Socket 13, control line A. This line is also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL…
- PL_IO_NUM_16_INT0 — Socket 1, control line D. This is also the interrupt line 0.
- PL_IO_NUM_17_INT1 — Socket 5, control line D. This is also the interrupt line 1.
- PL_IO_NUM_18_INT2 — Socket 9, control line D. This is also the interrupt line 2.
- PL_IO_NUM_19_INT3 — Socket 13, control line D. This is also the interrupt line 3.
- PL_IO_NUM_20_INT4 — Socket 3, control line D. This is also the interrupt line 4.
- PL_IO_NUM_21_INT5 — Socket 7, control line D. This is also the interrupt line 5.
- PL_IO_NUM_22_INT6 — Socket 11, control line D. This is also the interrupt line 5.
- PL_IO_NUM_23_INT7 — Socket 15, control line D. This is also the interrupt line 5.
- PL_IO_NUM_24 — Socket 17, control line A.
- PL_IO_NUM_25 — Socket 17, control line B.
- PL_IO_NUM_26 — Socket 17, control line C.
- PL_IO_NUM_27 — Socket 17, control line D.
- PL_IO_NUM_28 — Socket 19, control line A.
- PL_IO_NUM_29 — Socket 19, control line B.
- PL_IO_NUM_30 — Socket 19, control line C.
- PL_IO_NUM_31 — Socket 19, control line D.
- PL_IO_NUM_32 — Socket 3, control line A.
- PL_IO_NUM_33 — Socket 3, control line B.
- PL_IO_NUM_34 — Socket 7, control line A.
- PL_IO_NUM_35 — Socket 7, control line B.
- PL_IO_NUM_36 — Socket 11, control line A.
- PL_IO_NUM_37 — Socket 11, control line B.
- PL_IO_NUM_38 — Socket 13, control line A.
- PL_IO_NUM_39 — Socket 13, control line B.
- PL_IO_NUM_40 — Socket 21, control line A.
- PL_IO_NUM_41 — Socket 21, control line B.
- PL_IO_NUM_42 — Socket 21, control line C.
- PL_IO_NUM_43 — Socket 21, control line D.
- PL_IO_NUM_44 — Socket 25, control line A.
- PL_IO_NUM_45_CO — A square wave output controlled by the beep object. This output is driving a buzzer. When the beeper pattern starts playing, the line is configured as…
- PL_IO_NUM_46 — Signal strength LED bar control circuit, reset line.
- PL_IO_NUM_47 — Signal strength LED bar control circuit, clock line.
- PL_IO_NUM_48 — Signal strength LED bar control circuit, data line.
- PL_IO_NUM_49 — Wireless add-on socket, CS line.
- PL_IO_NUM_50 — Wireless add-on socket, DO line.
- PL_IO_NUM_51 — Wireless add-on socket, RST line.
- PL_IO_NUM_52 — Wireless add-on socket, DI line.
- PL_IO_NUM_53 — Wireless add-on socket, CLK line.
- PL_IO_NUM_54 — Socket 23, control line A.
- PL_IO_NUM_55 — Socket 23, control line B.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (LCD data lines D0-7).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## TPP3W(G3) — TPP3(G3) Board

- PLATFORM_ID: 47; rom=1310720 ram=132352; firmware file(s): tios-tpp3w(g3)-4_01_08.bin
- Object headers included: gen, sys-2xxx, tpp3w(g3)_sock, net, pppoe, io-2xxx, beep, rtc, kp, ssi, fd, wln, adc, bt, tls, i2c
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, OBJECT_KP KP_ENABLED, OBJECT_FD FD_ENABLED, OBJECT_WLN WLN_ENABLED, OBJECT_BT BT_ENABLED, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_adc_num`:
- PL_ADC_NUM_0 — ADC channel 0 (mapped to I/O line 40).
- PL_ADC_NUM_1 — ADC channel 1 (mapped to I/O line 41).
- PL_ADC_NUM_2 — ADC channel 2 (mapped to I/O line 42).
- PL_ADC_NUM_3 — ADC channel 3 (mapped to I/O line 43).

`enum pl_io_num`:
- PL_IO_NUM_0 — Socket 1, control line C.
- PL_IO_NUM_1 — Socket 5, control line C.
- PL_IO_NUM_2 — Socket 9, control line C.
- PL_IO_NUM_3 — Socket 13, control line C.
- PL_IO_NUM_4 — Socket 3, control line C.
- PL_IO_NUM_5 — Socket 7, control line C.
- PL_IO_NUM_6 — Socket 11, control line C.
- PL_IO_NUM_7 — Socket 15, control line C.
- PL_IO_NUM_8_RX0 — Socket 1, control line B. This line is also the RX/W1in/din input of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_SER…
- PL_IO_NUM_9_TX0 — Socket 1, control line A. This line is also the TX/W1out/dout output of the serial port 0. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_10_RX1 — Socket 5, control line B. This line is also the RX/W0&1in/din input of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_11_TX1 — Socket 5, control line A. This line is also the TX/W1out/dout output of the serial port 1. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_12_RX2 — Socket 9, control line B. This line is also the RX/W0&1in/din input of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_S…
- PL_IO_NUM_13_TX2 — Socket 9, control line A. This line is also the TX/W1out/dout output of the serial port 2. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_14_RX3 — Socket 13, control line B. This line is also the RX/W0&1in/din input of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL_…
- PL_IO_NUM_15_TX3 — Socket 13, control line A. This line is also the TX/W1out/dout output of the serial port 3. When this serial port is in the UART mode (ser.mode= 0- PL…
- PL_IO_NUM_16_INT0 — Socket 1, control line D. This is also the interrupt line 0.
- PL_IO_NUM_17_INT1 — Socket 5, control line D. This is also the interrupt line 1.
- PL_IO_NUM_18_INT2 — Socket 9, control line D. This is also the interrupt line 2.
- PL_IO_NUM_19_INT3 — Socket 13, control line D. This is also the interrupt line 3.
- PL_IO_NUM_20_INT4 — Socket 3, control line D. This is also the interrupt line 4.
- PL_IO_NUM_21_INT5 — Socket 7, control line D. This is also the interrupt line 5.
- PL_IO_NUM_22_INT6 — Socket 11, control line D. This is also the interrupt line 5.
- PL_IO_NUM_23_INT7 — Socket 15, control line D. This is also the interrupt line 5.
- PL_IO_NUM_24 — Socket 17, control line A.
- PL_IO_NUM_25 — Socket 17, control line B.
- PL_IO_NUM_26 — Socket 17, control line C.
- PL_IO_NUM_27 — Socket 17, control line D.
- PL_IO_NUM_28 — Socket 19, control line A.
- PL_IO_NUM_29 — Socket 19, control line B.
- PL_IO_NUM_30 — Socket 19, control line C.
- PL_IO_NUM_31 — Socket 19, control line D.
- PL_IO_NUM_32 — Socket 3, control line A.
- PL_IO_NUM_33 — Socket 3, control line B.
- PL_IO_NUM_34 — Socket 7, control line A.
- PL_IO_NUM_35 — Socket 7, control line B.
- PL_IO_NUM_36 — Socket 11, control line A.
- PL_IO_NUM_37 — Socket 11, control line B.
- PL_IO_NUM_38 — Socket 13, control line A.
- PL_IO_NUM_39 — Socket 13, control line B.
- PL_IO_NUM_40 — Socket 21, control line A.
- PL_IO_NUM_41 — Socket 21, control line B.
- PL_IO_NUM_42 — Socket 21, control line C.
- PL_IO_NUM_43 — Socket 21, control line D.
- PL_IO_NUM_44 — Socket 25, control line A.
- PL_IO_NUM_45_CO — A square wave output controlled by the beep object. This output is driving a buzzer. When the beeper pattern starts playing, the line is configured as…
- PL_IO_NUM_46 — Signal strength LED bar control circuit, reset line.
- PL_IO_NUM_47 — Signal strength LED bar control circuit, clock line.
- PL_IO_NUM_48 — Signal strength LED bar control circuit, data line.
- PL_IO_NUM_49 — Wireless add-on socket, CS line.
- PL_IO_NUM_50 — Wireless add-on socket, DO line.
- PL_IO_NUM_51 — Wireless add-on socket, RST line.
- PL_IO_NUM_52 — Wireless add-on socket, DI line.
- PL_IO_NUM_53 — Wireless add-on socket, CLK line.
- PL_IO_NUM_54 — Socket 23, control line A.
- PL_IO_NUM_55 — Socket 23, control line B.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 24-31 (LCD data lines D0-7).

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to I/O line 16).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to I/O line 17).
- PL_INT_NUM_2 — Interrupt line 2 (mapped to I/O line 18).
- PL_INT_NUM_3 — Interrupt line 3 (mapped to I/O line 19).
- PL_INT_NUM_4 — Interrupt line 4 (mapped to I/O line 20).
- PL_INT_NUM_5 — Interrupt line 5 (mapped to I/O line 21).
- PL_INT_NUM_6 — Interrupt line 6 (mapped to I/O line 22).
- PL_INT_NUM_7 — Interrupt line 7 (mapped to I/O line 23).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## WM2000 — WM2000 Module

- PLATFORM_ID: 44; rom=1728512 ram=59392; firmware file(s): app0, tios-wm2000-4_03_08.bin
- Object headers included: gen, sys-2xxx, wm2000_ser, wm2000_sys, wm2000_wln, wm2000_sock, io-1xxx, adc, beep, bt, dhcp, fd, kp, pwm, rtc, ssi, wln, tls
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, OBJECT_KP KP_ENABLED, OBJECT_FD FD_ENABLED, OBJECT_WLN WLN_ENABLED, OBJECT_BT BT_ENABLED, OBJECT_LCD LCD_ENABLED, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_adc_num`:
- PL_ADC_NUM_0 — ADC channel 0 (mapped to GPIO line 4).
- PL_ADC_NUM_1 — ADC channel 1 (mapped to GPIO line 5).
- PL_ADC_NUM_2 — ADC channel 2 (mapped to GPIO line 6).

`enum pl_pwm_num`:
- PL_PWM_NUM_0 — PWM channel 0 (mapped to GPIO line 0).
- PL_PWM_NUM_1 — PWM channel 1 (mapped to GPIO line 1).
- PL_PWM_NUM_2 — PWM channel 2 (mapped to GPIO line 2).
- PL_PWM_NUM_3 — PWM channel 3 (mapped to GPIO line 3).
- PL_PWM_NUM_4 — PWM channel 4 (mapped to GPIO line 4).
- PL_PWM_NUM_5 — PWM channel 5 (mapped to GPIO line 5).
- PL_PWM_NUM_6 — PWM channel 6 (mapped to GPIO line 6).
- PL_PWM_NUM_7 — PWM channel 7 (mapped to GPIO line 7).
- PL_PWM_NUM_8 — PWM channel 8 (mapped to GPIO line 8).

`enum pl_io_num`:
- PL_IO_NUM_0_RX0 — General-purpose I/O line 0 (P0.0), also the RX/W1in/din input of the serial port 0. When this serial port 0 is in the UART mode (ser.mode = 0- PL_SER_…
- PL_IO_NUM_1_TX0 — General-purpose I/O line 1 (P0.1), also the TX/W1out/dout output of the serial port 0. When this serial port 0 is in the UART mode (ser.mode = 0- PL_S…
- PL_IO_NUM_2_INT0 — General-purpose I/O line 2 (P0.2), also the interrupt line 0.
- PL_IO_NUM_3_INT1 — General-purpose I/O line 3 (P0.3), also the interrupt line 1.
- PL_IO_NUM_4 — General-purpose I/O line 4 (P0.4).
- PL_IO_NUM_5 — General-purpose I/O line 5 (P0.5).
- PL_IO_NUM_6 — General-purpose I/O line 6 (P0.6).
- PL_IO_NUM_7_RX1 — General-purpose I/O line 7 (P0.7), also the RX/W1in/din input of serial port 1, and the RX line of the debug serial port. Enabling the serial debuggin…
- PL_IO_NUM_8_TX1 — General-purpose I/O line 8 (P1.0), also the TX/W1out/dout output of serial port 1, and the TX line of the debug serial port. Enabling the serial debug…
- PL_IO_NUM_9 — General-purpose I/O line 9 (P1.1), also a square wave output controlled by the beep. object.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7. This is a virtual port. During reads (io.portget, io.portstate(g)) and writes (io.portset, io.portstate(s)), eac…
- PL_IO_PORT_NUM_1 — 8-bit port 1, contains I/O lines 8 and 9. This is a virtual port. During reads (io.portget, io.portstate(g)) and writes (io.portset, io.portstate(s)),…

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to GPIO line 2).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to GPIO line 3).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## WS1101 — WS1101

- PLATFORM_ID: 45; rom=1728512 ram=59392; firmware file(s): —
- Object headers included: gen, sys-2xxx, ws1101_ser, ws1101_sys, ws1101_wln, io-1xxx, beep, bt, dhcp, fd, rtc, ssi, wln, tls
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, OBJECT_KP KP_ENABLED, OBJECT_FD FD_ENABLED, OBJECT_WLN WLN_ENABLED, OBJECT_BT BT_ENABLED, OBJECT_LCD LCD_ENABLED, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0_RX0 — General-purpose I/O line 0 (P0.0), also the RX/W1in/din input of serial port 0. When this serial port is in UART mode (ser.mode = 0- PL_SER_MODE_UART …
- PL_IO_NUM_1_TX0 — General-purpose I/O line 1 (P0.1), also the TX/W1out/dout output of serial port 0. When this serial port is in UART mode (ser.mode = 0- PL_SER_MODE_UA…
- PL_IO_NUM_2_CTS_INT0 — General-purpose I/O line 2 (P0.2), also the interrupt line 0. In RS232 and RS422 mode this line is used as serial CTS input. This line is not used in …
- PL_IO_NUM_3_RTS_INT1 — General-purpose I/O line 3 (P0.3), also the interrupt line 1. In RS232 and RS422 mode this line is used as serial RTS output. This line is used in RS4…
- PL_IO_NUM_4 — Not implemented.
- PL_IO_NUM_5_EXPANDER_SCL — General-purpose I/O line 5 (P0.5). This line is used as SCL in I2C communications with an MCP23008 IO expander. This IO expander is used to control th…
- PL_IO_NUM_6_EXPANDER_SDA — General-purpose I/O line 6 (P0.6). This line is used as SDA in I2C communications with an MCP23008 IO expander. This IO expander is used to control th…
- PL_IO_NUM_7_RX1_DSR — General-purpose I/O line 7 (P0.7) also the RX/W1in/din input of serial port 1 or RX of the debug serial port. When this serial port is in UART mode (s…
- PL_IO_NUM_8_TX1_DTR — General-purpose I/O line 8 (P1.0), also the TX/W1out/dout output of serial port 1 or TX of the debug serial port. When this serial port is in UART mod…
- PL_IO_NUM_9_BUZZER — General-purpose I/O line 9 (P1.1). This output is driving a buzzer.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7. This is a virtual port. During reads (io.portget, io.portstate(g)) and writes (io.portset, io.portstate(s)), eac…
- PL_IO_PORT_NUM_1 — 8-bit port 1, contains I/O lines 8-11. This is a virtual port. During reads (io.portget, io.portstate(g)) and writes (io.portset, io.portstate(s)), ea…

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to GPIO line 2).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to GPIO line 3).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## WS1102 — WS1102

- PLATFORM_ID: 46; rom=1728512 ram=59392; firmware file(s): app0, app1, tios-ws1102-4_03_08.bin
- Object headers included: gen, sys-2xxx, ws1102_ser, ws1102_sys, ws1102_wln, io-1xxx, beep, bt, dhcp, fd, rtc, ssi, wln, tls
- Feature defines: BUFF_PAGE_TYPE word, BUFF_SIZE_TYPE dword, EXTENDED_SOCK 1, SER_7BIT_LIMITATION 1, PLATFORM_TYPE_32 1, OBJECT_KP KP_ENABLED, OBJECT_FD FD_ENABLED, OBJECT_WLN WLN_ENABLED, OBJECT_BT BT_ENABLED, OBJECT_LCD LCD_ENABLED, EXTENDED_FD 1
- TIDE project templates: 1 - Empty BASIC Project, 2 - Empty C Project, 3 - Empty BASIC and C Project

`enum pl_sock_interfaces`:
- PL_SOCK_INTERFACE_NULL — Null interface (no connection possible).
- PL_SOCK_INTERFACE_NET — Ethernet interface.
- PL_SOCK_INTERFACE_WLN — Wi-Fi interface.
- PL_SOCK_INTERFACE_PPP — PPP interface on a serial port.
- PL_SOCK_INTERFACE_PPPOE — PPPoE interface.

`enum pl_io_num`:
- PL_IO_NUM_0_RX0 — General-purpose I/O line 0 (P0.0), also the RX/W1in/din input of the serial port 0. When this serial port 0 is in the UART mode (ser.mode = 0- PL_SER_…
- PL_IO_NUM_1_TX0 — General-purpose I/O line 1 (P0.1), also the TX/W1out/dout output of the serial port 0. When this serial port 0 is in the UART mode (ser.mode = 0- PL_S…
- PL_IO_NUM_2_CTS_INT0 — General-purpose I/O line 2 (P0.2), also the interrupt line 0. In the RS232 and RS422 modes, this line is used as the CTS input of the serial port 0. T…
- PL_IO_NUM_3_RTS_INT1 — General-purpose I/O line 3 (P0.3), also the interrupt line 1. In the RS232 and RS422 modes, this line is used as the RTS output of the serial port 0. …
- PL_IO_NUM_4 — On the WS1102 device this line is not in use.
- PL_IO_NUM_5_EXPANDER_SCL — General-purpose I/O line 5 (P0.5). This line is used as the SCL line of the I2C port. The I2C port is connected to the MCP23008 IO expander. IO lines …
- PL_IO_NUM_6_EXPANDER_SDA — General-purpose I/O line 6 (P0.6). This line is used as the SDA line of the I2C port. The I2C port is connected to the MCP23008 IO expander. IO lines …
- PL_IO_NUM_7_RX1_DSR — General-purpose I/O line 7 (P0.7), also the RX/W1in/din input of serial port 1, and the RX line of the debug serial port. In the RS232 mode, this line…
- PL_IO_NUM_8_TX1_DTR — General-purpose I/O line 8 (P1.0), also the TX/W1out/dout output of serial port 1, and the TX line of the debug serial port. In the RS232 mode, this l…
- PL_IO_NUM_9_BUZZER — General-purpose I/O line 9 (P1.1), also a square wave output controlled by the beep. object. This output is driving a buzzer.
- PL_IO_NULL — This is a NULL line that does not physically exist. The state of this line is always detected as LOW. Setting this line has no effect.

`enum pl_io_port_num`:
- PL_IO_PORT_NUM_0 — 8-bit port 0, contains I/O lines 0-7. This is a virtual port. During reads (io.portget, io.portstate(g)) and writes (io.portset, io.portstate(s)), eac…
- PL_IO_PORT_NUM_1 — 8-bit port 1, contains I/O lines 8 and 9. This is a virtual port. During reads (io.portget, io.portstate(g)) and writes (io.portset, io.portstate(s)),…

`enum pl_int_num`:
- PL_INT_NUM_0 — Interrupt line 0 (mapped to GPIO line 2).
- PL_INT_NUM_1 — Interrupt line 1 (mapped to GPIO line 3).
- PL_INT_NULL — This is a NULL interrupt line that does not physically exist.

## em203 — EM203 Module

- PLATFORM_ID: ?; rom=63488 ram=20480; firmware file(s): tios-em202-2_05_12.bin
- Object headers included: 
- Feature defines: 
- TIDE project templates: 1 - Empty Project, 2 - DHCP Project, 3 - DHCP+setup Project

`enum off_on`:
- PL_OFF — GENERIC PLATFORM CONSTANT
- PL_ON — GENERIC PLATFORM CONSTANT

`enum no_yes`:
- NO — GENERIC PLATFORM CONSTANT
- YES — GENERIC PLATFORM CONSTANT

`enum dis_en`:
- DISABLED — GENERIC PLATFORM CONSTANT
- ENABLED — GENERIC PLATFORM CONSTANT

`enum low_high`:
- LOW — GENERIC PLATFORM CONSTANT
- HIGH — GENERIC PLATFORM CONSTANT

`enum ok_ng`:
- OK — GENERIC PLATFORM CONSTANT
- NG — GENERIC PLATFORM CONSTANT

`enum pl_sock_state`:
- PL_SST_CLOSED — Connection is closed (and haven't been opened yet, it is a post-powerup state). Applies both to UDP and TCP.
- PL_SST_CL_PCLOSED — Connection is closed (it was a passive close). Applies only to TCP.
- PL_SST_CL_ACLOSED — Connection is closed (it was an active close by the application). Applies only to TCP.
- PL_SST_CL_PRESET_POPENING — Connection is closed (it was a passive reset during a passive open). Applies only to TCP.
- PL_SST_CL_PRESET_AOPENING — Connection is closed (it was a passive reset during an active open). Applies only to TCP.
- PL_SST_CL_PRESET_EST — Connection is closed (it was a passive reset while in "connection established" state). Applies only to TCP.
- PL_SST_CL_PRESET_PCLOSING — Connection is closed (it was a passive reset while performing a passive close). Applies only to TCP.
- PL_SST_CL_PRESET_ACLOSING — Connection is closed (it was a passive reset while performing an active close). Applies only to TCP.
- PL_SST_CL_PRESET_STRANGE — Connection is closed (it was a passive reset, no further details available). Applies only to TCP.
- PL_SST_CL_ARESET_CMD — Connection is closed (it was an active reset issued by the application). Applies only to TCP.
- PL_SST_CL_ARESET_RE_PO — Connection is closed (it was an active reset issued because of excessive retransmission attempts during a passive open). Applies only to TCP.
- PL_SST_CL_ARESET_RE_AO — Connection is closed (it was an active reset issued because of excessive retransmission attempts during an active open). Applies only to TCP.
- PL_SST_CL_ARESET_RE_EST — Connection is closed (it was an active reset issued because of excessive retransmission attempts while in "connection established" state). Applies onl…
- PL_SST_CL_ARESET_RE_PC — Connection is closed (it was an active reset issued because of excessive retransmission attempts during a passive close). Applies only to TCP.
- PL_SST_CL_ARESET_RE_AC — Connection is closed (it was an active reset issued because of excessive retransmission attempts during a passive open). Applies only to TCP.
- PL_SST_CL_ARESET_TOUT — Connection is closed (it was an active reset caused by connection timeout, i.e. no data was exchanged for sock.connectiontout number of seconds). Appl…
- PL_SST_CL_ARESET_DERR — Connection is closed (it was an active reset caused by a data exchange error). Applies only to TCP.
- PL_SST_CL_DISCARDED_CMD — Connection is closed (it was discarded by the application). Applies both to UDP and TCP.
- PL_SST_CL_DISCARDED_PO_WCS — Connection is closed (it was discarded because an error in connection sequence was detected during a passive open). Applies only to TCP.
- PL_SST_CL_DISCARDED_AO_WCS — Connection is closed (it was discarded because an error in connection sequence was detected during an active open). Applies only to TCP.
- PL_SST_CL_DISCARDED_ARPFL — Connection is closed (it was discarded because the device has failed to resolve the IP address of the destination during an active open, i.e. there wa…
- PL_SST_CL_DISCARDED_TOUT — Connection is closed (it was discarded because connection has timed out, i.e. no data was exchanged for sock.connectiontout number of seconds). Applie…
- PL_SST_ARP — ARP resolution is an progress (it is an active open). Applies both to UDP and TCP.
- PL_SST_PO — Connection is being established (it is a passive open). Applies only to TCP.
- PL_SST_AO — Connection is being established (it is an active open). Applies only to TCP.
- PL_SST_EST — Connection is established (generic, includes both passive and active open). Applies both to UDP and TCP.
- PL_SST_EST_POPENED — Connection is established (it was a passive open). Applies both to UDP and TCP.
- PL_SST_EST_AOPENED — Connection is established (it was an active open). Applies both to UDP and TCP.
- PL_SST_PC — Connection is being closed (it is a passive close). Applies only to TCP.
- PL_SST_AC — Connection is being closed (it is an active close). Applies only to TCP.

`enum pl_sock_state_simple`:
- PL_SSTS_CLOSED — Connection is closed. Applies both to UDP and TCP.
- PL_SSTS_ARP — ARP resolution is an progress (it is an active open). Applies both to UDP and TCP.
- PL_SSTS_PO — Connection is being established (it is a passive open). Applies only to TCP.
- PL_SSTS_AO — Connection is being established (it is an active open). Applies only to TCP.
- PL_SSTS_EST — Connection is established. Applies both to UDP and TCP.
- PL_SSTS_PC — Connection is being closed (it is a passive close). Applies only to TCP.
- PL_SSTS_AC — Connection is being closed (it is an active close). Applies only to TCP.

`enum pl_sys_mode`:
- PL_SYS_MODE_RELEASE — Debugging is not possible, application execution starts immediately after device powers up. Severe errors such as "divizion by zero" are ignored and d…
- PL_SYS_MODE_DEBUG — Debug mode in which it is possible to cross-debug the application (under the control of TIDE software). Application execution is not started automatic…

`enum pl_sys_reset_type`:
- PL_SYS_RESET_TYPE_INTERNAL — The most recent reset was generated internally.
- PL_SYS_RESET_TYPE_EXTERNAL — The most recent reset was generated externally (through RST pin or power cycle).

`enum pl_ser_mode`:
- PL_SER_MODE_UART — (DEFAULT). UART mode, suitable for RS232, RS422, RS485, etc. communications in full-duplex or half-duplex mode (see ser.interface). Data is transmitte…
- PL_SER_MODE_WIEGAND — Wiegand mode, suitable for sending to or receiving data from any standard Wiegand device. Data transmission is through pins W0out and W1out, reception…
- PL_SER_MODE_CLOCKDATA — Clock/data mode, suitable for sending to or receiving data from any standard clock/data (or magstripe) device. Data transmission is through pins cout …

`enum pl_ser_interface`:
- PL_SER_SI_FULLDUPLEX — (DEFAULT). Full-duplex mode, suitable for RS232, RS422, or four-wire RS485 communications. RTS output (together with CTS input) can be used for option…
- PL_SER_SI_HALFDUPLEX — Half-duplex mode, suitable for two-wire RS485 communications. RTS line is used for direction control. Direction control polarity can be set through se…

`enum pl_ser_dircontrol`:
- PL_SER_DCP_LOWFORINPUT — (DEFAULT). Specifies (for UART/half-duplex mode of the serial port) that the RTS output will be LOW when the serial port is ready to RX data and HIGH …
- PL_SER_DCP_HIGHFORINPUT — Specifies (for UART/half-duplex mode of the serial port) that the RTS output will be HIGH when the serial port is ready to RX data and LOW when the se…

`enum pl_ser_parity`:
- PL_SER_PR_NONE — (DEFAULT). No parity bit to be transmitted.
- PL_SER_PR_EVEN — Even parity.
- PL_SER_PR_ODD — Odd parity.
- PL_SER_PR_MARK — Parity bit always at "1". Also can be used to emulate second stop bit (there is no separate property to explicitely select the number of stop bits).
- PL_SER_PR_SPACE — Parity bit always at "0".

`enum pl_ser_bits`:
- PL_SER_BB_7 — Data word TXed/RXed by the serial port is to contain 7 data bits.
- PL_SER_BB_8 — (DEFAULT). Data word TXed/RXed by the serial port is to contain 8 data bits.

`enum pl_ser_esctype`:
- PL_SER_ET_DISABLED — Recognition of serial escape sequences disabled.
- PL_SER_ET_TYPE1 — Escape sequences of type1 are to be recognized. Type1 escape sequence is "prev_charECECEC", where "EC" is escape character defined by the ser.escchar …
- PL_SER_ET_TYPE2 — Escape sequences of type2 are to be recognized. Type2 escape sequence is "EC OC", where "EC" is escape character defined by the ser.escchar property a…

`enum pl_net_linkstate`:
- PL_NET_LINKSTAT_NOLINK — No physical Ethernet link exists at the moment (the Ethernet port of the device is not connected to a hub).
- PL_NET_LINKSTAT_10BASET — The Ethernet port of the device is linked to a hub (or directly to another device) at 10Mbit/sec.
- PL_NET_LINKSTAT_100BASET — The Ethernet port of the device is linked to a hub (or directly to another device) at 100Mbit/sec.

`enum pl_sock_inconmode`:
- PL_SOCK_INCONMODE_NONE — The socket does not accept any incoming connections.
- PL_SOCK_INCONMODE_SPECIFIC_IPPORT — The socket will only accept an incoming connection from specific IP (matching sock.targetip) and specific port (matching sock.targetport)
- PL_SOCK_INCONMODE_SPECIFIC_IP_ANY_PORT — The socket will only accept an incoming connection from specific IP (matching sock.targetip), but any port.
- PL_SOCK_INCONMODE_ANY_IP_ANY_PORT — The socket will accept an incoming connection from any IP and any port.

`enum pl_sock_reconmode`:
- PL_SOCK_RECONMODE_0 — For UDP: Reconnects accepted only from the same IP as the one already engaged in the current connection with this socket, but any port; port switchove…
- PL_SOCK_RECONMODE_1 — For UDP: Reconnects accepted from any IP, any port; port switchover will not happen. TCP: reconnects accepted only from the same IP and port as the on…
- PL_SOCK_RECONMODE_2 — For UDP: Reconnects accepted only from the same IP as the one already engaged in the current connection with this socket, but any port; port switchove…
- PL_SOCK_RECONMODE_3 — For UDP: Reconnects accepted from any IP, any port; port switchover will happen. TCP: reconnects accepted from any IP, any port.

`enum pl_sock_protocol`:
- PL_SOCK_PROTOCOL_UDP — Specifies UDP transport protocol for the socket.
- PL_SOCK_PROTOCOL_TCP — Specifies TCP transport protocol for the socket.

`enum pl_io_num`:
- PL_IO_NUM_0 — Selects general-purpose I/O line 0. Only available on the EM200.
- PL_IO_NUM_1 — Selects general-purpose I/O line 1. Only available on the EM200.
- PL_IO_NUM_2_DSR — Selects general-purpose I/O line 2. This is also a DSR input of serial port 0. On EM202 and EM200 works as input/output. On EM202-EV and DS202 works a…
- PL_IO_NUM_3_DTR — Selects general-purpose I/O line 3. This is also a DTR output of serial port 0. On EM202 and EM200 works as input/output. On EM202-EV and DS202 works …
- PL_IO_NUM_4_CTS — Selects general-purpose I/O line 4. This is also a CTS input of serial port 0. On EM202 and EM200 works as input/output. Cannot be set through io.stat…
- PL_IO_NUM_5_RTS — Selects general-purpose I/O line 5. This is also a RTS output of serial port 0. On EM202 and EM200 works as input/output. Cannot be set through io.sta…
- PL_IO_NUM_6 — Selects general-purpose I/O line 6. Only available on the EM200.
- PL_IO_NUM_7 — Selects general-purpose I/O line 7. Only available on the EM200.
- PL_IO_NUM_8 — Selects general-purpose I/O line 8. Only available on the EM200.

`enum pl_pat_int`:
- PL_PAT_NOINT — Tells the pat.play method that the new pattern can only be loaded if no pattern is playing at the moment (no interrupting of previous pattern).
- PL_PAT_CANINT — Tells the pat.play method that the new pattern can be loaded even if another pattern is currently playing (previous pattern can be interrupted).
