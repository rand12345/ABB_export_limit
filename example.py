# -*- coding: utf-8 -*-
from custom_aurorapy.client_ import AuroraTCPClient
import time
import datetime

'''
EXPERIMENTAL, DO NOT MODIFY.
USE AT YOUR OWN RISK
OTHER SERVICE MODE PARAMETERS CAN POTENTIALLY DAMAGE YOUR INVERTER

Tested on ABB Power One 3.6 OUTD
'''
solar_inverter_ip = '10.0.1.38'
solar_inverter_port = 2000
solar_inverter_id = 2

client = AuroraTCPClient(ip=solar_inverter_ip, port=solar_inverter_port, address=solar_inverter_id)


def enter_service_mode():
    serial_number = client.serial_number()
    if not client.enter_service_mode(serial_number):  # must send twice
        if not client.enter_service_mode(serial_number):
            print('Service mode failed after 2 attempts)')
            return False
        return True


def print_power_vars():
    if enter_service_mode():
        print('Power limiter active = {}'.format(client.read_limiter_val(133)))
        print('Timeout timer = {}mins'.format(client.read_limiter_val(132)))
        print('Power limiting = {}%'.format(client.read_limiter_val(134)))
        print('Smoothing = {}secs'.format(client.read_limiter_val(135)))


def run_code():
    client.connect()
    now = datetime.datetime.now()
    print('{} - {}W'.format(now, client.measure(3)))
    print_power_vars()

    # example settings
    power_ = 100     # limit max generation to percent [int]
    timeout_ = 4    # minutes [int]
    smooth_ = 4     # power transition in seconds [int]

    while power_ > 9:
        now = datetime.datetime.now()
        print('{} - Setting max power to {}%'.format(now, power_))
        if enter_service_mode():
            client.send_power_limiter(timeout_, power_, smooth_)
        else:
            continue
        print_power_vars()
        time.sleep(smooth_ + 1)
        print('{} - {}W'.format(now, client.measure(3)))
        power_ -= 10

    print('\nFinished, setting inverter back to 100%')
    power_ = 100
    if enter_service_mode():
        client.send_power_limiter(timeout_, power_, smooth_)
        print('Done, exiting')
    else:
        print('Service mode failed')
    client.close()


if __name__ == "__main__":
    run_code()
