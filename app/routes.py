# -*- coding: utf-8 -*-
from app import app


@app.route('/')
@app.route('/index')
def idex():
    return "Уряяя... Май"
