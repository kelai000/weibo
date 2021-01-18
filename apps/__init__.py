from sqlalchemy.sql.expression import false
from flask import Flask

app=Flask(__name__,template_folder='html')
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:k2132009@121.196.32.103:3306/new_wb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=false

from apps import routes