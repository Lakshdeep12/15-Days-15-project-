import datetime
import time

end_time = datetime.datetime(2024, 6, 30, 23, 59, 59)  # Set the end time for blocking
hosts_path = "C:/Windows/System32/drivers/etc/hosts"  # Path to
sites_to_block = ["www.facebook.com", "www.youtube.com"]  
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        print("Blocking sites...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in sites_to_block:
                if site not in content:
                    file.write(redirect + " " + site + "\n")
    else:        
        print("Unblocking sites...")
        with open(hosts_path, 'r+') as file:    
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites_to_block):
                    file.write(line)
            file.truncate()
            time.sleep(5)  # Check every 5 seconds