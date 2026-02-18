import tkinder as tk   #Para la interfaz grafica
from tkinder import ttk #Para agregar mas estilos
import socket           #Para ña comunicacion en red 
import threading
import time             #Para manejar tiempos de espera 

#--- CONFIGURACION---
IP_ESP32="192.168.20.37"#Cambio por la IP que de el ESP32
PUERTO = 80

#--- CLASE DE DATOS (Para practicar)
class DatosSensor:
    def_init_(self,valor):
        self.valor = valor 
#---