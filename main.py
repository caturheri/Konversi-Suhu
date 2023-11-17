def kelvin_to_celsius(kelvin):
    """
    Konversi suhu dari Kelvin ke Celsius.

    Parameters:
    kelvin (float): Suhu dalam Kelvin.

    Returns:
    float: Suhu dalam Celsius.
    """
    celsius = kelvin - 273.15
    return celsius

def celsius_to_kelvin(celsius):
    """
    Konversi suhu dari Celsius ke Kelvin.

    Parameters:
    celsius (float): Suhu dalam Celsius.

    Returns:
    float: Suhu dalam Kelvin.
    """
    kelvin = celsius + 273.15
    return kelvin

def convert_to_fahrenheit(suhu, scale):
    """
    Konversi suhu dari Celsius atau Kelvin ke Fahrenheit.

    Parameters:
    suhu (float): Suhu dalam Celsius atau Kelvin.
    scale (str): Skala suhu, 'C' untuk Celsius, 'K' untuk Kelvin.

    Returns:
    float: Suhu dalam Fahrenheit.
    """
    if scale == 'C':
        # Konversi dari Celsius ke Fahrenheit
        fahrenheit = (suhu * 9/5) + 32
    elif scale == 'K':
        # Panggil fungsi untuk konversi Kelvin ke Celsius
        celsius = kelvin_to_celsius(suhu)
        # Konversi dari Celsius ke Fahrenheit
        fahrenheit = (celsius * 9/5) + 32
    else:
        raise ValueError("Skala suhu tidak valid. Gunakan 'C' atau 'K'.")

    return fahrenheit

def convert_fahrenheit(suhu, output_scale):
    """
    Konversi suhu dari Fahrenheit ke Celsius atau Kelvin.

    Parameters:
    suhu (float): Suhu dalam Fahrenheit.
    output_scale (str): Skala keluaran, 'C' untuk Celsius, 'K' untuk Kelvin.

    Returns:
    float: Suhu dalam Celsius atau Kelvin.
    """
    # Konversi dari Fahrenheit ke Celsius
    celsius = (suhu - 32) * 5/9

    if output_scale == 'C':
        return celsius
    elif output_scale == 'K':
        # Panggil fungsi untuk konversi Celsius ke Kelvin
        kelvin = celsius_to_kelvin(celsius)
        return kelvin
    else:
        raise ValueError("Skala suhu keluaran tidak valid. Gunakan 'C' atau 'K.'")

# Judul Konversi dari Kelvin ke Celsius
print("\nKonversi dari Kelvin ke Celsius")
print("===============================")

# Penggunaan input() untuk menerima nilai dari pengguna
suhu_input = float(input("Masukkan nilai suhu (Kelvin): "))
suhu_celsius = kelvin_to_celsius(suhu_input)
print(f"{suhu_input} Kelvin sama dengan {suhu_celsius:.2f} Celsius")

# Penutup Konversi dari Kelvin ke Celsius
print("===============================\n")

# Judul Konversi dari Celsius ke Kelvin
print("Konversi dari Celsius ke Kelvin")
print("===============================")

# Penggunaan input() untuk menerima nilai dari pengguna
suhu_input = float(input("Masukkan nilai suhu (Celsius): "))
suhu_kelvin = celsius_to_kelvin(suhu_input)
print(f"{suhu_input} Celsius sama dengan {suhu_kelvin:.2f} Kelvin")

# Penutup Konversi dari Celsius ke Kelvin
print("===============================\n")

# Judul Konversi dari Celsius atau Kelvin ke Fahrenheit
print("Konversi dari Celsius atau Kelvin ke Fahrenheit")
print("==============================================")

# Penggunaan input() untuk menerima nilai dari pengguna
suhu_input = float(input("Masukkan nilai suhu: "))
scale_input = input("Masukkan skala suhu (C untuk Celsius, K untuk Kelvin): ")

suhu_fahrenheit = convert_to_fahrenheit(suhu_input, scale_input.upper())
print(f"{suhu_input} {scale_input.upper()} sama dengan {suhu_fahrenheit:.2f} Fahrenheit")

# Penutup Konversi dari Celsius atau Kelvin ke Fahrenheit
print("==============================================\n")

# Judul Konversi dari Fahrenheit ke Celsius atau Kelvin
print("Konversi dari Fahrenheit ke Celsius atau Kelvin")
print("==============================================")

# Penggunaan input() untuk menerima nilai dari pengguna
suhu_input = float(input("Masukkan nilai suhu (Fahrenheit): "))
output_scale_input = input("Masukkan skala keluaran (C untuk Celsius, K untuk Kelvin): ")

suhu_output = convert_fahrenheit(suhu_input, output_scale_input.upper())
print(f"{suhu_input} Fahrenheit sama dengan {suhu_output:.2f} {output_scale_input.upper()}")

# Penutup Konversi dari Fahrenheit ke Celsius atau Kelvin
print("==============================================")
