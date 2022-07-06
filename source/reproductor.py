import os
import moviepy.editor as mp
import time
import threading
from os import getcwd,listdir
from pygame import mixer
from pytube import YouTube
from youtubesearchpython import VideosSearch







class Sistema:
    def __init__(self):
        self.ruta_descargas="{}\\temp\\descargas".format(getcwd())
        self.ruta_reproducir="{}\\temp\\reproducir".format(getcwd())
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
        if clave=="None":
            return r # retorna diccionario
        else:
            return r[clave] #retorna clave
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
        self.convertidor(cancion["title"])
    def limpiar(self):
        os.system("erase /Q {}".format(self.ruta_descargas))
        os.system("erase /Q {}".format(self.ruta_reproducir))
class Reproductor:
    def __init__(self):
        self.siguiente=False
        self.parar=False
        self.lista_buscar=[]
        self.lista_resultados=[]
        self.sistema=Sistema()
    def sig(self):              #--------------------------------
        self.siguiente=True     # FUNCION PARA BOTON SIGUIENTE
    def stop(self):             #--------------------------------
        self.siguiente=True
        self.parar=True         # FUNCION PARA BOTON PARAR
    def buscar_resultados(self):
        self.lista_resultados.clear()
        for busqueda in self.lista_buscar:
            self.lista_resultados.append(self.sistema.buscador(busqueda))
    def reproducir(self,cancion):
        mixer.init()
        mixer.music.load("{}\\{}.mp3".format(self.sistema.ruta_reproducir,cancion["title"]))
        mixer.music.play()    
        
        for i in range(1,self.sistema.obtener_duracion(cancion["duration"])):
            time.sleep(1)
        
        mixer.music.stop()
        mixer.stop()
    def reproducir_lista(self):
        lista=self.lista_resultados # LISTA DE CANCIONES A REPRODUCIR
        lista2=lista[1:]            # LISTA DE CANCIONES A CARGAR
        lista2.append("FIN")        # ELEMENTO AGREGADO PARA EVITAR ERRORES
        self.sistema.cargar(lista[0]) # SE CARGA (DESCARGA Y CONVIERTE) LA PRIMERA CANCION
        
        for c_actual,c_siguiente in zip(lista,lista2): # ITERACION DOBLE, CANCION ACTUAL, CANCION SIGUIENTE
            self.siguiente=False
            self.parar=False
            subp_repr=threading.Thread(target=self.reproducir,args=(c_actual,),daemon=True) #SUBPROCESO (HILO) DE REPRODUCCION DE AUDIO
            subp_repr.start()
            self.sistema.limpiar() # BORRAR ARCHIVOS DESCARGADOS (ES IMPORTANTE QUE SEA EN ESTE MOMENTO)
            
            if c_siguiente=="FIN": # SI ES EL ULTIMO ELEMENTO DE LA LISTA NO CARGAMOS LA SIGUIENTE CANCION
                pass
            else:
                subp_cargar=threading.Thread(target=self.sistema.cargar,args=(c_siguiente,),daemon=True)
                subp_cargar.start() #CARGAMOS LA SIGUIENTE CANCION
            while True:
                if subp_repr.is_alive() == True: # SI EL SUBPROCESO DE REPRODUCCION SIGUE EJECUTANDOSE
                    if self.siguiente==True:
                        break # SI SE PRESIONÓ EL BOTON DE SIGUIENTE O PARAR ROMPER BUCLE
                    else:
                        time.sleep(1) # SINO, ESPERA UN SEGUNDO PARA VOLVER A CHEKEAR
                else:
                    break # SI EL SUBPROCESO DE REPRODUCCION NO SE SIGUE EJECUTANDO ENTONES ROMPEMOS BUCLE
            
            if self.parar==True:
                break # SI SE PRESIONÓ EL BOTON DE PARAR ROMPER BUCLE
            
            while True:
                if subp_cargar.is_alive()==True: # SI EL SUBPROCESO DE CARGAR SIGUIENTE CANCION SIGUE EJECUTANDOSE ESPERAMOS
                    self.estado="CARGANDO SIGUIENTE CANCION"
                    time.sleep(1)
                else:
                    break
            subp_cargar._stop() # TERMINAMOS LOS PROCESOS MANUALMENTE POR LAS DUDAS
            subp_repr._stop()
