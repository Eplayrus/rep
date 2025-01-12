������������ ��� ������� Flask � �������� Book � Genre:

**�������� �������**

���������� ������������ ����� ���-���� ��� ���������� ����� ������ ���� � ������. ��� ������� � �������������� Flask � SQLAlchemy. ������������ ����� ������������� ������ ���� � ���������� � ��������� ���� �� ������������ �����.

**�������� ����������**

### ������������� ���������� Flask

� ����� `flask_app.py` �������� � ��������������� ������ Flask. ������������ SQLite � �������� ���� ������ ��� �������� �������������.

```python
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

������ SQLAlchemy ����������� � ����������� ��� ���������� ����� ������.

### ������ ���� ������

#### Genre � ������ ����� ����:

* `id`: ��������� ����.
* `name`: �������� ����� (������ ������ �� 50 ��������).
* `books`: ��������� � ������� Book.

#### Book � ������ �����:

* `id`: ��������� ����.
* `title`: �������� �����.
* `author`: ����� �����.
* `created_at`: ���� �������� ������, �� ��������� �������.
* `genre_id`: ������� ����, ��������� � ������� Genre.

**������ ���������� �������:**

```python
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    books = db.relationship('Book', backref='genre', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
```

### ������������� (Views)

#### ������� �������� (/):

���������� 15 ��������� ����������� ����, ������������� �� ���� ��������.

```python
@app.route('/')
def index():
    books = Book.query.order_by(Book.created_at.desc()).limit(15).all()
    return render_template('index.html', books=books)
```

#### �������� ����� (/genre/<int:genre_id>):

���������� ��� ����� ��� ���������� �����.

```python
@app.route('/genre/<int:genre_id>')
def genre_view(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    books = Book.query.filter_by(genre_id=genre.id).all()
    return render_template('genre.html', genre=genre, books=books)
```

### ������������� ���� ������ � ��������� ������

```python
with app.app_context():
    db.create_all()  # �������� ������ ��� ������ �������

    if not Genre.query.first():
        genres = [Genre(name='Fiction'), Genre(name='Science Fiction'), Genre(name='Fantasy')]
        db.session.add_all(genres)
        db.session.commit()

    if not Book.query.first():
        books = [
            Book(title='Book 1', author='Author A', genre_id=1),
            # ��������� ��������� �����...
        ]
        db.session.add_all(books)
        db.session.commit()
```

### ������ ����������

```python
if __name__ == '__main__':
    app.run(debug=True)
```

**���������� �� �������**

1. ���������, ��� ���������� Python 3 � ����������� ����������.
2. ���������� �����������:
   ```
pip install Flask SQLAlchemy
```
3. ��������� ����������:
   ```bash
python flask_app.py
```
4. ��������� � �������� �� ������ http://127.0.0.1:5000.