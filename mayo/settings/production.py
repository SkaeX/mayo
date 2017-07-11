from .base import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='y7v%p_9i9y(9rqm1r3r2uko*ei_j*8vgjtpoyzccqw457j805*')


ALLOWED_HOSTS += ['0.0.0.0', 'young-thicket-12790.herokuapp.com', 'mentor-a-youth.herokuapp.com']


import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
