import time
from datetime import datetime as dt

# Hosts files
# /etc/hosts
hosts_path_0unix = "/etc/hosts"
hosts_temp = "hosts"

redirect = "127.0.0.1"

website_list = [
    'www.xataka.com', 'store.playstation.com', 'www3.animeflv.net', 'mercadolibre.com.co',
    'ebiblioteca.org', 'www.amazon.com', 'www.lectulandia2.org', 'cuevana3.io', 'www.netflix.com', 'www.olx.com.co', 'www.disneyplus.com', 'www.bbc.com'
]

from_hour = 6
to_hour = 16

while True: 
    if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print("Working...")

        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " +  website + "\n")
            

    else:
        print("Fun...")
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
                
            
        
    
    time.sleep(1)
    