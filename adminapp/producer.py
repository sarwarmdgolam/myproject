#!/usr/bin/env python
import pika


def new_job_produced():
    credentials = pika.PlainCredentials(username='user', password='password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.10.100', credentials=credentials))
    channel = connection.channel()
    channel.basic_publish(exchange='my_exchange', routing_key='test', body='new_job_added')
    connection.close()
