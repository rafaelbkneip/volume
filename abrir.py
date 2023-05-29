import subprocess

from time import sleep


import return_date

#None aberto, 1 fechado

def abrir():

    open = subprocess.Popen([''])
    sleep(15)

    while (True):

        data, dia = return_date.today()

        print(data)
        print(dia)

        #Para essa aplicação, o computador deve ser mutado após às 23 horas das sextas, nos sábados e nos domingos /  For this application, the computer must be muted after Friday at 11 p.m., on Saturdays and on Sundays
        if ((dia == 4 and int(str(data).split(" ")[1].split(":")[0]) == 23)  or dia == 5 or dia == 6):

            
            poll = open.poll()

            if poll is None:
                open.terminate()

            else:
                print("Fechado.")

                sleep(15)
            
            
        else:

            poll = open.poll()

            if poll is None:
                print('Aberto.')

            else:
                open = subprocess.Popen([''])

        
        sleep(60)

