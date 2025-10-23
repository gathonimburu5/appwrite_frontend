from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from application.services.supplier_service import SupplierService


supplier_router = Blueprint('supplier_router', __name__)
supplier_service = SupplierService()

@supplier_router.route('/', methods=['GET', 'POST'])
def list_suppliers():
    if request.method == "GET":
        if "access_token" not in session:
            flash("you have to loggin first", "error")
            return redirect(url_for("auth_router.login_page"))

        user = session["user"]
        token = session["access_token"]
        data = supplier_service.getAllSupplier()
        return render_template("suppliers.html", data=data, user=user, token=token)

    if request.method == "POST":
        form_data = {
            "supplier_name": request.form.get("supplierName"),
            "supplier_code": request.form.get("supplierCode"),
            "supplier_email": request.form.get("supplierEmail"),
            "supplier_phone": request.form.get("supplierPhone"),
            "postal_address": request.form.get("postalAddress"),
            "physical_address": request.form.get("physicalAddress"),
            "dob": request.form.get("dob")
        }
        response = supplier_service.createSupplier(form_data)
        flash(response.get("message", "Supplier created successfully"), "success")
        return redirect(url_for("supplier_router.list_suppliers"))

@supplier_router.route("/edit/<string:supplier_id>", methods=["GET", "POST"])
def update_supplier(supplier_id):
    user = session["user"]
    token = session["access_token"]

    if request.method == "POST":
        form_data = {
            "supplier_name": request.form.get("supplierName"),
            "supplier_code": request.form.get("supplierCode"),
            "supplier_email": request.form.get("supplierEmail"),
            "supplier_phone": request.form.get("supplierPhone"),
            "postal_address": request.form.get("postalAddress"),
            "physical_address": request.form.get("physicalAddress"),
            "dob": request.form.get("dob")
        }
        response = supplier_service.updateSupplier(supplier_id, form_data)
        flash(response.get("message", "Supplier updated successfully"), "success")
        return redirect(url_for("supplier_router.list_suppliers"))

    data = supplier_service.getSupplierById(supplier_id)
    return render_template("edit_supplier.html", data=data, user=user, token=token)