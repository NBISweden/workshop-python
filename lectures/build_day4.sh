jupyter nbconvert --to slides Day_4.ipynb
python ../scripts/convert_html_to_standalone.py --infile Day_4.slides.html  --outfile Day_4.slides.embedded.html --css custom.css
