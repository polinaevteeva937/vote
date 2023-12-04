### ПРИЕМ СООБЩЕНИЯ

import pika
import threading

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue= 'queue_test')

def transfer_bot(chat_id=0, task_id=0):
    from bot_main import transfer_hometask
    transfer_hometask(chat_id, task_id)

def callback(ch, method, properties, body):
    print('Сообщение принято из очереди')
    message = body.decode('utf-8')
    print(f'Сообщение: \n{message}')

    # message = '123102490, 20101'
    # my_list = ['12310290', '20101']

    my_list = message.split(", ")
    chat_id = int(my_list[0])
    task_id = int(my_list[1])
    
    transfer_bot(chat_id, task_id)
    print('Сообщение отправлено боту')



channel.start_consuming()

thread = threading.Thread(target=transfer_bot)
thread.start()
thread.join()

channel.basic_consume(queue= 'queue_test', on_message_callback= callback, auto_ack= True)