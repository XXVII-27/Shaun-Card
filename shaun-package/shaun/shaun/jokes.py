import random

JOKES = [
    "I put 'pip install shaun' on a business card. The recruiter smiled. The terminal applauded.",
    "Kindness is free. Shipping projects is optional — I pick both.",
    "My CI pipeline runs on espresso and late-night curiosity.",
    "I don’t chase titles. I merge pull requests.",
]

QUOTES = [
    "Respect is louder when whispered.",
    "Move like a gentleman, ship like a machine.",
    "Understate. Overdeliver.",
]

def random_joke() -> str:
    return random.choice(JOKES)

def random_quote() -> str:
    return random.choice(QUOTES)
