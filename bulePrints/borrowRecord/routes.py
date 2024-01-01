from . import record_bp
from models.book import Book
from models.user import User
from models.record import Record
from flask import jsonify, request
from app import db
from datetime import datetime, timedelta


# record模块
@record_bp.route('/')
def index():
    return '/borrow 借书<br>' \
          '/*暂时只有这个功能*/<br>' \
           '传来的JSON包含uid 和bid '


@record_bp.route('/borrow', methods=['GET', 'POST'])
def borrow():
    try:
        data = request.get_json()
        user = db.session.query(User).get(data.get('uid'))
        if user:
            book = db.session.query(Book).get(data.get('bid'))
            if book:
                if not book.borrowed:
                    book.borrowed = True
                    db.session.add(
                        Record(
                            bid=book.bid,
                            uid=user.uid,
                            checkOutDate=datetime.now(),
                            returnDate=datetime.now() + timedelta(days=90)
                        )
                    )
                    db.session.commit()
                    return jsonify({'message': 'Book borrowed successfully!'})
                else:
                    raise Exception('Book already borrowed')
            else:
                raise Exception('Book not found')
        else:
            raise Exception('User not found')

    except Exception as e:
        return jsonify({"error": str(e)})


# @record_bp.route('/return', methods=['GET', 'POST'])
# def bookReturn():
#     try:
#         book = Book.query.filter_by(BID=bid).first()
#         if book:
#             if book.borrowed:
#                 book.borrowed = False
#                 db.session.commit()
#                 return jsonify({'message': 'Book returned successfully!'})
#             else:
#                 return jsonify({'message': 'Book not borrowed'})
#         else:
#             return jsonify({'message': 'Book not found'})
#     except Exception as e:
#         return jsonify({'error': str(e)})
