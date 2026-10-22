// Refresh data/registry.json from the AppBlocks editor (run in the browser console / javascript tool
// on https://app.appblocks.io with any project open). Downloads appblocks_defs.json; then:
//     python3 scripts/build_registry.py appblocks_defs.json
// Read-only: it only calls the editor's own getList()/getItem() and changes nothing in the account.
// Module numbers change between AppBlocks builds, so registries are found by shape, and kinds by their ids.
(async () => {
  let req;
  self.webpackChunk_appblocks_frontend.push([[Math.random()], {}, r => { req = r; }]);
  const regs = [];
  for (const id of Object.keys(req.m)) {
    let ex; try { ex = req(id); } catch (e) { continue; }
    for (const v of Object.values(ex || {})) {
      if (typeof v === 'function' && typeof v.getList === 'function' && typeof v.getItem === 'function') regs.push(v);
    }
  }
  const kindOf = ids => ids.some(i => /^node_/.test(i)) ? 'nodes'
    : ids.some(i => /^tibbit_\d/.test(i)) ? 'tibbits'
    : ids.includes('variable') || ids.includes('tbl_table') ? 'items'
    : ids.some(i => /_widget$/.test(i)) ? 'widgets'
    : ids.includes('global_vars') || ids.includes('boardsetting') ? 'features'
    : ids.includes('sock') || ids.includes('stg') ? 'libraries' : 'peripherals';
  const port = p => ({ id: p.portId ?? p.id, n: p.name, p: (p.params || []).map(q => ({ n: q.name, t: q.dataType })) });
  const set = s => ({ id: s.id, n: s.name, t: s.settingType, refId: s.refId, default: s.default, required: s.required,
    readonly: s.readonly, min: s.min, max: s.max, o: (s.options || []).map(o => (typeof o === 'object' ? { v: o.value, n: o.name } : { v: o })) });
  const COMMON = new Set(['ID', 'DISPLAY_NAME', 'FEATURE', 'X', 'Y', 'INPUTS', 'OUTPUTS', 'GROUP']);
  const one = it => it && ({
    name: it.name, description: it.description, linkedFeature: it.linkedFeature, isAsync: it.isAsync,
    singleInstance: it.singleInstance, featureType: it.featureType, priority: it.priority, devices: it.devices,
    unsupportedDevices: it.unsupportedDevices, requirements: it.requirements, capabilities: it.capabilities,
    in: it.inputs && it.inputs.map(port), out: it.outputs && it.outputs.map(port),
    set: (it.settings || []).filter(s => !COMMON.has(s.id)).map(set)
  });
  const dump = {};
  for (const R of regs) {
    let list; try { list = R.getList(); } catch (e) { continue; }
    const ids = (list || []).map(x => (typeof x === 'string' ? x : x.id)).filter(Boolean);
    if (!ids.length) continue;
    const kind = kindOf(ids);
    dump[kind] = dump[kind] || {};
    for (const id of ids) {
      const e = {};
      for (const rt of ['tios', 'zephyr', 'micropython']) {
        try { e[rt] = one(R.getItem(id, { runtime: rt })); } catch (err) { e[rt] = { err: String(err) }; }
      }
      // keep other runtimes only when they differ from tios
      for (const rt of ['zephyr', 'micropython']) if (JSON.stringify(e[rt]) === JSON.stringify(e.tios)) delete e[rt];
      dump[kind][id] = e;
    }
  }
  // palette: the source literal [{name:"System",nodes:[...]}, ...] inside the bundle that defines it
  let paletteSrc = '';
  for (const id of Object.keys(req.m)) {
    const src = req.m[id].toString();
    const m = src.match(/\[\{name:"System",nodes:\[[\s\S]*?name:"Hidden",nodes:\[[^\]]*\]\}\]/);
    if (m) { paletteSrc = m[0]; break; }
  }
  const out = { snapshot: new Date().toISOString().slice(0, 10), dump, paletteSrc };
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([JSON.stringify(out)], { type: 'application/json' }));
  a.download = 'appblocks_defs.json'; a.click();
  return Object.fromEntries(Object.entries(dump).map(([k, v]) => [k, Object.keys(v).length]));
})();
