import random

industry = input("Enter an industry: ")

startup_names = [
    "AINova",
    "SmartSync",
    "VisionAI",
    "FutureFlow",
    "InnoTech"
]

startup_ideas = [
    "AI Assistant",
    "AI Analytics Platform",
    "AI Marketplace",
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
idea = random.choice(startup_ideas)
customer = random.choice(customers)
revenue = random.choice(revenue_models)

print("\n===== Startup Generated =====")
print("Startup Name:", name)
print("Startup Idea:", idea, "for", industry)
print("Target Customers:", customer)
print("Revenue Model:", revenue)