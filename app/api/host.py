# encoding: utf-8
from . import api
from flask import jsonify, request
from app import db
from app.models import User
import json
from decorators import login_required


@api.route('/')
@login_required
def index():
    return 'index'
