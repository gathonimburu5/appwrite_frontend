from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from application.services.todo_service import ToDoService

todo_router = Blueprint('todo_router', __name__)
todo_service = ToDoService()

@todo_router.route('/', methods=['GET', 'POST'])
def list_todo():
    if request.method == "GET":
        data = todo_service.get_todo()
        return render_template("todo.html", data = data)
    if request.method == "POST":
        form_data = {
            "title": request.form.get("title"),
            "description": request.form.get("description")
        }
        response = todo_service.create_todo(form_data)
        flash(response.get("message", "Todo created successfully"), "success")
        return redirect(url_for("todo_router.list_todo"))