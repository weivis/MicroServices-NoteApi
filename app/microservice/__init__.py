from flask import Blueprint
microservice = Blueprint('microservice', __name__)
from ..microservice import urls