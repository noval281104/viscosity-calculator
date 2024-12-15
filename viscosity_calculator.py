import tkinter as tk
from tkinter import messagebox

def calculate_viscosity():
    try:
        temperature = float(entry_temperature.get())
        
        if temperature < 0 or temperature > 100:
            messagebox.showerror("Error", "Silakan masukkan suhu antara 0°C dan 100°C.")
            return

        # Menghitung viskositas dinamis (dalam cP) berdasarkan suhu
        if temperature <= 20:
            dynamic_viscosity = 1.002 - 0.0014 * temperature  # Contoh rumus
        else:
            dynamic_viscosity = 0.00179 * temperature**2 - 0.034 * temperature + 1.002  # Contoh rumus

        # Menghitung kinematik viskositas (dalam cSt)
        density = 0.9982 - 0.0001 * temperature  # Kerapatan air dalam g/cm³
        kinematic_viscosity = dynamic_viscosity / density  # cSt

        result_text = f"Viskositas Dinamis: {dynamic_viscosity:.3f} cP\n"
        result_text += f"Viskositas Kinematik: {kinematic_viscosity:.3f} cSt"
        label_result.config(text=result_text)

    except ValueError:
        messagebox.showerror("Error", "Silakan masukkan nilai suhu yang valid.")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Viskositas Air")

# Mengatur ukuran jendela (lebar x tinggi)
root.geometry("400x300")  # Ukuran jendela lebih besar

# Membuat elemen GUI
label_temperature = tk.Label(root, text="Masukkan Suhu (°C):")
label_temperature.pack(pady=10)  # Menambahkan padding vertikal

entry_temperature = tk.Entry(root)
entry_temperature.pack(pady=10)  # Menambahkan padding vertikal

button_calculate = tk.Button(root, text="Hitung Viskositas", command=calculate_viscosity)
button_calculate.pack(pady=10)  # Menambahkan padding vertikal

label_result = tk.Label(root, text="")
label_result.pack(pady=10)  # Menambahkan padding vertikal

# Menjalankan aplikasi
root.mainloop()