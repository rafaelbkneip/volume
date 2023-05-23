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


cont = 0

while(True):

    data, dia = return_date.today()

    print(data)
    print(dia)

    #if ((dia == 4 and int(str(data).split(" ")[1].split(":")[0]) >= 19)  or dia == 5 or dia == 6): SA1

    if ((dia == 4 and int(str(data).split(" ")[1].split(":")[0]) == 23)  or dia == 5 or dia == 6): #SA2
        volume.SetMasterVolumeLevel(-65, None)

    else:
        volume.SetMasterVolumeLevel(-10, None)
    


    sleep(60)

