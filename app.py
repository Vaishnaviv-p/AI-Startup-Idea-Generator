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

name = random.choice(startup_names)
idea = random.choice(startup_ideas)

print("\n===== Startup Generated =====")
print("Startup Name:", name)
print("Startup Idea:", idea, "for", industry)