#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################################
####Script para conectar WebSocket con OBS y desplegar las escenas, se puede  ####
####cambiar de escena digitando elumero.o.                                    ####
####BY:  a2mx                                                                 ####
##################################################################################



import os
import sys
import time
import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, requests  # noqa: E402

host = "127.0.0.1"
port = 4444
password = "changeme"

ws = obsws(host, port, password)
ws.connect()

try:
    list=[]
    scenes = ws.call(requests.GetSceneList())

    for s in scenes.getScenes():
        name = s['name']
        list.append(name) 


except KeyboardInterrupt:
    pass



def menu():

    """

    Funcion que limpia la pantalla y muestra nuevamente el menu

    """

    #os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    os.system('clear')

    print ("""
        `--         .-`               
          `--     --                  
       ....../o/++-............        
      |  ---------------   :-  |              _    
      | |               |  +   |     ___  ___| |___   __         
      | |               | .--  |    / __|/ _ \ __\ \ / /     
      | |               | o::+ |    \__ \  __/ |_ \ V /     
      | |               | `--` |    |___/\___|\__| \_/   
      |  ---------------       |       
      `------------------------`         by: a2mx
         ++                 ++
          """)


    print ("Select Overlay")


    cont=1
    for n in list:
        opnum=str(cont)
        print("\t"+opnum+" - "+n)
        cont+=1

    print ("\t99 - salir")
    return cont

#para mantener el menu activo
while True:

    while True:
        try:
            a=menu()
            opcionMenu = int(input("type an option >> "))

            break
        except ValueError:
            print("No valid integer! Please try again ...")
            time.sleep(2)
            os.system('clear')

    #ciclo para cada una de las escenas
    for i in range(0, a):
        #if para la seleccion del usuario
        if opcionMenu==i:
            e=i-1
            o=list[e]
            print(u"Switching to {}".format(o))
            ws.call(requests.SetCurrentScene(o))
            time.sleep(1)
            break


    if opcionMenu==99:

        break


ws.disconnect()
