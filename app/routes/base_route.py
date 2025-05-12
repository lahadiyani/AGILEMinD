from flask import render_template
from app.blueprints import main
from app.controllers.base_controller import BaseController

@main.route('/')
def index():
    return BaseController.index()