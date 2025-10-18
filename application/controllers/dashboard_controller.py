from flask import Blueprint, render_template, redirect, url_for, request

dashboard_router = Blueprint("dashboard_router", __name__)

@dashboard_router.route("/", methods=['GET', 'POST'])
def dashboard_page():
    return render_template("dashboard.html")