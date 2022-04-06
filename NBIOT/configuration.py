from NBIOT.send_cmd import send_cmd
import serial
import json

from constants import MY_PHONE_PASS

def enter_pin(ser, response_history=[]):
    cmd_response = send_cmd("AT+CPIN?", ser, 6,  print_response=True)
    response_history.append(cmd_response)

    response_code = response_history[-1]["response"][1][0:-2] # [0:-2] to remove \r\n
    
    if response_code == "+CPIN: SIM PIN":
        cmd_response = send_cmd("AT+CPIN=" + MY_PHONE_PASS, ser, 8,  print_response=True, ms_of_delay_after=1000)
        response_history.append(cmd_response)
        response_status = response_history[-1]["status"]

        if response_status == "ERROR":
            status = "ERROR"
            message = "SIM PIN SENT AND ERROR"
        elif response_status == "OK":
            status = "OK"
            message = "SIM PIN SENT AND SUCCESS"
        else:
            status = "ERROR"
            message = "SIM PIN SENT AND UNFINISHED"
    elif response_code == "+CPIN: READY":
        status = "OK"
        message = "+CPIN: READY"
    else:
        print('==> SIM error with message ' + response_code)
        status = "ERROR"
        message = response_code
        
    return({"response_history": response_history, "status": status, "message": message})

def configure_modem(ser):
    '''
    Hace aqui la funcion que haga la configuracion
    '''


def start_up_nbiot(ser, response_history=[]):
    '''
    Hacer una funcion que conecte a nbiot partiendo de que la configuracion esta correcta
    '''


def check_nbiot_conection(ser, retries=3, response_history=[], custom_delay=2000):
    '''
    Hacer aqui una funcion que chequee si el modem esta registrado en la red nbiot, que devuelva e imprima el resultado 
    '''