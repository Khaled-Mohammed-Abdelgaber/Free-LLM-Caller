import google.generativeai as genai
from google.generativeai.types import GenerationConfig
from config import Settings
from groq import Groq
import requests
import json
from openai import OpenAI
import openai
#===================================================================================
settings = Settings()
temp = float(settings.TEMPR)
#===================================================================================
def read_text_file(file_path):
    """
    READS AND RETURNS THE CONTENT OF A TEXT FILE.
    
    Parameters:
    - file_path (str): Path to the text file
    
    Returns:
    - str: Content of the file as a string
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError as e:
        print(f"IO error occurred: {e}")
#===================================================================================
system_prompt = read_text_file("system_prompt.txt")
#===================================================================================
gemini_key = settings.GEMINI_API_KEY
gemini_model = settings.GEMINI_MODEL

def get_gemini_response(user_prompt: str, 
                        system_prompt=system_prompt,
                        api_key = gemini_key,
                        model_name= gemini_model):
    """
    Interacts with the Gemini API to generate a response.

    Args:
        api_key (str): Your Google Cloud API key.
        model_name (str): The name of the Gemini model to use (e.g., "gemini-pro").
        system_prompt (str): The system-level instructions or context for the model.
        user_prompt (str): The user's input or question.

    Returns:
        str or None: The generated response text if successful, None otherwise.
    """
    try:
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_prompt
        )

        # Create a GenerationConfig object with the temperature parameter
        generation_config = GenerationConfig(temperature=temp)

        # Pass the generation_config to the generate_content method
        response = model.generate_content(
            user_prompt,
            generation_config=generation_config
        )

        return response.text

    except Exception as e:
        print(f"Google API Error: {e}")
        return None
#===================================================================================
groq_key = settings.GROQ_API_KEY
groq_model = settings.GROQ_MODEL

def get_groq_response(user_prompt, groq_key = groq_key, model_name = groq_model, 
                      system_prompt=system_prompt):
    # Instantiation of Groq Client
    client = Groq(
        api_key=groq_key,
        )
    try:
        llm = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
            model=model_name,
            temperature=temp,
        )
        return llm.choices[0].message.content
        
    except Exception as e:
        print("ERRR")
        print("groq error : ",str(e).encode('utf-8', errors='replace').decode('utf-8'))
        return None
#===================================================================================

openrouter_model = settings.OPENROUTER_MODEL_NAME
openrouter_key = settings.OPENROUTER_API_KEY

def get_openrouter_response(user_prompt, openrouter_key = openrouter_key, 
                            model_name = openrouter_model, system_prompt=system_prompt):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {openrouter_key}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": model_name,
                "messages": [
                {"role": "system", 
                 "content": system_prompt},
                {"role": "user", "content": user_prompt}
                        ],
            "temperature": temp
            })
        )

        response.raise_for_status()
        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("openrouter error: " ,e)
        return None

#===================================================================================
mistral_model= settings.MISTRAL_MODEL
mistral_key= settings.MISTRAL_KEY

def get_mistral_response(user_prompt, mistral_key = mistral_key, 
                            mistral_model = mistral_model, system_prompt=system_prompt):
    try:
        API_URL = "https://api.mistral.ai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {mistral_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": mistral_model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": temp,
            "stream": False
        }

        response = requests.post(API_URL, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(e)
        return None
#===================================================================================
openai_key = settings.OPENAI_KEY
openai_model = settings.OPENAI_MODEL

def get_openai_response(user_prompt, openai_key = openai_key, 
                            openai_model = openai_model, system_prompt=system_prompt):
    try:
        endpoint = "https://models.inference.ai.azure.com" 

        client = OpenAI(
            base_url=endpoint,
            api_key=openai_key,
        )

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "developer",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
            model=openai_model,
            temperature=temp
        )

        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return None
    
#==========================================================================================

fireworks_key = settings.FIREWORKS_API_KEY
fireworks_model = settings.FIREWORKS_MODEL

def get_fireworks_response(user_prompt,
                          fireworks_key=fireworks_key,
                          fireworks_model=fireworks_model,
                          system_prompt=system_prompt):
    try:
        client = OpenAI(
            base_url="https://api.fireworks.ai/inference/v1",  # Clean URL
            api_key=fireworks_key,
        )

        stream = client.chat.completions.create(
            model=fireworks_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.0,
            max_tokens=128000,
            stream=True  # 🔥 Required for long outputs
        )

        full_response = ""
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                full_response += content

        return full_response.strip()

    except Exception as e:
        print("Fireworks error:", e)

        return None
