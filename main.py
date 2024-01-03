import port_scanner


portScanner = port_scanner.scanner()

portScanner.getOpenPorts("heartlandsupport.us", [20, 8450], True)
