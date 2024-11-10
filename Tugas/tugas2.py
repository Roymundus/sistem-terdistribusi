import tkinter as tk
from tkinter import messagebox
import time

class SimulasiSistemTerdistribusi:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulasi Model Komunikasi Terdistribusi")

        # Kanvas untuk representasi visual
        self.kanvas = tk.Canvas(self.root, width=600, height=400)
        self.kanvas.pack()

        # Buat komponen visual
        self.buat_komponen()

        # Tombol untuk memicu simulasi
        self.buat_tombol_simulasi()

    def buat_komponen(self):
        # Membuat representasi server, klien, dan broker
        self.server = self.kanvas.create_rectangle(250, 50, 350, 100, fill="lightblue", tags="server")
        self.kanvas.create_text(300, 75, text="Server")

        self.klien1 = self.kanvas.create_rectangle(50, 300, 150, 350, fill="lightgreen", tags="klien1")
        self.kanvas.create_text(100, 325, text="Klien 1")

        self.klien2 = self.kanvas.create_rectangle(450, 300, 550, 350, fill="lightgreen", tags="klien2")
        self.kanvas.create_text(500, 325, text="Klien 2")

        # Broker untuk publish-subscribe
        self.broker = self.kanvas.create_rectangle(250, 200, 350, 250, fill="lightyellow", tags="broker")
        self.kanvas.create_text(300, 225, text="Broker")

    def buat_tombol_simulasi(self):
        # Membuat tombol simulasi
        tombol_frame = tk.Frame(self.root)
        tombol_frame.pack(pady=10)

        # Tombol-tombol simulasi
        tk.Button(tombol_frame, text="Simulasi Request-Response", command=self.simulasi_request_response).pack(side=tk.LEFT, padx=10)
        tk.Button(tombol_frame, text="Simulasi Publish-Subscribe", command=self.simulasi_publish_subscribe).pack(side=tk.LEFT, padx=10)
        tk.Button(tombol_frame, text="Simulasi Message Passing", command=self.simulasi_message_passing).pack(side=tk.LEFT, padx=10)
        tk.Button(tombol_frame, text="Simulasi RPC", command=self.simulasi_rpc).pack(side=tk.LEFT, padx=10)

    def simulasi_request_response(self):
        self.perbarui_status("Klien 1 mengirimkan Request ke Server...")
        self.animasi_pesan("klien1", "server", "Request")
        self.tunda_pemrosesan()
        self.perbarui_status("Server mengirimkan Response ke Klien 1...")
        self.animasi_pesan("server", "klien1", "Response")

    def simulasi_publish_subscribe(self):
        self.perbarui_status("Klien 1 (Publisher) mengirimkan Publish ke Broker...")
        self.animasi_pesan("klien1", "broker", "Publish")
        self.tunda_pemrosesan()
        self.perbarui_status("Broker memberi notifikasi ke Klien 2 (Subscriber)...")
        self.animasi_pesan("broker", "klien2", "Notify")

    def simulasi_message_passing(self):
        self.perbarui_status("Klien 1 mengirimkan Pesan ke Klien 2...")
        self.animasi_pesan("klien1", "klien2", "Pesan")
        self.tunda_pemrosesan()
        self.perbarui_status("Klien 2 menerima Pesan dari Klien 1.")

    def simulasi_rpc(self):
        self.perbarui_status("Klien 1 memanggil RPC di Server...")
        self.animasi_pesan("klien1", "server", "RPC: sum(5, 3)")
        self.tunda_pemrosesan()
        self.perbarui_status("Server mengeksekusi RPC dan mengembalikan hasil...")
        self.animasi_pesan("server", "klien1", "Hasil: 8")
        self.perbarui_status("RPC selesai. Hasil diterima oleh Klien 1.")

    def animasi_pesan(self, pengirim, penerima, pesan):
        koordinat_pengirim = self.kanvas.bbox(pengirim)
        koordinat_penerima = self.kanvas.bbox(penerima)

        # Membuat teks pesan yang bergerak dari pengirim ke penerima
        teks_pesan = self.kanvas.create_text(koordinat_pengirim[0] + 50, koordinat_pengirim[1] - 20, text=pesan, fill="red")

        # Menghitung langkah-langkah untuk animasi
        jarak = ((koordinat_penerima[0] - koordinat_pengirim[0]) ** 2 + (koordinat_penerima[1] - koordinat_pengirim[1]) ** 2) ** 0.5
        langkah = int(jarak / 5)
        x_diff = (koordinat_penerima[0] - koordinat_pengirim[0]) / langkah
        y_diff = (koordinat_penerima[1] - koordinat_pengirim[1]) / langkah

        for _ in range(langkah):
            self.kanvas.move(teks_pesan, x_diff, y_diff)
            self.root.update()
            time.sleep(0.02)

        # Setelah mencapai penerima, hapus pesan
        self.kanvas.delete(teks_pesan)

    def perbarui_status(self, status):
        self.kanvas.delete("status")
        self.kanvas.create_text(300, 20, text=status, fill="black", tags="status")

    def tunda_pemrosesan(self):
        self.root.update()
        time.sleep(1)

# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = SimulasiSistemTerdistribusi(root)
    root.mainloop()
