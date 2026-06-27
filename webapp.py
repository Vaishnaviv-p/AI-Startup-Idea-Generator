from flask import Flask, request, render_template, send_file
import random
from startup_data import startup_data, startup_names
from pdf_generator import create_pdf

app = Flask(__name__)

latest_result = None


@app.route("/")
def home():

    global latest_result

    result = None
    industry = request.args.get("industry")

    if industry:

        industry = industry.lower()

        if industry in startup_data:
            data = startup_data[industry]
        else:
            data = startup_data["default"]

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

        roadmap = [
            "Month 1 - Market Research",
            "Month 2 - Build MVP",
            "Month 3 - Beta Testing",
            "Month 4 - Marketing Campaign",
            "Month 5 - Scale Business",
            "Month 6 - Official Launch"
        ]

        score = random.randint(75, 100)

        if score >= 90:
            success_level = "🚀 Excellent Chance of Success"
        elif score >= 80:
            success_level = "🌟 Very Good Potential"
        elif score >= 70:
            success_level = "👍 Good Potential"
        else:
            success_level = "⚠️ Needs Improvement"

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

            "score": score,
            "success_level": success_level,

            "strength": random.choice(strengths),
            "weakness": random.choice(weaknesses),
            "opportunity": random.choice(opportunities),
            "threat": random.choice(threats),

            "roadmap": roadmap,
            "business_tips": data["business_tips"]

        }

        latest_result = result

    return render_template("index.html", result=result)


@app.route("/download")
def download():

    global latest_result

    if latest_result is None:
        return "Generate a startup idea first."

    filename = create_pdf(latest_result)

    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
