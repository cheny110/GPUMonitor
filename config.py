
import json
from base64 import b64decode,b64encode
import sys
from unicodedata import name


#encodeConfig=b64encode(str(config).encode("utf-8"))
#decodeConfig=b64decode(encodeConfig)



def alterConfig(key=None,value=None):
    conf=None
    with open("./config.conf","r+b")as rawFile:
        encript=rawFile.read()
        conf=b64decode(encript).decode("utf-8").replace('\'','\"').replace("None","null")
        #print(conf)
        config=json.loads(conf)
        rawFile.close()
    if key not in config.keys():
        print("error configuration item. supported configurations include:",config.keys())
        print("\n your item is :",key)
        sys.exit(0)
    else:
        config[key]=value
    # save updated configuration 
    with open("./config.conf","w+b")as newFile:
        encodeConfig=b64encode(str(config).encode("utf-8"))
        newFile.write(encodeConfig)
        newFile.close()

def loadConfig():
    conf=None
    with open("./config.conf","r+b")as rawFile:
        encript=rawFile.read()
        conf=b64decode(encript).decode("utf-8").replace('\'','\"').replace("None","null")
        conf=json.loads(conf)
        rawFile.close()
    return conf
    

config=loadConfig()

if __name__=="__main__":
    print(config)
    