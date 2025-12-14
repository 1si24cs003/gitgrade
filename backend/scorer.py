def calculate_score(data):
    score = 0

    score += 20 if data["has_readme"] else 5

    if data["commit_count"] >= 20:
        score += 25
    elif data["commit_count"] >= 5:
        score += 15
    else:
        score += 5

    score += 20 if data["language"] else 10
    score += 20

    return min(score, 100)
