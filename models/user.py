from app import db


class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column('UID', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    id = db.Column('id', db.String)
    tel = db.Column('tel', db.String)
    password = db.Column('password', db.String)
    borrowings = db.relationship("Record", back_populates="user")

    def toDict(self):
        return {
            'UID': self.uid,
            'name': self.name,
            'id': self.id,
            'tel': self.tel,
        }

    @staticmethod
    def queryAll():
        datas = db.session.query(User).all()
        return [data.toDict() for data in datas]