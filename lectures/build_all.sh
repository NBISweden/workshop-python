##!/bin/bash
#
SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR" || exit 1

for day in $(seq 5)
do
  echo
  echo Build Day $day
  jupyter nbconvert --to slides Day_$day.ipynb
  python ../scripts/convert_html_to_standalone.py --infile Day_$day.slides.html  --outfile Day_$day.slides.embedded.html --css custom.css
done
