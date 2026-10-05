from flask import Flask, render_template, request
import os

app = Flask(__name__)
print("TEMPLATES:", os.listdir("templates"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ai-jobs")
def ai_jobs():
    return render_template("ai-jobs.html")

@app.route("/ai-tools")
def ai_tools():
    return render_template("AITools.html")

@app.route("/helper")
def helper():
    return render_template("helper.html")

@app.route("/generate-prompt", methods=["POST"])
def generate_prompt():
    subject = request.form["subject"]
    task = request.form["task"]
    topic = request.form["topic"]
    level = request.form["level"]

    if task == "Explain":
        prompt = f"Explain {topic} in simple language suitable for a {level} studying {subject}. Give a clear definition, important points, and a simple example."

    elif task == "Summarize":
        prompt = f"Summarize {topic} for a {level} studying {subject}. Use simple language and provide the most important points for quick revision."

    elif task == "Practice":
        prompt = f"Create 10 practice questions about {topic} for a {level} studying {subject}. Include answers at the end and keep the questions suitable for the student's level."

    elif task == "Code":
        prompt = f"Help me understand and solve this programming task: {topic}. Explain the solution in simple language suitable for a {level}. Provide simple code and explain the important parts."

    elif task == "Notes":
        prompt = f"Create clear and exam-friendly notes about {topic} for a {level} studying {subject}. Include definitions, important points, examples, and a short summary."

    elif task == "Ideas":
        prompt = f"Generate useful and creative ideas related to {topic} for a {level}. Explain each idea briefly and keep the suggestions practical."

    elif task == "Improve":
        prompt = f"Improve the following text while keeping its original meaning. Make it clear, grammatically correct, and suitable for a {level}: {topic}"

    else:
        prompt = f"Help me with {topic}. Give a clear and simple answer suitable for a {level} studying {subject}."

    return render_template("helper.html", prompt=prompt)

if __name__ == "__main__":
    app.run(debug=True)