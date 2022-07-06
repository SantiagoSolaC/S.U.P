Reproductor de música programado en python. 

La dinamica del sistema es:
    1. Buscar.
    2. Descargar.
    3. Convertir.
    4. Reproducir.
    5. Borrar.
    
 
Metodos:
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Buscar: este metodo recibe un string de búsqueda. Utilizando el módulo "VideoSearch" de la libreria "youtubesearchpython" retornamos un diccionario de valores:
            type
            id
            title <--- Nombre de cancion y archivo
            publishedTime
            duration <---- Duracion en formato string, debe ser convertido a segundos
            viewCount
            thumbnails <---- Miniatura (es un diccionario, las claves son "url","width","height" si no me equivoco xd
            richThumbnail
            descriptionSnippet
            channel
            accessibility
            link <-- Esta clave usamos para descargar
            shelfTitle
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Descargar: este metodo recbe un link en formato string. Utilizando el modulo 'YouTube' de la libreria 'pytube' descarga un archivo '.mp4'.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Convertir: este metodo recibe un nombre de archivo. Utilizando el modulo 'moviepy.editor' convierte un archivo '.mp4' a '.mp3'. Las rutas están ensambladas en el                    codigo
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Reproducir: este metodo recibe un nombre de archivo y una duracion. 
                - Utilizando el modulo "mixer" (metodo 'music') de la libreria 'pygame' reproducimos el audio.
                - Utilizando el modulo "time" (metodo 'sleep') esperamos la duracion del audio para finalizar la funcion.
        Externo - Utilizando el modulo threading (clase 'Thread()') ejecutamos la funcion en un hilo paralelo.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Borrar: este metodo elimina los archivos '.mp4' y '.mp3' de sus respectivas carpetas, utilizando el modulo os (metodo 'system("erase /Q ruta")'). Es importante                 elegir el momento, para evitar fallos.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


Las librerias necesarias están especificadas en el archivo 'requirements.txt'. 
Para instalarlas ejecutar: "pip install -r requirements.txt"
