def menu():
    while True:
        print()
        print("    Menu  ")
        print("================")
        print("1. Enkripsi ")
        print("2. Dekripsi")
        print("3. Exit")
        print()

        input_menu = int(input("Masukan Menu yang kamu pilih? "))
        if input_menu == 1:
            result_enkripsi = enkripsi()
            print()
            print("Hasil enkripsi: " + result_enkripsi)
            print("Kembali ke Menu Awal.....")
        elif input_menu == 2:
            dekripsi()
            print()
            print("Hasil dekripsinya bisa di lihat di atas")
            print("Kembali ke Menu Awal.....")
        elif input_menu == 3:
            break
        else:
            print("Error: angka yang dimasukkan salah!")


def enkripsi():
    input_text = str(input("Masukan Text yang akan dienkripsi? "))
    key = int(input("Masukan key yang akan dipakai? "))
    result = ""
    for i in range(len(input_text)):
        char = input_text[i]
    #proses enskripsi dalam huruf kecil di abjad plain text

        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        #proses enskripsi dalam huruf kecil di abjad plain text
        elif char == " ":
            result += " "
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result

def dekripsi():
    Alpabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    input_encrypted = str(input("Masukan pesan yang akan dideskripsi?" ))

    for key in range(len(Alpabet1)):
        translated = ""
        for symbol in input_encrypted:
            if symbol in Alpabet1:
                num = Alpabet1.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(Alpabet1)
                translated = translated + Alpabet1[num]
            else:
                translated = translated + symbol

        print('Hacking key #%s: %s' % (key, translated))

def main():
    menu()


if __name__ == '__main__':
    main()