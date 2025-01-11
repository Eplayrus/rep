# flask_app.py
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Инициализация приложения Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модели базы данных
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    books = db.relationship('Book', backref='genre', lazy=True)

    def __repr__(self):
        return f'<Genre {self.name}>'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


# Представления
@app.route('/')
def index():
    books = Book.query.order_by(Book.created_at.desc()).limit(15).all()
    return render_template('index.html', books=books)


@app.route('/genre/<int:genre_id>')
def genre_view(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    books = Book.query.filter_by(genre_id=genre.id).all()
    return render_template('genre.html', genre=genre, books=books)


# Запуск приложения
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создаем таблицы при первом запуске

        # Добавление начальных данных
        if not Genre.query.first():
            genre1 = Genre(name='Fiction')
            genre2 = Genre(name='Science Fiction')
            genre3 = Genre(name='Fantasy')
            db.session.add_all([genre1, genre2, genre3])
            db.session.commit()

        if not Book.query.first():
            books = [
                Book(title='Book 1', author='Author A', genre_id=1),
                Book(title='Book 2', author='Author B', genre_id=1),
                Book(title='Book 3', author='Author C', genre_id=2),
                Book(title='Book 4', author='Author D', genre_id=2),
                Book(title='Book 5', author='Author E', genre_id=3),
                Book(title='Book 6', author='Author F', genre_id=1),
                Book(title='Book 7', author='Author G', genre_id=1),
                Book(title='Book 8', author='Author H', genre_id=2),
                Book(title='Book 9', author='Author I', genre_id=2),
                Book(title='Book 10', author='Author J', genre_id=3),
                Book(title='Book 11', author='Author K', genre_id=3),
                Book(title='Book 12', author='Author L', genre_id=1),
                Book(title='Book 13', author='Author M', genre_id=2),
                Book(title='Book 14', author='Author N', genre_id=3),
                Book(title='Book 15', author='Author O', genre_id=1),
                Book(title='Book 16', author='Author O', genre_id=1),
                Book(title='Book 17', author='Author O', genre_id=1),
                Book(title='Book 18', author='Author O', genre_id=1),
                Book(title='Book 19', author='Author O', genre_id=1),
                Book(title='Book 20', author='Author O', genre_id=1)
            ]
            db.session.add_all(books)
            db.session.commit()

    app.run(debug=True)
