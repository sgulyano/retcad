# retcad
Retinal Fundus Photography Computer Aided Diagnosis (CAD)

------
## Installation ##
### [Windows](https://docs.djangoproject.com/en/2.1/howto/windows/) ###
`virtualenv` and `virtualenvwrapper` provide a dedicated environment for each Django project you create. Install by typing
```
pip install virtualenvwrapper-win
```
Then create a virtual environment for your project:
```
mkvirtualenv myproject
```
If you start a new command prompt, you will need to activate the environment again using:
```
workon myproject
```

### Linux (Tested on [Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04)) ###
To install `virtualenv`, we will use the `pip3` command, as shown below:
```
pip3 install virtualenv
virtualenv --version
```
While inside the `django-apps` directory, create your virtual environment. Let call it env.
```
virtualenv env
```
Activate the virtual environment with the following command:
```
. env/bin/activate
```

### Dependencies ###
- Django 2.1.3
- PyTorch 0.4.1
- torchvision 0.2.1
- Pillow 5.2.0
- OpenCV (cv2) 3.4.1
- skimage (scikit-image) 0.14.1
- scikit-learn 0.20.0

To install dependency, type:
```
pip install django
pip3 install django-widget-tweaks
pip install pillow
pip3 install http://download.pytorch.org/whl/cu80/torch-0.4.1-cp36-cp36m-linux_x86_64.whl
pip3 install torchvision

```


------
### Run ###
Change into the outer project directory, and run `makemigrations` to tell Django that you've made some changes to your models and that you'd like the changes to be stored as a migration.
```Python
python manage.py makemigrations
```
`migrate` command that will run the migrations for you and manage your database schema automatically.
```Python
python manage.py migrate
```
Run the following commands to start the server
```Python
python manage.py runserver
```

------
### Requirements ###
Test on Django 2.1.2 Python 3.6

------
### Dockerize ###
Follow this [tutorial](https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99)
Use the given `requirements.txt` or create one by typing
```
pip freeze > requirements.txt
```
To list all the libraries in the environment.

(Optional step for GPU support) Install [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker)
Put `runtime: nvidia` in `docker-compose.yml`
And make sure in `Dockerfile` use images that pre-install cuda and maybe even the gpu-dependent libs you want to use ,e.g, `pytorch/pytorch`

Next, install `Docker compose` following this [link](https://docs.docker.com/compose/install/#install-compose)
Then, build and run the container with the command:
```
docker-compose up
```
If there is any error and you need to build the docker image again, type:
```
docker build -t retcad_web .
```
Finally, the web app for development should start at http://0.0.0.0:8000/


