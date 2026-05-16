from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "A Court of Thones and Roses", "author": "Sarah J Maas", "genre": "Romantacy", "series": "A Court of Thorns and Roses", "status": "Read", "rating": "5/5", "comments": "dont trust the plot line."},
    {"id": 2, "title": "Losing Sam", "author": "Nicole Maser", "genre": "Romance", "series": "Losing Sam", "status": "Read", "rating": "5/5", "comments": "best book ever"},
]

@app.route('/books')
def get_books():
    return jsonify(books)


if __name__ == "__main__":
    app.run(debug=True, port=5001)