from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from application.services.todo_service import ToDoService

todo_router = Blueprint('todo_router', __name__)
todo_service = ToDoService()

@todo_router.route('/', methods=['GET', 'POST'])
def list_todo():
    if request.method == "GET":
        if "access_token" not in session:
            flash("you have to loggin first", "error")
            return redirect(url_for("auth_router.login_page"))

        user = session["user"]
        token = session["access_token"]
        data = todo_service.get_todo()
        return render_template("todo.html", data = data, user=user, token=token)
    if request.method == "POST":
        form_data = {
            "title": request.form.get("title"),
            "description": request.form.get("description")
        }
        response = todo_service.create_todo(form_data)
        flash(response.get("message", "Todo created successfully"), "success")
        return redirect(url_for("todo_router.list_todo"))

@todo_router.route("/edit/<string:todo_id>", methods=["GET", "POST"])
def update_todo(todo_id):
    user = session["user"]
    token = session["access_token"]

    if request.method == "POST":
        form_data = {
            "title": request.form.get("title"),
            "description": request.form.get("description")
        }
        response = todo_service.update_todo(todo_id, form_data)
        flash(response.get("message", "Todo updated successfully"), "success")
        return redirect(url_for("todo_router.list_todo"))

    data = todo_service.get_todo_id(todo_id)
    return render_template("list_todo.html", data=data, user=user, token=token)