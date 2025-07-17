import random
import string
import os

def generate_combo_to_file(count=10000, min_len=6, max_len=12, filename="combo_random.txt"):
    output_dir = "wordlists/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    with open(f"{output_dir}/{filename}", "w", encoding="utf-8") as f:
        for _ in range(count):
            length = random.randint(min_len, max_len)
            pwd = ''.join(random.choices(chars, k=length))
            f.write(pwd + "\n")
    print(f"[+] Done writing {count} random combo passwords to {output_dir}/{filename}")
