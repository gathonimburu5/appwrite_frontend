from flask import Blueprint, url_for, redirect, render_template, flash, request, session
from application.services.auth_service import AuthService

auth_router = Blueprint("auth_router", __name__)
auth_service = AuthService()

@auth_router.route("/login", methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        form_data = {
            "username": request.form.get("username"),
            "password": request.form.get("password")
        }
        response = auth_service.LoginUser(form_data)

        if "error" in response:
            flash(response.get("message", "username or password not found, please check!"), "error")
            return redirect(url_for("auth_router.login_page"))

        session["access_token"] = response["access_token"]
        session["user"] = {
            "id":response.get("$id"),
            "full_name": response.get("full_name"),
            "email_address": response.get("email_address"),
            "phone_number": response.get("phone_number"),
            "username": response.get("username")
        }

        flash(response.get("message", "successfully logged in"), "success")
        return redirect(url_for("dashboard_router.dashboard_page"))

    return render_template("login.html")