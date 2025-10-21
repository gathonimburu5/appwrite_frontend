from flask import Blueprint, render_template, redirect, url_for, request, session, flash

dashboard_router = Blueprint("dashboard_router", __name__)

@dashboard_router.route("/", methods=['GET', 'POST'])
def dashboard_page():
    if "access_token" not in session:
        flash("you have to loggin first", "error")
        return redirect(url_for("auth_router.login_page"))

    user = session["user"]
    token = session["access_token"]
    return render_template("dashboard.html", token=token, user=user)