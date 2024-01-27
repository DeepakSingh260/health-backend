from flask import Blueprint

task_route = Blueprint('task', __name__)
@task_route.route('/task' , methods=["GET"])
def get_task():
    return [
        ["task_name", "timeFrom-timeTo" ]
    ]

@task_route.route('/task', methods= ["POST"])
def add_task():
    return 'success'