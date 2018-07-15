from django.core.management import execute_from_command_line
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.conf import settings
import os
import sys

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', '4=8dr@oa-sy#3z^__9f+8jrwxhon)hf08low!+_d4cx_e)6pfx')
# Works for http://localhost:8000/
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
