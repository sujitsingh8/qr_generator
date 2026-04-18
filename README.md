# 🔲 QR Code Generator

A terminal-based QR code generator written in Python. Encode any URL or text into a PNG image and manage all your saved QR codes from the command line.

---

## 📸 Demo

```
=============================================
        QR CODE GENERATOR
=============================================

What would you like to do?
1. Generate QR code for a URL
2. Generate QR code for any text
3. View all saved QR codes
4. Exit
---------------------------------------------
Enter your choice (1-4): 1

Enter the URL: https://github.com/your-username
Enter a name for this QR code file: github_profile

QR code saved: qr_codes/github_profile.png
```

---

## ✨ Features

- Generate QR codes for any URL or plain text
- Saves output as PNG images in a local `qr_codes/` folder
- Auto-creates the output folder if it doesn't exist
- Lists all previously saved QR codes
- Sanitises filenames automatically (alphanumeric and underscores only)
- Warns if a URL is missing the `http://` or `https://` prefix

---

## 📁 Project Structure

```
qr-code-generator/
│
├── main.py           # CLI interface — menu, input handling, user flow
├── qr_generator.py   # Core logic — QR generation and file management
│
└── qr_codes/         # Auto-created folder where PNG files are saved
    └── *.png
```

---

## 🚀 Getting Started

**Requirements:** Python 3.7+

**Install the dependency:**

```bash
pip install qrcode[pil]
```

**Run the program:**

```bash
python main.py
```

---

## 🔧 How It Works

`qr_generator.py` uses the `qrcode` library to build each QR image with these settings:

| Parameter | Value | Description |
|---|---|---|
| `version` | 1 | Starting grid size (auto-adjusts if data is too large) |
| `error_correction` | L | ~7% damage tolerance |
| `box_size` | 10 px | Size of each individual module |
| `border` | 4 boxes | Quiet zone around the code |

The generated image is saved as `qr_codes/<filename>.png` with black modules on a white background.
