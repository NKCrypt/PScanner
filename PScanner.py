#coding: utf-8
# -*- coding:utf-8 -*-

import sys
import time
import socket
import os

purpleClaro = "\033[1;35m"
cyanClaro = "\033[1;36m"
vermelho = "\033[31;1m"
amarelo = "\033[1;33m"
magenta = "\033[45m"
normal = "\033[0;0m"
fundo_Vermelho = '\033[41;1;37m'
verde = "\033[32;1m"  
azul = "\033[34;1m"
branco = "\033[0m"
ciano = "\033[46m"
Logo = """
██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                                                                                                                                                                                                                                                                                                                                                
"""
Logo1 = """
		+================================================+
		|                   PORT SCANNER                 |
		+================================================+
		| ♚ Coded: WheezySec                             |
		| ♚ Contact: @TheWheezy (Telegram)               |
		| ♚ Date: 03/06/2017                             |
		| ♚ Chanell: telegram.me/TerminalRoot404         |
		| ♚ Page: facebook.com/TerminalRoot404           |
		+================================================+
		|             ♚ ŧєrмiηαł Røøŧ 404                |
		+================================================+
"""
os.system("clear")

print verde + Logo
print verde + Logo1
time.sleep(1.5) #tempo de delay
print fundo_Vermelho
ip = raw_input("Digite o IP Ou Endereco~# ")
porta = []
x = input("Digite a Quantidade de Portas~# ")
i = 0
 
while i < x:
	       porta.append(int(raw_input("Digite a porta~# ")))
	       i += 1
	      
print "[$] Verificando se as portas estao abertas... [$]"
	      
for port in porta:	       
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    conexao = cliente.connect_ex((ip, port))
    if conexao == 0:
		print str(port) + "Porta Aberta! :D"
else:
		print str(port) + " Porta Fechada! :("