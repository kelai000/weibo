from apps import app
from flask import render_template,jsonify
from apps.Model import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html') 

@app.route('/top10')
def get_table():
    st=db.session.query(bolg.createtime,user.name,body.str,bolg.sended).\
        filter(body.strid==bolg.strid,user.wbid==bolg.wbid).\
        order_by(bolg.createtime.desc()).\
        limit(10).\
        all()
    return jsonify(st)





