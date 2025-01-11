from flask import render_template
from models import Book, db

def index():
    books = Book.query.order_by(Book.created_at.desc()).limit(15).all()
    return render_template('index.html', books=books)



def genre():
    id = request.args.get('id')
    genre = Genre.query.get(id)
    books = Book.query.filter_by(genre_id=id).all()
    return render_template('genre.html', genre=genre, books=books)
