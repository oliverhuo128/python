# Conda environments

Type the commands in an Anaconda Prompt or Anaconda PowerShell Prompt

## Take a look at the environments and packages

To see a list of environments currently in your computer

`conda env list`

To see a list of packages and their versions installed in the current environment

`conda list`

## Creating a new environment

Create a new environment with python 3.7 version

`conda create -n de25_env python=3.7`

Activate the new environment

`conda activate de25_env`

List the packages in this new environment

`conda list`

Note that the version in Python in this new environment is 3.7.xx. Also, this new environment does not have packages such as numpy, pandas etc. as in the base environment.

Update all packages in this environment

`conda update --all`

Install a new package in the current environment

`conda install <package_name>`

For example, to install numpy, run `conda install numpy`

Aside: In some cases, `conda install <package_name>` will not work. They may be available through other channels. For example, the wordcloud package is not available to be installed as `conda install wordcloud`. But it is available in the `conda-forge` channel. To install a package from a different channel, you run 

`conda install -c <channel_name> <package_name>`.

To install wordcloud, you'll do something like `conda install -c conda-forge wordcloud`.

If the package is not available through any channels in conda, then a `pip install <package_name>` would typically work

To deactivate an environment and switch to the previously activated environment:

`conda deactivate`

## Saving our environment

`conda env export > de25_env.yml`

This creates a snapshot of all the packages and their versions in the current environment into a yaml file. This file can then be used to recreate the same environment on a different machine. 

## Deactivating and removing the environment

Deactivate an environment

`conda deactivate`

Remove an environment

`conda env remove -n de25_env`

## Recreating the environment

Recreate an environment from a yaml file

`conda env create -f <file_name>`

For example, if you want to install from the previously created file, you do `conda env create -f de25_env.yml`

## For more information, see the anaconda cheat sheet

<https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>