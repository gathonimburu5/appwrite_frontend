from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from application.services.employee_service import EmployeeService

employee_router = Blueprint('employee_router', __name__)
employee_service = EmployeeService()

@employee_router.route('/', methods=['GET', 'POST'])
def list_employees():
    if request.method == "GET":
        if "access_token" not in session:
            flash("you have to loggin first", "error")
            return redirect(url_for("auth_router.login_page"))

        user = session["user"]
        token = session["access_token"]
        data = employee_service.getAllEmployee()
        return render_template("employees.html", data=data, user=user, token=token)

    if request.method == "POST":
        form_data = {
            "employee_name": request.form.get("employeeName"),
            "employee_email": request.form.get("employeeEmail"),
            "phone_number": request.form.get("phoneNumber"),
            "postal_address": request.form.get("postalAddress"),
            "physical_address": request.form.get("physicalAddress"),
            "department": request.form.get("department"),
            "gender": request.form.get("gender"),
            "kra_pin": request.form.get("kraPin"),
            "date_birth": request.form.get("dateOfBirth"),
        }
        response = employee_service.createEmployee(form_data)
        flash(response.get("message", "Employee created successfully"), "success")
        return redirect(url_for("employee_router.list_employees"))

@employee_router.route("/edit/<string:emp_id>", methods=["GET", "POST"])
def update_employee(emp_id):
    user = session["user"]
    token = session["access_token"]

    if request.method == "POST":
        form_data = {
            "employee_name": request.form.get("employeeName"),
            "employee_email": request.form.get("employeeEmail"),
            "phone_number": request.form.get("phoneNumber"),
            "postal_address": request.form.get("postalAddress"),
            "physical_address": request.form.get("physicalAddress"),
            "department": request.form.get("department"),
            "gender": request.form.get("gender"),
            "kra_pin": request.form.get("kraPin"),
            "date_birth": request.form.get("dateOfBirth")
        }
        response = employee_service.editEmployee(emp_id, form_data)
        flash(response.get("message", "Employee updated successfully"), "success")
        return redirect(url_for("employee_router.list_employees"))

    data = employee_service.getEmployeeById(emp_id)
    return render_template("edit_employee.html", data=data, user=user, token=token)