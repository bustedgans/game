#program game pertama gua:v
#mau recode?mikir dulu ya anjg
import random
import os
import time

b = '\033[34;1m'
g = '\033[32;1m'
p = '\033[35;1m'
c = '\033[36;1m'
r = '\033[31;1m'
w = '\033[37;1m'
y = '\033[33;1m'


os.system('pkg install figlet')
os.system('figlet PERMAINAN')

print ('\033[31;1m[----------------------------------------------]')
print ('\033[31;1m[               Author : Insan Gans            ]')
print ('\033[31;1m[             Team : ATTACKER NETWORK TEAM     ]')
print ('\033[31;1m[             Contact Me : 081295978029        ]')
print ('\033[31;1m[----------------------------------------------]')
print('')

def login():
      print("\033[32;1mWelkom in \033[35;1mTOOLS \033[32;1mMe:v")

login()
print('')
time.sleep(1)
print('\033[35;1mKenalan Dlu su')
nama = input("\033[33;1mNama lo sapa jing: ")
print('\033[35;1mUmur Lu Brp cuk?:v')
age = int(input("\033[33;1mUmur :"))
time.sleep(0.5)

print('')
print('\033[32;1mDaftar Pilihan')
print('')
print('\033[37;1m[\033[34;1m\033[34;1m01\033[37;1m]\033[35;1mBatu')
print('\033[37;1m[\033[34;1m\033[34;1m02\033[37;1m]\033[35;1mGunting')
print('\033[37;1m[\033[34;1m\033[34;1m03\033[37;1m]\033[35;1mKertas')
print('')
 
def permainan():
    kamu = int(input("Lu apa tod: "))
    kom = random.choice(["Batu", "Gunting", "Kertas"])
    if kamu == 1:
        print ("Kamu     : Batu")
        print("Komputer :", kom)
        if kom == "Batu":
            print ("\033[35;1m\tDraw")
        if kom == "Gunting":
            print ("\033[32;1m\tLu menang")
        if kom == "Kertas":
            print ("\033[31;1m\tLu kalah")
    if kamu == 2:
        print ("Kamu     : Gunting")
        print("Komputer :", kom)
        if kom == "Batu":
            print ("\033[31;1m\tKamu kalah")
        if kom == "Gunting":
            print ("\033[35;1m\tDraw")
        if kom == "Kertas":
            print ("\033[32;1m\tLu Menang")
    if kamu == 3:
        print ("Kamu     : Kertas")
        print("Komputer :", kom)
        if kom == "Batu":
            print ("\033[32;1m\tLu menang")
        if kom == "Gunting":
            print ("\033[31;1m\tLu kalah")
        if kom == "Kertas":
            print ("\033[35;1m\tDraw")
    if kamu >= 4:
        print ("Pilihanmu salah!!!")
       
permainan()