import serial
import time
import boto3
from decimal import *


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table=dynamodb.Table('globalproject')


ser=serial.Serial("/dev/ttyUSB0",9600)
ser.baudrate=9600

while True:
    read_ser=ser.readline()
    item={
        "timestamp":Decimal(time.time()),
        "current":Decimal(read_ser.decode('ascii')),
        
    }
    print(item)
    print('--')
    table.put_item(Item=item)