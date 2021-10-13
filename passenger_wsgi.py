import os
import sys

sys.path.insert(0, "/home/sopfurni/public_html/kusort")
os.environ['DJANGO_SETTINGS_MODULE'] = 'kusort.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
