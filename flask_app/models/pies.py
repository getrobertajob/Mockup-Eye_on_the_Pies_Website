from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re


class Pie:
    DB = "PieShopDB"

    #pie class structure  
    def __init__(self, pies):
        self.id = pies["id"]
        self.name = pies["name"]
        self.filling = pies["filling"]
        self.crust = pies["crust"]
        self.description = pies["description"]
        self.user = None

    #method to get all pie records by user ID
    @classmethod
    def get_by_user_id(cls, data):
        query = """SELECT * from pies JOIN users on pies.user_id = users.id WHERE pies.user_id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        pies = []
        for pie_dict in results:
            pie_obj = Pie(pie_dict)
            user_obj = user.User(
                {
                    "id": pie_dict["users.id"],
                    "first_name": pie_dict["first_name"],
                    "last_name": pie_dict["last_name"],
                    "email": pie_dict["email"],
                    "password": pie_dict["password"],
                    "created_at": pie_dict["created_at"],
                    "updated_at": pie_dict["updated_at"],
                }
            )
            pie_obj.user = user_obj
            pies.append(pie_obj)
        return pies

    #method to validate form data for pie records
    @staticmethod
    def is_valid(pie_dict):
        # checks if validation was passed
        # if validation fails returns False
        valid = True
        query = "SELECT * FROM pies WHERE name = %(name)s;"
        results = connectToMySQL(Pie.DB).query_db(query, pie_dict)
        if len(results) >= 1:
            valid = False
            flash("Sorry that name is already taken.")
        if len(pie_dict["name"]) == 0:
            valid = False
            flash("Name is required.")
        elif len(pie_dict["name"]) < 3:
            valid = False
            flash("Name must be a minimum of 3 characters.")
        if len(pie_dict["filling"]) == 0:
            valid = False
            flash("Filling is required.")
        elif len(pie_dict["filling"]) < 3:
            valid = False
            flash("Filling must be a minimum of 3 characters.")
        if len(pie_dict["crust"]) == 0:
            valid = False
            flash("Crust is required.")
        elif len(pie_dict["crust"]) < 3:
            valid = False
            flash("Crust must be a minimum of 3 characters.")
        if len(pie_dict["description"]) == 0:
            valid = False
            flash("Description is required.")
        elif len(pie_dict["description"]) < 3:
            valid = False
            flash("Description must be a minimum of 3 characters.")
        return valid

    #method to save new pie records
    @classmethod
    def save(cls, pie_data):
        query = "INSERT INTO pies (name, filling, crust, description, user_id) VALUES (%(name)s, %(filling)s, %(crust)s, %(description)s, %(user_id)s);"
        connectToMySQL(cls.DB).query_db(query, pie_data)

    #method to get single pie record and related user record based on user id
    @classmethod
    def get_one_by_id(cls, pie_id):
        query = """SELECT * from pies JOIN users on pies.user_id = users.id WHERE pies.id = %(id)s;"""
        data = {"id": pie_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        pie_dict = results[0]
        pie_obj = Pie(pie_dict)
        user_obj = user.User(
            {
                "id": pie_dict["users.id"],
                "first_name": pie_dict["first_name"],
                "last_name": pie_dict["last_name"],
                "email": pie_dict["email"],
                "password": pie_dict["password"],
                "created_at": pie_dict["created_at"],
                "updated_at": pie_dict["updated_at"],
            }
        )
        pie_obj.user = user_obj
        return pie_obj

    #method to remove a single record from the pies table
    @classmethod
    def delete_by_id(cls, pie_id):
        query = "DELETE from pies WHERE id = %(id)s;"
        data = {"id": pie_id}
        connectToMySQL(cls.DB).query_db(query, data)
        return

    #method to update a single record from the pies table
    @classmethod
    def update(cls, pie_data):
        query = "UPDATE pies SET name = %(name)s, filling = %(filling)s, crust = %(crust)s, description = %(description)s WHERE id = %(id)s;"
        connectToMySQL(cls.DB).query_db(query, pie_data)
        return

    #method to get all pie records by user id
    @classmethod
    def get_all_pies(cls):
        query1 = """SELECT * from pies JOIN users on pies.user_id = users.id;"""
        results = connectToMySQL(cls.DB).query_db(query1)
        pies = []
        for pie_dict in results:
            pie_obj = Pie(pie_dict)
            user_obj = user.User(
                {
                    "id": pie_dict["users.id"],
                    "first_name": pie_dict["first_name"],
                    "last_name": pie_dict["last_name"],
                    "email": pie_dict["email"],
                    "password": pie_dict["password"],
                    "created_at": pie_dict["created_at"],
                    "updated_at": pie_dict["updated_at"],
                }
            )
            pie_obj.user = user_obj
            pies.append(pie_obj)
        return pies