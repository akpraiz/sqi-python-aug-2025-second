question_bank = [
    {
        "question": "What is Photosynthesis?",
        "keywords": {
            "Photosynthesis": 2,
            "Light energy": 1,
            "Chemical energy": 1,
            "Chloroplasts": 2,
            "Chlorophyll": 1,
            "Carbon dioxide": 1,
            "Water": 1,
            "Glucose": 1,
            "Oxygen": 1,
            "ATP": 1
        }
    },
    {
        "question": "Explain Newton's First Law of Motion",
        "keywords": {
            "Inertia": 2,
            "Rest": 1,
            "Motion": 1,
            "Force": 2,
            "Object": 1,
            "Velocity": 1,
            "Balanced forces": 1,
            "Straight line": 1,
            "Constant speed": 1
        }
    },
    {
        "question": "What is the function of the heart in the human body?",
        "keywords": {
            "Heart": 2,
            "Blood": 2,
            "Circulation": 2,
            "Oxygen": 1,
            "Nutrients": 1,
            "Carbon dioxide": 1,
            "Pumping": 1,
            "Arteries": 1,
            "Veins": 1,
            "Body": 1
        }
    },
    {
        "question": "Describe the process of photosynthetic cellular respiration",
        "keywords": {
            "Cellular respiration": 2,
            "Glucose": 2,
            "ATP": 2,
            "Mitochondria": 2,
            "Oxygen": 1,
            "Carbon dioxide": 1,
            "Water": 1,
            "Energy": 1,
            "Aerobic": 1,
            "Anaerobic": 1
        }
    },
    {
        "question": "What is the significance of the French Revolution?",
        "keywords": {
            "French Revolution": 2,
            "1789": 1,
            "Monarchy": 1,
            "Equality": 1,
            "Liberty": 1,
            "Fraternity": 1,
            "Revolution": 1,
            "Bastille": 1,
            "Reforms": 1,
            "Democracy": 1
        }
    }
]


score = 0
max_score = 0
for question in question_bank:
    print(question["question"])
    choice = input("Enter your answer here: ").strip().lower()

    for keyword, weight in question["keywords"].items():
        max_score += weight
        if keyword.lower() in choice:
            score += weight


print(f"Total Score: {score} out of {max_score} points.")