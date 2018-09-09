import os

from eve import Eve

import sassutils.wsgi

app = Eve()
app.wsgi_app = sassutils.wsgi.SassMiddleware(app.wsgi_app, {})