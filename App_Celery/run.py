from main import app
from main import celery


print(celery.conf)
#print(app.config)
app.run()