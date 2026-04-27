from tkinter import *
from speedtest import Speedtest
import threading

def check_speed():
    download_label.config(text="Testing...")
    upload_label.config(text="")
    check_button.config(state="disabled")

    def run_test():
        st = Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000

        # Safely update UI from main thread
        sp.after(0, update_ui, download_speed, upload_speed)

    threading.Thread(target=run_test).start()

def update_ui(download, upload):
    download_label.config(text=f"Download Speed: {download:.2f} Mbps")
    upload_label.config(text=f"Upload Speed: {upload:.2f} Mbps")
    check_button.config(state="normal")

sp = Tk()
sp.title("Internet Speed Checker")
sp.geometry("300x150")

check_button = Button(sp, text="Check Speed", command=check_speed)
check_button.pack(pady=10)

download_label = Label(sp, text="")
download_label.pack()

upload_label = Label(sp, text="")
upload_label.pack()

sp.mainloop()