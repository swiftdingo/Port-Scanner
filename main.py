import port_scanner


portScanner = port_scanner.scanner()

portScanner.getOpenPorts("104.175.19.70", [20, 115], True)
