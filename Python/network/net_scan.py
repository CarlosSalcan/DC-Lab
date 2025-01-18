import nmap

def scan_network():
    # Crea un objeto para escanear la red
    nm = nmap.PortScanner()
    
    ip_range = "192.168.1.0/24" 

    # Realiza el escaneo en la red
    nm.scan(hosts=ip_range, arguments='-sn')  # '-sn' significa escaneo sin puertos (ping scan)

    for host in nm.all_hosts():  
        if 'mac' in nm[host]['addresses']: 
            ip = nm[host]['addresses'].get('ipv4', 'IP no encontrada')
            mac = nm[host]['addresses']['mac']
            
            print("IP:", ip)
            print("MAC:", mac)

scan_network()
