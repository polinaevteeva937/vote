import aio_pika
import asyncio

async def main():
    # Подключаемся к RabbitMQ серверу
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")

    # Создаем асинхронный канал
    channel = await connection.channel()

    # Объявляем очередь
    queue = await channel.declare_queue('queue_test')

    async def send_channel(chat_id, task_id):
        print('ФУНКЦИЯ send_channel запустилась')
        message = aio_pika.Message(body=f'{chat_id}, {task_id}'.encode())
        # Отправляем сообщение в очередь
        await channel.default_exchange.publish(
            message, routing_key='queue_test'
        )
        print('Сообщение в очередь отправлено')

    # Здесь можем вызвать send_channel для отправки сообщения
    await send_channel("123", "456")

    # Закрываем соединение
    await connection.close()

# Запускаем асинхронный event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())