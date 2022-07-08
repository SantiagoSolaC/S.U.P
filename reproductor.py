import os
import moviepy.editor as mp
import time
import threading
from pygame import mixer
from pytube import YouTube
from youtubesearchpython import VideosSearch
from tabulate import tabulate
from random import randint






class Sistema:
    def __init__(self):
        self.ruta_descargas="{}\\temp\\descargas".format(os.getcwd())
        self.ruta_reproducir="{}\\temp\\reproducir".format(os.getcwd())
    def descargar(self,link):
        yt=YouTube(link)
        st=yt.streams.filter(mime_type="video/mp4")
        st=st[0]
        audio=yt.streams.get_by_itag(st.itag)
        audio.download(self.ruta_descargas)
    def buscador(self,nombre,clave="None"):
        buscador=VideosSearch(nombre,limit=1)
        r=buscador.result()
        r=r["result"]
        r=r[0]
        info={}
        info["title"]=r["title"]
        info["link"]=r["link"]
        info["duration"]=self.obtener_duracion(r["duration"])
        return info
    def convertidor(self,nombre):
        video=mp.VideoFileClip('{}\\{}.mp4'.format(self.ruta_descargas,nombre))
        video.audio.write_audiofile('{}\\{}.mp3'.format(self.ruta_reproducir,nombre),verbose=False,logger=None)
        #-----------------------------------------------------------------------------NO IMPRIMIR PROGRESO
        video.audio.close()
        video.close()
    def obtener_duracion(self,duracion):
        duracion=duracion.split(":")
        minutos=int(duracion[0])
        segundos=int(duracion[1])
        return minutos*60 + segundos
    def cargar(self,cancion):
        self.descargar(cancion["link"])
        time.sleep(3)
        self.convertidor(cancion["title"])
    def limpiar(self):
        for carpeta in [self.ruta_descargas,self.ruta_reproducir]:
            for archivo in os.listdir(carpeta):
                try:
                    os.remove("{}/{}".format(carpeta,archivo))
                except:
                    pass
class Reproductor:
    def __init__(self):
        self.lista_reproduccion=[]
        self.estado="DETENIDO"
        self.sistema=Sistema()
        self.visual=Visual()
    def agregar_cancion(self,buscar):
        cancion=self.sistema.buscador(buscar)
        self.lista_reproduccion.append(cancion)
    def cambiar_estado(self,state):
        self.estado=tabulate({1:[state]},tablefmt="fancy_grid",stralign="left")
        self.visual.estado()
    def reproducir(self,cancion):
        mixer.init()
        mixer.music.load('{}\\{}.mp3'.format(self.sistema.ruta_reproducir,cancion["title"]))
        mixer.music.play()    
        for i in range(cancion["duration"]):
            time.sleep(1)
        mixer.music.stop()
        mixer.stop()
    def reproducir_lista(self):
        self.cambiar_estado("INICIANDO")
        lista=self.lista_reproduccion # LISTA DE CANCIONES A REPRODUCIR
        lista2=lista[1:]            # LISTA DE CANCIONES A CARGAR
        lista2.append({"title":"FIN"})        # ELEMENTO AGREGADO PARA EVITAR ERRORES
        self.sistema.cargar(lista[0]) # SE CARGA (DESCARGA Y CONVIERTE) LA PRIMERA CANCION
        for c_actual,c_siguiente in zip(lista,lista2): # ITERACION DOBLE, CANCION ACTUAL, CANCION SIGUIENTE
            self.visual.cambiar_color()

            self.subp_repr=threading.Thread(target=self.reproducir,args=(c_actual,),daemon=True) #SUBPROCESO (HILO) DE REPRODUCCION DE AUDIO
            self.subp_repr.start()
            
            self.cambiar_estado("♦ ACTUAL     ► {}\n♦ SIGUIENTE ►► {}".format(c_actual["title"],c_siguiente["title"]))
            self.sistema.limpiar() # BORRAR ARCHIVOS DESCARGADOS (ES IMPORTANTE QUE SEA EN ESTE MOMENTO)
            
            if c_siguiente["title"]=="FIN": # SI ES EL ULTIMO ELEMENTO DE LA LISTA NO CARGAMOS LA SIGUIENTE CANCION
                pass
            else:
                self.subp_cargar=threading.Thread(target=self.sistema.cargar,args=(c_siguiente,),daemon=True)
                self.subp_cargar.start() #CARGAMOS LA SIGUIENTE CANCION
            
            while True:
                if self.subp_repr.is_alive(): # SI EL SUBPROCESO DE REPRODUCCION SIGUE EJECUTANDOSE
                    time.sleep(1) # SINO, ESPERA UN SEGUNDO PARA VOLVER A CHEKEAR
                else:
                    break # SI EL SUBPROCESO DE REPRODUCCION NO SE SIGUE EJECUTANDO ENTONES ROMPEMOS BUCLE
            
            if c_siguiente["title"]=="FIN": # SI ES EL ULTIMO ELEMENTO DE LA LISTA NO CARGAMOS LA SIGUIENTE CANCION
                pass
            else:
                while True:
                    try:
                        if self.subp_cargar.is_alive(): # SI EL SUBPROCESO DE CARGAR SIGUIENTE CANCION SIGUE EJECUTANDOSE ESPERAMOS
                            self.cambiar_estado("CARGANDO SIGUIENTE CANCION")
                            time.sleep(1)
                    except:
                        pass
                    else:
                        break

            try:
                self.subp_cargar._stop() # TERMINAMOS LOS PROCESOS MANUALMENTE POR LAS DUDAS
                self.subp_repr._stop()
            except:
                pass

class UI:
    def __init__(self):
        self.visual=Visual()
    def main_loop(self):
        self.visual.cambiar_color()
        reproductor.limpiar
        while True:
            self.visual.cls()
            print("")
            print(self.visual.espaciado("► REPRODUCTOR DE MUSICA ◄",80))
            print(self.visual.espaciado(self.visual.opciones,80))
            print(self.visual.separador)
            print("           │                            ♦                           │")
            print("           │ Ingrese un nombre para agregar a la lista o una opcion │")
            print("           │________________________________________________________│")
            print("           │")
            selection=input("           │►► ")
            if selection=="exit":
                break
                reproductor.limpiar()
            elif len(selection)<3:
                pass
            elif selection=="play":
                try:
                    reproductor.reproducir_lista()
                except KeyboardInterrupt:
                    pass
            elif selection=="del":
                self.eliminar_cancion()
            else:
                reproductor.agregar_cancion(selection)
    def eliminar_cancion(self):
        while True:
            lista_nombres=[]
            for cancion in reproductor.lista_reproduccion:
                lista_nombres.append(cancion["title"])
            self.visual.cls()
            print("")
            print(self.visual.espaciado("► REPRODUCTOR DE MUSICA ◄",80))
            self.visual.menu("Lista De Reproducción - Eliminar",lista_nombres)
            selection=input("                   │►► ")
            if selection=="0":
                break
            elif int(selection)-1 <= len(reproductor.lista_reproduccion):
                reproductor.lista_reproduccion.pop(int(selection)-1)
            else:
                pass





class Visual:
    def __init__(self):
        opciones={
            "Iniciar Reproducción":["play"],
            "Eliminar Cancion":["del"],
            "Salir":["exit"]}
        self.opciones=tabulate(opciones,tablefmt="fancy_grid",headers="keys",stralign="center")
        self.separador="_______________________________________________________________________________"
        self.separador_centro="                    ________________________________________                    "
    def prompt(self):
        pass
    def cls(self):
        if os.name=="posix":
            os.system("clear")
        elif os.name=="ce"or"nt"or"dos":
            os.system("cls")
    def espaciado(self,texto,ancho):
        resultado=str()
        renglones=texto.split("\n")
        espacios=int(ancho)-len(renglones[0])
        for renglon in renglones:
            x=0
            while x<=espacios/2:
                resultado=resultado+" "
                x=x+1
            resultado=resultado+renglon+"\n"
        return resultado[:-1]
    def menu(self,titulo,opciones):
        print("")
        print(self.separador_centro)
        print(self.espaciado(titulo,80))
        print("                    ____________________♦___________________                    ")
        x=1
        for opcion in opciones:
            if len(opcion)>28:
                o=opcion[:28]
            else:
                o=opcion
            print("                       {}    │   {}".format(x,o))
            print("                    ----------------------------------------")
            x=x+1
        print("                   │   0    │           VOLVER              │")
        print("                   │________│_______________________________│")
        print("                   │")
    def estado(self):
        self.cls()
        print("")
        print(self.espaciado("► REPRODUCTOR DE MUSICA ◄",80))
        print("")
        print(self.espaciado(reproductor.estado,80))
    def cambiar_color(self):
        colores="9ABCDEF"
        os.system("color 0{}".format(colores[randint(0,6)]))




reproductor=Reproductor()
interfaz=UI()
interfaz.main_loop()