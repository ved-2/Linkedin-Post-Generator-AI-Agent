# LinkedIn Post Generator

A Streamlit app that generates LinkedIn posts, evaluates them with AI feedback, and improves them based on your audience, tone, length, emoji preference, and custom feedback.

## Features

- Generate LinkedIn-ready posts from a topic
- Optimize posts with hidden AI evaluator feedback
- Control target audience, tone, length, and emoji usage
- Copy the final post and open LinkedIn from the app

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Create your local environment file:

   ```bash
   copy .env.example .env
   ```

3. Add your Groq API key to `.env`:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

