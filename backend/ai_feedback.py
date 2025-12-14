import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_summary(data, score):
    prompt = f"""
You are an AI code reviewer.

Analyze this GitHub repository and write a short honest summary (2–3 lines).

Repository: {data['name']}
Language: {data['language']}
Commits: {data['commit_count']}
README Present: {data['has_readme']}
Score: {score}/100
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return completion.choices[0].message.content.strip()


def generate_roadmap(data):
    prompt = f"""
You are an AI coding mentor.

Create a personalized improvement roadmap in bullet points.

Language: {data['language']}
Commits: {data['commit_count']}
README Present: {data['has_readme']}
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return completion.choices[0].message.content.strip()
