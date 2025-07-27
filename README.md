# Handoff Agents 🧠→💡

A multi-agent system that analyzes user mood and provides intelligent suggestions using Gemini AI.

## Features ✨

- **Mood Detection**: Identifies 6 emotional states (happy, sad, angry, stressed, excited, neutral)
- **Smart Handoff**: Routes to specialist agents when needed
- **Activity Suggestions**: Provides personalized recommendations
- **Positive Reinforcement**: Encourages good moods

## How It Works ⚙️

```mermaid
graph TD
    A[User Input] --> B(Mood Analyzer)
    B --> C{Triage Agent}
    C -->|Negative Mood| D[Activity Suggester]
    C -->|Positive Mood| E[Positive Response]
Example Sessions 💬
Case 1: Happy Mood

text
How are you feeling today? I just got promoted!

Mood detected: happy
😊 Great to hear you're doing well!
Case 2: Stressed Mood

text
How are you feeling today? Work is overwhelming me...

Mood detected: stressed
🌟 Suggestion: Try the 4-7-8 breathing technique (inhale 4s, hold 7s, exhale 8s). 
A 10-minute walk outside can also help clear your mind.

## Installation 🛠️

Clone repo:

bash
git clone https://github.com/AyeshaNasirWebDeveloper/Agentic-AI-Assignment-1/mood-analyzer.git
cd mood-analyzer
Create virtual environment:

bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
Install dependencies:

bash
Add .env file:

env
GEMINI_API_KEY=your_api_key_here
Usage 🚀
Run the analyzer:

bash
python main.py
Agent Architecture 🏗️
Agent	Role	Tools
Mood Analyzer	Classifies emotional state	None
Triage Agent	Routes to specialists	Decision logic
Activity Suggester	Provides coping strategies	Suggestion database
Requirements 📦
Python 3.10+

Gemini API Key

Packages:

python-dotenv

agents

## Contributing 🤝

Fork the project

Create your feature branch

Commit changes

Push to branch

Open PR

License 📜
MIT License - See LICENSE

Created with ❤️ by [Ayesha Nasir] | https://linktr.ee/ayesha_nasir
