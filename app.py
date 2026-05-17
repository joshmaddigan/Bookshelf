from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "A Court of Thones and Roses", "author": "Sarah J Maas", "genre": "Romantacy", "series": "A Court of Thorns and Roses", "status": "Read", "rating": "5/5", "comments": "dont trust the plot line."},
    {"id": 2, "title": "Losing Sam", "author": "Nicole Maser", "genre": "Romance", "series": "Losing Sam", "status": "Read", "rating": "5/5", "comments": "best book ever"},
]

@app.route('/books')
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author'],
        'genre': data['genre'],
        'series': data['series'],
        'status': data['status'],
        'rating': data['rating'],
        'comments': data['comments']
    }
    books.append(new_book)
    return jsonify(new_book)


@app.route('/books/<id>', methods=["GET"])
def get_id(id):

    for book in books:
        if book['id'] == int(id):
            return jsonify(book)
    else:
        return (f"no book found")






if __name__ == "__main__":
    app.run(debug=True, port=5001)