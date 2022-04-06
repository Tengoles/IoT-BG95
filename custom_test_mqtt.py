from constants import MY_PHONE_PASS
from configuration import optimized_start_up_nbiot
from PDP_context import optimized_setup_PDP_context
from MQTT import publish_mqtt_message, open_mqtt_network, connect_to_mqtt_server, check_connection_to_mqtt_server

import serial
import serial.tools.list_ports
from print_cmd_history import print_cmd_history
from send_cmd import send_cmd

from datetime import datetime

from time import sleep

'''
The objective of this test is to measure the energy needed to send a message of different length
using mqtt protocol

Observation: To measure energy further hardware is needed

'''

def custom_test_mqtt(ser=-1, msg_length=10, nbiot_connected = False):
    list = serial.tools.list_ports.comports()
    print(*list)
    if (ser == -1):
        ser = serial.Serial(port='COM3', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=5)
    if not nbiot_connected:
        response = optimized_start_up_nbiot(ser)

        response = optimized_setup_PDP_context(ser, response_history=response["response_history"], retries=3, custom_delay=1000)

    mqtt_check = check_connection_to_mqtt_server(ser)

    mqtt_open = {}
    mqtt_connect = {}

    for time in range(0,3):

        print(mqtt_open)
        if mqtt_open.get('status') != 'OK': mqtt_open = open_mqtt_network(ser)
        print(mqtt_open)
        if mqtt_open.get('status') != 'OK': break
        
        mqtt_check = check_connection_to_mqtt_server(ser)

        print(mqtt_connect)
        if mqtt_connect.get('status') != 'OK': mqtt_connect = connect_to_mqtt_server(ser)
        print(mqtt_connect)
        if mqtt_connect.get('status') != 'OK': break

        mqtt_check = check_connection_to_mqtt_server(ser)

    if mqtt_check.get('status') == 'OK':
        start = datetime.now()
        response = publish_mqtt_message(ser, 'a'*msg_length)
        end = datetime.now()
        diff = end-start
        print('tiempo: ' + str(diff))
        cmd_response = send_cmd("AT+CSQ", ser)
    
    

    # print_cmd_history(response)

    ser.close()

    return response


# custom_test_mqtt()

def custom_test_mqtt_iterative(
    ser=-1, 
    msg_length_start=10, 
    msg_length_end=100, 
    msg_length_step_size=10, 
    nbiot_connected = False,
    is_connected_to_mqtt_broker = True,
    wait=True,
    ):
    list = serial.tools.list_ports.comports()
    print(*list)
    if (ser == -1):
        ser = serial.Serial(port='COM3', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=5)
    
    if not nbiot_connected:
        response = optimized_start_up_nbiot(ser)
        response = optimized_setup_PDP_context(ser, response_history=response["response_history"], retries=3, custom_delay=1000)
    
    if not is_connected_to_mqtt_broker:
        open_mqtt_network(ser)
        sleep(1)
        connect_to_mqtt_server(ser)
        sleep(1)

    for msg_length in range(msg_length_start, msg_length_end+1, msg_length_step_size):
        start = datetime.now()
        response = publish_mqtt_message(ser, 'a'*msg_length)
        end = datetime.now()
        diff = end-start
        print('tiempo: ' + str(diff) + '\n')
        # if wait & msg_length < msg_length_end: # corregir para que no se llame la ultima vez
            # input(str(msg_length) + " - press Enter to continue...")

        cmd_response = send_cmd("AT+CSQ", ser, ms_of_delay_before=5000 )

    # print_cmd_history(response)
    ser.close()
    return response


custom_test_mqtt_iterative(msg_length_start=10, msg_length_end=1010, msg_length_step_size=250, nbiot_connected = True, wait=False)


'''
# from setup_serial_connection import *
from custom_test_connection import custom_test_connection
ser = serial.Serial(port='COM3', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=5)

from configuration import optimized_start_up_nbiot
from PDP_context import optimized_setup_PDP_context
# custom_test_connection(ser)
# optimized_start_up_nbiot(ser)
# optimized_setup_PDP_context(ser, response_history=[], retries=3, custom_delay=1000)

open_mqtt_network(ser)
connect_to_mqtt_server(ser)
ser.close()
custom_test_mqtt_iterative(msg_length_start=50, msg_length_end=100, msg_length_step_size=50, wait=False, already_connected=True)
# custom_test_mqtt.custom_test_mqtt(msg_length=16, already_connected = True)
'''

'''
send_cmd("AT+QMTPUB=" + str(tcp_connect_id) + "," + str(msgID) + "," + str(qos) + "," + str(retain) + "," + "\"" + topic + "\"," + str(len(str_to_send)),ser,  custom_response_end='>',print_response=print_response)
send_cmd(str_to_send, ser,  print_response=print_response)
'''