from openai import OpenAI

client = OpenAI(
    base_url="your_ollama_base_url",  # Replace with your actual Ollama or openAI API base URL
    api_key="your_API_KEY",# Replace with your actual API key
)

chat_history = [
    {"role": "system", "content": "You are a helpful assistant."}# Enter your system prompt here
]

def update_chat_history(role, content):
    chat_history.append({"role": role, "content": content})

def ai_chat(user_input: str) -> str:
    update_chat_history("user", user_input.strip())
    chat_completion = client.chat.completions.create(
        model='llama3.2:3b',# Replace with your actual model name
        messages=chat_history,
    )
    response_text = chat_completion.choices[0].message.content
    update_chat_history("assistant", response_text)
    return response_text
