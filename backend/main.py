from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from analyzer import analyze_repo
from scorer import calculate_score
from ai_feedback import generate_summary, generate_roadmap

# -----------------------------
# App initialization
# -----------------------------
app = FastAPI(
    title="GitGrade API",
    description="AI-powered GitHub Repository Analyzer",
    version="1.0.0"
)

# -----------------------------
# ✅ CORS CONFIGURATION (FIX)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (OK for hackathon/demo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request model
# -----------------------------
class RepoRequest(BaseModel):
    repo_url: str

# -----------------------------
# Root route (optional but helpful)
# -----------------------------
@app.get("/")
def root():
    return {"message": "GitGrade Backend is running"}

# -----------------------------
# Analyze repository endpoint
# -----------------------------
@app.post("/analyze")
def analyze(request: RepoRequest):
    try:
        repo_url = request.repo_url

        # Analyze GitHub repository
        analysis_data = analyze_repo(repo_url)

        # Calculate score
        score = calculate_score(analysis_data)

        # Generate AI feedback
        summary = generate_summary(analysis_data, score)
        roadmap = generate_roadmap(analysis_data)

        return {
            "score": score,
            "summary": summary,
            "roadmap": roadmap
        }

    except Exception as e:
        return {
            "score": 0,
            "summary": "Failed to analyze repository.",
            "roadmap": str(e)
        }
