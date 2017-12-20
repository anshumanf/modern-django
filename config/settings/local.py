from .base import *

SECRET_KEY = env.str('DJANGO_SECRET_KEY', '5ej+1zrn8963-9$)g-0u#0_lpsr#ubhaufg!0pus#+n)qdnh-&')

DEBUG = env.bool('DJANGO_DEBUG', True)
