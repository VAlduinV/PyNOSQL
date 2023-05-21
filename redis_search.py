import redis
from mongoengine.queryset.visitor import Q
from models import Author, Quote

r = redis.Redis(host='localhost', port=6379, db=0)


while True:
    input_data = input('Enter command: ')
    command, value = input_data.split(':', 1)
    value = value.strip()

    if command == 'exit':
        break
    elif command == 'name':
        key = f'name:{value}'
        if r.exists(key):
            print(r.get(key).decode('utf-8'))
        else:
            author = Author.objects(name__icontains=value).first()  # Use case-insensitive regex search
            if author:
                quotes = Quote.objects(author=author)
                quote_texts = [quote.text for quote in quotes]
                result = '\n'.join(quote_texts)
                print(result)
                r.set(key, result)  # Cache the result
    elif command == 'tag':
        key = f'tag:{value}'
        if r.exists(key):
            print(r.get(key).decode('utf-8'))
        else:
            quotes = Quote.objects(tags__icontains=value)  # Use case-insensitive regex search
            quote_texts = [quote.text for quote in quotes]
            result = '\n'.join(quote_texts)
            print(result)
            r.set(key, result)  # Cache the result
    else:
        print('Invalid command')
