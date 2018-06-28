from flask import render_template
from app import app
from app import db

@app.errorhandler(404)
def four_oh_four(error):
    return render_template('/errors/404.html'), 404

@app.errorhandler(500)
def five_hundred(error):
    db.session.rollback()
    return render_template('/errors/500.html'), 500