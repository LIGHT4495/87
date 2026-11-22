# Summarize HyperFrames `check --json` results for several episodes.
import json, sys
out = sys.argv[1]
for n in sys.argv[2:]:
    try:
        d = json.load(open(f"{out}/ep{n}/check.out"))
    except Exception as e:
        print(f"ep{n}: no report ({e})"); continue
    items = [(sec, f["severity"], f["code"], f.get("time"), f["message"][:90])
             for sec in ("runtime", "layout", "contrast", "craft", "audio")
             for f in d.get(sec, {}).get("findings", []) if f["severity"] != "info"]
    print(f"ep{n}: ok={d['ok']} findings={len(items)}")
    for it in items:
        print("   ", *it)
