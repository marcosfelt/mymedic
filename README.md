# MyMedic

This is a backend for the Google Assistant Action.  It uses the web microframework flask along with an extension called [flask-ask](https://github.com/johnwheeler/flask-ask).

## Dev Installation

1. Download [ngrok](https://ngrok.com/) and start tunnel port 5000. Save the https link you receive.

    ./ngrok http 5000

2. In a new terminal window, clone this repo from github:

    git clone https://github.com/marcosfelt/mad-minute

3. Change into the app/ directory and start the server:

    python main.py

4. Navigate to the Alexa [developer console](https://developer.amazon.com/alexa)
   and create a new skill from the "Your Alexa Consoles"

5. Paste in the [scheme.json](./app/scheme.json) into the Interaction Model under the build   tab.  Use the json editor.

6. Under endpoint, select https and paste the https link from ngrok under default region.

7. Now you can test the skill from the test tab.

## Deployment

1. Make sure the docker container builds properly locally and serves correctly.

    docker build -t myimage .
    docker run -d --name mycontainer -p 5000:5000 myimage

2. Deploy to now (make sure ot the [now cli](https://github.com/zeit/now-cli) installed).

    now

3. Copy and paste the link you get into the endpoint field in the alexa skill setup


## Some Notes

- When testing in the Alexa Console, make sure to enter numbers as text (e.g., ten not 10)

- The flask-ask source is included in this directory (and the docker build) because it the pypi install wasn't working.