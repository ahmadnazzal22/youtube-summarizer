from flask import Flask, render_template, request, jsonify, Response
from transcript import get_transcript
from summarizer import summarize
from dotenv import load_dotenv
import json
import sys
import io


load_dotenv()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize_video():
    data = request.get_json()
    url = data.get("url", "").strip()

    if not url:
        return jsonify({"success": False, "error": "أدخل رابط الفيديو"})

    transcript_result = get_transcript(url)
    if not transcript_result["success"]:
        return jsonify(transcript_result)

    summary_result = summarize(
        text=transcript_result["text"],
        language=transcript_result["language"]
    )

    if not summary_result["success"]:
        return jsonify(summary_result)

    return Response(
        json.dumps({
            "success": True,
            "summary": summary_result["summary"],
            "language": transcript_result["language"],
            "video_id": transcript_result["video_id"]
        }, ensure_ascii=False),
        mimetype="application/json; charset=utf-8"
    )

if __name__ == "__main__":
    app.run(debug=True)