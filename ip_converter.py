#!/usr/bin/python3
import socket
import signal, sys, time
from os import system

def ctrl_c(sig, frame):
    system('clear')
    print("\n [!] Saliendo [!]")
    sys.exit(0)
signal.signal(signal.SIGINT, ctrl_c)

# Banner
def banner():
    font = """
     ___ ___  ___                     _           
    |_ _| _ \/ __|___ _ ___ _____ _ _| |_ ___ _ _ 
     | ||  _/ (__/ _ \ ' \ V / -_) '_|  _/ -_) '_|
    |___|_|  \___\___/_||_\_/\___|_|  \__\___|_|   by H4RRIZN"""
    print(font)

def ip_conversion(ip_address):
    try:
        parts = ip_address.split('.')
        if len(parts) != 4:
            raise ValueError
        for part in parts:
            if not 0 <= int(part) <= 255:
                raise ValueError
    except (ValueError, TypeError):
        return "Dirección IP inválida"

    decimal_ip = int(socket.inet_aton(ip_address).hex(), 16)
    binary_parts = [format(int(part), '08b') for part in parts]
    binary_ip = '0b' + ''.join(binary_parts)[2:].lstrip('0')
    hex_ip = '0x' + ''.join(format(int(part), '02X') for part in parts)
    octal_ip = '.'.join(format(int(part), '03o') for part in parts)

    return {
        'Decimal': decimal_ip,
        'Binario': binary_ip,
        'Hexadecimal': hex_ip,
        'Octal': octal_ip
    }

if __name__ == "__main__":
    banner()
    # Solicita al usuario una dirección IP
    ip = input("\nIngresa una dirección IP en formato x.x.x.x: ")
    
    # Realiza las conversiones
    result = ip_conversion(ip)
    
    # Muestra los resultados
    print("\nDirección IP:", ip)
    for format, value in result.items():
        print(f'{format}: {value}')
