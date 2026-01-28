from google from genai
from dotenv import load_dotenv
import os
load_dotenv()

# Custom Settings
max_words=20 #Sets the max words for the reponse
model="gemini-3-flash-preview" #Sets the Gemini model
api_key = os.getenv("GEMINI_API_KEY")

def ask(prompt=input('Enter prompt: \n')):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model, 
        contents=f'Answer this prompt {prompt}, in the max words of {max_words}.' 
    )

    print(response.text)
    
