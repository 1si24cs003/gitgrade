🚀 GitGrade – AI-Powered GitHub Repository Analyzer

GitGrade is an intelligent web application that analyzes any public GitHub repository and converts it into a developer-friendly score, AI-generated summary, and personalized improvement roadmap.
It helps students understand how their code looks to recruiters and mentors.


🔍 Problem Statement

A GitHub repository is a developer’s real portfolio, but students often struggle to evaluate:
  -Code quality & structure
  -Documentation completeness
  -Commit consistency
  -Real-world readiness

GitGrade solves this by acting as an AI mentor, giving honest feedback and actionable steps based purely on repository data.

Introduction:https://www.canva.com/design/DAG7e-n6_n8/DnEHq8gF_PGHgYY4YpqoYA/view?utm_content=DAG7e-n6_n8&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he51a06a921

Presentation:https://www.canva.com/design/DAG7e2vm1lY/gVnJ1rruoEKuCOjfKW1P8Q/view?utm_content=DAG7e2vm1lY&utm_campaign=designshare&utm_medium=link&utm_source=viewer

✨ Key Features
  -🔗 Accepts any public GitHub repository URL
  -📊 Generates a Score (0–100) with skill level
  -🧠 AI-generated project summary
  -🛠️ Personalized improvement roadmap
  -⚡ Fast analysis using Groq LLaMA-3.1
  -🌐 Fully deployed frontend + backend


🧠 Evaluation Criteria

GitGrade evaluates repositories on:
  -Code quality & readability
  -Project structure & organization
  -Documentation (README) quality
  -Commit history & consistency
  -Test presence & maintainability
  -Real-world usefulness


🏷️ Sample Output

Input

-- https://github.com/octocat/Hello-World


Output

  Score: 75 / 100
  Level: Intermediate 👍
  
  Summary:
  Clean project structure with consistent commits, but lacks documentation and testing.
  
  Roadmap:
  • Add a detailed README  
  • Write unit tests  
  • Improve commit messages  
  • Add CI/CD pipeline  

🛠️ Tech Stack
Frontend
-Next.js (App Router)
-TypeScript
-Tailwind CSS
-Deployed on Vercel

Backend
-FastAPI (Python)
-GitHub REST API
-Groq LLaMA-3.1 (Free LLM)
-Deployed on Vercel

🌐 Live Demo

Frontend Website:
👉 https://gitgrade-five.vercel.app

Backend API (Swagger Docs):
👉 https://gitgrade-backend-v1.vercel.app/docs

🗂️ Project Structure
gitgrade/
├── backend/
│   ├── main.py
│   ├── analyzer.py
│   ├── scorer.py
│   ├── ai_feedback.py
│   ├── requirements.txt
│   └── vercel.json
│
├── frontend/
│   ├── app/
│   ├── globals.css
│   ├── package.json
│   └── next.config.js
│
├── .gitignore
└── README.md

⚙️ How It Works

User enters a GitHub repository URL
1.Backend fetches repository metadata using GitHub API
2.Repository is scored using rule-based logic
3.AI gnerates summary & roadmap using Groq LLaMA-3.1
4.Results are displayed in a clean UI

🧪 Local Setup (Optional)
Backend
  cd backend
  pip install -r requirements.txt
  uvicorn main:app --reload


Create .env:
  GROQ_API_KEY=your_groq_api_key

Frontend
  cd frontend
  npm install
  npm run dev


Create .env.local:
  NEXT_PUBLIC_API_URL=https://gitgrade-backend-v1.vercel.app/analyze

🎥 Demo Flow (For Judges)
1.Open the frontend link
2.Paste any public GitHub repository
3.Click Analyze Repository
4.View score, summary, and roadmap

🎯 Hackathon Alignment

  ✔ AI + Code Analysis
  ✔ Real-world developer profiling
  ✔ Honest, actionable feedback
  ✔ Fully working deployment
  ✔ Open to future enhancements

🚀 Future Enhancements
  -Language-specific scoring models
  -CI/CD detection
  -Code complexity analysis
  -GitHub OAuth for private repos
  -PDF report export

👨‍💻 Author - Abdullah Saad Sharief

📌 Conclusion

GitGrade acts as a mirror for developers, reflecting strengths and weaknesses of a GitHub repository and guiding them toward becoming better engineers.

⭐ If you like this project, don’t forget to star the repository!

