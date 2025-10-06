                                      🐕 Stray Dog Detection & Adoption Platform

🚀 An AI-powered solution to detect stray dogs, track them, and connect with adoption platforms & NGOs.
This project blends Computer Vision + Web Development to tackle one of society’s most urgent challenges: helping stray animals find safe homes.


✨ Why this Project?

Every day, thousands of stray dogs are left unnoticed and uncared for. This system aims to:

🐾 Detect and count stray dogs in an area.

🏡 Provide an adoption channel for rescued dogs.

🤝 Connect NGOs and volunteers with reports of strays.

A small step with technology → a giant leap for animal welfare. ❤️


⚡ Features

🔍 Real-time Dog Detection using YOLOv8.

📷 Upload images → automatically count dogs.

🐶 Adoption Hub – add dogs with details & images for adoption.

📡 NGO Alerts – notify animal welfare groups instantly.

🌐 Clean Flask Web Interface with simple navigation.


🛠️ Tech Stack

Layer	Technology

👨‍💻 Frontend	HTML, CSS (Flask Templates)
⚙️ Backend	Python, Flask
🧠 AI/ML	YOLOv8 (Ultralytics)
🗄️ Database	SQLite (via SQLAlchemy in models.py)
📦 Environment	Virtualenv, pip


📂 Project Structure

stray_dog_project/

├── app.py              # Main Flask app

├── models.py           # Database models (dogs, users, NGOs)

├── detection/

│   └── detect.py       # YOLOv8 detection logic

├── recommender/

│   └── recommend.py    # Simple recommender for adopters

├── static/

│   ├── css/

│   │   └── styles.css  # Custom styles

│   └── images/         # Uploaded images

├── templates/

│   ├── base.html       # Shared layout

│   ├── index.html      # Home page

│   ├── upload.html     # Detection upload page

│   └── adopt.html      # Adoption listing

├── requirements.txt    # Dependencies

└── README.md           # Documentation


⚙️ Installation & Setup

1️⃣ Clone Repository
git clone https://github.com/your-username/stray_dog_project.git
cd stray_dog_project

2️⃣ Setup Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py
Now open 👉 http://127.0.0.1:5000

🚀 Future Roadmap

📹 Live CCTV feed integration.

📱 Mobile app for adoption + rescue alerts.

🌍 GPS-based stray reporting system.

🤖 Advanced ML recommender for matching adopters.

❤️ Acknowledgements
Built with love for stray animals 🐾.
Let’s use AI for Good ✨.

📜 License
This project is licensed under the MIT License – free to use and improve.

