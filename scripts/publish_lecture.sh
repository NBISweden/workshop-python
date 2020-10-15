#!/bin/bash 
# For publishing a lecture to the course web page.

# Copies and commits a given lecture, all images (png and jpg) in lectures/img and the css
# files to the gh-pages branch.
# Usage: ./scripts/publish_lecture lectures/Day_1.slides.html
# Remember to push the gh-pages branch when you're done.
# Also, check that ht20/topics.md is updated to show the lecture you want to publish.
set -e
TMP="tmp_lecture.tmp"
TMP_IMG="tmpimgtmp"
TMP_CSS="tmpcsstmp"
DEST="$(basename $1)"

mkdir -p $TMP_IMG
mkdir -p $TMP_CSS
cp $1 $TMP
cp lectures/img/*{png,jpg,PNG} $TMP_IMG
cp lectures/*css $TMP_CSS
git checkout gh-pages
mv $TMP ht20/lecture/$DEST
mv $TMP_IMG/* ht20/lecture/img/
mv $TMP_CSS/* ht20/lecture/
git add ht20/lecture/$DEST
git add ht20/lecture/img/*{png,jpg,PNG}
git add ht20/lecture/*css
git commit -m "Update lecture $DEST"
git checkout ht20
