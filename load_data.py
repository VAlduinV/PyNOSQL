import json
from mongoengine import connect
from models import Author, Quote

connect(host=your_mongodb_url)  # Вказуємо свій URL MONGODB

with open('authors.json') as f:
    authors_data = json.load(f)

for author in authors_data:
    author_doc = Author(**author)
    author_doc.save()

with open('quotes.json') as f:
    quotes_data = json.load(f)

for quote in quotes_data:
    author_name = quote['author']
    author_doc = Author.objects(name=author_name).first()
    quote['author'] = author_doc
    quote_doc = Quote(**quote)
    quote_doc.save()
