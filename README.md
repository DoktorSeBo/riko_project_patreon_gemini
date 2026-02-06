<div align="center">
  <img src="https://img.shields.io/badge/AI-Gemini%20API-orange?style=for-the-badge&logo=google-gemini" alt="Gemini Badge">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" alt="Python Badge">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status Badge">

  <h1>🌌 Riko Project: Gemini Integration</h1>
  <p><i>A seamless rewrite of the Riko logic to leverage the power of Google Gemini AI.</i></p>

  <a href="#-quick-start">Quick Start</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-finishing-steps">Finishing Steps</a>
</div>

---

## 📖 Overview
This repository provides a modified version of the `llm_scr.py` script. It replaces the default OpenAI implementation with the **Google Gemini API**, allowing for different model capabilities within the Project Riko ecosystem.

---

## 🚀 Quick Start

Follow these steps to get your Gemini-powered Riko up and running:

### 1. Get your Gemini API Key
You need an active API key from Google AI Studio.

👉 <a href="https://aistudio.google.com/api-keys" target="_blank">Generate your Key here</a>


### 2. Base Project Setup
Ensure you have the original Riko project files. If you haven't set up the base project yet, follow Rayen's official guide:

👉 <a href="https://www.patreon.com/posts/project-riko-v1-134743975" target="_blank">Rayen's Setup Guide</a>


---

## 🛠 Installation

### 1. Install Dependencies
Run the following command in your terminal to install the necessary Google GenAI library:

```bash
pip install -U google-genai
```
### 2. Replace the Logic File
Download the `llm_scr.py` from this repository.

Locate the original `llm_scr.py` in your main Riko project folder.

Replace the old file with the new one.


### 4. Replace the Logic File
Download the `llm_scr.py` file from this repository and use it to replace the original `llm_scr.py` file inside your main project folder.

## 🎯 Finishing Steps

### Update Environment Keys
You need to rename your API key variable so the new script can recognize it.
* Search for every `OPEN_AI_KEY` instance and change it to `GEMINI_AI_KEY`.
* *Tip: Use **Ctrl + F** in your editor to find all instances quickly.*
* Don't forget your `.env` file!

### Change AI model
In your `character_config.yaml`, update the model field to your preferred Gemini model.

**Example:** `model: "gemini-2.5-flash"` (or your desired model)

---

<div align="center">
  <p>Made with ❤️ for the Riko Community</p>
  <sub>Thanks to Rayen for creating the main project.</sub>
</div>
