from flask import Flask, request, render_template, send_file, redirect
import random

from startup_data import startup_data, startup_names
from startup_scorer import calculate_startup_score
from pdf_generator import create_pdf
from database import db, Startup

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///startup.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

latest_result = None


@app.route("/")
def home():

    global latest_result

    startup_results = []
    latest_id = None

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

        for idea in data["ideas"]:

            evaluation = calculate_startup_score()
            score = evaluation["total"]

            if score >= 90:
                success_level = "🚀 Excellent Chance of Success"
            elif score >= 80:
                success_level = "🌟 Very Good Potential"
            elif score >= 70:
                success_level = "👍 Good Potential"
            else:
                success_level = "⚠️ Needs Improvement"

            if score >= 95:
                funding = "Venture Capital"
                funding_reason = "Excellent growth potential for VC investment."

            elif score >= 90:
                funding = "Angel Investment"
                funding_reason = "Strong early-stage investment opportunity."

            elif score >= 80:
                funding = "Seed Funding"
                funding_reason = "Suitable for seed funding."

            else:
                funding = "Bootstrapping"
                funding_reason = "Can initially be self-funded."

            result = {

                "industry": industry.title(),

                "name": random.choice(startup_names),

                "idea": idea,

                "customer": random.choice(data["customers"]),

                "revenue": random.choice(data["revenue_models"]),

                "description": random.choice(data["descriptions"]),

                "target_market": data["target_market"],

                "investment": data["investment"],

                "development_time": data["development_time"],

                "market_potential": data["market_potential"],

                "category": data["category"],

                "score": score,

                "evaluation": evaluation,

                "success_level": success_level,

                "funding": funding,

                "funding_reason": funding_reason,

                "strength": random.choice(strengths),

                "weakness": random.choice(weaknesses),

                "opportunity": random.choice(opportunities),

                "threat": random.choice(threats),

                "roadmap": roadmap,

                "business_tips": data["business_tips"],

                "competitors": data["competitors"]

            }

            startup_results.append(result)
                        # Save startup to database
            startup = Startup(
                industry=result["industry"],
                name=result["name"],
                idea=result["idea"],
                customer=result["customer"],
                revenue=result["revenue"],
                description=result["description"],
                score=result["score"]
            )

            db.session.add(startup)
            db.session.flush()

            latest_id = startup.id

        # Save all startups
        db.session.commit()

        # Highest score first
        startup_results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        latest_result = startup_results[0]

    return render_template(
        "index.html",
        results=startup_results,
        latest_id=latest_id
    )


@app.route("/history")
def history():

    search = request.args.get("search")
    favorites = request.args.get("favorites")

    query = Startup.query

    if favorites:
        query = query.filter_by(favorite=True)

    if search:
        query = query.filter(
            Startup.industry.contains(search) |
            Startup.name.contains(search) |
            Startup.idea.contains(search)
        )

    startups = query.order_by(
        Startup.id.desc()
    ).all()

    return render_template(
        "history.html",
        startups=startups,
        search=search
    )


@app.route("/favorite/<int:id>")
def favorite(id):

    startup = Startup.query.get_or_404(id)

    startup.favorite = not startup.favorite

    db.session.commit()

    return redirect("/history")


@app.route("/delete/<int:id>")
def delete(id):

    startup = Startup.query.get_or_404(id)

    db.session.delete(startup)

    db.session.commit()

    return redirect("/history")


@app.route("/download")
def download():

    global latest_result

    if latest_result is None:
        return "Generate a startup idea first."

    filename = create_pdf(latest_result)

    return send_file(
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)