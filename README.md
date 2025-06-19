# 🤖 Local CLI Chatbot using Hugging Face

This project is a lightweight, terminal-based chatbot built as part of an internship assignment. It uses a Hugging Face-supported language model (`microsoft/phi-2`) to simulate multi-turn conversation with short-term memory.

---

## 💡 Features

- Chatbot runs fully **locally** via command-line
- Uses Hugging Face `pipeline` and a **better-than-GPT2** model
- Maintains a **sliding window memory** of recent user-bot exchanges (e.g. last 3 turns)
- Modular code structure for clarity and reuse
- Clean exit via `/exit` command

---

## 🧱 Project Structure

chatbot_project/
├── model_loader.py # Loads model and tokenizer
├── chat_memory.py # Manages memory buffer (sliding window)
├── interface.py # Main CLI loop
├── requirements.txt # Dependencies
├── README.md # Project description and instructions


---

## ⚙️ Setup Instructions

### 🐍 1. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the chatbot
```bash
python interface.py
```
