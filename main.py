"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
"""

def ekstraksi_data():
    """
    Tanggal: 25 Juli 2023
    Waktu: 07:25:12 WIB
    Magnitudo: 6.0
    Kedalaman: 75 km
    Lokasi: 9.26 LS - 123.95 BT
    Pusat gempa:  berada dilaut 74 km BaratLaut TimorTengah Utara
    Dirasakan: (Skala MMI): II-III Alor, II-III Maumere, III Lembata, II-III Larantuka, II-III Waingapu ,
    II Kupang, II Ende, II-III Kefa, II-III Soe, II Atambua
    :return:
    """
    hasil = dict()
    hasil["tanggal"] = "25 Juli 2023"
    hasil["waktu"] = "07:25:12 WIB"
    hasil["kedalaman"] = "75 Km"
    hasil["lokasi"] = {"LS": 9.26, "BT": 123.95}
    hasil["pusat"] = "berada dilaut 74 km BaratLaut TimorTengah Utara"
    hasil[
        "dirasakan"
    ] = "(Skala MMI): II-III Alor, II-III Maumere, III Lembata, II-III Larantuka, II-III Waingapu"
    print(hasil)
    return hasil


def tampilkan_data():
    print("Gempa Terakhir Yang Terjadi Menurut Laporan BMKG")
    print(f"Tanngal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi LS={result['lokasi']['LS']}, BT={result['lokasi']['BT']}")


if __name__ == "__main__":
    print("Aplikasi Utama")
    result = ekstraksi_data()
    tampilkan_data()
