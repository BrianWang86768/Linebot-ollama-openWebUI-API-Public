# LineBot with Ollama and OpenWebUI Integration

## Overview
This project is a LineBot built with Django, integrating **Ollama** (a local large language model framework) and **OpenWebUI** (a web-based interface for AI interactions). The bot allows users to interact with an AI model via Line messaging, while OpenWebUI provides a web interface for enhanced user experience. The project is designed to handle natural language queries, leveraging Ollama's local AI capabilities and OpenWebUI's user-friendly frontend.

## Features
- **LineBot Integration**: Communicate with the AI via Line messaging.
- **Ollama Integration**: Utilizes a locally hosted language model for fast and private AI responses.
- **OpenWebUI Support**: Provides a web interface for interacting with the AI model.
- **Django Backend**: Manages bot logic, API requests, and web interface routing.
- **Customizable**: Easily configure for different AI models or Line channels.

## Prerequisites
- Python 3.8+
- Django 4.x
- Line Messaging API account and channel access token
- Ollama installed locally with a supported model (e.g., LLaMA, Mistral)
- OpenWebUI installed and configured
- Git for version control
- (Optional) Ngrok or similar for local webhook testing

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/BrianWang86768/jangogpt.git
cd jangogpt
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
Ensure `requirements.txt` includes:
```
django>=4.0
line-bot-sdk
requests
```

### 4. Install and Configure Ollama
- Follow the [Ollama installation guide](https://ollama.ai/) to set up Ollama locally.
- Pull a model (e.g., `ollama pull llama3`).
- Start the Ollama server:
  ```bash
  ollama run llama3
  ```

### 5. Install and Configure OpenWebUI
- Follow the [OpenWebUI setup guide](https://github.com/open-webui/open-webui) to install and run the web interface.
- Ensure OpenWebUI is connected to your Ollama instance (default: `http://localhost:11434`).

### 6. Configure Line Messaging API
1. Create a Line Official Account and obtain:
   - Channel Secret
   - Channel Access Token
2. Set up a webhook URL (e.g., using Ngrok for local testing: `ngrok http 8000`).
3. Update `settings.py` with your Line credentials:
   ```python
   LINE_CHANNEL_ACCESS_TOKEN = 'your-channel-access-token'
   LINE_CHANNEL_SECRET = 'your-channel-secret'
   ```

### 7. Set Up Django
- Apply migrations:
  ```bash
  python manage.py migrate
  ```
- Start the Django development server:
  ```bash
  python manage.py runserver
  ```

### 8. Configure Webhook
- Set the Line webhook URL to your server (e.g., `https://your-ngrok-url/linebot/webhook`).
- Verify the webhook in the Line Developer Console.

## Usage
1. Add the LineBot to your Line contacts by scanning the QR code from your Line Official Account.
2. Send messages to the bot to interact with the AI model powered by Ollama.
3. Access the OpenWebUI interface (default: `http://localhost:3000`) for a web-based AI chat experience.
4. Example commands:
   - Send "Hello, how can you help?" to get an AI response via Line.
   - Use OpenWebUI to explore advanced AI features or customize prompts.

## Project Structure
```
LineBotProject/
├── manage.py             # Django management script
├── jangogpt/             # Django project & LineBot settings
├── app/                  # Django app for LineBot logic
│   ├── views.py          # Handles webhook and AI requests
│   └── services          # Handles AI services
│       ├──ai_chat.py     # use Ollama or OpenAI API
│       └──OpenWebUIAPI.py# use OpenWebUI API
└── README.md             # This file
```

## Notes
- **Security**: Do not expose sensitive information (e.g., Line credentials, API keys) in your Git repository. Use environment variables or a `.env` file.
- **Local Testing**: Use Ngrok or similar tools to expose your local server for Line webhook testing.
- **Ollama Models**: Ensure sufficient disk space and RAM for the selected AI model.
- **Public Repository**: If making this repository public, ensure no sensitive data is included in the commit history (see [Cleaning Git History](#cleaning-git-history)).

## Cleaning Git History
If you accidentally committed sensitive data (e.g., API keys), clean the repository history before making it public:
```bash
git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch path/to/sensitive/file' \
--prune-empty --tag-name-filter cat -- --all
git push origin main --force
```
**Warning**: This rewrites history and may affect collaborators.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for bugs, features, or improvements.
