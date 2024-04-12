from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask import render_template, redirect, request, session, flash
import re

#REGEX to set formatting for email validation
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

class User:
    DB = "PieShopDB"

    #user class structure   
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    #method to insert new records in the users table
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    #method to get a list of all users
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    #method to get a single record from the users table by user ID
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    #method to validate form data for user registration
    #if any validations fail alerts user
    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.DB).query_db(query, user)
        #checks if email already exist in users table
        if len(results) >= 1:
            flash("Sorry that email is already taken.", "register")
            is_valid = False
        #checks email formatting
        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email address. ", "register")
            is_valid = False
        if len(user["first_name"]) < 2:
            flash("First name minimum length is 2 characters long.", "register")
            is_valid = False
        if len(user["last_name"]) < 2:
            flash("Last name minimum length is 2 characters long.", "register")
            is_valid = False
        if len(user["password"]) < 8:
            flash("Password minimum length is 8 characters long.", "register")
            is_valid = False
        #checks if both password fields match
        if user["password"] != user["confirm"]:
            flash("Passwords don't match.", "register")
            is_valid = False
        return is_valid

    #method to validate form data for log in
    #if any validations fail alerts user
    @staticmethod
    def validate_login(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(User.DB).query_db(query, user)
        return is_valid
