from Veritabani import *

def print_menu():
    print("""
    1-Giriş Yap
    2-Kaydol
    3-Kapat
    """)


def login(user):
    print(f"""
    {user[1]} {user[2]} {user[3]} 
    
    1-Bir kullanıcı arama
    2-Tüm hesapları yazdır
    3-Hesabımı sil 
    4-Çıkış yap  """)

creat_table()

while True:
    print_menu()
    secim = input("Seçiminiz : ")

    if secim == "1":
        username = input("Username : ")
        password = input("Password : ")
        search = search(username)

    if secim == None:
        print("Böyle bir kullanıcı yok")
        continue

    if password == search[4]:
        while True:
            login(search)
            secim = input("Seçim :")
            if secim == "1":
                u = input("Kullanıcı adı :")
                birisi = search(u)
                if birisi == None:
                    print("KUllanıcı bulunamadı")
                    continue
                print(f"{birisi[1]} {birisi[2]} {birisi[3]}")

    if secim == "2":
        name = input("İsim giriniz : ")
        lastname = input("Soyad giriniz : ")
        username = input("Kullanıcı adı giriniz : ")
        password = input("Şifrenizi giriniz")

        search = search(username)
        if search != None:
            print("BU KULLANICI ADI KULLANILIYOR! ")
            continue
        insert(name, lastname, username, password)
        print("Kayıt işlemi başarılı")

    if secim == "3":
        break