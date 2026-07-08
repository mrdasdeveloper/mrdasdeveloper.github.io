#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────
# generate_and_optimize.sh
# Run any page generator, then immediately apply the SEO optimizer
# so every freshly generated page gets all improvements.
#
# Usage:
#   ./generate_and_optimize.sh generate_australia_pages.py
#   ./generate_and_optimize.sh generate_usa_pages.py
#   ./generate_and_optimize.sh          # run ALL generators
# ─────────────────────────────────────────────────────────────────

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

run_generator() {
  local script="$1"
  echo "▶ Running $script …"
  python3 "$DIR/$script"
  echo "✓ $script done"
}

run_optimizer() {
  echo ""
  echo "▶ Running SEO optimizer on all HTML pages …"
  python3 "$DIR/seo_optimizer.py"
  echo "✓ Optimizer done"
}

if [ $# -eq 0 ]; then
  # Run all generators
  for gen in \
    generate_uae_pages.py \
    generate_usa_pages.py \
    generate_uk_pages.py \
    generate_canada_pages.py \
    generate_australia_pages.py \
    generate_germany_pages.py \
    generate_japan_pages.py \
    generate_singapore_pages.py \
    generate_saudi_pages.py \
    generate_qatar_pages_v2.py \
    generate_hubs.py; do
    if [ -f "$DIR/$gen" ]; then
      run_generator "$gen"
    fi
  done
else
  run_generator "$1"
fi

run_optimizer
echo ""
echo "All done — pages generated and SEO-optimized."
