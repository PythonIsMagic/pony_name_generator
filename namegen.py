""" Django project to generate random pony names when a button is clicked. """
from django.core.management import execute_from_command_line
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.conf import settings
import os
import sys


DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', 'p9^bx%7c^_hlc#56na65()6k=ti8y+@@o@^*#*xkcbfpite36*')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# Settings
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


# View
def index(request):
    return HttpResponse('Hello world')

# urls
urlpatterns = (
    url(r'^$', index),
)

application = get_wsgi_application()

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
