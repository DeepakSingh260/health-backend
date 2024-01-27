from flask import Blueprint
from .tasks import task_route

main_bp = Blueprint('main' , __name__)
main_bp.register_blueprint(task_route)


