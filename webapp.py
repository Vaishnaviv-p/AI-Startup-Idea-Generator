from flask import Flask, request, render_template
import random
from startup_data import startup_data, startup_names

app = Flask(__name__)

@app.route("/")
def home():

    result = None
    industry = request.args.get("industry")

    if industry:

        industry = industry.lower()

        if industry in startup_data:
            data = startup_data[industry]
        else:
            data = startup_data["default"]

        # SWOT Analysis

        strengths = [
            "Strong AI-driven solution",
            "High market demand",
            "Scalable business model",
            "Innovative technology"
        ]

        weaknesses = [
            "High initial investment",
            "Requires skilled developers",
            "Strong market competition",
            "Continuous maintenance required"
        ]

        opportunities = [
            "Growing AI adoption",
            "Global expansion",
            "Government support",
            "Enterprise partnerships"
        ]

        threats = [
            "Rapid technology changes",
            "Cybersecurity risks",
            "New competitors",
            "Changing regulations"
        ]

        # Startup Roadmap

        roadmap = [
            "Month 1 - Market Research",
            "Month 2 - Build MVP",
            "Month 3 - Beta Testing",
            "Month 4 - Marketing Campaign",
            "Month 5 - Scale Business",
            "Month 6 - Official Launch"
        ]

        result = {

            "industry": industry.title(),

            "name": random.choice(startup_names),
            "idea": random.choice(data["ideas"]),
            "customer": random.choice(data["customers"]),
            "revenue": random.choice(data["revenue_models"]),
            "description": random.choice(data["descriptions"]),

            "target_market": data["target_market"],
            "investment": data["investment"],
            "development_time": data["development_time"],
            "market_potential": data["market_potential"],
            "category": data["category"],

            "score": random.randint(75, 100),

            "strength": random.choice(strengths),
            "weakness": random.choice(weaknesses),
            "opportunity": random.choice(opportunities),
            "threat": random.choice(threats),

            "roadmap": roadmap,

            # ⭐ NEW FEATURE (Version 13.3)
            "business_tips": data["business_tips"]

        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)