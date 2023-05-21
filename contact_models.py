from mongoengine import Document, StringField, EmailField, BooleanField, DateTimeField, IntField


class Contact(Document):
    full_name = StringField(required=True)
    email = EmailField(required=True)
    message_sent = BooleanField(default=False)
    date_of_birth = DateTimeField()  # Дата народження
    phone_number = StringField()  # Номер телефону
    age = IntField()  # Вік
    address = StringField()  # Адреса
    prefer_sms = BooleanField(default=False)  # preferred messaging method
    # інші поля...
