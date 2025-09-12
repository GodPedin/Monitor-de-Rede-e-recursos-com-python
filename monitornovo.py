import tkinter as tk
import psutil
import time
def cor_progresso(valor):
    if valor < 50:
        return "green"
    elif valor < 80:
        return "orange"
    else:
        return "red"
    
def medir_rede(intervalo=1):
    global last_net_io, last_time
    net_io = psutil.net_io_counters()
    now = time.time()
    if last_net_io is None:
        last_net_io = net_io
        last_time = now
        return 0,0
    tempo = now - last_time
    download = (net_io.bytes_recv - last_net_io.bytes_recv) / tempo
    upload = (net_io.bytes_sent - last_net_io.bytes_sent) / tempo
    last_net_io = net_io
    last_time = now
    download_mbps = (download * 8) / (1024 * 1024)
    upload_mbps = (upload * 8) / (1024 * 1024)
    return download_mbps, upload_mbps
def atualizar():
    down,up = medir_rede()
    label_download.config(text=f"Download: {down:.2f} Mbps")
    label_upload.config(text=f"Upload: {up:.2f} Mbps")
    root.after(1000, atualizar)

root = tk.Tk()
root.title("Gerenciador de processos e rede")
root.geometry("500x300")
root.resizable(False,False)
label_download = tk.Label(root, text ="Download: 0.00 Mbps" ,font=("Arial",14))
label_download.pack(pady=10)
label_upload = tk.Label(root,text="Upload: 0.00 Mbps", font=("Arial",14))
label_upload.pack(pady=10)
last_net_io = None
last_time = None
atualizar()
root.mainloop()