from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    publisher = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Book(id={self.id}, book_name='{self.book_name}', author='{self.author}', publisher='{self.publisher}')"

# Routes
@app.route('/api/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher} for book in books])

@app.route('/api/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher})

@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(book_name=data['book_name'], author=data['author'], publisher=data['publisher'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'id': new_book.id, 'book_name': new_book.book_name, 'author': new_book.author, 'publisher': new_book.publisher}), 201

@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.book_name = data['book_name']
    book.author = data['author']
    book.publisher = data['publisher']
    db.session.commit()
    return jsonify({'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher})

@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Deleted book'}), 200

if __name__ == '__main__':
    app.run(debug=True)
