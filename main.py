from generators.numeric_gen import generate_numeric_random_to_file
from generators.alpha_gen import generate_alpha_random_to_file
from generators.combo_gen import generate_combo_to_file
from generators.smart_gen import generate_smart_passwords

def main():
    print("="*40)
    print("🔐 MegaCrackX Password Generator")
    print("="*40)

    username_or_email = input("👤 Enter username or email: ").strip()
    birth_date = input("📅 Enter birth date (optional) [YYYY-MM-DD or YYYY/MM/DD or YYYYMMDD]: ").strip()
    birth_date = birth_date if birth_date else None

    print("\n[1] 🔢 Generating numeric passwords...")
    generate_numeric_random_to_file(count=5000, min_len=4, max_len=8)

    print("[2] 🔡 Generating alphabetic passwords...")
    generate_alpha_random_to_file(count=5000, min_len=4, max_len=8)

    print("[3] 🔤 Generating combo passwords...")
    generate_combo_to_file(count=5000, min_len=6, max_len=12)

    print("[4] 🧠 Generating smart passwords based on input...")
    generate_smart_passwords(username_or_email, birth_date)

    print("\n✅ All wordlists generated successfully and saved in 'wordlists/output/'")

if __name__ == "__main__":
    main()
