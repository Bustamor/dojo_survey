from operator import is_
from flask import flash

class User:
    def __init__(self,data):
        self.date = data ['name']
        self.data = data ['location']
        self.data = data ['favorite_lang']
        self.data = data ['kind_of_ninja']


    @staticmethod
    def validate_user(user):
        print("----------------------------------")
        print(user)
        print("----------------------------------")
        is_valid = True 
        if len(user['name'])<2:
            is_valid = False 
            flash("Username too short")
        if (user['location']) == "null":
            is_valid = False
            flash("Must select location")
        if (user['favorite_lang']) == "null":
            is_valid = False
            flash("Must choose a language")
        if len(user['kind_of_ninja']) <1:
            is_valid = False
            flash("Must enter a comment")
        return is_valid

    