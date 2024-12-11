# Aniyah C.

from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    # Fetch a random joke from the Official Joke API
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke = response.json()  # Get the JSON data

    # Extract the setup and punchline from the joke data
    setup = joke['setup']
    punchline = joke['punchline']

    # Render the HTML template and pass the joke data
    return render_template('index.html', setup=setup, punchline=punchline)


if __name__ == '__main__':
    app.run(debug=True)
