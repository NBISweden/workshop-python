# Guide for teachers - Get started
In the following guide, we are using conda for installing the various packages. However, feel free to select the package manager of your choice
Creating a conda environment is one solution for installing the required packages.

## Environment
* Create environment for the course using
 ```bash
conda create -n python_workshop jupyter
```

* Activate the environment using
 ```bash
conda activate python_workshop
```

* Install [RISE](https://rise.readthedocs.io/en/stable/). For conda installations run
```bash
conda install -c conda-forge rise
```
* Install [nbextensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/index.html). For conda installations run
```bash
conda install -c conda-forge jupyter_contrib_nbextensions
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
