# OTP Verification System
## Introduction
This project implements an OTP (One-Time Password) verification system using Python. It generates a secure 6-digit OTP and sends it to the user’s email address for authentication. This approach is commonly used to verify users during actions like login, registration, or sensitive transactions, providing an extra layer of security.
## Features
Generates a random 6-digit OTP.
Sends OTP via email using SMTP.
Verifies the OTP entered by the user.
Error handling for incorrect or expired OTP entries.
## Technologies Used
Programming Language: Python
Libraries:
smtplib for sending OTP emails
random and secrets for OTP generation
## Configuration
Before using the OTP system, update the config.py file with your email server settings:
EMAIL_ADDRESS = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'
SMTP_SERVER = 'smtp.example.com'  # e.g., smtp.gmail.com for Gmail
SMTP_PORT = 587                   # Port for TLS
Make sure to enable "less secure app access" or generate an app-specific password if you're using Gmail or other email providers that enforce strict security settings.

## Usage
Running the OTP Verification System
Ensure your config.py is correctly set up.
Run the script:
python otp_verification.py
The script will prompt you to enter the recipient's email address. It will then generate and send a 6-digit OTP to that email.
Enter the received OTP when prompted to verify it.
## Project Structure
OTP-Verification-System/
├── otp_verification.py
├── config.py
├── requirements.txt
├── README.md
└── LICENSE


Contact
If you have any questions, feel free to reach out:
Uday - udayagiriudayvsk106@gmail.com
