from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():

    industry = request.args.get("industry")
    result = None

    if industry:

        industry = industry.title()

        startup_names = [
            "AINova",
            "SmartSync",
            "VisionAI",
            "FutureFlow",
            "InnoTech",
            "NextGenAI",
            "BrainBoost",
            "TechSphere"
        ]

        # ---------------- HEALTHCARE ----------------

        if industry.lower() == "healthcare":

            ideas = [
                "AI Medical Assistant",
                "AI Hospital Management System",
                "AI Patient Monitoring Platform",
                "AI Health Analytics Platform"
            ]

            customers = [
                "Doctors",
                "Hospitals",
                "Patients",
                "Clinics"
            ]

            revenue_models = [
                "Subscription",
                "Enterprise Licensing",
                "Pay-per-use"
            ]

            descriptions = [
                "Helps doctors diagnose diseases using AI.",
                "Automates hospital operations efficiently.",
                "Monitors patients remotely using AI.",
                "Provides healthcare analytics for hospitals."
            ]

            target_market = "Global"
            investment = "₹15 Lakhs"
            development_time = "8 Months"
            market_potential = "Very High"
            category = "Healthcare Technology"

        # ---------------- EDUCATION ----------------

        elif industry.lower() == "education":

            ideas = [
                "AI Learning Assistant",
                "AI Exam Generator",
                "AI Tutor Platform",
                "AI Student Analytics"
            ]

            customers = [
                "Students",
                "Teachers",
                "Schools",
                "Universities"
            ]

            revenue_models = [
                "Freemium",
                "Subscription",
                "Advertising"
            ]

            descriptions = [
                "Personalized AI tutor for students.",
                "Creates smart online exams.",
                "Tracks student learning progress.",
                "Improves classroom engagement using AI."
            ]

            target_market = "National"
            investment = "₹8 Lakhs"
            development_time = "5 Months"
            market_potential = "High"
            category = "Education Technology"

        # ---------------- FINANCE ----------------

        elif industry.lower() == "finance":

            ideas = [
                "AI Investment Advisor",
                "AI Fraud Detection",
                "AI Budget Planner",
                "AI Financial Analytics"
            ]

            customers = [
                "Banks",
                "Investors",
                "Businesses",
                "Financial Advisors"
            ]

            revenue_models = [
                "Subscription",
                "Enterprise Licensing",
                "Commission"
            ]

            descriptions = [
                "Detects financial fraud instantly.",
                "Provides AI investment recommendations.",
                "Analyzes financial performance.",
                "Helps customers manage budgets."
            ]

            target_market = "Global"
            investment = "₹25 Lakhs"
            development_time = "10 Months"
            market_potential = "Very High"
            category = "FinTech"

        # ---------------- AGRICULTURE ----------------

        elif industry.lower() == "agriculture":

            ideas = [
                "AI Crop Monitoring",
                "AI Farm Assistant",
                "AI Weather Prediction",
                "AI Smart Irrigation"
            ]

            customers = [
                "Farmers",
                "Agricultural Companies",
                "Food Producers",
                "Cooperatives"
            ]

            revenue_models = [
                "Subscription",
                "Government Partnership",
                "Pay-per-use"
            ]

            descriptions = [
                "Monitors crop health using AI.",
                "Predicts weather for farming.",
                "Optimizes irrigation systems.",
                "Improves agricultural productivity."
            ]

            target_market = "Rural & Global"
            investment = "₹12 Lakhs"
            development_time = "7 Months"
            market_potential = "Medium"
            category = "AgriTech"
                    # ---------------- DEFAULT ----------------

        else:

            ideas = [
                "AI Assistant",
                "AI Marketplace",
                "AI Analytics Platform",
                "AI Automation Tool",
                "AI Recommendation System"
            ]

            customers = [
                "Startups",
                "Small Businesses",
                "Companies",
                "Professionals"
            ]

            revenue_models = [
                "Subscription",
                "Freemium",
                "Advertising"
            ]

            descriptions = [
                "Automates business operations using AI.",
                "Provides intelligent recommendations.",
                "Improves productivity using AI.",
                "Connects businesses with AI solutions."
            ]

            target_market = "Global"
            investment = "₹10 Lakhs"
            development_time = "6 Months"
            market_potential = "High"
            category = "Artificial Intelligence"

        result = {
            "name": random.choice(startup_names),
            "idea": random.choice(ideas),
            "customer": random.choice(customers),
            "revenue": random.choice(revenue_models),
            "description": random.choice(descriptions),
            "target_market": target_market,
            "investment": investment,
            "development_time": development_time,
            "market_potential": market_potential,
            "category": category,
            "score": random.randint(75, 100),
            "industry": industry
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)