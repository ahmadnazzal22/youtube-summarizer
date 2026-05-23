from youtube_transcript_api import YouTubeTranscriptApi
import re
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv() # تفعيل القراءة هنا أيضاً للاحتياط

# السطر رقم 9 الذي كان يسبب المشكلة:
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
def extract_video_id(url: str) -> str | None:
    patterns = [
        r"v=([a-zA-Z0-9_-]{11})",
        r"youtu\.be/([a-zA-Z0-9_-]{11})",
        r"embed/([a-zA-Z0-9_-]{11})"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_transcript(url: str) -> dict:
    video_id = extract_video_id(url)
    if not video_id:
        return {"success": False, "error": "الرابط غير صحيح"}

    try:
        ytt = YouTubeTranscriptApi()

        # نجرب عربي أول، ثم إنجليزي، ثم أي لغة
        try:
            entries = ytt.fetch(video_id, languages=['ar'])
            language = "arabic"
        except:
            try:
                entries = ytt.fetch(video_id, languages=['en'])
                language = "english"
            except:
                entries = ytt.fetch(video_id)
                language = "unknown"

        full_text = " ".join([entry.text for entry in entries])

        return {
            "success": True,
            "text": full_text,
            "language": language,
            "video_id": video_id
        }

    except Exception as e:
        return {"success": False, "error": f"خطأ في جلب النص: {str(e)}"}