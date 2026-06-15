# 🚀 The 10-Minute CTO

The 10-Minute CTO is a quick prototype tool designed for initiatives and indie hackers. Simply enter your startup idea, and it leverages a 32B Large Language Model (or a handy mock fallback) to instantly generate:

1. A recommended **Tech Stack** 
2. A high-level **Database Schema**
3. A **downloadable `.zip` file** containing a ready-to-run FastAPI backend scaffold.

## Setup & Installation

1. Ensure you have Python installed (Python 3.8+ recommended).
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or venv\Scripts\activate on Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

To start the Gradio application locally:

```bash
python app.py
```

The app will start up on `http://127.0.0.1:7860/` by default. Open this URL in your browser.

## Usage
- Enter your startup idea in the text area.
- (Optional) Provide your Open Source API token. If valid, the app will ping a hosted 32B model (e.g., `openbmb/MiniCPM4.1-8B`) via the `Open Source_hub` Serverless Inference API to generate a dynamic response and code scaffolding.
- If you don't provide a token or if the API limits are reached, the app automatically falls back to a locally generated **mock response** so you can still experience the end-to-end functionality of receiving a tech stack, schema, and downloading the `.zip` scaffold!

**Note:** Do not deploy this specific project setup to Open Source or GitHub as per requirements. Keep it running locally.
