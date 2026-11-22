#!/usr/bin/env bash
# 현재 환경변수(EPMOD/SERIESDIR 등)의 시리즈에서 mp4가 아직 없는 편만 렌더링한다.
# 클라우드 컨테이너가 약 13~15분마다 재시작되며 백그라운드 렌더링이 끊기므로, 끊기면 이 스크립트를 다시 실행한다.
#   setsid nohup bash scripts/render_missing.sh >/dev/null 2>&1 </dev/null &
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
d="${REELS_WORK:?}/${SERIESDIR:?}"
miss=""
for e in $(ls -d "$d"/ep* | sed 's|.*/ep||' | sort -n); do [ -f "$d/reel_ep$e.mp4" ] || miss="$miss $e"; done
[ -z "$miss" ] && { echo "all rendered"; exit 0; }
echo "rendering:$miss"
bash "$HERE/run_pipeline.sh" render $miss
