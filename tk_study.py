from tkinter import *
from tkinter import ttk 
import time
from tkinter import messagebox



class Window():

    def __init__(self, window):
        
        self.root = window
        window.geometry('400x250')
        window.title('Centro de estudio')
        
        self.nb = ttk.Notebook(window)
        self.nb.pack(fill= 'both', expand= 'yes')

        self.p1 = ttk.Frame(self.nb)
        self.p2 = ttk.Frame(self.nb)

        self.nb.add(self.p1, text='Método de estudio')
        self.nb.add(self.p2, text='Reproductor de música')

        

        '''
        ### LABELS PESTAÑA 1 ###
        '''
        self.label1 = Label(self.p1, text='Ingrese los tiempos: ', font=(12))
        self.label1.pack(anchor=CENTER)
        self.label1.config(width=400)

        self.n_estudio = Label(self.p1, text="Estudio",
                              font=(10)).place(x=0, y=45)

        self.n_descanso = Label(
            self.p1, text="Descanso", font=(10)).place(x=0, y=90)
        self.n_veces = Label(self.p1, text='Repeticiones', font=(10)).place(x=0,y=135)



        '''
        ### BOTONES PESTAÑA 1 ###
        '''

        self.cronometro = Button(self.p1, text="Empezar cronometro",  padx=10, command=self.cronometro,
                                      pady=3, activebackground="green", activeforeground="white")
        self.cronometro.place(x=170, y=180)
    

        '''
        ### ENTRYS PESTAÑA 1 ###
        '''

        self.e_estudio = Entry(self.p1)
        self.e_descanso= Entry(self.p1)
        self.e_veces = Entry(self.p1)

        self.e_estudio.place(x=175, y=45)
        self.e_descanso.place(x=175, y=90)
        self.e_veces.place(x=175, y= 135)

        '''
        ### LABELS PESTAÑA 2 ###
        '''

        self.reproducir = Label(self.p2, text="Aquí va nombre de la cancion",
                              font=(10))
        self.reproducir.place(x=80, y=50)
        
        self.play = Button(self.p2, text="Play",  padx=10,
                                      pady=3, activebackground="green", activeforeground="white")
        self.play.place(x=140, y=100)

        self.stop = Button(self.p2, text="Stop",  padx=10,
                                      pady=3, activebackground="green", activeforeground="white")
        self.stop.place(x=200, y =100)
    
    def cronometro(self):
        studySeconds = int(self.e_estudio.get())
        restSeconds = int(self.e_descanso.get())
        howManyTimes = int(self.e_veces.get())

        # Making a bucle for the times asked before...
        for i in range(howManyTimes):
            # Sleep for time equal to studySeconds...
            time.sleep(studySeconds)
            messagebox.showinfo(
            'Centro de estudio', 'El tiempo de estudio ha concluido, disfruta de tu recreo!')
            # Sleep for time equal to restSeconds...
            time.sleep(restSeconds)
            #Here comes the pop-up message that rest time is completed and start the study again...
            messagebox.showinfo(
            'Centro de estudio', 'Tu recreo terminó')
            
