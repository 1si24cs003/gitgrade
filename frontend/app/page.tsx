"use client";

import { useState } from "react";

export default function Home() {
  const [repo, setRepo] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const API_URL = process.env.NEXT_PUBLIC_API_URL!;

  const getLevel = (score: number) => {
    if (score >= 80) return "Advanced 🚀";
    if (score >= 50) return "Intermediate 👍";
    return "Beginner 🌱";
  };

  const analyzeRepo = async () => {
    if (!repo) return;

    setLoading(true);
    setResult(null);

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ repo_url: repo }),
      });

      if (!res.ok) {
        throw new Error("Failed to analyze repository");
      }

      const data = await res.json();
      setResult(data);
    } catch (err) {
      alert("Something went wrong while analyzing the repository");
    }

    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-100 to-slate-200 flex flex-col items-center justify-center p-6">
      <h1 className="text-5xl font-extrabold mb-8 text-gray-900">
        GitGrade 🚀
      </h1>

      <div className="bg-white p-6 rounded-2xl shadow-lg w-full max-w-xl">
        <input
          className="w-full border border-gray-300 p-3 rounded-lg mb-4 text-gray-900"
          placeholder="https://github.com/user/repo"
          value={repo}
          onChange={(e) => setRepo(e.target.value)}
        />

        <button
          onClick={analyzeRepo}
          disabled={loading}
          className="w-full bg-black text-white p-3 rounded-lg font-semibold hover:bg-gray-800"
        >
          {loading ? "Analyzing..." : "Analyze Repository"}
        </button>
      </div>

      {result && (
        <div className="bg-white mt-8 p-6 rounded-2xl shadow-lg w-full max-w-xl text-gray-900">
          <h2 className="text-3xl font-bold mb-2">
            Score: {result.score}/100
          </h2>

          <p className="text-lg font-semibold mb-4">
            Level: {getLevel(result.score)}
          </p>

          <div className="mb-4">
            <h3 className="text-xl font-bold mb-1">Summary</h3>
            <p className="leading-relaxed">{result.summary}</p>
          </div>

          <div>
            <h3 className="text-xl font-bold mb-1">Personalized Roadmap</h3>
            <pre className="whitespace-pre-wrap">{result.roadmap}</pre>
          </div>
        </div>
      )}
    </main>
  );
}
