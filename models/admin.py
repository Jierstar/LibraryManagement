from app import db


class Admin(db.Model):
    __tablename__ = 'admin'
    admId = db.Column('ADM_ID', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    password = db.Column('password', db.String)

    def toDict(self):
        return {
            'admId': self.admId,
            'name': self.name
        }

    @staticmethod
    def queryAll():
        datas = db.session.query(Admin).all()
        return [data.toDict() for data in datas]

