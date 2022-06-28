
from tkinter import NONE
from pynvml import *

from log import eventLogger,monitorLogger
from config import config
from events import *


class GpuMonitor():
    def __init__(self,config=config,spareEvent=None,spareEventArg=None,occupyEvent=None,occupyEventArg=None,monitorDevice=[0],notifyReceiver=None) -> None:
        #self.config=config
        self.monitorInterval=0
        self.spareEvent=spareEvent
        self.occupyEvent=occupyEvent
        self.LOWTHRES=int(config["lowThres"])
        self.HIGHTHRES=int(config["highThres"])
        self.spareEventArg=spareEventArg
        self.occupyEventArg=occupyEventArg
        self.monitorDevice= monitorDevice if monitorDevice is not None  else config["monitorDevice"]
        self.notifyReceiver=notifyReceiver if notifyReceiver is not None else config["receiver"]
        nvmlInit()
        self.deviceCount=nvmlDeviceGetCount()
        for i in range(self.deviceCount):
            exec("self.handler{}=nvmlDeviceGetHandleByIndex({})".format(i,i))
            exec("self.statusDict{}=dict()".format(i))
    
    
    def updateStatus(self):
        for i in range(self.deviceCount):
            exec("self.infor{}=nvmlDeviceGetMemoryInfo(self.handler{})".format(i,i))
            #monitorLogger.info("monitor update status once.")

    def monitor(self):
        for i in range(self.deviceCount):
            if i in self.monitorDevice:
                #exec("print('mem occupy:',self.infor{}.used/1024/1024)".format(i))
                exec("if self.infor{}.used/1024/1024 < self.LOWTHRES and self.spareEvent is not None:\r\n self.spareEvent(self.spareEventArg,self.notifyReceiver)".format(i,i))
                exec("if self.infor{}.used/1024/1024> self.HIGHTHRES and self.occupyEvent is not None:\r\n self.occupyEvent(self.occupyEventArg,self.notifyReceiver)".format(i,i))







if __name__== "__main__":
    gmonitor=GpuMonitor(occupyEvent=run_shell_Cmd,occupyEventArg=['notify-send','hello'])
    gmonitor.updateStatus()
    gmonitor.monitor()
    
            
