from . import book_bp
from models.book import Book
from flask import jsonify, request
from app import db
from datetime import datetime, timedelta


# book模块
@book_bp.route('/')
def index():
    return '/all 全部信息<br>' \
           '/add 增<br>\n' \
           '/delete/<id> 删<br>\n' \
           '/query_by_id/<id> 查(id)<br>\n' \
           '/query_by_title/<title> 查(书名)<br>\n' \
           '/edit/<id> 改<br>\n'


@book_bp.route('/all', methods=['GET'])
def getAll():
    return jsonify(Book.queryAll())


@book_bp.route('/query_by_title/<qname>', methods=['GET'])
def getName(qname):
    try:
        rec = Book.getName(qname)
        return jsonify(rec)
    except Exception as e:
        return jsonify({"error": str(e)})


@book_bp.route('/query_by_id/<qid>', methods=['GET'])
def getId(qid):
    try:
        rec = Book.getId(int(qid))
        return jsonify(rec)
    except Exception as e:
        return jsonify({"error": str(e)})


@book_bp.route('/edit/<bid>', methods=['GET', 'POST'])
def edit(bid):
    try:
        book = Book.query.get(bid)

        if not book:
            return jsonify({"error": "Book not found"}), 404

        if request.method == 'POST':
            data = request.get_json()
            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            book.publisher = data.get('publisher', book.publisher)
            book.publishDate = data.get('publishDate', book.publishDate)
            book.callNumber = data.get('callNumber', book.callNumber)
            book.category = data.get('category', book.category)
            db.session.commit()
            return jsonify({'status_code': 200})

    except Exception as e:
        return jsonify({"error": str(e)})


@book_bp.route('/delete/<bid>', methods=['GET', 'POST', 'DELETE'])
def delete(bid):
    try:
        if request.method == 'DELETE':
            book = Book.query.get(bid)
            if not book:
                raise Exception('book not found')
            db.session.delete(book)
            db.session.commit()
            return jsonify({'status_code': 200})
        else:
            raise Exception("method error")

    except Exception as e:
        return jsonify({'error': str(e)})


@book_bp.route('/add', methods=['GET', 'POST'])
def add():
    try:
        data = request.get_json()
        if not data:
            raise Exception('No data received')
        db.session.add(
            Book(
                title = data.get('title'),
                author = data.get('author'),
                publisher = data.get('publisher'),
                publishDate = data.get('publishDate'),
                callNumber = data.get('callNumber'),
                category = data.get('category'),
            )
        )
        db.session.commit()
        return jsonify({'status_code': 200})
    except Exception as e:
        return jsonify({'error':str(e)})

