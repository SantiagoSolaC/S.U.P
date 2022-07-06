import time

# Asking time for study and rest in minutes...
studyMinutes = int(input("Ingresar tiempo de estudio en minutos: "))
restMinutes = int(input("Ingresar tiempo de descanso en minutos: "))

# Asking for how many times the cicle will be maked...
howManyTimes = int(input("Ingresar cuantas veces se repetira el ciclo: "))

# Changing minutes to seconds, if you want to test this functions in seconds, you just delete " * 60 "...
studySeconds = studyMinutes
restSeconds = restMinutes

# Function S.U.P with Stopwatch...
def supCounter(studySeconds, restSeconds, howManyTimes):

    # Making a bucle for the times asked before...
    for i in range(howManyTimes):
        
        # Creating 2 variables that will decrease on each while bucle...
        studySecondsA = studySeconds
        restSecondsA = restSeconds

        # Stopwatch for study time...
        while studySecondsA:
            mins, secs = divmod(studySecondsA, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            studySecondsA -= 1

        # Here comes the pop-up message that study time is completed and start the rest...
        print(f"Se cumplio el tiempo de estudio, ahora tenes un recreo de {restSeconds} minutos!")

        # Stopwatch for rest time...
        while restSecondsA:
            mins, secs = divmod(restSecondsA, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            restSecondsA -= 1

        #Here comes the pop-up message that rest time is completed and start the study again...
        print(f"Se termino el recreo, de vuelta a estudiar por otros {studySeconds} minutos!")


# Function S.U.P without Stopwatch...
def supWithoutCounter(studySeconds, restSeconds, howManyTimes):

    # Making a bucle for the times asked before...
    for i in range(howManyTimes):

        # Sleep for time equal to studySeconds...
        time.sleep(studySeconds)

        # Here comes the pop-up message that study time is completed and start the rest...
        print(f"Se cumplio el tiempo de estudio, ahora tenes un recreo de {restSeconds} minutos!")

        # Sleep for time equal to restSeconds...
        time.sleep(restSeconds)

        #Here comes the pop-up message that rest time is completed and start the study again...
        print(f"Se termino el recreo, de vuelta a estudiar por otros {studySeconds} minutos!")


supCounter(studySeconds, restSeconds, howManyTimes)
supWithoutCounter(studySeconds, restSeconds, howManyTimes)