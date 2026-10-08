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

## Rise usage
### Jupyter notebook 7
For having access to RISE go to View → Right Sidebar → Show Notebook Tools.
Then in the common tools one can choose the slide type.

### JupyterLab
Open the Property inspector on the top right and then choose the slide type.

## Presentation mode
Slideshows use RISE (`jupyterlab_rise`). The course theme (beige) is stored in each lecture notebook's metadata, so nothing needs to be configured:
* Load the notebook you want
* Enter presentation mode with `Alt+R`

If you create a new lecture notebook, add the theme to its metadata (Right sidebar → Advanced Tools → Notebook metadata):
```json
"rise": {
  "theme": "beige"
}
```

You should be ready to go!

## Create lecture material
### HTML slides
HTML slides are created and put on the website. Create the html slides using:
```bash
jupyter nbconvert --to slides <notebookename>
```
To convert html slides to stand-alone html:
```bash
cd lectures/
python ../scripts/convert_html_to_standalone.py --infile <html file> --outfile <html file>.embedded.html --css custom.css
``` 

### Create pdfs
1. Open the generated html slides in a browser. 
2. Replace the # in the end of the url with ?print-pdf. 
3. Right click and select Print, and print the pages to pdf.

### Publish all material to Canvas

#### Lectures

Use https://htmlview.glitch.me/?https://github.com/NBISweden/workshop-python/blob/htXX/lectures/\<file\>.embedded.html


#### Exercises

Use https://nbviewer.jupyter.org/github/NBISweden/workshop-python/blob/htXX/exercises/dayX/\<file\>.ipynb

Note! nbviewer is sometimes very slow in updating (some known issue), so you might have to wait for the changes to show

