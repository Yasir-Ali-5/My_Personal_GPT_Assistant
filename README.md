# My_Personal_GPT_Assistant
# ChatGPT Assistant (FastAPI + Static Frontend)

A simple, yet feature-rich ChatGPT-powered chatbot built with FastAPI and a static HTML/CSS/JavaScript frontend. This project demonstrates how to serve static assets, handle environment variables securely, and interact with OpenAI’s GPT models in a production-ready manner.

---

## 🔖 Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Prerequisites](#prerequisites)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Usage](#usage)
8. [Endpoints](#endpoints)
9. [Customization](#customization)
10. [Deployment](#deployment)
11. [Troubleshooting](#troubleshooting)
12. [License](#license)

---

## 🌟 Features

* **FastAPI Backend**: Lightweight and high-performance Python API.
* **OpenAI v1.x SDK**: Modern class-based client for interacting with GPT-4 or GPT-3.5 models.
* **Static Frontend**: Pure HTML, internal CSS, and vanilla JavaScript—no templating required.
* **Responsive UI**: Gradient backgrounds, custom chat bubbles, avatars, and loading animations.
* **Secure Config**: Environment variables loaded via `python-dotenv`.
* **Git Ignored**: Sensitive files, build artifacts, and IDE settings are excluded.
* **Clear Button**: Reset chat history on demand.

---

## 🛠️ Tech Stack

| Component   | Technology                         |
| ----------- | ---------------------------------- |
| Backend     | Python, FastAPI                    |
| HTTP Server | Uvicorn                            |
| AI Client   | OpenAI Python SDK (v1.x)           |
| Frontend    | HTML, CSS (internal), JavaScript   |
| Styling     | CSS Variables, Flexbox, Animations |
| Environment | python-dotenv                      |

---

## 📋 Prerequisites

* Python 3.9 or higher
* An OpenAI API key (generate at [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))
* `pip` package manager

---

## 📁 Project Structure

```plaintext
├── main.py             # FastAPI application
├── static/             # Static assets served under '/static'
│   └── index.html      # Chat UI with internal CSS
├── .env                # Environment variables (ignored by Git)
├── requirements.txt    # Python dependencies
├── .gitignore          # Files and folders to ignore in Git
└── README.md           # This documentation file
```

---

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/chatgpt-fastapi-static.git
   cd chatgpt-fastapi-static
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

1. **Create a `.env` file** in the project root:

   ```ini
   OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX
   ```
2. **Ensure `.env` is listed in `.gitignore`** to avoid leaking secrets.

---

## ▶️ Usage

1. **Start the FastAPI server**

   ```bash
   uvicorn main:app --reload
   ```

2. **Open your browser** at `http://127.0.0.1:8000/` to access the chat UI.

3. **Type a message** and hit **Send** or press **Enter**.

4. **Clear chat** anytime using the **Clear** button.

---

## 🌐 Endpoints

* **GET /**

  * Serves the static `index.html` chat UI.
* **POST /chat**

  * Accepts JSON: `{ "message": "<your text>" }`
  * Returns JSON: `{ "reply": "<AI response>" }`

---

## 🎨 Customization

* **Models**: Swap `gpt-4` with `gpt-3.5-turbo` in `main.py` if needed.
* **Styling**: Modify CSS variables in `index.html` for color/theme changes.
* **Avatars**: Replace avatar image URLs in the script with your own assets.
* **Timeout & Error Handling**: Tweak `timeout` parameter and exception logic in `main.py`.

---

## 📦 Deployment

* **Docker**: Add a `Dockerfile` to containerize the app.
* **Cloud Providers**: Deploy on Heroku, Render, or AWS.
* **HTTPS**: Use a reverse proxy (NGINX) or cloud-managed TLS.

---

## 🐛 Troubleshooting

* **401 Unauthorized**: Check `.env` for correct API key format (no quotes).
* **Request timed out**: Add a `timeout` argument to `client.chat.completions.create` or reduce model size.
* **Static 404**: Ensure `app.mount("/static", StaticFiles(directory="static"))` matches your folder name.

---

## 📄 License

This project is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute.

---

*Happy chatting!* 🚀
