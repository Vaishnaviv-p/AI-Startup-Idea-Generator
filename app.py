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

name = random.choice(startup_names)
idea = random.choice(startup_ideas)
customer = random.choice(customers)

print("\n===== Startup Generated =====")
print("Startup Name:", name)
print("Startup Idea:", idea, "for", industry)
print("Target Customers:", customer)