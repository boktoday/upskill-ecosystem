#!/usr/bin/env python3
"""
Artifact Generator
==================
Generates personalized learning materials (flashcards, quizzes, progress views)
based on student progress and connects to the orchestrator workflow.

Output: artifacts/generated/ directory with HTML files
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

# Configuration
BASE_DIR = Path(__file__).parent.parent
STUDENTS_DIR = BASE_DIR / "students"
OUTPUT_DIR = BASE_DIR / "artifacts" / "generated"

# Module content for generating flashcards
MODULE_CONCEPTS = {
    "module-1": {
        "title": "The Agentic Revolution",
        "concepts": [
            {"id": "agent-framework", "term": "AI Agent Framework", "definition": "The scaffolding that allows an LLM to perform tasks beyond generating text — providing tools, memory, and action capabilities."},
            {"id": "autonomous-execution", "term": "Autonomous Execution", "definition": "The ability to complete multi-step tasks without continuous human intervention."},
            {"id": "tool-use", "term": "Tool Use", "definition": "Calling external functions, APIs, and services to interact with the real world."},
            {"id": "memory-context", "term": "Memory & Context", "definition": "Maintaining state across interactions and learning from past experiences. Types: Working, Semantic, Episodic."},
            {"id": "decision-making", "term": "Decision Making", "definition": "Evaluating options and choosing actions based on goals, constraints, and context."},
            {"id": "action-chaining", "term": "Action Chaining", "definition": "Breaking complex tasks into sequences of smaller actions that achieve a larger goal."},
            {"id": "chatbot-vs-agent", "term": "Chatbot vs Agent", "definition": "Chatbots are reactive (wait for prompt), agents are proactive (take initiative)."},
            {"id": "agent-loop", "term": "The Agent Loop", "definition": "Think → Decide → Act → Observe → repeat until goal is complete."}
        ]
    },
    "module-2": {
        "title": "The Tech Stack of 2026",
        "concepts": [
            {"id": "llm", "term": "LLM (Large Language Model)", "definition": "AI model trained on vast text data, capable of understanding and generating human-like text."},
            {"id": "api", "term": "API (Application Programming Interface)", "definition": "A set of rules allowing software applications to communicate. You ask, it answers."},
            {"id": "webhook", "term": "Webhook", "definition": "HTTP callback that notifies you when something happens. Like a doorbell - alerts you to events."},
            {"id": "function-calling", "term": "Function Calling", "definition": "Ability for AI to call custom functions/APIs during generation to perform actions."},
            {"id": "prompt-engineering", "term": "Prompt Engineering", "definition": "The practice of designing effective inputs to get desired outputs from LLMs."},
            {"id": "context-window", "term": "Context Window", "definition": "The amount of text an LLM can consider at once when generating responses."},
            {"id": "temperature", "term": "Temperature", "definition": "Controls randomness in LLM output. Low = focused/deterministic, High = creative/varied."},
            {"id": "token", "term": "Token", "definition": "Basic unit of text a model reads/writes. ~4 characters = 1 token."}
        ]
    },
    "module-3": {
        "title": "Deep Dive into OpenClaw",
        "concepts": [
            {"id": "gateway", "term": "OpenClaw Gateway", "definition": "Central hub that connects agents to channels and tools."},
            {"id": "skill", "term": "Skill", "definition": "Pre-built capability package that extends agent functionality."},
            {"id": "agent", "term": "Agent", "definition": "AI entity with defined role, tools, and behaviors using OpenClaw structure."},
            {"id": "memory", "term": "Memory System", "definition": "4-layer system: Working, Short-term, Long-term, Semantic."},
            {"id": "channel", "term": "Channel", "definition": "Communication platform (Telegram, Discord, WhatsApp) where agents interact."},
            {"id": "jentic", "term": "Jentic", "definition": "Security framework for managing credentials without exposing them to agents."},
            {"id": "cron", "term": "Cron Jobs", "definition": "Scheduled tasks that run automatically at set times."},
            {"id": "model-routing", "term": "Model Routing", "definition": "Sending requests to different AI models based on task complexity."}
        ]
    },
    "module-4": {
        "title": "Strategy, Ethics, Application",
        "concepts": [
            {"id": "ai-ethics", "term": "AI Ethics", "definition": "Moral principles for AI development and use: fairness, transparency, privacy, safety."},
            {"id": "hallucination", "term": "Hallucination", "definition": "When AI generates false or nonsensical information presented as fact."},
            {"id": "prompt-injection", "term": "Prompt Injection", "definition": "Malicious input designed to make AI ignore instructions or leak information."},
            {"id": "data-privacy", "term": "Data Privacy", "definition": "Protecting user data when using AI. GDPR, consent, minimal data collection."},
            {"id": "human-oversight", "term": "Human Oversight", "definition": "Keeping humans in the loop for important decisions AI makes."},
            {"id": "use-cases", "term": "Practical Use Cases", "definition": "Real applications: customer service, content creation, data analysis, automation."}
        ]
    }
}


def get_student_progress(student_id: str) -> Optional[dict]:
    """Load student progress data."""
    profile_path = STUDENTS_DIR / student_id / "profile.json"
    if profile_path.exists():
        with open(profile_path) as f:
            return json.load(f)
    return None


def generate_flashcards(student_id: str, module_id: str) -> str:
    """Generate flashcard HTML for a specific module."""
    if module_id not in MODULE_CONCEPTS:
        return f"<p>Unknown module: {module_id}</p>"
    
    module = MODULE_CONCEPTS[module_id]
    concepts = module["concepts"]
    
    cards_html = ""
    for concept in concepts:
        cards_html += f"""
    <div class="card cursor-pointer w-full h-48 mb-4" onclick="this.classList.toggle('flipped')">
      <div class="card-inner relative w-full h-full">
        <div class="card-front absolute w-full h-full bg-indigo-600 rounded-xl p-6 flex items-center justify-center">
          <p class="text-xl text-center font-bold">{concept['term']}</p>
        </div>
        <div class="card-back absolute w-full h-full bg-green-600 rounded-xl p-6 flex items-center justify-center">
          <p class="text-sm text-center">{concept['definition']}</p>
        </div>
      </div>
    </div>
"""
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flashcards - {module['title']}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    .card {{ perspective: 1000px; }}
    .card-inner {{ transition: transform 0.6s; transform-style: preserve-3d; }}
    .card.flipped .card-inner {{ transform: rotateY(180deg); }}
    .card-front, .card-back {{ backface-visibility: hidden; }}
    .card-back {{ transform: rotateY(180deg); }}
  </style>
</head>
<body class="bg-slate-900 min-h-screen text-white p-8">
  <div class="max-w-2xl mx-auto">
    <h1 class="text-3xl font-bold mb-2 text-center">🧠 {module['title']}</h1>
    <p class="text-slate-400 text-center mb-8">Click cards to flip • Review daily for spaced repetition!</p>
    
    {cards_html}
    
    <div class="mt-8 text-center">
      <a href="progress.html?student={student_id}&module={module_id}" class="text-indigo-400 hover:underline">View Progress →</a>
    </div>
  </div>
</body>
</html>"""


def generate_quiz(student_id: str, module_id: str) -> str:
    """Generate interactive quiz HTML for a module."""
    if module_id not in MODULE_CONCEPTS:
        return f"<p>Unknown module: {module_id}</p>"
    
    module = MODULE_CONCEPTS[module_id]
    concepts = module["concepts"]
    
    # Generate questions from concepts
    questions_html = ""
    for i, concept in enumerate(concepts[:5], 1):  # Limit to 5 questions
        questions_html += f"""
      <div class="question mb-6 p-4 bg-slate-800 rounded-lg" data-correct="{i}">
        <p class="font-bold mb-3">{i}. What is {concept['term']}?</p>
        <div class="options space-y-2">
          <label class="flex items-center p-2 rounded hover:bg-slate-700 cursor-pointer">
            <input type="radio" name="q{i}" value="wrong" class="mr-2">
            <span>A completely different concept</span>
          </label>
          <label class="flex items-center p-2 rounded hover:bg-slate-700 cursor-pointer">
            <input type="radio" name="q{i}" value="correct" class="mr-2">
            <span>{concept['definition'][:100]}...</span>
          </label>
          <label class="flex items-center p-2 rounded hover:bg-slate-700 cursor-pointer">
            <input type="radio" name="q{i}" value="wrong2" class="mr-2">
            <span>Another alternative definition</span>
          </label>
        </div>
      </div>
"""
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz - {module['title']}</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 min-h-screen text-white p-8">
  <div class="max-w-2xl mx-auto">
    <h1 class="text-3xl font-bold mb-2 text-center">📝 Quiz: {module['title']}</h1>
    <p class="text-slate-400 text-center mb-8">Test your knowledge</p>
    
    <form id="quiz-form">
      {questions_html}
      
      <button type="submit" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3 px-4 rounded-lg">
        Submit Answers
      </button>
    </form>
    
    <div id="result" class="hidden mt-6 p-4 rounded-lg text-center">
    </div>
  </div>
  
  <script>
    document.getElementById('quiz-form').addEventListener('submit', function(e) {{
      e.preventDefault();
      
      let score = 0;
      const total = {len(concepts[:5])};
      
      for (let i = 1; i <= total; i++) {{
        const selected = document.querySelector('input[name="q' + i + '"]:checked');
        if (selected && selected.value === 'correct') {{
          score++;
        }}
      }}
      
      const result = document.getElementById('result');
      result.classList.remove('hidden', 'bg-red-600', 'bg-green-600');
      
      if (score >= total * 0.7) {{
        result.classList.add('bg-green-600');
        result.innerHTML = '<h3 class="text-2xl font-bold">🎉 Great job! Score: ' + score + '/' + total + '</h3>';
      }} else {{
        result.classList.add('bg-red-600');
        result.innerHTML = '<h3 class="text-2xl font-bold">Keep practicing! Score: ' + score + '/' + total + '</h3>';
      }}
    }});
  </script>
</body>
</html>"""


def generate_progress(student_id: str) -> str:
    """Generate progress visualization HTML."""
    progress = get_student_progress(student_id)
    
    if not progress:
        return """<!DOCTYPE html>
<html><head><script src="https://cdn.tailwindcss.com"></script></head>
<body class="bg-slate-900 min-h-screen text-white p-8">
<h1>No progress data found</h1></body></html>"""
    
    # Build progress data
    modules = progress.get("progress", {}).get("modules", {})
    
    module_items = ""
    for module_id, data in modules.items():
        status = data.get("status", "not-started")
        score = data.get("quizScore", 0)
        
        status_icon = {"completed": "✅", "in-progress": "⏳", "not-started": "⬜"}.get(status, "⬜")
        
        module_items += f"""
        <div class="flex items-center justify-between p-3 bg-slate-800 rounded mb-2">
          <span>{status_icon} {module_id}</span>
          <span class="text-yellow-400">{score}%</span>
        </div>
"""
    
    # Calculate overall progress
    total_modules = 5
    completed = sum(1 for m in modules.values() if m.get("status") == "completed")
    progress_pct = int((completed / total_modules) * 100)
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Progress</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 min-h-screen text-white p-8">
  <div class="max-w-2xl mx-auto">
    <h1 class="text-3xl font-bold mb-8 text-center">📊 Your Learning Progress</h1>
    
    <!-- Overall Progress -->
    <div class="mb-8">
      <div class="flex justify-between mb-2">
        <span>Overall Progress</span>
        <span>{progress_pct}%</span>
      </div>
      <div class="w-full bg-slate-700 rounded-full h-4">
        <div class="bg-gradient-to-r from-indigo-500 to-purple-500 h-4 rounded-full" style="width: {progress_pct}%"></div>
      </div>
    </div>
    
    <!-- Module Progress -->
    <h2 class="text-xl font-bold mb-4">Modules</h2>
    {module_items}
    
    <!-- Quick Actions -->
    <div class="mt-8 grid grid-cols-2 gap-4">
      <a href="flashcards.html?student={student_id}" class="block text-center bg-indigo-600 hover:bg-indigo-700 py-3 rounded-lg">
        🧠 Flashcards
      </a>
      <a href="quiz.html?student={student_id}" class="block text-center bg-green-600 hover:bg-green-700 py-3 rounded-lg">
        📝 Take Quiz
      </a>
    </div>
  </div>
</body>
</html>"""


def generate_all_artifacts(student_id: str, module_ids: list[str] = None) -> dict:
    """
    Generate all artifacts for a student.
    
    Returns dict of generated files.
    """
    if module_ids is None:
        module_ids = list(MODULE_CONCEPTS.keys())
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    generated = {}
    
    # Generate progress page (always needed)
    progress_file = OUTPUT_DIR / "progress.html"
    progress_file.write_text(generate_progress(student_id), encoding='utf-8')
    generated["progress"] = str(progress_file)
    
    # Generate flashcards and quizzes for each module
    for module_id in module_ids:
        if module_id not in MODULE_CONCEPTS:
            continue
        
        # Flashcards
        flash_file = OUTPUT_DIR / f"flashcards-{module_id}.html"
        flash_file.write_text(generate_flashcards(student_id, module_id), encoding='utf-8')
        generated[f"flashcards-{module_id}"] = str(flash_file)
        
        # Quiz
        quiz_file = OUTPUT_DIR / f"quiz-{module_id}.html"
        quiz_file.write_text(generate_quiz(student_id, module_id), encoding='utf-8')
        generated[f"quiz-{module_id}"] = str(quiz_file)
    
    return generated


def list_available_artifacts() -> dict:
    """List all available artifact types."""
    return {
        "flashcards": list(MODULE_CONCEPTS.keys()),
        "quizzes": list(MODULE_CONCEPTS.keys()),
        "progress": ["progress.html"]
    }


# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("""
Artifact Generator
==================
Usage:
  python artifact_generator.py list                              - List available artifacts
  python artifact_generator.py flashcards <student_id> <module> - Generate flashcards
  python artifact_generator.py quiz <student_id> <module>       - Generate quiz
  python artifact_generator.py progress <student_id>            - Generate progress view
  python artifact_generator.py generate <student_id>            - Generate all artifacts
        """)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "list":
        artifacts = list_available_artifacts()
        print("📦 Available Artifacts:")
        for artifact_type, modules in artifacts.items():
            print(f"  {artifact_type}: {modules}")
    
    elif command == "flashcards" and len(sys.argv) >= 4:
        student_id = sys.argv[2]
        module_id = sys.argv[3]
        content = generate_flashcards(student_id, module_id)
        output_file = OUTPUT_DIR / f"flashcards-{module_id}.html"
        output_file.write_text(content, encoding='utf-8')
        print(f"✅ Generated: {output_file}")
    
    elif command == "quiz" and len(sys.argv) >= 4:
        student_id = sys.argv[2]
        module_id = sys.argv[3]
        content = generate_quiz(student_id, module_id)
        output_file = OUTPUT_DIR / f"quiz-{module_id}.html"
        output_file.write_text(content, encoding='utf-8')
        print(f"✅ Generated: {output_file}")
    
    elif command == "progress" and len(sys.argv) >= 3:
        student_id = sys.argv[2]
        content = generate_progress(student_id)
        output_file = OUTPUT_DIR / "progress.html"
        output_file.write_text(content, encoding='utf-8')
        print(f"✅ Generated: {output_file}")
    
    elif command == "generate" and len(sys.argv) >= 3:
        student_id = sys.argv[2]
        generated = generate_all_artifacts(student_id)
        print(f"[OK] Generated {len(generated)} artifacts:")
    for name, path in generated.items():
        print(f"  * {name}: {path}")
    
    else:
        print("Invalid command. Run without args for usage.")
