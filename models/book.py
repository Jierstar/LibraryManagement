from app import db


class Book(db.Model):
    __tablename__ = 'book'
    BID = db.Column('BID', db.Integer, primary_key=True)
    publishDate = db.Column('publish_date', db.Date)
    publisher = db.Column('publisher', db.String)
    borrowed = db.Column('borrowed', db.Boolean)
    callNumber = db.Column('call_number', db.String)
    ISBN = db.Column('ISBN', db.String)
    title = db.Column('title', db.String)
    author = db.Column('author', db.String)
    category = db.Column('category', db.String)
    # borrowings = db.relationship("Record", back_populates="book")

    def toDict(self):
        return {
            'BID': self.BID,
            'publishDate': self.publishDate,
            'publisher': self.publisher,
            'borrowed': self.borrowed,
            'callNumber': self.callNumber,
            'ISBN': self.ISBN,
            'title': self.title,
            'author': self.author,
            'category': self.category
        }

    @staticmethod
    def queryAll():
        datas = db.session.query(Book).all()
        return [data.toDict() for data in datas]

    @staticmethod
    def getName(qname):
        ret = db.session.query(Book).filter(Book.title.like('%' + qname + '%')).all()
        ret = map(lambda a: a.toDict(), ret)
        return list(ret)

    @staticmethod
    def getId(qid):
        book = Book.query.filter_by(BID=qid).first()
        if book:
            return book.toDict()
        else:
            raise Exception("Book not found")
