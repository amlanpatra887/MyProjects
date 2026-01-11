import tkinter as tk
from tkinter import messagebox, ttk
import qrcode
from PIL import Image, ImageTk
from urllib.parse import quote
import re


class UPIQRGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("UPI QR Code Generator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # UPI App URLs
        self.upi_urls = {
            "PhonePe": "upi://pay?pa={upi_id}&pn=Merchant&am=&cu=INR",
            "Paytm": "upi://pay?pa={upi_id}&pn=Merchant&am=&cu=INR",
            "Google Pay": "upi://pay?pa={upi_id}&pn=Merchant&am=&cu=INR"
        }

        self.setup_ui()

    def setup_ui(self):
        title_label = tk.Label(self.root, text="UPI QR Code Generator",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter UPI ID:", font=("Arial", 12)).pack()
        self.upi_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
        self.upi_entry.pack(pady=5)
        self.upi_entry.bind('<Return>', lambda e: self.generate_qr())

        tk.Label(input_frame, text="Select App:", font=("Arial", 12)).pack(pady=(10,0))
        self.app_var = tk.StringVar(value="PhonePe")
        app_combo = ttk.Combobox(input_frame, textvariable=self.app_var,
                                values=list(self.upi_urls.keys()),
                                state="readonly")
        app_combo.pack(pady=5)

        generate_btn = tk.Button(self.root, text="Generate QR Code",
                                 command=self.generate_qr,
                                 bg="#4CAF50", fg="white",
                                 font=("Arial", 12, "bold"))
        generate_btn.pack(pady=20)

        self.qr_frame = tk.Frame(self.root, bg="white")
        self.qr_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        self.status_label = tk.Label(self.root, text="", fg="blue")
        self.status_label.pack(pady=5)

    # ✅ Correct UPI validation
    def validate_upi(self, upi_id):
        pattern = r'^[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,64}$'
        return re.match(pattern, upi_id) is not None

    def generate_qr(self):
        upi_id = self.upi_entry.get().strip()
        app = self.app_var.get()

        if not upi_id:
            messagebox.showerror("Error", "Please enter UPI ID")
            return

        if not self.validate_upi(upi_id):
            messagebox.showerror("Error",
                                 "Invalid UPI ID format\nExample:\nname@oksbi\nmerchant@ybl")
            return

        try:
            upi_url = self.upi_urls[app].format(upi_id=quote(upi_id))

            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(upi_url)
            qr.make(fit=True)

            qr_img = qr.make_image(fill_color="black", back_color="white")

            filename = f"{app.lower().replace(' ', '_')}_upi_qr.png"
            qr_img.save(filename)

            self.display_qr(qr_img, filename, app, upi_id)

            self.status_label.config(text=f"QR saved as {filename}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_qr(self, qr_img, filename, app, upi_id):
        for widget in self.qr_frame.winfo_children():
            widget.destroy()

        display_img = qr_img.resize((250, 250), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(display_img)

        tk.Label(self.qr_frame, text=f"{app} QR Code",
                 font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.qr_frame, text=f"UPI ID: {upi_id}").pack()

        img_label = tk.Label(self.qr_frame, image=photo)
        img_label.image = photo
        img_label.pack(pady=10)

        tk.Label(self.qr_frame, text=f"Saved as {filename}", fg="green").pack()

def main():
    root = tk.Tk()
    app = UPIQRGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
