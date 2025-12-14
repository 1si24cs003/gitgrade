from analyzer import analyze_repo
from scorer import calculate_score
from ai_feedback import generate_summary, generate_roadmap

try:
    repo_url = input("Enter GitHub Repository URL (https://github.com/user/repo): ")

    data = analyze_repo(repo_url)
    score = calculate_score(data)

    summary = generate_summary(data, score)
    roadmap = generate_roadmap(data)

    print("\n==============================")
    print(" GitGrade Repository Report")
    print("==============================")

    print(f"\nScore: {score} / 100")

    print("\nSummary:")
    print(summary)

    print("\nPersonalized Roadmap:")
    print(roadmap)

except ValueError as e:
    print("\n❌ Error:", e)

except Exception as e:
    print("\n❌ Something went wrong:", e)
