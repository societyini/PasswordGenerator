import random
import string
import configparser
import os
import time

# =========================
# COLORES
# =========================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# =========================
# BANNER
# =========================
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Colors.CYAN}{Colors.BOLD}
   ██████╗  █████╗ ███████╗███████╗
   ██╔══██╗██╔══██╗██╔════╝██╔════╝
   ██████╔╝███████║███████╗███████╗
   ██╔═══╝ ██╔══██║╚════██║╚════██║
   ██║     ██║  ██║███████║███████║
   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝

            SOCIETY.INI
        Password Generator Tool
        discord.gg/7ZHueg8gWZ
{Colors.RESET}""")

# =========================
# CONFIG
# =========================
def load_config():
    config = configparser.ConfigParser()

    defaults = {
        "length": 12,
        "use_uppercase": True,
        "use_lowercase": True,
        "use_digits": True,
        "use_symbols": True,
        "save_to_file": False,
        "output_file": "passwords.txt"
    }

    if os.path.exists("society.ini"):
        config.read("society.ini")
        settings = config["SETTINGS"]
        return {
            "length": int(settings.get("length", defaults["length"])),
            "use_uppercase": settings.getboolean("use_uppercase", defaults["use_uppercase"]),
            "use_lowercase": settings.getboolean("use_lowercase", defaults["use_lowercase"]),
            "use_digits": settings.getboolean("use_digits", defaults["use_digits"]),
            "use_symbols": settings.getboolean("use_symbols", defaults["use_symbols"]),
            "save_to_file": settings.getboolean("save_to_file", defaults["save_to_file"]),
            "output_file": settings.get("output_file", defaults["output_file"])
        }
    return defaults

# =========================
# GENERADOR
# =========================
def generate_password(length, cfg):
    chars = ""
    if cfg["use_uppercase"]:
        chars += string.ascii_uppercase
    if cfg["use_lowercase"]:
        chars += string.ascii_lowercase
    if cfg["use_digits"]:
        chars += string.digits
    if cfg["use_symbols"]:
        chars += "!@#$%^&*()-_=+[]{};:,.<>?"

    if not chars:
        raise ValueError("No hay caracteres habilitados")

    return ''.join(random.choice(chars) for _ in range(length))

# =========================
# MAIN
# =========================
def main():
    while True:
        banner()
        config = load_config()

        while True:
            user_input = input(
                f"{Colors.YELLOW}¿Cuántas contraseñas quieres generar? (1–100): {Colors.RESET}"
            )

            if not user_input.isdigit():
                print(f"{Colors.RED}Debes introducir un número.{Colors.RESET}")
                time.sleep(1.5)
                continue

            amount = int(user_input)

            if amount == 0:
                print(f"{Colors.RED}No se puede generar 0 contraseñas.{Colors.RESET}")
                time.sleep(1.5)
                continue

            if amount > 100:
                print(f"{Colors.RED}El máximo permitido es 100.{Colors.RESET}")
                time.sleep(1.5)
                continue

            break

        print(f"\n{Colors.GREEN}Generando contraseñas...\n{Colors.RESET}")
        time.sleep(0.5)

        passwords = []
        for _ in range(amount):
            pwd = generate_password(config["length"], config)
            passwords.append(pwd)
            print(f"{Colors.CYAN}{pwd}{Colors.RESET}")
            time.sleep(0.03)

        if config["save_to_file"]:
            with open(config["output_file"], "w", encoding="utf-8") as f:
                for p in passwords:
                    f.write(p + "\n")

            print(f"\n{Colors.GREEN}Guardadas en {config['output_file']}{Colors.RESET}")

        choice = input(
            f"\n{Colors.YELLOW}¿Quieres generar más contraseñas? (s/n): {Colors.RESET}"
        ).lower()

        if choice != "s":
            print(f"\n{Colors.BOLD}Proceso finalizado.{Colors.RESET}")
            break

# =========================
# START
# =========================
if __name__ == "__main__":
    main()