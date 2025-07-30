#no 1
def convert_temperature(value, unit):
    if unit.uper() == 'C':
        return (value * 9/5) + 32
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    else:
        raise ValueError("Unit harus 'C' atau 'f'")
    
print("======= KONVERSI SUHU =======")
try:
    input_suhu = float(input( "Masukkan nilai suhu:" ))
    unit = input (" Masukkan satuan suhu ('C' untuk Celcius atau 'F' untuk Fahrenheit ): ")
    konversi = convert_temperature(input_suhu, unit)
    if unit.upper() == 'C':
        print(f"{input_suhu}°C = {konversi:.2f}°F")
    elif unit.upper() == 'F':
        print(f"{input_suhu}°F = {konversi:.2f}°C")
except ValueError as e:
    print(f"Terjadi Kesalaha:", e)

#no 2
luas_lingkaran = Lambda jejari: 3.14159 * jejari **2

print("\n====== Hitung Luas Lingkaran======")
try:
    jejari = float(input("Masukkan jari-jari lingkaran: "))
    result = luas_lingkaran(jejari)
    print(f"Luas lingkaran dengan jari-jari {jejari} adalah {result:.2f}")
except ValueError as e:
     print("input harus berupa angka")
