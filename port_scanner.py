import socket
import common_ports


class scanner:
    
    #initialize mode False by default
    def _init_(self,mode,portRange):
        self.mode = mode
        self.portRange = portRange
        mode = False
        portRange = []
        

    def getOpenPorts(self, target, portRange, optional:mode):
        #create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #make a copy of the keys
        portList = list(common_ports.ports_and_services.keys())
        serviceList = list(common_ports.ports_and_services.values())
        openPorts = {}
       
        #grab hi and low ports from portRange list
        lowPort = portRange[0]
        hiPort = portRange[1]
        
        #iterate through the ports, save open ports to list 
        index = 0
        for i in portList:
            if (i == lowPort or i <= hiPort):
                location = (target, i)
                if(s.connect_ex(location) == 1):
                    #if open, add to Dictionary
                    print(f"port: {i} is open")
                    openPorts[index] = common_ports.ports_and_services.copy()[i]  
                    index += 1  
                #increase the index and lowPort          
                else:
                    print(f"port {serviceList[index]} is closed") 
                    index += 1      
                s.close()

        print("\n")
        if mode == True:
            if(openPorts == None):
                print(f"There are no open ports at {target}")
            else:
                print(f"Open ports for {target})")
                print("PORT     SERVICE")
                for i in openPorts:
                    print(f"{openPorts.keys()[i]}      {openPorts.item()[i]}")
