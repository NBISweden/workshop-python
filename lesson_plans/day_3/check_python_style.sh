#!/bin/bash
#
#

# Ignore the first ruff error
ruff day_3.qmd > temp_ruff_results.txt 2>&1

last_line=$(cat temp_ruff_results.txt | tail -n 1)
# echo "last_line: ${last_line}"
n_errors_plus_one=$(echo "${last_line}" | cut -d ' ' -f 2)
# echo "Number of errors plus one: ${n_errors_plus_one}"
n_errors=$((n_errors_plus_one-1))
echo "Number of errors: ${n_errors}"

exit ${n_errors}

# FAILS: will still always give an error
# Remove the part between '---'
#tail -n +11 day_3.qmd > temp_day_3.qmd
#ruff temp_day_3.qmd
