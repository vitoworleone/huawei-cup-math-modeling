#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
source_tex="${1:-sample.tex}"
base_name="${source_tex%.tex}"
mkdir -p build
if command -v latexmk >/dev/null 2>&1 && command -v xelatex >/dev/null 2>&1; then
  latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build "$source_tex"
elif command -v tectonic >/dev/null 2>&1; then
  tectonic --keep-logs --keep-intermediates --outdir build "$source_tex"
elif command -v xelatex >/dev/null 2>&1; then
  for pass in 1 2 3; do
    xelatex -interaction=nonstopmode -halt-on-error -output-directory=build "$source_tex"
  done
else
  echo "需要 XeLaTeX 或 Tectonic。" >&2
  exit 1
fi
if [[ "$base_name" == "sample" ]]; then
  mkdir -p preview
  cp "build/${base_name}.pdf" "preview/${base_name}.pdf"
  printf '已生成 preview/sample.pdf\n'
else
  printf '已生成 build/%s.pdf\n' "$base_name"
fi
