import flask
from flask import request, render_template, redirect
import json

app = flask.Flask(__name__)

@app.route("/sign-up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":

        req = request.form
        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("sign_up.html", feedback=feedback)
        elif req['username'] in profiles.keys():
            feedback = f'Username taken. Pick a different one'
            return render_template("sign_up.html", feedback=feedback)
        else:
            saveProf(req)
            
        return redirect(f"/show-info?username={req['username']}")

    return render_template("sign_up.html")

@app.route("/show-info", methods=["GET"])
def show_info():
    profile = profiles[request.args.get('username')]
    print(profile)
    return render_template("info.html", data=profile, profiles=profiles)

def saveProf(profile):
    profiles[profile['username']] = {}
    profiles[profile['username']] = profile
    with open("profiles.json", 'w') as f:
        json.dump(profiles, f, indent=4)

def readProf():
    # print("READING PROFILES")
    with open("profiles.json", "r") as f:
        return json.load(f)

# @app.route("/favicon.ico")
# def favicon():
#     return 200

if __name__ == "__main__":
    profiles = readProf()
    app.run(debug=True)