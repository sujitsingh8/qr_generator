"""
qr_generator.py
Generates QR codes for URLs using the qrcode library.
Saves them as PNG images in a local folder.
"""

import qrcode
import os

QR_FOLDER = "qr_codes"


def ensure_folder():
    """Create the qr_codes folder if it doesn't exist."""
    if not os.path.exists(QR_FOLDER):
        os.makedirs(QR_FOLDER)


def generate_qr(url, short_code):
    """
    Generate a QR code image for the given URL.
    Saves it as qr_codes/<short_code>.png
    Returns the file path.
    """
    ensure_folder()

    qr = qrcode.QRCode(
        version=1,           # controls size (1 = smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,         # size of each box in pixels
        border=4,            # border thickness in boxes
    )

    qr.add_data(url)
    qr.make(fit=True)       # auto-adjust version if needed

    img = qr.make_image(fill_color="black", back_color="white")

    file_path = os.path.join(QR_FOLDER, f"{short_code}.png")
    img.save(file_path)

    return file_path


def qr_exists(short_code):
    """Check if a QR code image already exists for this short code."""
    file_path = os.path.join(QR_FOLDER, f"{short_code}.png")
    return os.path.exists(file_path)