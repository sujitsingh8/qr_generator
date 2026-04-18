"""
main.py
QR Code Generator
Terminal-based project using Python concepts from IITM BS lectures.
"""

import qr_generator
import os


def print_banner():
    print("=" * 45)
    print("        QR CODE GENERATOR")
    print("=" * 45)


def print_menu():
    print("\nWhat would you like to do?")
    print("1. Generate QR code for a URL")
    print("2. Generate QR code for any text")
    print("3. View all saved QR codes")
    print("4. Exit")
    print("-" * 45)


def get_filename(prompt="Enter a filename (no extension): "):
    name = input(prompt).strip()
    name = "".join(c for c in name if c.isalnum() or c == "_")
    if not name:
        name = "qr_code"
    return name


def handle_url_qr():
    url = input("Enter the URL: ").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Warning: URL should start with http:// or https://")
        confirm = input("Continue anyway? (y/n): ").strip().lower()
        if confirm != "y":
            return

    filename = get_filename("Enter a name for this QR code file: ")
    path = qr_generator.generate_qr(url, filename)
    print(f"\nQR code saved: {path}")


def handle_text_qr():
    text = input("Enter the text to encode: ").strip()
    if not text:
        print("Text cannot be empty.")
        return

    filename = get_filename("Enter a name for this QR code file: ")
    path = qr_generator.generate_qr(text, filename)
    print(f"\nQR code saved: {path}")


def handle_view_all():
    folder = qr_generator.QR_FOLDER
    if not os.path.exists(folder):
        print("\nNo QR codes generated yet.")
        return

    files = [f for f in os.listdir(folder) if f.endswith(".png")]
    if not files:
        print("\nNo QR codes found.")
        return

    print(f"\nSaved QR codes in '{folder}/':")
    for i, f in enumerate(files, 1):
        print(f"  {i}. {f}")


def main():
    print_banner()

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            handle_url_qr()
        elif choice == "2":
            handle_text_qr()
        elif choice == "3":
            handle_view_all()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Enter a number between 1 and 4.")


if __name__ == "__main__":
    main()