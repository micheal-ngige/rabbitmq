import pika


connection_parameters= pika.ConnectionParameters('localhost') 

connection = pika.BlockingConnection(connection_parameters) #connecting to rabbitmq broker

channel = connection.channel() # using a default channel

channel.queue_declare(queue= 'letterbox') # name of the queue 

message = "Hello this is my first message"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f" sent message:{message}")
connection.close()

#producer =>exchange => queue => consumer
# exchange => queue is connected by binding 
