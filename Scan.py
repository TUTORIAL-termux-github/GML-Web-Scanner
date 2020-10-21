#!/usr/bin/python
# coding: utf-8

import os
import sys
import socket
os.system("clear")
os.system("echo TOOL INI BERGUNA UNTUK MENCARI HALAMAN WEB |lolcat")
os.system("echo TARGET YANG TERDAPAT CELAH SQL dan XSS  |lolcat")
os.system("sleep 5")
os.system("clear")
os.system("figlet SQL-SEARCH")
print "V 0.1"
print ""
print "======================================="
os.system("echo Author:R3D BULL BAR² |lolcat")
os.system("echo Youtube:R3D BULL CYBER |lolcat")
os.system("echo github:https://github.com/TUTORIAL-termux-github |lolcat")
print "======================================="
print ""
os.system("echo [!] Awal url tidak boleh menggunakan = https/https |lolcat")
name=raw_input('Masukkan web: ')
os.system("clear")
print("sedang mencari celah keamanan sql injection | %s |" % name)
print "Mohon tunggu beberapa saat"
addr=socket.gethostbyname(name)
print("ip webnya {} = {}".format(name, addr))
os.system("google --rua %s php id=" % name)
os.system("google --rua %s php?cid=" % name)
print "Scan web selesai"
