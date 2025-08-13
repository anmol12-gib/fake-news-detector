# 📰 Fake News Detection Tool

Ever read a headline and thought, *“Wait… is this for real?”*  
This project is here to help you find out in seconds.  

It’s a **React + Flask** app powered by a **pretrained AI model** (via Hugging Face Transformers) that tells you whether a news headline is **Fake** or **Real** — along with a confidence score and even a quick AI-generated summary.

---

## ✨ Features
- ⚡ **Instant results** — no need to train anything, it’s ready to go out of the box.  
- 🧠 **Understands context** — uses a pretrained language model to analyze the headline.  
- 📊 **Confidence score** — so you know how certain the model is.  
- 📝 **AI Summary** — gives you a quick, human-readable explanation of the headline.  
- 📱 Fully responsive — works on both desktop and mobile.

---

## 🖼 Preview

### **Homepage**
![Homepage Screenshot](https://github.com/anmol12-gib/fake-news-detector/blob/f65cc59b27c9ab5bb0836467097b02e60c084889/interface.png)

### **Positive Prediction**
![Prediction Screenshot](https://github.com/anmol12-gib/fake-news-detector/blob/7bad61b206959e560da647967d0e7b2de00952d9/positive_result.png)

### **Negative Prediction**
![Prediction Screenshot](https://github.com/anmol12-gib/fake-news-detector/blob/35560aa1ef4c9bb545a92d7f6fbb57f3561a67f4/negative_result.png)

---

## 🗂 Project Structure
project-root/
│
├── backend/
│ ├── app.py # Flask backend API — handles requests from the frontend and runs the AI model
│ ├── requirements.txt # Python dependencies (Flask, Flask-CORS, transformers, etc.)
│
├── frontend/
│ ├── src/
│ │ ├── App.js # Main React component — handles UI and talks to the backend
│ │ ├── App.css # Styling for the app (fonts, colors, buttons)
│ │ ├── components/ # Reusable UI components
│ │ └── assets/ # Images, icons
│ ├── package.json # Frontend dependencies (React, Axios, etc.)
│ └── public/ # Public assets
│
├── docs/
│ ├── homepage.png # Screenshot of homepage
│ ├── result.png # Screenshot of results
│
└── README.md # This file

