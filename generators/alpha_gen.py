import random
import string
import os

def generate_alpha_random_to_file(count=10000, min_len=4, max_len=8, filename="alpha_random.txt"):
    output_dir = "wordlists/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    chars = string.ascii_lowercase
    with open(f"{output_dir}/{filename}", "w", encoding="utf-8") as f:
        for _ in range(count):
            length = random.randint(min_len, max_len)
            pwd = ''.join(random.choices(chars, k=length))
            f.write(pwd + "\n")
    print(f"[+] Done writing {count} random alphabetic passwords to {output_dir}/{filename}")
