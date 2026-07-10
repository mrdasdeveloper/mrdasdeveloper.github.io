#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ "${1:-}" = "--city-only" ]; then
  python3 "$DIR/page_generator.py" --city-pages --hubs --fix-meta
elif [ $# -eq 0 ]; then
  python3 "$DIR/page_generator.py" --all --fix-meta
else
  python3 "$DIR/page_generator.py" --city-pages --hubs --country "$1" --fix-meta
fi

echo ""
echo "All done — pages generated and SEO meta applied."
