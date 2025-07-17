def save_to_file(filename, passwords):
    with open(f"wordlists/output/{filename}.txt", "w", encoding="utf-8") as f:
        for pwd in passwords:
            f.write(pwd + "\n")
    print(f"[+] Saved {len(passwords)} passwords to {filename}.txt")
