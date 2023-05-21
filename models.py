from mongoengine import Document, StringField, ListField, ReferenceField


class Author(Document):
    name = StringField(required=True)
    birth_date = StringField(required=True)
    birth_place = StringField(required=True)
    bio = StringField(required=True)


class Quote(Document):
    author = ReferenceField(Author)
    text = StringField(required=True)
    tags = ListField(StringField())
