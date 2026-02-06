# Gemini tool calling with history 
### Uses a sample function
import yaml
import gradio as gr
import json
import os
from google import genai
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))

env_path = os.path.join(root_dir, ".env")

# DEBUG-PRINTS 
print(f"--- DEBUG INFO ---")
print(f"Skript-Folder: {current_dir}")
print(f"Searching .env in: {env_path}")

if os.path.exists(env_path):
    print("DATA-CHECK: .env found!")
    load_dotenv(dotenv_path=env_path)
else:
    print("DATA-CHECK: .env NOT found. Check folder.")
    load_dotenv()

# --- LOADING API KEY ---
google_api_key = os.getenv("GOOGLE_API_KEY")

# DEBUG-PRINTS 
if google_api_key:
    print(f"KEY-CHECK: Key found! (Ending on ...{google_api_key[-4:]})")
    client = genai.Client(api_key=google_api_key)
else:
    print("KEY-CHECK: ERROR! Variable is empty.")

print(f"------------------")


with open('character_config.yaml', 'r') as f:
    char_config = yaml.safe_load(f)


client = genai.Client(api_key=google_api_key)

# Constants
HISTORY_FILE = char_config['history_file']
MODEL = char_config['model']
SYSTEM_PROMPT =  [
        {
            "role": "system",
            "content": [
                {
                    "type": "input_text",
                    "text": char_config['presets']['default']['system_prompt']  
                }
            ]
        }
    ]

# Load/save chat history
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return SYSTEM_PROMPT

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

#============================
# THIS IS THE IMPORTANT PART
#           vvvv
#============================

def get_riko_response_no_tool(messages):
    system_instruction_text = ""
    chat_history = []

    for m in messages:
        if m["role"] == "system":
            system_instruction_text = m["content"][0]["text"]
        else:
            chat_history.append(m)

    formatted_contents = []
    for m in chat_history:
        role = "model" if m["role"] == "assistant" else "user"
        
        text_parts = [p["text"] for p in m["content"] if "text" in p]
        formatted_contents.append({
            "role": role,
            "parts": [{"text": t} for t in text_parts]
        })

    response = client.models.generate_content(
        model=MODEL,
        contents=formatted_contents, 
        config={
            "system_instruction": system_instruction_text, 
            "temperature": 1,
            "top_p": 1,
            "max_output_tokens": 2048,
        }
    )

    return response


def llm_response(user_input):

    messages = load_history()

    # Append user message to memory
    messages.append({
        "role": "user",
        "content": [
            {"type": "input_text", "text": user_input}
        ]
    })


    riko_test_response = get_riko_response_no_tool(messages)


    # just append assistant message to regular response. 
    messages.append({
    "role": "assistant",
    "content": [
        {"type": "output_text", "text": riko_test_response.text}
    ]
    })

    save_history(messages)
    return riko_test_response.text


if __name__ == "__main__":
    print('running main')
