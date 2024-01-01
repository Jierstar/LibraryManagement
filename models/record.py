from app import db


class Record(db.Model):
    __tablename__ = 'borrow_record'
    RID = db.Column(db.Integer, primary_key=True)
    BID = db.Column(db.Integer)
    UID = db.Column(db.Integer)
    # BID = db.Column(db.Integer, db.ForeignKey('books.BID'))
    # UID = db.Column(db.Integer, db.ForeignKey('users.UID'))
    checkOutDate = db.Column('Check_out_Date', db.Date)
    returnDate = db.Column('Return_Date', db.Date)
    returnLimit = db.Column('return_limit', db.Date)
    # book = db.relationship("Book", back_populates="borrowings")
    # user = db.relationship("User", back_populates="borrowings")

    def toDict(self):
        return {
            'RID': self.RID,
            'BID': self.BID,
            'UID': self.UID,
            'checkOutDate': self.checkOutDate,
            'returnLimit': self.returnLimit,
            'returnDate': self.returnDate
        }

    @staticmethod
    def queryAll():
        datas = db.session.query(Record).all()
        return [data.toDict() for data in datas]
