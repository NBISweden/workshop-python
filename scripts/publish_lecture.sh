#!/bin/bash 
# For publishing a lecture to the course web page.

# Copies and commits a given lecture, all images (png and jpg) in lectures/img and the css
# files to the gh-pages branch.
# Usage: ./scripts/publish_lecture lectures/Day_1.slides.html
# Remember to push the gh-pages branch when you're done.
# Also, check that ht19/topics.md is updated to show the lecture you want to publish.
set -e
TMP="tmp_lecture.tmp"
TMP_IMG="tmpimgtmp"
TMP_CSS="tmpcsstmp"
DEST="$(basename $1)"

mkdir -p $TMP_IMG
mkdir -p $TMP_CSS
cp $1 $TMP
cp lectures/img/*{png,jpg} $TMP_IMG
cp lectures/*css $TMP_CSS
git checkout gh-pages
mv $TMP ht19/lecture/$DEST
mv $TMP_IMG/* ht19/lecture/img/
mv $TMP_CSS/* ht19/lecture/
git add ht19/lecture/$DEST
git add ht19/lecture/img/*{png,jpg}
git add ht19/lecture/*css
git commit -m "Update lecture $DEST"
git checkout ht19
