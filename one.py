from sqlalchemy.orm import session
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from lxml import etree
import random
app = Flask(__name__, template_folder='ones')
app.config['SECRET_KEY'] = '11111111'

# app.config['DEBUG']=True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:k2132009@121.196.32.103:3306/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class user(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))

    def __repr__(self):
        return "di=%d ,name=%s" % (self.id, self.name)




@app.route('/', methods=['GET', 'POST'])
def index():
    user_list = user.query.all()
    print(user_list)
    return render_template("python.html", str=user_list)


def add():

  
    
    

    


if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()
    # st=db.session.query(user.name,subject.sub,func.max(number.number)).filter(number.user_id==user.id,number.sub_id==subject.id).group_by(subject.id).all()
    st=db.session.query(user).first()
    
    stt=db.session.execute('''SELECT DISTINCT `name`,sub,number FROM users,numbers,(
                              SELECT sub,max(number) as max FROM `users`,subjects,numbers
                              WHERE numbers.user_id=users.id and numbers.sub_id=subjects.id
                              GROUP BY sub)  t2
                              WHERE t2.max=numbers.number and user_id=users.id''').fetchall()
    
    print(st)
    
    # print(session.query().all())
