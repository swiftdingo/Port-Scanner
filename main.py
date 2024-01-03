import port_scanner


portScanner = port_scanner.scanner()

portScanner.getOpenPorts("192.168.0.1", [20, 88], True)
