from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():

    industry = request.args.get("industry")

    result = ""

    if industry:

        startup_names = [
            "AINova",
            "SmartSync",
            "VisionAI",
            "FutureFlow",
            "InnoTech"
        ]

        ideas = [
            "AI Assistant",
            "AI Marketplace",
            "AI Analytics Platform",
            "AI Automation Tool",
            "AI Recommendation System"
        ]

        customers = [
            "Students",
            "Doctors",
            "Small Businesses",
            "Teachers",
            "Startups"
        ]

        revenue_models = [
            "Subscription",
            "Freemium",
            "Pay-per-use",
            "Advertising",
            "Enterprise Licensing"
        ]

        result = {
            "name": random.choice(startup_names),
            "idea": random.choice(ideas),
            "customer": random.choice(customers),
            "revenue": random.choice(revenue_models),
            "score": random.randint(60, 100),
            "industry": industry
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)