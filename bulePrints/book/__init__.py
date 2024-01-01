from flask import Blueprint

book_bp = Blueprint('book', __name__, url_prefix='/book')

from . import routes