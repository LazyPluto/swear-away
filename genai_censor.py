from google import genai
from google.genai.types import HarmCategory, HarmBlockThreshold
import env

client = genai.Client(api_key=env.GEMINI_API_KEY)

client = genai.Client(api_key="AIzaSyBZBs70e2NE0hUz2jZDWMG6PjrgRLmp4wc")
harm_categories = [
    HarmCategory.HARM_CATEGORY_HATE_SPEECH,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
    HarmCategory.HARM_CATEGORY_HARASSMENT,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
    HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY,
]
config = {
    'system_instruction': open("censor-prompt.txt").read(),
    'safety_settings': [{ 'category': category, 'threshold': HarmBlockThreshold.OFF } for category in harm_categories]
}

async def censor(message: str) -> str:
	response =  client.models.generate_content(model="gemini-2.0-flash", contents=message, config=config)
	return response.text.strip()
