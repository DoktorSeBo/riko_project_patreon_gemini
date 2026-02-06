<div align="center">
  <img src="https://img.shields.io/badge/AI-Gemini%20API-orange?style=for-the-badge&logo=google-gemini" alt="Gemini Badge">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" alt="Python Badge">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status Badge">

  <h1>🌌 Riko Project: Gemini Integration</h1>
  <p><i>A seamless rewrite of the Riko logic to leverage the power of Google Gemini AI.</i></p>

  <a href="#-quick-start">Quick Start</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-configuration">Configuration</a>
</div>

---

## 📖 Overview
This repository provides a modified version of the `llm_scr.py` script. It replaces the default OpenAI implementation with the **Google Gemini API**, allowing for faster response times and different model capabilities within the Project Riko ecosystem.

---

## 🚀 Quick Start

Follow these steps to get your Gemini-powered Riko up and running:

<details>
<summary><b>Step 1: Get your Gemini API Key</b></summary>
<br>
You need an active API key from Google AI Studio.
<br><br>
👉 <a href="https://aistudio.google.com/api-keys" target="_blank">Generate your Key here</a>
</details>

<details>
<summary><b>Step 2: Base Project Setup</b></summary>
<br>
Ensure you have the original Riko project files. If you haven't set up the base project yet, follow Rayen's official guide:
<br><br>
👉 <a href="https://www.patreon.com/posts/project-riko-v1-134743975" target="_blank">Rayen's Setup Guide</a>
</details>

---

## 🛠 Installation

### 1. Install Dependencies
Run the following command in your terminal to install the necessary Google GenAI library:

```bash
pip install -U google-genai
