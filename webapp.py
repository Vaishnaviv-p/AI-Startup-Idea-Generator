from flask import Flask, request
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

        name = random.choice(startup_names)
        idea = random.choice(ideas)
        customer = random.choice(customers)
        revenue = random.choice(revenue_models)
        score = random.randint(60, 100)

        result = f"""
        <h2>🚀 Startup Name: {name}</h2>
        <h3>💡 Startup Idea: {idea} for {industry}</h3>
        <p><b>🎯 Target Customers:</b> {customer}</p>
        <p><b>💰 Revenue Model:</b> {revenue}</p>
        <p><b>📈 Startup Score:</b> {score}/100</p>
        """

    return f"""
    <html>
    <head>
        <title>AI Startup Idea Generator</title>
    </head>

    <body style="
        font-family: Arial;
        background-color: #f4f6f9;
        text-align: center;
        padding-top: 50px;
    ">

        <h1 style="color: blue;">
            🚀 AI Startup Idea Generator
        </h1>

        <form>
            <input
                type="text"
                name="industry"
                placeholder="Enter Industry"
                style="
                    padding:10px;
                    width:250px;
                    border-radius:5px;
                "
            >

            <button
                type="submit"
                style="
                    padding:10px 20px;
                    background-color:green;
                    color:white;
                    border:none;
                    border-radius:5px;
                    cursor:pointer;
                "
            >
                Generate
            </button>
        </form>

        <br>

        <div style="
            background:white;
            width:600px;
            margin:auto;
            padding:20px;
            border-radius:10px;
            box-shadow:0px 0px 10px gray;
        ">
            {result}
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)