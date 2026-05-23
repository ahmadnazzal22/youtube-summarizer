# summarizer.py
# مسؤول عن التلخيص باستخدام Groq

from groq import Groq
import os

os.environ["PYTHONIOENCODING"] = "utf-8"

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
def summarize(text: str, language: str) -> dict:
    """
    يرسل النص لـ Groq ويرجع ملخص منظم
    """

    # نقطع النص لو كان طويل جداً (Groq عنده حد للتوكنز)
    max_chars = 12000
    if len(text) > max_chars:
        text = text[:max_chars] + "..."

    prompt = f"""
أنت مساعد ذكي متخصص في تلخيص محتوى الفيديوهات.

النص التالي مأخوذ من فيديو YouTube، لغته: {language}

النص:
{text}

المطلوب منك:
1. **ملخص عام** (5-7 جمل تغطي كامل الفيديو)
2. **النقاط الرئيسية** (5-8 نقاط مرقمة)
3. **أبرز الاقتباسات** (2-3 جمل مهمة من النص الأصلي)
4. **ملخص بالعربي** (حتى لو الفيديو بالإنجليزي، اشرح بالعربي)

استخدم تنسيق واضح مع العناوين.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=1500
        )
        result = response.choices[0].message.content
        return {"success": True, "summary": result}

    except Exception as e:
        return {"success": False, "error": f"خطأ في التلخيص: {str(e)}"}