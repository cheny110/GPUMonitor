
from typing import List
import subprocess
from log import eventLogger
from time import sleep

from notify import emailNotify

def decorcate_event(func):
    def wrapper(*args,**kargs):
        print("interval_event:",*args,**kargs)
        print("delay for 3 secs...")
        sleep(3)
        if len(args)>1:
            receiver=args[-1]
            emailNotify(receiver,"your event {} had triggered.".format(func.__name__))
        func(*args,**kargs)
    return wrapper

@decorcate_event
def run_shell_Cmd(cmd:List,*arg,**kargs):
    try:
        subprocess.call(cmd,shell=True)
        eventLogger.info("run shell cmd once:"+str(cmd))
    except Exception as e:
        print(e)
        eventLogger.error("run shell cmd:"+str(cmd)+"failed"+e )
   
    

@decorcate_event
def run_shell_file(filePath,*args,**kargs):
    try:
        eventLogger.info("run shell from file once"+filePath)
        subprocess.call(["/bin/bash",filePath])
    except Exception as e:
        eventLogger.error("run shell from file:"+str(filePath)+"failed"+e )



@decorcate_event
def run_python_script(filePath,*arg,**kargs):
    script=None
    with open (filePath,"r")as scriptFile:
        script=scriptFile.read()
        scriptFile.close()
    if script is not None:
        try:
            exec(script)
            eventLogger.info("run python script once:"+filePath)
        except Exception as e:
            eventLogger.error("run python script from file:"+str(filePath)+"failed"+e)



if __name__=="__main__":
    run_shell_Cmd(["notify-send","hello"])
