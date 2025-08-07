# 🔗 Free-LLM-Caller

A flexible Python script that connects to **multiple LLM providers** (Gemini, Groq, OpenRouter, Mistral, OpenAI, Fireworks, and more) using a unified configuration system. Perfect for testing, comparing, and switching between models without changing code.

🔧 Powered by:
- `pydantic-settings` – Clean environment-based config
- Multiple LLM APIs – Gemini, Groq, OpenRouter, Mistral, Fireworks, Azure OpenAI
- `.env` file support – Secure key management
- Modular design – Easy to extend

🚀 Use cases:
- Compare model outputs
- Fallback across providers
- Research & content formatting
- Arabic/English mixed text processing

---

## 🧰 Features

| Feature | Description |
|-------|-------------|
| ✅ Multiple LLMs | Gemini, Groq, OpenRouter, Mistral, OpenAI, Fireworks |
| 🔐 Secure Keys | All API keys loaded from `.env` file |
| 🧩 Unified Interface | Same `get_xxx_response()` pattern for all providers |
| 📦 Pydantic Settings | Type-safe, auto-validating config |
| 🌍 Temperature Control | Global `TEMPR` setting |
| 🛠️ Easy to Extend | Add new providers in seconds |

---

## ⚙️ Supported Providers

| Provider | Model Example | Environment Variables |
|--------|----------------|------------------------|
| **Google Gemini** | `gemini-1.5-pro` | `GEMINI_API_KEY`, `GEMINI_MODEL` |
| **Groq** | `llama3-8b-8192` | `GROQ_API_KEY`, `GROQ_MODEL` |
| **OpenRouter** | `mistralai/mixtral-8x7b-instruct` | `OPENROUTER_API_KEY`, `OPENROUTER_MODEL_NAME` |
| **Mistral AI** | `mistral-large-latest` | `MISTRAL_KEY`, `MISTRAL_MODEL` |
| **Azure OpenAI** | `gpt-4o-mini` | `OPENAI_KEY`, `OPENAI_MODEL` |
| **Fireworks AI** | `mixtral-8x7b-instruct` | `FIREWORKS_API_KEY`, `FIREWORKS_MODEL` |

> 💡 All use the same `system_prompt.txt` and `read_text_file()` utility.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/Free-LLM-Caller.git
cd Free-LLM-Caller

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```
## 🔐 Setup: 
**Create .env File**
- Rename the ```.env.example``` to be ```.env``` and enter your API Keys and Models names<br>

**System Prompt**
- Enter your system prompt in system_prompt.txt file

**Import into your code**
```bash
from llm_providers import *
user_input = "your user prompt"

# Test multiple models
response1 = get_gemini_response(user_input)
response2 = get_groq_response(user_input)
response3 = get_fireworks_response(user_input)

# put your code here to compare or ....
```
### 🙌 Support
🐞 Report bugs via GitHub Issues<br>

🌟 Star the repo if you like it!<br>

📧 Contact: Khaled.edu.engineer@gmail.com<br>



