
from datetime import datetime

def log_mood():
    while True:
        mood = input("आज आपका मूड कैसा है? (खुश/उदास/ठीक, 'exit' छोड़ने के लिए): ")
        if mood.lower() == 'exit':
            break
        with open("mood_log.txt", "a") as f:
            f.write(f"{mood} - {datetime.now()}\n")
        print("मूड लॉग हो गया!")
    print("मूड लॉगिंग खत्म!")

print("Welcome to Mental Health App Prototype!")
log_mood()
