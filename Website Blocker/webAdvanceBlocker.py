import datetime
import time

# -------- CONFIG --------
SITES_TO_BLOCK = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com"
]

REDIRECT_IP = "127.0.0.1"
HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"

START_HOUR = 9   # 9 AM
END_HOUR = 18    # 6 PM


def is_block_time():
    now = datetime.datetime.now().hour
    return START_HOUR <= now < END_HOUR


def block_sites():
    with open(HOSTS_PATH, "r+") as file:
        content = file.read()

        for site in SITES_TO_BLOCK:
            entry = f"{REDIRECT_IP} {site}"
            if entry not in content:
                file.write(entry + "\n")


def unblock_sites():
    with open(HOSTS_PATH, "r+") as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            if not any(site in line for site in SITES_TO_BLOCK):
                file.write(line)

        file.truncate()


while True:
    if is_block_time():
        print("Blocking websites...")
        block_sites()
    else:
        print("Unblocking websites...")
        unblock_sites()

    time.sleep(5)