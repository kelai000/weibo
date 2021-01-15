from apps import app
from flask import render_template,jsonify
from apps.Model import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html') 

@app.route('/table')
def get_table():
    st=db.session.query(user.name,bolg.strid).filter(user.wbid==bolg.wbid).all()
    return jsonify(st)





