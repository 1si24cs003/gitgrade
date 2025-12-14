from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from analyzer import analyze_repo
from scorer import calculate_score
from ai_feedback import generate_summary, generate_roadmap

# ✅ CREATE APP FIRST
app = FastAPI(title="GitGrade API")

# ✅ ADD CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ REQUEST MODEL
class RepoRequest(BaseModel):
    repo_url: str

# ✅ ROUTE (AFTER app IS DEFINED)
@app.post("/analyze")
def analyze(request: RepoRequest):
    try:
        data = analyze_repo(request.repo_url)
        score = calculate_score(data)

        summary = generate_summary(data, score)
        roadmap = generate_roadmap(data)

        return {
            "score": score,
            "summary": summary,
            "roadmap": roadmap
        }

    except Exception as e:
        # Never crash the API
        return {
            "score": 0,
            "summary": "Failed to analyze repository.",
            "roadmap": str(e)
        }
