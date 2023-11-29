import speech_recognition as sr
#import openai
import pyttsx3
#import env  # Import your OpenAI API key from the env module

# Set your OpenAI API key
#openai.api_key = "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"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("พูดอะไรสักอย่าง...")
        recognizer.adjust_for_ambient_noise(source)  # ปรับตัวให้เหมาะสมกับเสียงรอบข้าง
        audio = recognizer.listen(source, timeout=5)  # ฟังเสียงได้ตลอด 5 วินาที

    try:
        print("กำลังจดจำ...")
        text = recognizer.recognize_google(audio, language="th-TH")  # ใช้ภาษาไทย
        print("คุณพูดว่า:", text)
        return text
    except sr.UnknownValueError:
        print("ขออภัยครับ/ค่ะ ไม่สามารถทำความเข้าใจคำพูดได้")
        return None
    except sr.RequestError as e:
        print(f"เกิดข้อผิดพลาดกับบริการรับรู้เสียง: {e}")
        return None

def openai_query(prompt):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def voice_assistant():
    speak("สวัสดีครับ/ค่ะ! ฉันคือผู้ช่วยเสียงของคุณ มีอะไรให้ฉันช่วยคุณไหมครับ/ค่ะ?")

    while True:
        command = listen()

        if command:
            if "หยุด" in command:
                speak("ลาก่อนครับ/ค่ะ! ขอให้คุณมีวันที่ดี")
                break
            else:
                prompt = f"คุณพูดว่า: {command}"
                response = openai_query(prompt)
                speak(response)

if __name__ == "__main__":
    voice_assistant()
