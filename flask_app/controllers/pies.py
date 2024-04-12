# Imports needed resources
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.pies import Pie
from flask import flash


# route to render dashboard page
@app.route("/dashboard")
def pies_home():
    # checks if the current session matches log in ID
    # redirests if not
    if "user_id" not in session:
        return redirect("/logout")
    data = {"id": session["user_id"]}
    pies = Pie.get_by_user_id(data)
    return render_template("dashboard.html", user=User.get_by_id(data), pies=pies)


# route to make new pie
@app.route("/pies/create", methods=["POST"])
def create_pie():
    # sends form data for validation
    is_valid = Pie.is_valid(request.form)
    # checks if validation was passed
    # if validation fails redirects to dashboard but without calling save
    if is_valid == True:
        # sends form data to save new pie
        Pie.save(request.form)
        return redirect("/dashboard")
    else:
        return redirect("/dashboard")


# route to render edit page
@app.route("/pie/edit/<int:pie_id>")
def edit_page(pie_id):
    # gets data about selected pie record
    pie = Pie.get_one_by_id(pie_id)
    return render_template("edit_pie.html", pie=pie)


# route to update current pie record
@app.route("/pie/update", methods=["POST"])
def update_recipe():
    # checks if validation was passed
    # if validation fails redirects to edit page
    is_valid = Pie.is_valid(request.form)
    if is_valid == True:
        Pie.update(request.form)
        return redirect("/dashboard")
    else:
        return redirect(f"/pie/edit/{request.form['id']}")


# route to delete selected pie record
@app.route("/pie/delete/<int:pie_id>")
def delete_pie(pie_id):
    Pie.delete_by_id(pie_id)
    return redirect("/dashboard")


# route to render display all pies page
@app.route("/pies")
def all_pies_page():
    pies = Pie.get_all_pies()
    return render_template("all_pies.html", pies=pies)


# route to render details page
@app.route("/pie/<int:pie_id>")
def detail_page(pie_id):
    data = {"id": session["user_id"]}
    user_id = data["id"]
    pie = Pie.get_one_by_id(pie_id)
    return render_template("detail_pie.html", user_id=user_id, pie=pie)
