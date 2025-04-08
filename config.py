# config.py
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "osint_db"

EMAIL = {
    "sender": "your.email@gmail.com",
    "password": "your_app_password",
    "recipient": "alert.recipient@gmail.com",
}

KEYWORDS = ["ransomware", "leak", "exploit", "breach", "zeroday", "hack"]
