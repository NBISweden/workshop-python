# Guide for teachers - Get started
In the following guide, we are using conda for installing the various packages. However, feel free to select the package manager of your choice
Creating a conda environment is one solution for installing the required packages.

## Environment
* Create environment for the course using
 ```bash
conda env create -f environment.yml
```

* Activate the environment using
 ```bash
conda activate python_workshop
```

* To start the jupyter notebooks run the following conda from the same terminal
```bash
jupyter notebook
```

## Select standard theme
The theme used in the course is part of the nbextensions and can be activated with the following sequence:
* Enable the nbextensions for the respective tab
* Select RISE in from the possible extensions
* Change the theme parameter to beige
* Load the notebook you want and enter the presentation mode

You should be ready to go!

## Create lecture material
### HTML slides
HTML slides are created and put on the website. Create the html slides using:
```bash
jupyter nbconvert --to slides <notebookename>
```

### Create pdfs
1. Open the generated html slides in a browser. 
2. Replace the # in the end of the url with ?print-pdf. 
3. Right click and select Print, and print the pages to pdf.

### Publish on course website
Copy over html slides, pdfs and all html associated files to the gh-pages branch using:
```bash
./scripts/publish_lecture.sh lectures/Day_X.slides.html
./scripts/publish_lecture.sh lectures/Day_X.slides.pdf
```
(Branch is hardcoded in the `publish_lecture.sh` script, so don't forget to update when new branch is created). All changes are commit to the gh-pages branch, but not yet pushed:
```bash
git checkout gh-pages
git push
```
