# Swear Away
Our submission to the Google Solution Challenge 2025.

A Discord bot designed to make conversations more respectful by detecting and rewording hate speech. Instead of simply deleting offensive messages, the bot uses Gemini to transform them into neutral or polite language while preserving the original intent. This ensures that discussions remain uninterrupted, promotes positive communication, and creates a healthier online environment. By moderating conversations in a constructive way, the bot helps maintain engagement without resorting to strict censorship.

## Getting Started

### Prerequisites
* python3

### Installation

#### 1. Get API keys:
* Get a Gemini API key at https://aistudio.google.com/app/apikey
* Get a Discord bot token at https://discordapp.com/developers/applications

#### 2. Clone the repository
```sh
git clone https://github.com/LazyPluto/swear-away.git
cd swear-away
```

#### 3. Install dependencies
```sh
pip install -r requirements.txt
```

#### 4. Add API keys to `.env`
```
DISCORD_BOT_TOKEN=your-discord-bot-token
GEMINI_API_KEY=your-gemini-api-key
```

### Usage
```sh
python3 main.py
```
