#enable venv
VENV_PATH="."
python3 -m venv $VENV_PATH

#activate venv
source $VENV_PATH/bin/activate

#install django module
pip3 install django

# docs: https://docs.djangoproject.com/en/4.0/intro/tutorial01/
#check django version
python3 -m django --version
output: 4.0.5

#create project with my username
django-admin startproject my-username

# deactivate venv
deactivate
