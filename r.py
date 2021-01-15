from apps import app
from apps.Model import *
if __name__ == "__main__":
    # app.run()
    # st=db.session.query(user.name,bolg.strid).filter(user.wbid==bolg.wbid).all()
    st=db.session.query(body).all()
    for i in st:
        print(i)