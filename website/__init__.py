from flask import Flask
def create_app():
    #Initializes Flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'encrypt cookies :)'

    from .views import views
    from .auth import auth  
    app.register_blueprint(views, url_prefix='/')
    #No prefix for auth because the blueprint
    #auto puts the name you defined as part of the url
    app.register_blueprint(auth, url_prefix='/')


    return app