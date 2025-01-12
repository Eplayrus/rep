Документация для проекта Flask с моделями Book и Genre:

**Описание проекта**

Приложение представляет собой веб-сайт для управления базой данных книг и жанров. Оно создано с использованием Flask и SQLAlchemy. Пользователь может просматривать список книг и переходить к просмотру книг по определённому жанру.

**Основные компоненты**

### Инициализация приложения Flask

В файле `flask_app.py` создаётся и конфигурируется объект Flask. Используется SQLite в качестве базы данных для простоты использования.

```python
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

Объект SQLAlchemy связывается с приложением для управления базой данных.

### Модели базы данных

#### Genre — модель жанра книг:

* `id`: первичный ключ.
* `name`: название жанра (строка длиной до 50 символов).
* `books`: отношение с моделью Book.

#### Book — модель книги:

* `id`: первичный ключ.
* `title`: название книги.
* `author`: автор книги.
* `created_at`: дата создания записи, по умолчанию текущая.
* `genre_id`: внешний ключ, связанный с моделью Genre.

**Пример объявления моделей:**

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

### Представления (Views)

#### Главная страница (/):

Отображает 15 последних добавленных книг, упорядоченных по дате создания.

```python
@app.route('/')
def index():
    books = Book.query.order_by(Book.created_at.desc()).limit(15).all()
    return render_template('index.html', books=books)
```

#### Страница жанра (/genre/<int:genre_id>):

Отображает все книги для выбранного жанра.

```python
@app.route('/genre/<int:genre_id>')
def genre_view(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    books = Book.query.filter_by(genre_id=genre.id).all()
    return render_template('genre.html', genre=genre, books=books)
```

### Инициализация базы данных и начальные данные

```python
with app.app_context():
    db.create_all()  # Создание таблиц при первом запуске

    if not Genre.query.first():
        genres = [Genre(name='Fiction'), Genre(name='Science Fiction'), Genre(name='Fantasy')]
        db.session.add_all(genres)
        db.session.commit()

    if not Book.query.first():
        books = [
            Book(title='Book 1', author='Author A', genre_id=1),
            # Добавлены остальные книги...
        ]
        db.session.add_all(books)
        db.session.commit()
```

### Запуск приложения

```python
if __name__ == '__main__':
    app.run(debug=True)
```

**Инструкции по запуску**

1. Убедитесь, что установлен Python 3 и необходимые библиотеки.
2. Установите зависимости:
   ```
pip install Flask SQLAlchemy
```
3. Запустите приложение:
   ```bash
python flask_app.py
```
4. Перейдите в браузере по адресу http://127.0.0.1:5000.