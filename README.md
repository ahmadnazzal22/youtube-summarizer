# 🎬 YouTube Summarizer

AI-powered YouTube video summarizer using Groq (LLaMA 3.3 70B).
Paste any YouTube link and get a structured summary in seconds.

## Features
- 📝 Full summary + key points + quotes
- 🌍 Supports Arabic & English videos
- 🌙 Dark UI with smooth animations
- ⚡ Powered by Groq API (ultra-fast)

## Setup

1. Clone the repo
   git clone https://github.com/yourusername/youtube-summarizer

2. Install dependencies
   pip install -r requirements.txt

3. Add your API key
   cp .env.example .env
   # then edit .env and add your GROQ_API_KEY

4. Run
   python app.py

## Stack
- Python + Flask
- Groq API (llama-3.3-70b-versatile)
- youtube-transcript-api
- Vanilla JS + CSS Dark UI