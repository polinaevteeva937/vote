import pika

# Устанавливаем соединение
# Одно соединение может иметь несколько каналов
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
# создает новый канал в существующем соединении
channel = connection.channel()

### ОТПРАВКА СООБЩЕНИЯ

# Создаем очередь
channel.queue_declare(queue= 'queue_test')

# Отправляем сообщение в очередь
# exchange - обменник, через который будет доставлено сообщение (у нас по умолчанию)
# routing_key - ключ маршрутизации, который определяет в какую очередь доставлено сообщение
# body - это и есть самое сообщение
channel.basic_publish(exchange= '', routing_key= 'queue_test', body= 'тестовое сообщение')

print('Сообщение отправлено ')
connection.close()

### ПРИЕМ СООБЩЕНИЯ

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Создаем очередь (или подключаемся к существующей)
channel.queue_declare(queue= 'queue_test')

# функция, выводящая содержимое сообщения в консоль
def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    print(f'Сообщение: \n{message}')

# queue - очередь, в которой нужно проверять новые сообщения
# on_message_callback - для указания функции, которую нужно вызывать каждый раз при приеме нового сообщения
# auto_ack - подтверждение о получении и обработке сообщения будет отправлено автоматически
channel.basic_consume(queue= 'queue_test', on_message_callback= callback, auto_ack= True)

print('Ожидаю сообщений')
# запускаем бесконечный опрос для проверки новых сообщений в очереди
channel.start_consuming()