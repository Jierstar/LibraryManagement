from flask import Blueprint

record_bp = Blueprint('record', __name__, url_prefix='/record')

from . import routes