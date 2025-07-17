import os

def generate_smart_passwords(username_or_email, birth_date=None, filename="smart_advanced.txt"):
    """
    username_or_email: رشته نام کاربری یا ایمیل
    birth_date: رشته تاریخ تولد به فرمت 'YYYY-MM-DD' یا 'YYYY/MM/DD' یا None
    """

    output_dir = "wordlists/output"
    os.makedirs(output_dir, exist_ok=True)

    base = username_or_email.split('@')[0] if '@' in username_or_email else username_or_email
    base_caps = base.capitalize()
    base_rev = base[::-1]

    passwords = set()

    # پسوردهای پایه
    base_variants = [
        base, base_caps, base_rev,
        base + "123", base + "2025", base + "!", base + "@123",
        "!" + base, base_caps + "2025", base + "#"
    ]
    passwords.update(base_variants)

    # پسوردهای با اعداد محبوب
    popular_nums = ["1234", "4321", "1111", "0000", "1122", "1212", "7777"]
    for num in popular_nums:
        passwords.add(base + num)
        passwords.add(num + base)
        passwords.add(base_rev + num)

    # اگر تاریخ تولد وارد شده باشه
    if birth_date:
        clean_date = birth_date.replace("-", "").replace("/", "").replace(".", "").strip()
        if len(clean_date) >= 6:  # بررسی صحت
            yyyy = clean_date[0:4]
            yy = clean_date[2:4]
            mm = clean_date[4:6]
            dd = clean_date[6:8] if len(clean_date) >= 8 else ""

            date_parts = [yyyy, yy, mm, dd]

            for part in date_parts:
                if part:
                    passwords.update([
                        base + part, part + base,
                        base_caps + part, part + base_rev,
                        base + "_" + part, part + "_" + base
                    ])

            # فرمت‌های خاص تاریخ
            combos = [
                yyyy + mm + dd, dd + mm + yyyy,
                mm + dd + yyyy, yyyy + dd + mm,
                yy + mm + dd, dd + mm + yy,
                mm + dd + yy, clean_date[::-1]
            ]
            passwords.update(combos)

    # افزودن کاراکترهای خاص برای سخت‌تر شدن
    specials = ['!', '@', '#', '$', '%', '&', '*']
    extended = set()
    for pwd in passwords:
        for s in specials:
            extended.update([
                pwd + s, s + pwd,
                pwd + s + "123",
                s + pwd + "2025"
            ])
    passwords.update(extended)

    # ذخیره در فایل
    with open(f"{output_dir}/{filename}", "w", encoding="utf-8") as f:
        for pwd in sorted(passwords):
            f.write(pwd + "\n")

    print(f"[+] {len(passwords)} smart passwords generated and saved to {output_dir}/{filename}")
