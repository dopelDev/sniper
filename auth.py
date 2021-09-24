#!/usr/bin/python3
# auth jwt token
from werkzeug.security import safe_str_cmp

# class User

class User(object):
    def __init__(self, id, username, password):
       self.id = id
       self.username = username
       self.password = password
    def __str__(self):
        return "User(id=%s)" % self.id

# users

users = [
        User(1, "admin", "1234"),
        User(2, "user_with_password", "4321")
        ]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

# functions para verificar user y pass 
# deben ser importados para el app.py o main file py 

def authenticate(username, password):
    user = userid_table.get(username, None)
    if user and safe_str_cmp(user.password.encode("utf-8"), password.encode("utf-8")):
        return user
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

