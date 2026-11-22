#!/usr/bin/env bash
# Run one stage of the reels pipeline for a content module.
#   REELS_WORK     workspace (default ./reels_work, prepared by setup.sh)
#   REELS_CONTENT  folder that holds your episodes_*.py        (default: cwd)
#   EPMOD          module name, e.g. episodes_prac             (required)
#   SERIESDIR      output folder inside the workspace          (default: series)
#   ENGINE         v1 = card theme (cream/sky) | v2 = paper/orange motion theme   (default v1)
#   BRAND          small tag text on every reel, e.g. "사회복지실천론"
#   v1 only: GROUND (#fff6e5) BLOB_A BLOB_B  background colors
# Usage: run_pipeline.sh <tts|html|audio|check|snapshot|render|all> [episode numbers...]
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
export REELS_WORK=${REELS_WORK:-$PWD/reels_work}
export REELS_CONTENT=${REELS_CONTENT:-$PWD}
: "${EPMOD:?set EPMOD to the content module name}"
export SERIESDIR=${SERIESDIR:-series}
ENGINE=${ENGINE:-v1}
PY="$REELS_WORK/venv/bin/python"
[ -f /root/.ccr/ca-bundle.crt ] && export SSL_CERT_FILE=/root/.ccr/ca-bundle.crt
if [ -f /root/.claude/skills/hyperframes/scripts/plugin-cli.mjs ]; then HF="node /root/.claude/skills/hyperframes/scripts/plugin-cli.mjs"; else HF="npx --yes hyperframes@0.9.75"; fi
STAGE=${1:-all}; shift || true
OUT="$REELS_WORK/$SERIESDIR"
eps() { if [ "$#" -gt 0 ]; then echo "$@"; else ls -d "$OUT"/ep* 2>/dev/null | sed 's|.*/ep||' | sort -n | tr '\n' ' '; fi; }
html() { if [ "$ENGINE" = v2 ]; then "$PY" "$HERE/build_v2.py" html "$@"; else "$PY" "$HERE/build_ep.py" html "$@"; fi; }
case "$STAGE" in
  tts)   "$PY" "$HERE/build_ep.py" tts "$@" ;;
  html)  html "$@" ;;
  audio) "$PY" "$HERE/build_ep.py" audio "$@" ;;
  check)
    for n in $(eps "$@"); do echo $n; done | xargs -P 4 -I{} sh -c "cd '$OUT/ep{}' && timeout 420 $HF check --safe-zone reels --json > check.out 2> check.err"
    "$PY" "$HERE/summarize_checks.py" "$OUT" $(eps "$@") ;;
  snapshot)  # contact sheet at ~mid of every narration line
    for n in $(eps "$@"); do
      ( cd "$OUT/ep$n" && ATS=$("$PY" -c "import json;t=json.load(open('timing.json'));a=[round(s+min(2.0,(e-s)*0.75),2) for s,e in zip(t['starts'],t['ends'])];a.append(round(t['total']-0.5,2));print(','.join(map(str,a)))" ) \
        && timeout 420 $HF snapshot --at "$ATS" > snap.out 2> snap.err; grep -h contact-sheet snap.out | awk '{print $1}' ) &
    done; wait ;;
  render)
    rm -f "$OUT/render_status.txt"
    for n in $(eps "$@"); do echo $n; done | xargs -P 3 -I{} sh -c "cd '$OUT/ep{}' && timeout 1800 $HF render --output '$OUT/reel_ep{}.mp4' > render.out 2> render.err; echo ep{} exit=\$? >> '$OUT/render_status.txt'"
    sort -V "$OUT/render_status.txt" ;;
  all)
    "$HERE/run_pipeline.sh" tts "$@"; "$HERE/run_pipeline.sh" html "$@"; "$HERE/run_pipeline.sh" audio "$@"; "$HERE/run_pipeline.sh" check "$@" ;;
  *) echo "unknown stage $STAGE"; exit 1 ;;
esac
