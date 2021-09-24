#!/usr/bin/python3
#base del servicio
# import base

from flask import Flask
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required, current_identity

# import auth.py
from auth import authenticate, identity

from sys import executable
print(executable)
