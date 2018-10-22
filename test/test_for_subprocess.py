#encoding=utf-8
import subprocess
import time


def test():
    binpath = r"f:\Tools\makedata.exe"
    popen = subprocess.Popen(binpath)
    waitsecond = 0
    while (popen.poll() == None):
        print 'not finished'
        time.sleep(1)
        waitsecond = waitsecond + 1
        if(waitsecond >= 30):
            popen.kill()

    print 'end'



test()
print 'end2'
