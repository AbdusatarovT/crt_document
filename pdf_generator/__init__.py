from flask import Blueprint

pdf_gen_route = Blueprint(__name__, 'pdf_generator', template_folder='./templates')

from .views import *
