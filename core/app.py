import os
import pdfkit
from flask import Flask
from models.models import db
from datetime import datetime
from utils.models_creator import *
from core.extensions import migrate
from flask import Flask, render_template, Response, request


def create_app(config='core.config'):

    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(db=db, app=app)

    # Blueprint views
    from pdf_generator import pdf_gen_route
    app.register_blueprint(pdf_gen_route)

    return app