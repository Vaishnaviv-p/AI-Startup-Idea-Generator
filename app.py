import random

industry = input("Enter an industry: ")

ideas = [
    "AI Assistant",
    "AI Analytics Platform",
    "AI Marketplace",
    "AI Automation Tool",
    "AI Recommendation System",
    "AI Chatbot",
    "AI Productivity Tool"
]

idea = random.choice(ideas)

print("\nGenerated Startup Idea:")
print(idea, "for", industry)