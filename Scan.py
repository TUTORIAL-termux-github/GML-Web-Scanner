#!/usr/bin/python2
import os,sys,socket
os.system('clear')
print "[•] Menyiapkan Installasi"
os.system('clear')
os.system('pkg install nmap -y')
os.system('pkg update && pkg upgrade')
os.system('clear')
os.system('pkg install python')
os.system('pkg install toilet')
os.system('clear')
print "[√] Installasi Selesai"
os.system('clear')
pilih = raw_input('pilih nomor:')
if pilih == "1":
   os.system('pkg update')

              
