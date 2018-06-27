from app import app

from app.controllers.home_controller import home

app.register_blueprint(home)
