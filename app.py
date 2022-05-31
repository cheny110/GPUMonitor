from ast import arg
from email.policy import default
from tkinter import N
from tkinter.tix import Tree
from monitor import GpuMonitor
import sys
from events import *


__VERSION="1.1.0"

__help='''
gpu-monitor--help monitors GPU memory and execute events when GPU memory satisfys the setting demand.

-h : output this help message.

-v(V) :show version information.

-u(U): show latest update information. 

--shell-cmd: the shell command that need to be execute as events.
--shell-script: the shell script file that need to be execute as events.
--python-script: the python script file that need to be execute as events, 
                 default python interpreter will be used.

--event-type : can be spare-event or occupy-event ,which will be executed when GPU memory is spare or occupied.
--monitor-device: should be list like [0], [0,1],[0,1,2] ,etc. the GPU device that you want to monitor. if no specified, default config will be used.

--notify-receiver: follow receiver's email link,  if not provided, config option will be used.

@author:Cheny chenyprivate@vip.qq.com
@web: https://chenycherry.top 
@License: GPL v3  This is an open source software. No one should make profits from this. If you find actions violate the license, please contact "chenyprivate@vip.qq.com" 
'''

__update_infor='''
                 from version : {1.0.0}
                 to version :{1.1.0}
                 update: 
                    1.fix adding --monitor-device param from system args.
                    2. add notification by email function.
                            '''


def main(): 
    
    args=sys.argv
    cmd=None
    filepath=None
    monitor=None
    triggerType=None
    cmdType=None
    monitorDevice=None
    notifyReceiver=None
    if len(args)<=1:
        print(__help)
        sys.exit(0)
    for i in range(args.__len__()):
        if args[i]=="-h":  #output help information
            print(__help)
            sys.exit(0)
        elif args[i]=="-v" or args[i]=="-V":
            print(__VERSION)
            sys.exit(0)
        elif args[i]=="-u" or args[i]=="-U":
            print(__update_infor)
            sys.exit(0)
        elif args[i] == "--shell-cmd":
            cmdType=args[i]
            try:
                cmd=list(args[i+1].split())
            except:
                print("wrong command type, run -h for help.")
                sys.exit(0)
        elif args[i] == "--shell-script":
            cmdType=args[i]
            try:
                filepath=args[i+1]
            except:
                print("error, wrong shell script path, run -h for help")
                sys.exit(0)
        elif args[i] == "--python-script":
            cmdType=args[i]
            try:
                filepath=args[i+1]
            except Exception as e:
                print("error, wrong python script path, run -h for help")
                sys.exit(0)
        elif args[i] == "--event-type":
            try:
                triggerType=args[i+1]
            except Exception as e:
                print("no event trigger type, run -h for help")
                exit(0)
        elif args[i]=="--monitor-device":
            try:
                strlist=args[i+1].replace('[','').replace(']','').split()
                monitorDevice=[int(x) for x in strlist]
                print(monitorDevice)
            except Exception as e:
                print("monitor-device not specified ,run -h for help")
        elif args[i]=="--notify-receiver":
            try:
                if args[i+1].find('@') is not -1 and args[i+1].endswith(".com"):
                    notifyReceiver=args[i+1]
            except Exception as e:
                print("No email address for receiver avaliable,default receiver will be used in config file.")

        

    # build monitor
    eventLogger.info("bulding monitor according to system parameters ...")
    if triggerType=="spare-event" and  cmdType == "--shell-cmd":
        monitor=GpuMonitor(spareEvent=run_shell_Cmd,spareEventArg=cmd,monitorDevice=monitorDevice,notifyReceiver=notifyReceiver)
    elif triggerType=="spare-event" and cmdType=="--shell-script":
        monitor=GpuMonitor(spareEvent=run_shell_file,spareEventArg=filepath,monitorDevice=monitorDevice,notifyReceiver=notifyReceiver)
    elif triggerType=="spare-event" and cmdType=="--python-script":
        monitor=GpuMonitor(spareEvent=run_python_script,spareEventArg=filepath,monitorDevice=monitorDevice,notifyReceiver=notifyReceiver)
    elif triggerType=="occupy-event" and  cmdType == "--shell-cmd":
        monitor=GpuMonitor(occupyEvent=run_shell_Cmd,occupyEventArg=cmd,monitorDevice=monitorDevice,notifyReceiver=notifyReceiver)
    elif triggerType=="occupy-event" and  cmdType == "--shell-script":
        monitor=GpuMonitor(occupyEvent=run_shell_file,occupyEventArg=cmd,monitorDevice=monitorDevice,notifyReceiver=notifyReceiver)
    elif triggerType=="occupy-event" and  cmdType == "--python-script":
        monitor=GpuMonitor(occupyEvent=run_python_script,occupyEventArg=cmd,monitorDevice=monitorDevice,notifyReceiver=notifyReceiver)
    else:
        print(__help)
        sys.exit(0)
    eventLogger.info("start running...")
    while True:
        monitor.updateStatus()
        monitor.monitor()

if __name__=="__main__":
    main()
    