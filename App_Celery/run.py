from main import app



#print(celery.conf)
print(app.config)
if __name__ == '__main__':    
    app.run()