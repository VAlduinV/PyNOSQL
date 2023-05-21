import pika
import json
from mongoengine import connect
from models import Contact
from faker import Faker

fake = Faker()

# connect to MongoDB
connect(host='your_mongodb_url')

# create a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create two queues: one for email and one for sms
channel.queue_declare(queue='email_queue')
channel.queue_declare(queue='sms_queue')

for _ in range(10):  # generate 10 fake contacts
    full_name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    prefer_sms = fake.boolean()

    contact = Contact(full_name=full_name, email=email, phone_number=phone_number, prefer_sms=prefer_sms)
    contact.save()

    # send the contact's id to the appropriate queue
    if prefer_sms:
        channel.basic_publish(exchange='', routing_key='sms_queue', body=str(contact.id))
    else:
        channel.basic_publish(exchange='', routing_key='email_queue', body=str(contact.id))

connection.close()
