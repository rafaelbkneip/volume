#Antes de rodar o código, deverão ser instalados os seguintes pacotes / Before running the code, it must be installed the following packages
#pip install comtypes
#pip install pycaw

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from time import sleep
import return_date

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

while(True):

    data, dia = return_date.today()

    print(data)
    print(dia)

    #Para essa aplicação, o computador deve ser mutado após às 23 horas das sextas, nos sábados e nos domingos /  For this application, the computer must be muted after Friday at 11 p.m., on Saturdays and on Sundays
    if ((dia == 4 and int(str(data).split(" ")[1].split(":")[0]) == 23)  or dia == 5 or dia == 6):
        volume.SetMasterVolumeLevel(-65, None)

    #Em qualquer outro dia, o som deve ser ligado no volume máximo / On any other day, the sound must be on and at maximum volume
    else:
        volume.SetMasterVolumeLevel(0, None)
    
    sleep(3600)

