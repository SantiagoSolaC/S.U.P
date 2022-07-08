from tkinter import *
from tkinter import ttk 
import time
from tkinter import messagebox



class Window():

    def __init__(self, window):       
        self.root = window
        window.geometry('400x250')
        window.title('Centro de estudio')
        


        '''
        ### LABELS  ###
        '''
        self.label1 = Label(window, text='Ingrese los tiempos: ', font=(12))
        self.label1.pack(anchor=CENTER)
        self.label1.config(width=400)

        self.n_estudio = Label(window, text="Estudio",
                              font=(10)).place(x=0, y=45)

        self.n_descanso = Label(
            window, text="Descanso", font=(10)).place(x=0, y=90)
        self.n_veces = Label(window, text='Repeticiones', font=(10)).place(x=0,y=135)



        '''
        ### BOTONES ###
        '''

        self.cronometro = Button(window, text="Empezar cronometro",  padx=10, command=self.cronometro,
                                      pady=3, activebackground="green", activeforeground="white")
        self.cronometro.place(x=170, y=180)
    

        '''
        ### ENTRYS###
        '''

        self.e_estudio = Entry(window)
        self.e_descanso= Entry(window)
        self.e_veces = Entry(window)

        self.e_estudio.place(x=175, y=45)
        self.e_descanso.place(x=175, y=90)
        self.e_veces.place(x=175, y= 135)

     
       
    
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
            
