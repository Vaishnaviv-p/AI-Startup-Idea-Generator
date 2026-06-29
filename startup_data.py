import random

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

startup_data = {

    "healthcare": {

    "ideas": [
        "AI Medical Diagnosis Platform",
        "AI Hospital Management System",
        "AI Drug Discovery Assistant",
        "AI Remote Patient Monitoring",
        "AI Medical Imaging Analyzer",
        "AI Mental Health Companion",
        "AI Nutrition Planner",
        "AI Surgery Assistance Platform",
        "AI Health Insurance Assistant",
        "AI Elder Care Monitoring"
    ],

    "customers": [
        "Hospitals",
        "Doctors",
        "Clinics",
        "Patients",
        "Healthcare Startups",
        "Diagnostic Centers",
        "Insurance Companies",
        "Government Health Departments",
        "Medical Colleges",
        "Pharmacies"
    ],

    "revenue_models": [
        "Subscription",
        "Enterprise Licensing",
        "Hospital SaaS",
        "Pay Per Consultation",
        "API Licensing",
        "Commission",
        "Freemium",
        "Usage Based Pricing",
        "Annual Contracts",
        "B2B Licensing"
    ],

    "descriptions": [
        "Uses AI to detect diseases at an early stage.",
        "Automates complete hospital operations.",
        "Accelerates drug discovery using machine learning.",
        "Monitors patient health remotely in real time.",
        "Analyzes X-rays, CT scans and MRIs with AI.",
        "Provides AI-powered mental health support.",
        "Generates personalized nutrition plans.",
        "Assists surgeons using computer vision.",
        "Simplifies health insurance claim processing.",
        "Monitors elderly people using wearable AI."
    ],

    "target_market": "Global",

    "investment": "₹20 Lakhs",

    "development_time": "8 Months",

    "market_potential": "Very High",

    "category": "Healthcare AI",

    "competitors": [
        "Practo",
        "Apollo 24/7",
        "Tata 1mg",
        "HealthifyMe",
        "Cure.fit",
        "Microsoft Healthcare",
        "Google Health",
        "Ada Health",
        "Babylon Health",
        "Teladoc"
    ],

    "business_tips": [
        "Follow HIPAA and healthcare regulations.",
        "Protect patient data using encryption.",
        "Partner with hospitals.",
        "Focus on clinical validation.",
        "Build trust with doctors.",
        "Offer multilingual support.",
        "Integrate wearable devices.",
        "Provide cloud-based dashboards.",
        "Support telemedicine.",
        "Continuously improve AI accuracy."
    ]

},

    "education": {

    "ideas": [
        "AI Personalized Learning Platform",
        "AI Virtual Tutor",
        "AI Exam Generator",
        "AI Homework Assistant",
        "AI Classroom Analytics",
        "AI Career Guidance Platform",
        "AI Language Learning Coach",
        "AI Skill Assessment System",
        "AI College Admission Assistant",
        "AI Teacher Productivity Suite"
    ],

    "customers": [
        "Students",
        "Teachers",
        "Schools",
        "Universities",
        "Parents",
        "Coaching Institutes",
        "EdTech Companies",
        "Corporate Trainers",
        "Government Education Boards",
        "Online Learning Platforms"
    ],

    "revenue_models": [
        "Subscription",
        "Freemium",
        "Institution Licensing",
        "Annual Plans",
        "Course Marketplace",
        "Advertising",
        "Corporate Licensing",
        "Pay Per Student",
        "Premium Membership",
        "Certification Fees"
    ],

    "descriptions": [
        "Creates personalized study plans using AI.",
        "Provides 24/7 AI tutoring.",
        "Automatically generates question papers.",
        "Solves homework with detailed explanations.",
        "Tracks student performance and engagement.",
        "Suggests career paths based on student skills.",
        "Helps users learn new languages faster.",
        "Evaluates skills using AI assessments.",
        "Guides students through college admissions.",
        "Automates lesson planning for teachers."
    ],

    "target_market": "Global",

    "investment": "₹10 Lakhs",

    "development_time": "6 Months",

    "market_potential": "Very High",

    "category": "EdTech AI",

    "competitors": [
        "BYJU'S",
        "Unacademy",
        "Coursera",
        "Udemy",
        "Khan Academy",
        "Duolingo",
        "Chegg",
        "Quizizz",
        "Google Classroom",
        "Microsoft Education"
    ],

    "business_tips": [
        "Keep the interface simple.",
        "Support mobile learning.",
        "Gamify the learning process.",
        "Provide personalized recommendations.",
        "Use adaptive learning algorithms.",
        "Partner with schools.",
        "Offer certificates.",
        "Track learning progress.",
        "Provide multilingual content.",
        "Regularly update educational material."
    ]

},
    "finance": {

    "ideas": [
        "AI Investment Advisor",
        "AI Fraud Detection Platform",
        "AI Budget Planner",
        "AI Personal Finance Coach",
        "AI Credit Score Analyzer",
        "AI Loan Approval Assistant",
        "AI Tax Filing Assistant",
        "AI Expense Tracker",
        "AI Wealth Management Platform",
        "AI Financial Forecasting Tool"
    ],

    "customers": [
        "Banks",
        "Investors",
        "Businesses",
        "Financial Advisors",
        "Individuals",
        "Insurance Companies",
        "Startups",
        "NBFCs",
        "Government Agencies",
        "Accounting Firms"
    ],

    "revenue_models": [
        "Subscription",
        "Enterprise Licensing",
        "Commission",
        "Freemium",
        "Premium Membership",
        "API Licensing",
        "Transaction Fees",
        "Consulting",
        "Pay Per Report",
        "Annual Plans"
    ],

    "descriptions": [
        "Provides AI-powered investment recommendations.",
        "Detects fraudulent financial transactions instantly.",
        "Creates smart monthly budgets.",
        "Acts as an AI financial advisor.",
        "Predicts and improves customer credit scores.",
        "Automates loan eligibility analysis.",
        "Simplifies tax filing using AI.",
        "Tracks expenses automatically.",
        "Helps users grow wealth intelligently.",
        "Predicts future financial performance using AI."
    ],

    "target_market": "Global",

    "investment": "₹25 Lakhs",

    "development_time": "9 Months",

    "market_potential": "Very High",

    "category": "FinTech AI",

    "competitors": [
        "Zerodha",
        "Groww",
        "Paytm Money",
        "INDmoney",
        "Cred",
        "Razorpay",
        "PhonePe",
        "Stripe",
        "Wealthfront",
        "Robinhood"
    ],

    "business_tips": [
        "Ensure bank-grade security.",
        "Comply with financial regulations.",
        "Build customer trust.",
        "Provide transparent pricing.",
        "Use strong encryption.",
        "Offer real-time analytics.",
        "Support multiple payment gateways.",
        "Automate reporting.",
        "Focus on user experience.",
        "Continuously improve fraud detection."
    ]

},
    "agriculture": {

    "ideas": [
        "AI Crop Monitoring",
        "AI Farm Assistant",
        "AI Weather Prediction",
        "AI Smart Irrigation"
    ],

    "customers": [
        "Farmers",
        "Agricultural Companies",
        "Food Producers",
        "Cooperatives"
    ],

    "revenue_models": [
        "Subscription",
        "Government Partnership",
        "Pay-per-use"
    ],

    "descriptions": [
        "Monitors crop health using AI.",
        "Predicts weather for farming.",
        "Optimizes irrigation systems.",
        "Improves agricultural productivity."
    ],

    "target_market": "Rural & Global",
    "investment": "₹12 Lakhs",
    "development_time": "7 Months",
    "market_potential": "Medium",
    "category": "AgriTech",
    "competitors": [
    "DeHaat",
    "CropIn",
    "AgroStar"
],

    "business_tips": [
        "Collaborate with local farmers.",
        "Use weather data effectively.",
        "Keep the app simple to use.",
        "Focus on affordable solutions."
    ]

},
    "default": {
    "ideas": [
        "AI Automation Tool",
        "AI Virtual Assistant",
        "Predictive Analytics Platform",
        "Recommendation Engine",
        "Business Intelligence Dashboard",
        "AI Chatbot Platform",
        "Workflow Automation System",
        "Smart Data Analysis Tool",
        "AI Scheduling Assistant",
        "Document Processing AI"
    ],

    "customers": [
        "Startups",
        "Small Businesses",
        "Companies",
        "Professionals"
    ],

    "revenue_models": [
        "Subscription",
        "Freemium",
        "Advertising"
    ],

    "descriptions": [
        "Automates business operations using AI.",
        "Provides intelligent recommendations.",
        "Improves productivity using AI.",
        "Connects businesses with AI solutions."
    ],

    "target_market": "Global",
    "investment": "₹10 Lakhs",
    "development_time": "6 Months",
    "market_potential": "High",
    "category": "Artificial Intelligence",
    "competitors": [
    "OpenAI",
    "Google",
    "Microsoft"
],

    "business_tips": [
        "Validate your idea before scaling.",
        "Build an MVP first.",
        "Listen to customer feedback.",
        "Invest in digital marketing."
    ]

}
}