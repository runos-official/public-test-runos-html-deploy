from flask import Flask, jsonify, render_template_string
import random
from datetime import datetime

app = Flask(__name__)

QUOTES = [
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Innovation distinguishes between a leader and a follower.", "author": "Steve Jobs"},
    {"text": "Life is 10% what happens to you and 90% how you react to it.", "author": "Charles R. Swindoll"},
    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"text": "It is during our darkest moments that we must focus to see the light.", "author": "Aristotle"},
    {"text": "The way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"text": "Don't let yesterday take up too much of today.", "author": "Will Rogers"},
    {"text": "You learn more from failure than from success. Don't let it stop you.", "author": "Unknown"},
    {"text": "It's not whether you get knocked down, it's whether you get up.", "author": "Vince Lombardi"},
    {"text": "People who are crazy enough to think they can change the world, are the ones who do.", "author": "Rob Siltanen"},
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Inspiration</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 60px 40px;
            max-width: 700px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            text-align: center;
        }
        h1 {
            color: #667eea;
            margin-bottom: 40px;
            font-size: 2.5em;
        }
        .quote {
            font-size: 1.5em;
            color: #333;
            line-height: 1.6;
            margin-bottom: 30px;
            font-style: italic;
        }
        .author {
            font-size: 1.2em;
            color: #764ba2;
            font-weight: bold;
        }
        .refresh-btn {
            margin-top: 40px;
            padding: 15px 30px;
            font-size: 1.1em;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        .refresh-btn:hover {
            transform: scale(1.05);
        }
        .footer {
            margin-top: 30px;
            color: #888;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>✨ Daily Inspiration ✨</h1>
        <div class="quote">"{{ quote.text }}"</div>
        <div class="author">— {{ quote.author }}</div>
        <button class="refresh-btn" onclick="location.reload()">Get New Quote</button>
        <div class="footer">{{ current_time }}</div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    quote = random.choice(QUOTES)
    current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    return render_template_string(HTML_TEMPLATE, quote=quote, current_time=current_time)

@app.route('/api/quote')
def api_quote():
    quote = random.choice(QUOTES)
    return jsonify({
        "quote": quote["text"],
        "author": quote["author"],
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "daily-inspiration"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
