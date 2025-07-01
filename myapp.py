

from datetime import datetime

def log_mood():
    mood = input("आज आपका मूड कैसा है? (खुश/उदास/ठीक):")
    with open("mood_log.txt", "a") as f:
        f.write(f"{mood} - {datetime.now()}\n")
    print("मूड लॉग हो गया!")

print("Welcome to Mental Health App Prototype!")
log_mood()
