import pyotp
import time

def otp():
    totp = pyotp.TOTP('base32secret3232')
    a=totp.now()
    time.sleep(30)
    return a
