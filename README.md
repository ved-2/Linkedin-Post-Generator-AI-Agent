# 🚀 LinkedIn Post Generator AI Agent

Generate high-quality LinkedIn posts using AI, evaluate them with multiple AI reviewers, improve them through human feedback, and create polished LinkedIn-ready content.

## 🌐 Live Demo

**Try it here:**

https://linkedin-post-generator-ai-agent.streamlit.app/

---

## 📌 Overview

LinkedIn Post Generator AI Agent is an AI-powered content creation assistant built using:

* LangChain
* Gemini / Groq LLMs
* Streamlit
* Pydantic Structured Outputs

The application generates LinkedIn posts, evaluates them using multiple AI evaluators, allows human feedback, and iteratively improves the content.

---

## ✨ Features

### 📝 AI Post Generation

Generate professional LinkedIn posts from a simple topic.

Examples:

* LangGraph Learning Journey
* AI Agents
* Machine Learning Projects
* Software Engineering Career Tips

---

### 🔥 Multi-Agent Evaluation

The generated post is reviewed by multiple AI evaluators.

#### Engagement Evaluator

Analyzes:

* Hook Quality
* Curiosity Generation
* CTA Effectiveness
* Virality Potential

#### Readability Evaluator

Analyzes:

* Clarity
* Grammar
* Simplicity
* Flow
* Readability

#### Recruiter Evaluator

Analyzes:

* Professionalism
* Personal Branding
* Career Impact
* Industry Relevance

---

### 📊 Final Evaluation

All evaluator feedback is aggregated into a final review.

Provides:

* Overall Score
* Summary
* Key Strengths
* Key Weaknesses
* Improvement Suggestions

---

### 🧠 Human-in-the-Loop

Users can provide custom feedback such as:

* Make it shorter
* Add emojis
* Improve storytelling
* Focus on recruiters
* Make it more technical

The AI then regenerates an improved version.

---

### ⚡ Advanced Optimization

Optimization supports:

* Audience Targeting
* Tone Selection
* Length Control
* Emoji Preferences

---

### 🎯 Audience Selection

Choose the target audience:

* Recruiters
* Developers
* Students
* Founders
* AI Engineers

---

### 🎨 Tone Selection

Generate content in different styles:

* Professional
* Technical
* Storytelling
* Motivational

---

### 📏 Length Control

Control output size:

* Short
* Medium
* Long

---

### 😊 Emoji Support

Enable or disable emojis for professional social media posts.

---

### 📈 Before vs After Score Comparison

Track improvements after optimization.

Example:

Before: 7.8/10

After: 9.2/10

---

### 💼 LinkedIn Integration

Quick action button to:

* Copy generated post
* Open LinkedIn
* Publish faster

---

## 🏗️ Tech Stack

### Frontend

* Streamlit

### LLM

* Groq
* Gemini

### Frameworks

* LangChain

### Validation

* Pydantic

### Environment Management

* Python Dotenv

---

## 📂 Project Structure

```text
linkedin-post-generator-ai-agent/
│
├── app.py
├── graph.py
├── prompts.py
├── models.py
├── llm.py
├── requirements.txt
├── .env
└── README.md
```

## 🚀 Installation

Clone repository:

```bash
git clone https://github.com/yourusername/linkedin-post-generator-ai-agent.git

cd linkedin-post-generator-ai-agent
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`

```env
GROQ_API_KEY=your_api_key
```

Run application:

```bash
streamlit run app.py
```

---

## 📷 Workflow

```text
Topic
  │
  ▼
Generate Post
  │
  ▼
Multi-Agent Evaluation
  │
  ├── Engagement Evaluator
  ├── Readability Evaluator
  └── Recruiter Evaluator
  │
  ▼
Final Evaluation
  │
  ▼
Human Feedback
  │
  ▼
Optimization
  │
  ▼
Re-Evaluation
  │
  ▼
Approved LinkedIn Post
```

---

## 🎯 Future Improvements

* Real LinkedIn API Integration
* Direct LinkedIn Publishing
* Image Generation for Posts
* Post Scheduling
* Analytics Dashboard
* LangGraph Parallel Workflows
* Memory & User Profiles

---

## 👨‍💻 Author

Vedant Kolte

B.Tech AI & Data Science Student

Passionate about AI Agents, GenAI, LangGraph, LangChain, and Full Stack Development.

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

🚀 Share with others
