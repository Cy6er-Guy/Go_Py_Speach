from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os
import uuid
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        lang = request.form.get("lang", "fr")  # Langue par défaut est "fr"
        filename = generate_speech(text, lang)
        return render_template("index.html", filename=filename)
    return render_template("index.html")

def generate_speech(text, lang):
    # Générer un nom de fichier unique
    unique_filename = f"output_{uuid.uuid4().hex}.mp3"  # Utilisation d'un UUID hexadécimal
    tts = gTTS(text=text, lang=lang)
    tts.save(os.path.join("static", unique_filename))
    return unique_filename

@app.route("/download/<filename>")
def download(filename):
    return send_file(os.path.join("static", filename), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
