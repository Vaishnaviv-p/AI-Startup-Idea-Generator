import random

def calculate_startup_score():

    implementation = random.randint(7, 10)
    scalability = random.randint(7, 10)
    profitability = random.randint(7, 10)
    market_demand = random.randint(7, 10)
    innovation = random.randint(7, 10)
    problem_solving = random.randint(7, 10)
    competition = random.randint(6, 10)
    investment = random.randint(6, 10)
    ai_value = random.randint(7, 10)
    future_growth = random.randint(7, 10)

    total = (
        implementation +
        scalability +
        profitability +
        market_demand +
        innovation +
        problem_solving +
        competition +
        investment +
        ai_value +
        future_growth
    )

    return {
        "implementation": implementation,
        "scalability": scalability,
        "profitability": profitability,
        "market_demand": market_demand,
        "innovation": innovation,
        "problem_solving": problem_solving,
        "competition": competition,
        "investment": investment,
        "ai_value": ai_value,
        "future_growth": future_growth,
        "total": total
    }