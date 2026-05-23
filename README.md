# 🎬 YouTube Video Summarizer AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**⚡ Paste a YouTube link. Get a full AI summary in seconds.**

</div>

---

## 🧠 What It Does

Drop any YouTube URL and get back:

- 📄 Full structured summary
- 🎯 Key points & takeaways  
- 💬 Notable quotes
- 🌐 Arabic translation (even for English videos)

Powered by **Groq API** + **LLaMA 3.3 70B** — blazing fast.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| AI Model | LLaMA 3.3 70B via Groq |
| Transcript | youtube-transcript-api |
| Frontend | HTML + CSS + Vanilla JS |
| Theme | Dark UI with 3D effects |

---

## ⚙️ Setup

```bash
# 1. Clone
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer

# 2. Install
pip install -r requirements.txt

# 3. Add your API key
echo "GROQ_API_KEY=your_key_here" > .env

# 4. Run
python app.py


Open http://localhost:5000 🚀

📂 Structure

youtube-summarizer/
├── app.py           # Flask server
├── summarizer.py    # Groq AI logic
├── transcript.py    # YouTube transcript extraction
├── templates/
│   └── index.html   # Dark UI frontend
├── .env
├── .gitignore
└── requirements.txt


🌍 Supports

	•	✅ Arabic & English videos
	•	✅ Standard YouTube URLs
	•	✅ Shortened URLs (youtu.be)
	•	✅ YouTube Shorts

👨‍💻 Built by Ahmad

Part of my AI development journey — building one project per week using Python + Groq.Check out my other projects on GitHub ⭐

If this helped you, drop a star — it means a lot ⭐


---

**استبدل `your-username` باسمك على GitHub وارفعه** 🚀
