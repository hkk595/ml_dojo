# ml_dojo

## Requirements
* Python 3.7+
  * Use [pyenv](https://github.com/pyenv/pyenv) to install and manage the Python version.
  * Follow the installation instructions in the official `pyenv` repository.
  * [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) is not needed because the built-in module [venv](https://docs.python.org/3/library/venv.html) is recommended for creating virtual environments since Python 3.6.

## Environment Setup
Navigate to the project folder in `Terminal` and run the following commands. Use the built-in `venv` module to create and activate virtual environment.
```bash
pyenv install 3.7           # assuming Python 3.7.17 will be installed
pyenv local 3.7.17          # use Python 3.7.17 for this project
python -m venv venv         # create a virtual environment called "venv" under this project
source venv/bin/activate    # activate the virtual environment "venv"
```

## Installation
```bash
pip install -r requirements.txt
# make sure the virtual environment is activated before pip install
```

## How to use
Run the main script for linear regression.
```bash
python main.py              # train the model and plot the graph
```

(Optional) When done using, deactivate the virtual environment.
```bash
deactivate                  # deactivate the virtual environment
```
