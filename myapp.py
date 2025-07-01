
from datetime import datetime

def log_mood():
    while True:
        mood = input("आज आपका मूड कैसा है? (खुश/उदास/ठीक, 'exit' छोड़ने के लिए): ")
        if mood.lower() == 'exit':  # सिर्फ "exit" चेक करेगा
            break
        elif mood.lower() not in ['खुश', 'उदास', 'ठीक']:  # वैलिडेशन जोड़ें
            print("कृपया 'खुश', 'उदास', या 'ठीक' चुनें!")
            continue
        with open("mood_log.txt", "a") as f:
            f.write(f"{mood} - {datetime.now()}\n")
        print("मूड लॉग हो गया!")
    print("मूड लॉगिंग खत्म!")

print("Welcome to Mental Health App Prototype!")
log_mood()
