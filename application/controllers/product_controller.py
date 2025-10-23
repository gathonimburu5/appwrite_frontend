from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from application.services.product_service import ProductService
from application.services.supplier_service import SupplierService

product_router = Blueprint('product_router', __name__)
product_service = ProductService()
supplier_service = SupplierService()

@product_router.route('/', methods=['GET', 'POST'])
def list_products():
    if request.method == "GET":
        if "access_token" not in session:
            flash("you have to loggin first", "error")
            return redirect(url_for("auth_router.login_page"))

        user = session["user"]
        token = session["access_token"]
        data = product_service.getAllProducts()
        activeCategories = product_service.getAllActiveCategory()
        activeUnits = product_service.getAllActiveMeasureUnit()
        activeSuppliers = supplier_service.getActiveSupplier()
        return render_template("products.html", data=data, user=user, token=token, activeCategories=activeCategories, activeUnits=activeUnits, activeSuppliers=activeSuppliers)

    if request.method == "POST":
        form_data = {
            "product_name": request.form.get("productName"),
            "product_description": request.form.get("productDescription"),
            "product_code": request.form.get("productCode"),
            "product_type": request.form.get("productType"),
            "product_origin": request.form.get("productOrigin"),
            "category_id": request.form.get("categoryId"),
            "measure_unit_id": request.form.get("measureUnitId"),
            "supplier_id": request.form.get("supplierId"),
            "vat_percentage": request.form.get("vatPercentage"),
            "quantity": request.form.get("quantity"),
            "reoder_level": request.form.get("reoderLevel"),
        }
        response = product_service.createProduct(form_data)
        flash(response.get("message", "Product created successfully"), "success")
        return redirect(url_for("product_router.list_products"))

@product_router.route("/edit/<string:product_id>", methods=["GET", "POST"])
def update_product(product_id):
    user = session["user"]
    token = session["access_token"]

    if request.method == "POST":
        form_data = {
            "product_name": request.form.get("productName"),
            "product_description": request.form.get("productDescription"),
            "product_code": request.form.get("productCode"),
            "product_type": request.form.get("productType"),
            "product_origin": request.form.get("productOrigin"),
            "category_id": request.form.get("categoryId"),
            "measure_unit_id": request.form.get("measureUnitId"),
            "supplier_id": request.form.get("supplierId"),
            "vat_percentage": request.form.get("vatPercentage"),
            "quantity": request.form.get("quantity"),
            "reoder_level": request.form.get("reoderLevel"),
        }
        response = product_service.editProduct(product_id, form_data)
        flash(response.get("message", "Product updated successfully"), "success")
        return redirect(url_for("product_router.list_products"))

    data = product_service.getProductPerId(product_id)
    activeCategories = product_service.getAllActiveCategory()
    activeUnits = product_service.getAllActiveMeasureUnit()
    activeSuppliers = supplier_service.getActiveSupplier()
    return render_template("edit_product.html", data=data, user=user, token=token, activeCategories=activeCategories, activeUnits=activeUnits, activeSuppliers=activeSuppliers)

@product_router.route('/categories', methods=['GET', 'POST'])
def list_categories():
    if request.method == "GET":
        if "access_token" not in session:
            flash("you have to loggin first", "error")
            return redirect(url_for("auth_router.login_page"))

        user = session["user"]
        token = session["access_token"]
        data = product_service.getAllCategory()
        return render_template("categories.html", data=data, user=user, token=token)

    if request.method == "POST":
        form_data = {
            "category_name": request.form.get("categoryName"),
        }
        response = product_service.createCategory(form_data)
        flash(response.get("message", "Category created successfully"), "success")
        return redirect(url_for("product_router.list_categories"))

@product_router.route("/categories/edit/<string:cat_id>", methods=["GET", "POST"])
def update_category(cat_id):
    user = session["user"]
    token = session["access_token"]

    if request.method == "POST":
        form_data = {
            "category_name": request.form.get("categoryName"),
        }
        response = product_service.updateCategory(cat_id, form_data)
        flash(response.get("message", "Category updated successfully"), "success")
        return redirect(url_for("product_router.list_categories"))

    data = product_service.getCategoryById(cat_id)
    return render_template("edit_category.html", data=data, user=user, token=token)

@product_router.route("/categories/deactivate/<string:cat_id>", methods=["POST"])
def deactivate_category(cat_id):
    form_data = {
        "category_status": False
    }
    response = product_service.deactivateCategory(cat_id, form_data)
    flash(response.get("message", "Category deactivated successfully"), "success")
    return redirect(url_for("product_router.list_categories"))

@product_router.route('/measure-units', methods=['GET', 'POST'])
def list_measure_units():
    if request.method == "GET":
        if "access_token" not in session:
            flash("you have to loggin first", "error")
            return redirect(url_for("auth_router.login_page"))

        user = session["user"]
        token = session["access_token"]
        data = product_service.getAllMeasureUnit()
        return render_template("measure_units.html", data=data, user=user, token=token)
    if request.method == "POST":
        form_data = {
            "unit_name": request.form.get("unitName"),
        }
        response = product_service.createMeasureUnit(form_data)
        flash(response.get("message", "Measure Unit created successfully"), "success")
        return redirect(url_for("product_router.list_measure_units"))

@product_router.route("/measure-units/edit/<string:unit_id>", methods=["GET", "POST"])
def update_measure_unit(unit_id):
    user = session["user"]
    token = session["access_token"]

    if request.method == "POST":
        form_data = {
            "unit_name": request.form.get("unitName"),
        }
        response = product_service.getMeasureUnitPerId(unit_id, form_data)
        flash(response.get("message", "Measure Unit updated successfully"), "success")
        return redirect(url_for("product_router.list_measure_units"))

    data = product_service.getMeasureUnitPerId(unit_id)
    return render_template("edit_measure_unit.html", data=data, user=user, token=token)

@product_router.route("/measure-units/deactivate/<string:unit_id>", methods=["POST"])
def deactivate_measure_unit(unit_id):
    form_data = {
        "unit_status": False
    }
    response = product_service.deactivateMeasureUnit(unit_id, form_data)
    flash(response.get("message", "Measure Unit deactivated successfully"), "success")
    return redirect(url_for("product_router.list_measure_units"))
