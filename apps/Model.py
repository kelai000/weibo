import json
from apps import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.util.langhelpers import repr_tuple_names

db = SQLAlchemy(app)


class bolg(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key=True)
    wbid = db.Column(db.String(20))
    strid = db.Column(db.String(20))
    createtime = db.Column(db.DateTime, server_default=db.FetchedValue())
    sendtime = db.Column(db.DateTime, server_default=db.FetchedValue())
    sended = db.Column(db.Integer, server_default=db.FetchedValue())

    def __repr__(self):
        return "wbid=%s,strid=%s,createtime=%s,sendtime=%s,sended=%d" % (self.wbid,
                                                                         self.strid,
                                                                         self.createtime,
                                                                         self.sendtime,
                                                                         self.sended)


class body(db.Model):
    __tablename__ = 'bodys'
    id = db.Column(db.Integer, primary_key=True)
    strid = db.Column(db.String(20))
    str = db.Column(db.String(255))

    def __repr__(self):
        return "strid=%s,str=%s" % (self.strid, self.str)


class user(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    wbid = db.Column(db.String(20))
    name = db.Column(db.String(10))
    
    def __repr__(self):
        return "wbid:%s,name:%s" % (self.wbid, self.name)
