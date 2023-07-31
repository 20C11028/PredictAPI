activate_this = 'D:/Projects/Python/PredictAPI/venv/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(), dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('D:/Projects/Python/PredictAPI/venv/Lib/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('D:/Projects/Python/PredictAPI')
sys.path.append('D:/Projects/Python/PredictAPI/PredictAPI')

os.environ['DJANGO_SETTINGS_MODULE'] = 'PredictAPI.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PredictAPI.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
