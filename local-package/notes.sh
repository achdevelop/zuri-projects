#enable venv
VENV_PATH="."
python3 -m venv $VENV_PATH

#activate venv
source $VENV_PATH/bin/activate

#install django module
pip3 install random

# deactivate venv
deactivate