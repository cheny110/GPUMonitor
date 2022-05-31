import logging

from config import config

logLevel=logging.DEBUG

logging.basicConfig(
                    datefmt=f"%Y-%m-%d:%H:%M:%S",
                    format="%(asctime)s %(filename)s %(levelname)s %(message)s",
                    level=logLevel                 )

monitorLogHandler=logging.FileHandler(config["monitorlogFile"],mode="w", encoding=config["logEncoding"])
formater=logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",datefmt=f"%Y-%m-%d:%H:%M:%S")
monitorLogger=logging.getLogger("monitor")
monitorLogHandler.setFormatter(formater)
monitorLogger.addHandler(monitorLogHandler)
monitorLogger.setLevel(logLevel)

eventLogger=logging.getLogger("event")
eventLogHandler=logging.FileHandler(config["eventlogFile"],mode="w",encoding=config["logEncoding"])
eventLogHandler.setFormatter(formater)
eventLogger.addHandler(eventLogHandler)
eventLogger.setLevel(logLevel)


