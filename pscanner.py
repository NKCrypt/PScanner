#!/usr/bin/env python

import socket

                                            
print "  ___   ___  ___ __ _ _ __  _ __   ___ _ __  "
print " | '_ \/ __|/ __/ _` | '_ \| '_ \ / _ \ '__| "
print " | |_) \__ \ (_| (_| | | | | | | |  __/ | " 
print " | .__/|___/\___\__,_|_| |_|_| |_|\___|_| "   
print " |_| "
print "" 
print " Criador: mutr0l    "     
print " Versao: 1.0    " 
print ""                                  

 
ip = raw_input("[+] Digite o IP Ou Endereco: ")
porta = []
x = input("[+] Digite a Quantidade de Portas: ")
i = 0
 
while i < x:
	       porta.append(int(raw_input("[+] Digite a porta: ")))
	       i += 1
	      
print "[+] Verificando se as portas estao abertas... [+]"
	      
for port in porta:	       
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    conexao = cliente.connect_ex((ip, port))
    if conexao == 0:
		print str(port) + "[+] porta aberta [+]"
else:
		print str(port) + "[+] porta fechada [+]"
