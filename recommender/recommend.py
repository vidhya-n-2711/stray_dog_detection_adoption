from models import Dog

def score_match(dog: Dog, prefs: dict):
    score = 0
    total = 0
    if not prefs:
        return 0

    if "size" in prefs and prefs["size"]:
        total += 1
        if dog.size.lower() == prefs["size"].lower():
            score += 1

    if "age" in prefs and prefs["age"]:
        total += 1
        if dog.age.lower() == prefs["age"].lower():
            score += 1

    if "health" in prefs and prefs["health"]:
        total += 1
        if dog.health.lower() == prefs["health"].lower():
            score += 1

    return (score / total) if total > 0 else 0

def recommend_dogs(db_session, prefs: dict, limit=10):
    dogs = db_session.query(Dog).filter(Dog.adopted == False).all()
    scored = [(score_match(dog, prefs), dog) for dog in dogs]
    scored.sort(key=lambda x: x[0], reverse=True)
    return [dog for score, dog in scored[:limit]]
