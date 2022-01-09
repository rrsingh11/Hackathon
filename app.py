from flask import Flask, request, jsonify, render_template, url_for, redirect
import requests
from twilio.rest import Client
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        text = request.form["q"]
        phoneno = "+918460830860"

        #ml code here
        var = 0
        
        if var == 0:
            var = "happy"
        else:
            var = "sad"

        #spotify code here
        client_id = '243d607748094783bffa1d52780e1f11'
        client_secret = 'fe26e826eefc4b3a8a11e3b792b2c87e'
        auth_url = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
        }
        auth_response = requests.post(auth_url, data=data)
        access_token = auth_response.json().get('access_token')
        search_url = 'https://api.spotify.com/v1/search?q=' + var + "&type=playlist&limit=1"
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        response = requests.get(search_url,headers=headers).json()
        var2 = response['playlists']['items'][0]['external_urls']['spotify']

        #twilio code here
        account_sid = "AC208602ce83ba2f9fb6725044be1ed619"
        auth_token = "38632370714ed18329d5071a2006bc08"

        client = Client(account_sid, auth_token)

        client.messages.create(
                to=phoneno,
                from_="+18508163920",
                body=var2
                )


        return redirect(url_for("test",txt=text))
    else:
        return render_template('index.html')

@app.route("/<txt>")
def test(txt):
    return f"<h1>{txt}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

