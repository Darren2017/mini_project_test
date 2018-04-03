# encoding: utf-8
from . import api
from flask import jsonify, request
from app import db
from app.models import User
import json


@api.route('/')
def index():
    return 'index'
