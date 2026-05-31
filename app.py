from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    risk_level = "High"

    shelters = [
        "Community Shelter A",
        "School Shelter B",
        "Cyclone Center C"
    ]

    evacuation_steps = [
        "Prepare emergency bag",
        "Charge mobile phone",
        "Move to nearest shelter",
        "Inform family members"
    ]

    return render_template(
        "index.html",
        risk=risk_level,
        shelters=shelters,
        steps=evacuation_steps
    )

if __name__ == "__main__":
    app.run(debug=True)
