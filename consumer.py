import pika
from mongoengine import connect
from contact_models import Contact

# connect to MongoDB
connect(host='your_mongodb_url')

# create a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# declare the same queue
channel.queue_declare(queue='email_queue')


def send_email(contact_id):
    # this is a stub function that imitates sending an email
    print(f"Email sent to contact with id {contact_id}")


def callback(ch, method, properties, body):
    contact_id = body.decode()
    send_email(contact_id)

    # set message_sent to True
    contact = Contact.objects.get(id=contact_id)
    contact.message_sent = True
    contact.save()


channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()
