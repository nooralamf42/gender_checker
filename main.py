from flask import Flask, render_template
import time
import requests
app = Flask(__name__)

@app.route("/")
def home():
    current_year = time.strftime(("%Y"))
    return render_template("main.html", current_year= current_year)

@app.route(f"/<guess>")
def guesser(guess):
    current_year = time.strftime(("%Y"))
    response_gender = requests.get(url=f"https://api.genderize.io?name={guess}")
    gender_text =response_gender.json()

    if gender_text["gender"] == "female":
        image_link = "https://media.giphy.com/media/xT9IgzLiWOvVrMguUo/giphy.gif"
    else:
        image_link = "https://media.giphy.com/media/tUQ5HioPD5QpW/giphy.gif"

    return render_template("index.html", guessed_gender = gender_text["gender"], current_year= current_year,
                           image_link= image_link, username = guess.title())

if __name__ == "__main__":
    app.run(debug=True)



