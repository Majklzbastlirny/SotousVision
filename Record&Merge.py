import time
import os
import subprocess
import os.path

time = time.strftime("%Y-%m-%d-%H-%M")
rectime = 10
#seconds
rectimems = 10000


vid = ("raspivid -o /home/pi/SotousVisionRAW/SotousVisionRAW_" + time + ".h264 -t 10000")
aud = ("arecord -f dat -d 10 /home/pi/SotousVisionRAW/SotousVisionRAW_" + time + ".wmv")

#subprocess.call(vid, shell=True)
#subprocess.call(vid, shell=True)
both = (aud + " & " + vid)
#print(vid)
#print(aud)
#print(both)
subprocess.call(both)
sleep(10)
end