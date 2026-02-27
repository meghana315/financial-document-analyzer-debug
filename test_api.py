from dotenv import load_dotenv
import os
load_dotenv()
from litellm import completion

models = [
    "gemini/gemini-2.0-flash-lite",
    "gemini/gemini-2.5-flash",
    "gemini/gemini-flash-latest",
]

for model in models:
    try:
        response = completion(
            model=model,
            api_key=os.getenv("GOOGLE_API_KEY"),
            messages=[{"role": "user", "content": "Say hello in one word"}]
        )
        print(f"SUCCESS with {model}:", response.choices[0].message.content)
        break
    except Exception as e:
        print(f"FAILED {model}:", str(e)[:100])