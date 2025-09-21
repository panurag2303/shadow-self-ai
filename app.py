from flask import Flask, request, render_template_string

app = Flask(__name__)

# Mock AI function (Shadow Self)
def ask_shadow_self(user_text):
    user_text = user_text.lower()
    if "exam" in user_text:
        return "It’s normal to feel nervous before exams. Take deep breaths and focus on one thing at a time."
    elif "lonely" in user_text:
        return "Even if you feel alone, reaching out to one trusted friend can help."
    elif "family" in user_text or "talk" in user_text:
        return "It can be scary, but sharing with someone you trust is a good start."
    elif "confidence" in user_text:
        return "Start small, celebrate little wins, and remember everyone learns at their own pace."
    else:
        return "Thanks for sharing. I’m here to listen. Can you tell me more?"

# Web page template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Shadow Self - Youth Wellness AI</title>
</head>
<body style="font-family: Arial; margin: 40px;">
    <h1>🌙 Shadow Self - Your Big Brother AI</h1>
    <form method="post">
        <label>Share your thoughts:</label><br><br>
        <input type="text" name="user_input" style="width:400px;" required>
        <button type="submit">Ask</button>
    </form>
    {% if reply %}
        <h2>Shadow Self says:</h2>
        <p>{{ reply }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    reply = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        reply = ask_shadow_self(user_input)
    return render_template_string(html_template, reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
