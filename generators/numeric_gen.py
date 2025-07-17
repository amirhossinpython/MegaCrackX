import random
import os

def generate_numeric_random_to_file(count=10000, min_len=4, max_len=8, filename="numeric_random.txt"):
    output_dir = "wordlists/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(f"{output_dir}/{filename}", "w", encoding="utf-8") as f:
        for _ in range(count):
            length = random.randint(min_len, max_len)
            num = ''.join(random.choices('0123456789', k=length))
            f.write(num + "\n")
    print(f"[+] Done writing {count} random numeric passwords to {output_dir}/{filename}")
