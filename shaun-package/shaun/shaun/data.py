from typing import List, Dict, Optional

ABOUT = {
    "name": "Shaun",
    "tagline": "Building data-driven systems • SWE + Analytics + Fullstack",
    "note": "Degree in Data Science. Everything else learned through projects, curiosity, and shipping.",
    "location": "India",
}

# Skills are 0-10 for simple bar displays
SKILLS = {
    "Python": 9,
    "Data Analysis": 8,
    "SQL": 7,
    "Fullstack (FE/BE)": 7,
    "Design (UI/UX, Graphics)": 7,
    "Business (SaaS, Product)": 8,
    "Management (Ops, Supply)": 8,
    "Automation": 8,
    "AI/ML": 7,
}

TOOLS = [
    "Power BI", "Excel", "SPSS", "SQL", "YOLO (no-train XAI)", "FastAPI/Flask",
    "GDevelop", "SMTP", "Git/GitHub", "Figma", "After Effects (learning)"
]

PROJECTS = [
    {
        "name": "XAI Object Classifier",
        "desc": "Explainable object classification using YOLO without model training; focuses on reasoning and interpretability.",
        "tags": ["AI", "XAI", "Computer Vision"],
        "year": "2022",
        "link": "",
    },
    {
        "name": "CSR Scholarship Aggregator (SaaS)",
        "desc": "Aggregates scholarship opportunities with filters and dashboards.",
        "tags": ["SaaS", "Ed-tech", "Analytics"],
        "year": "2020",
        "link": "",
    },
    {
        "name": "Inventory Analysis",
        "desc": "Data app to track inventory KPIs and patterns.",
        "tags": ["Analytics", "Ops"],
        "year": "2021",
        "link": "",
    },
    {
        "name": "Market-Basket Analysis",
        "desc": "Association rules to boost cross-sell and product placement.",
        "tags": ["Analytics", "Retail"],
        "year": "2021",
        "link": "",
    },
    {
        "name": "Multi-Modal Assistant",
        "desc": "Assistant combining modalities; foundation for debate-style collaboration.",
        "tags": ["AI", "Multimodal"],
        "year": "2024",
        "link": "",
    },
    {
        "name": "Debate AI Whiteboard",
        "desc": "Dot-grid whiteboard UI; call multiple model APIs using @mentions to collaborate and debate on tasks.",
        "tags": ["AI", "Tooling"],
        "year": "2025",
        "link": "",
    },
    {
        "name": "Social Interactivity Automation Bot",
        "desc": "Automates social interactions for engagement and outreach.",
        "tags": ["Automation"],
        "year": "2023",
        "link": "",
    },
    {
        "name": "Bulk Email Sender (SMTP Free Tier)",
        "desc": "Low-cost bulk mailer with templating and rate limiting.",
        "tags": ["Automation"],
        "year": "2023",
        "link": "",
    },
    {
        "name": "27th — Detective Board Game",
        "desc": "Immersive, psychologically rich tabletop mystery with multi-truth endings.",
        "tags": ["Game", "Design", "Narrative"],
        "year": "2025",
        "link": "",
    },
]

TIMELINE = [
    ("2019", "Started Data Science degree"),
    ("2020", "Built CSR Scholarship Aggregator SaaS"),
    ("2021", "Inventory & Market-Basket analytics apps"),
    ("2022", "XAI object classifier w/ YOLO (no train)"),
    ("2023", "Automation bots: social & SMTP bulk email"),
    ("2024", "Multi-Modal assistant experiments; deeper design work"),
    ("2025", "Debate AI whiteboard • Board game '27th'"),
]

# Minimal, humble snapshot. This is not advice.
INVESTMENTS = {
    "summary": "Personal learning journey; small-scale, conservative bias.",
    "dividend_stocks": 2,
    "index_sips": 1,
    "penny_stocks": "a few (experimental)",
    "realized_status": "modest positive",
    "disclaimer": "Not investment advice. Shared for transparency and craft ethos.",
}

HOBBIES = {
    "sports": ["Basketball"],
    "gaming": True,
    "music_albums": [
        "Kendrick Lamar — Mr. Morale & The Big Steppers",
        "NF — HOPE",
        "Eminem — The Eminem Show",
        "J. Cole — The Off-Season",
        "Drake — Dark Lane Demo Tapes",
        "Central Cee — Wild West",
        "Travis Scott — UTOPIA",
        "Playboi Carti — Whole Lotta Red",
    ],
    "movies": ["Wolf of Wall Street", "Goodfellas", "A Bronx Tale", "Bolt", "Soul"],
    "cars_bikes": ["Mazda MX-5", "AMG", "Yamaha R15", "Royal Enfield Bullet 350", "Harley Davidson 48/Sportster"],
}

ASCII = {
    "mafia": "     ____             _  __ _           \n    / ___| ___  _ __(_)/ _(_) ___ _ __ \n   | |  _ / _ \| '__| | |_| |/ _ \ '__|\n   | |_| | (_) | |  | |  _| |  __/ |   \n    \____|\___/|_|  |_|_| |_|\___|_|   ",
    "poster_box": "+--------------------------------------+\n|                                      |\n|           SHAUN • PORTFOLIO          |\n|       data • swe • fullstack         |\n|                                      |\n+--------------------------------------+",
}
