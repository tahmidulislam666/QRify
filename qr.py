import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode
from pyzbar.pyzbar import decode

def generate_qr():
    text = entry.get().strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter text or URL.")
        return
    global qr_image
    qr = qrcode.make(text)
    qr = qr.resize((200, 200))
    qr_image = qr
    qr_tk = ImageTk.PhotoImage(qr)
    qr_label.config(image=qr_tk)
    qr_label.image = qr_tk

def save_qr():
    if qr_image is None:
        messagebox.showwarning("No QR", "Please generate a QR code first.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
    if file_path:
        qr_image.save(file_path)
        messagebox.showinfo("Saved", "QR code saved successfully!")

def decode_qr():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
    if file_path:
        try:
            img = Image.open(file_path)
            result = decode(img)
            if result:
                qr_data = result[0].data.decode("utf-8")
                messagebox.showinfo("Decoded QR", f"Content:\n{qr_data}")
            else:
                messagebox.showwarning("No QR Found", "No QR code found in the image.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("QRify - QR Code Generator & Scanner")
root.geometry("400x550")
root.configure(bg="#f8f8ff")

tk.Label(root, text="Enter Text / URL", font=("Arial", 14), bg="#f8f8ff").pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Generate QR Code", command=generate_qr,
          bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

qr_label = tk.Label(root, bg="#f8f8ff")
qr_label.pack(pady=10)

tk.Button(root, text="Save QR Code", command=save_qr,
          bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=10)

tk.Label(root, text="OR", font=("Arial", 12, "italic"), bg="#f8f8ff").pack(pady=5)

tk.Button(root, text="Decode QR from Image", command=decode_qr,
          bg="#FF5722", fg="white", font=("Arial", 12)).pack(pady=10)

qr_image = None
root.mainloop()