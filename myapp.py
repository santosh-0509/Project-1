
from datetime import datetime

def show_mood_history():
    try:
        with open("mood_log.txt", "r") as f:
            history = f.readlines()
            if not history:
                print("कोई मूड हिस्ट्री नहीं मिली!")
            else:
                print("\nमूड हिस्ट्री:")
                for entry in history:
                    print(entry.strip())
    except FileNotFoundError:
        print("मूड लॉग फाइल नहीं मिली!")

def log_mood():
    while True:
        mood = input("आज आपका मूड कैसा है? (खुश/उदास/ठीक, 'exit' छोड़ने के लिए, 'history' हिस्ट्री देखने के लिए): ")
        if mood.lower() == 'exit':
            break
        elif mood.lower() == 'history':
            show_mood_history()
            continue
        elif mood.lower() not in ['खुश', 'उदास', 'ठीक']:
            print("कृपया 'खुश', 'उदास', या 'ठीक' चुनें!")
            continue
        with open("mood_log.txt", "a") as f:
            f.write(f"{mood} - {datetime.now()}\n")
        print("मूड लॉग हो गया!")
    print("मूड लॉगिंग खत्म!")

print("Welcome to Mental Health App Prototype!")
log_mood()
