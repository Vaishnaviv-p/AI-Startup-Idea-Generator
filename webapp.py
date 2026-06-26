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

        result = {
            "name": random.choice(startup_names),
            "idea": random.choice(ideas),
            "customer": random.choice(customers),
            "revenue": random.choice(revenue_models),
            "description": random.choice(descriptions),
            "target_market": target_market,
            "score": random.randint(75, 100),
            "industry": industry
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)