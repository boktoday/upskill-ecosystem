#!/usr/bin/env python3
"""Generate all HTML artifacts"""
import random
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MODULES = {
    "module-1": {"title": "The Agentic Revolution", "duration": "45 min"},
    "module-2": {"title": "The Tech Stack of 2026", "duration": "45 min"},
    "module-3": {"title": "Deep Dive into OpenClaw", "duration": "60 min"},
    "module-4": {"title": "Strategy, Ethics, Application", "duration": "30 min"},
    "module-5": {"title": "Knowledge Check & Practice", "duration": "Variable"},
}

CONCEPTS = {
    "module-1": [
        ("AI Agent Framework", "The scaffolding that allows an LLM to perform tasks beyond generating text."),
        ("Autonomous Execution", "Ability to complete multi-step tasks without continuous human intervention."),
        ("Tool Use", "Calling external functions, APIs, and services to interact with the real world."),
        ("Memory & Context", "Maintaining state across interactions. Types: Working, Semantic, Episodic."),
        ("Decision Making", "Evaluating options and choosing actions based on goals and context."),
        ("Action Chaining", "Breaking complex tasks into sequences of smaller actions."),
        ("Chatbot vs Agent", "Chatbots are reactive, agents are proactive."),
        ("The Agent Loop", "Think → Decide → Act → Observe → repeat until goal is complete."),
    ],
    "module-2": [
        ("LLM", "Large Language Model - AI trained on vast text data."),
        ("API", "You ask, it answers. Pull-based communication."),
        ("Webhook", "It notifies you when something happens. Push-based."),
        ("Function Calling", "AI calling custom functions/APIs during generation."),
        ("Prompt Engineering", "Designing effective inputs to get desired outputs."),
        ("Context Window", "Amount of text an LLM can consider at once."),
        ("Temperature", "Controls randomness. Low = focused, High = creative."),
        ("Token", "Basic unit of text. ~4 characters = 1 token."),
    ],
    "module-3": [
        ("Gateway", "Central hub connecting agents to channels and tools."),
        ("Skill", "Pre-built capability package extending agent functionality."),
        ("Agent", "AI entity with defined role, tools, and behaviors."),
        ("Memory System", "4-layer system: Working, Short-term, Long-term, Semantic."),
        ("Channel", "Platform (Telegram, Discord, WhatsApp) where agents interact."),
        ("Jentic", "Security framework for managing credentials."),
        ("Cron Jobs", "Scheduled tasks running automatically at set times."),
        ("Model Routing", "Sending requests to different AI models."),
    ],
    "module-4": [
        ("AI Ethics", "Moral principles: fairness, transparency, privacy, safety."),
        ("Hallucination", "AI generating false information presented as fact."),
        ("Prompt Injection", "Malicious input to make AI ignore instructions."),
        ("Data Privacy", "Protecting user data. GDPR, consent, minimal collection."),
        ("Human Oversight", "Keeping humans in the loop for important decisions."),
        ("Practical Use Cases", "Real applications: customer service, content, data."),
    ],
    "module-5": [
        ("Mastery Quiz", "Assessment covering all modules."),
        ("Hands-On Exercises", "Practical tasks: creating prompts, mapping workflows."),
        ("SKILL.md Creation", "Creating skill definition files for OpenClaw."),
        ("Action Chain Mapping", "Designing AI agent task sequences."),
        ("Integration Design", "Planning AI connections to tools/workflows."),
    ],
}

QUIZZES = {
    "module-1": [
        ("What is the primary difference between a chatbot and an AI agent?", ["Chatbots are smarter", "Agents are proactive, chatbots are reactive", "Agents can't use tools", "Chatbots have better memory"], 1, "Agents take initiative, chatbots only respond."),
        ("Which is NOT a core capability of AI agents?", ["Autonomous Execution", "Tool Use", "Writing Novels", "Decision Making"], 2, "Core capabilities: Execution, Tool Use, Memory, Decision, Action Chaining."),
        ("What is Action Chaining?", ["Linking agents", "Breaking tasks into steps", "Connecting APIs", "Storing history"], 1, "Breaking complex goals into logical action sequences."),
        ("What is the Agent Loop?", ["A programming language", "Think → Decide → Act → Observe → repeat", "A type of chatbot", "A security protocol"], 1, "Continuous cycle until goal completion."),
        ("What stores facts and general knowledge?", ["Working Memory", "Episodic Memory", "Semantic Memory", "Procedural Memory"], 2, "Semantic Memory stores facts and world knowledge."),
    ],
    "module-2": [
        ("API vs Webhook?", ["APIs are faster", "APIs pull, Webhooks push", "Webhooks are secure", "No difference"], 1, "APIs = pull (you ask), Webhooks = push (they notify)."),
        ("What is Temperature?", ["Processing speed", "Server temperature", "Controls output randomness", "Model size"], 2, "Low = focused/deterministic, High = creative/varied."),
        ("What is a Token?", ["API password", "Cryptographic key", "~4 chars = 1 token", "AI model type"], 2, "Basic text unit. ~4 characters ≈ 1 token."),
        ("What is Function Calling?", ["Writing code", "Emergency calls", "AI calling APIs", "A chatbot type"], 2, "Ability for AI to invoke external tools/APIs."),
        ("What is Prompt Engineering?", ["Building AI", "Designing effective inputs", "Writing code", "Creating chatbots"], 1, "Crafting inputs to get better outputs from LLMs."),
    ],
    "module-3": [
        ("Which file defines agent persona?", ["SOUL.md", "AGENTS.md", "TOOLS.md", "USER.md"], 0, "SOUL.md defines identity, voice, and behaviors."),
        ("What are the 4 memory layers?", ["Input, Process, Output, Store", "Working, Short, Long, Semantic", "Fast, Medium, Slow, Archive", "User, Agent, Tool, Channel"], 1, "Working, Short-term, Long-term, Semantic."),
        ("What does the Gateway do?", ["Connects to internet", "Security, routing, cron", "Stores memories", "Creates agents"], 1, "Central hub handling security, sessions, and scheduling."),
        ("What is a Channel?", ["TV channel", "YouTube video", "Communication platform", "Memory type"], 2, "Platforms like Telegram, Discord, WhatsApp."),
        ("What is Jentic?", ["A chatbot", "A programming language", "Security for credentials", "An AI model"], 2, "Security framework managing credentials without exposure."),
    ],
    "module-4": [
        ("What is Hallucination?", ["AI dreaming", "AI generating false info", "Error message", "Security feature"], 1, "Plausible-sounding but false/fabricated information."),
        ("What is Prompt Injection?", ["Injecting code", "Malicious input to bypass instructions", "Improving prompts", "A chatbot"], 1, "Security threat trying to make AI ignore its instructions."),
        ("What is Human Oversight?", ["AI watching humans", "Humans in the loop for decisions", "Humans overseeing companies", "AI supervising humans"], 1, "Keeping humans involved in critical AI decisions."),
        ("Practical use cases include?", ["Gaming, Entertainment", "Customer service, Content, Data", "Cooking, Sports", "Fashion, Music"], 1, "Automating service, generating content, analyzing data."),
        ("Data Privacy is?", ["Making data bigger", "Protecting user data", "Storing all conversations", "Sharing publicly"], 1, "Protection through consent, minimal collection, GDPR."),
    ],
    "module-5": [
        ("What goes in SKILL.md?", ["Only the name", "Description, Templates, Resources, Steps", "Just code", "A list of users"], 1, "Include description, templates, resources, instructions."),
        ("When mapping Action Chains, start with?", ["Code to write", "Final goal, work backwards", "AI model", "Budget"], 1, "Start with final goal, identify steps backwards."),
        ("How handle complex IEP documents?", ["All at once", "Chunk into smaller steps", "Print it out", "Ignore it"], 1, "Break into smaller, actionable chunks."),
        ("Best hands-on exercise?", ["Just reading", "Creating real workflows", "Memorizing", "Watching videos"], 1, "Build actual solutions that solve real problems."),
        ("Design AI integration by?", ["Copying others", "Starting with the problem", "Most expensive tools", "Avoiding planning"], 1, "Understand the problem first, then design."),
    ],
}

def make_flashcards(module_id):
    m = MODULES[module_id]
    concepts = CONCEPTS[module_id]
    cards = ""
    for term, defn in concepts:
        cards += f'''
    <div class="card cursor-pointer w-full h-48 mb-4" onclick="this.classList.toggle('flipped')">
      <div class="card-inner relative w-full h-full">
        <div class="card-front absolute w-full h-full bg-gradient-to-br from-indigo-600 to-purple-600 rounded-xl p-6 flex items-center justify-center shadow-lg">
          <p class="text-2xl font-bold text-center">{term}</p>
        </div>
        <div class="card-back absolute w-full h-full bg-gradient-to-br from-green-600 to-teal-600 rounded-xl p-6 flex items-center justify-center">
          <p class="text-lg text-center">{defn}</p>
        </div>
      </div>
    </div>'''
    
    html = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flashcards - {m["title"]}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    .card {{ perspective: 1000px; }}
    .card-inner {{ transition: transform 0.6s; transform-style: preserve-3d; }}
    .card.flipped .card-inner {{ transform: rotateY(180deg); }}
    .card-front, .card-back {{ backface-visibility: hidden; }}
    .card-back {{ transform: rotateY(180deg); }}
  </style>
</head>
<body class="bg-gradient-to-br from-slate-900 via-slate-800 to-indigo-900 min-h-screen text-white p-8">
  <div class="max-w-2xl mx-auto">
    <div class="text-center mb-8">
      <h1 class="text-4xl font-bold mb-2">🧠 {m["title"]}</h1>
      <p class="text-slate-400">{m["duration"]} • Click cards to flip</p>
    </div>
    {cards}
    <div class="text-center mt-8">
      <a href="progress.html" class="px-6 py-3 bg-slate-700 rounded-lg hover:bg-slate-600">📊 Progress</a>
    </div>
  </div>
</body>
</html>'''
    return html

def make_quiz(module_id):
    m = MODULES[module_id]
    qs = QUIZZES[module_id]
    
    questions_html = ""
    for i, (q, opts, correct, exp) in enumerate(qs, 1):
        opts_html = ""
        for j, opt in enumerate(opts):
            opts_html += f'''
              <label class="opt flex items-center p-4 rounded-lg border-2 border-slate-600 hover:border-indigo-400 cursor-pointer mb-2 transition-all" data-correct="{correct}">
                <input type="radio" name="q{i}" value="{j}" class="hidden">
                <span class="w-10 h-10 rounded-full bg-slate-700 flex items-center justify-center mr-3 font-bold text-lg">{chr(65+j)}</span>
                <span class="opt-text">{opt}</span>
              </label>'''
        
        questions_html += f'''
      <div class="question mb-8 p-6 bg-slate-800 rounded-xl border border-slate-700" data-question="{i}">
        <p class="text-xl font-bold mb-4">Q{i}. {q}</p>
        <div class="options space-y-2">{opts_html}</div>
        <div class="feedback mt-4 p-4 rounded-lg hidden">
          <p class="fb-text font-bold"></p>
          <p class="exp-text mt-2 text-sm text-slate-300"></p>
        </div>
      </div>'''
    
    html = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz - {m["title"]}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    .opt {{ transition: all 0.2s; }}
    .opt.selected {{ border-color: #6366f1; background: rgba(99,102,241,0.1); }}
    .opt.correct {{ border-color: #22c55e; background: rgba(34,197,94,0.2); }}
    .opt.incorrect {{ border-color: #ef4444; background: rgba(239,68,68,0.2); }}
    .feedback.show {{ display: block !important; }}
  </style>
</head>
<body class="bg-gradient-to-br from-slate-900 via-slate-800 to-green-900 min-h-screen text-white p-8">
  <div class="max-w-3xl mx-auto">
    <div class="text-center mb-8">
      <h1 class="text-4xl font-bold mb-2">📝 {m["title"]}</h1>
      <p class="text-slate-400">Select answers • Instant feedback • See your score!</p>
    </div>
    
    <div class="fixed top-4 right-4 bg-slate-800 rounded-xl p-4 shadow-xl border border-slate-700 z-50">
      <p class="text-slate-400 text-sm text-center">Score</p>
      <p id="score" class="text-4xl font-bold text-green-400 text-center">0</p>
      <p class="text-slate-400 text-sm text-center">/ {len(qs)}</p>
    </div>
    
    <form id="quiz-form">{questions_html}
      <div class="text-center mt-8">
        <button type="submit" class="px-8 py-4 bg-gradient-to-r from-green-600 to-teal-600 rounded-xl font-bold text-lg shadow-lg hover:from-green-700 hover:to-teal-700">
          🎯 See Final Score
        </button>
      </div>
    </form>
    
    <div id="results" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50 p-4">
      <div class="bg-slate-800 rounded-2xl p-8 max-w-md w-full text-center border border-slate-700">
        <div id="results-icon" class="text-6xl mb-4">🎉</div>
        <h2 id="results-title" class="text-3xl font-bold mb-4">Great Job!</h2>
        <p id="results-message" class="text-slate-400 mb-6"></p>
        <p id="results-score" class="text-5xl font-bold text-green-400 mb-6"></p>
        <div class="space-y-3">
          <a href="progress.html" class="block w-full py-3 bg-indigo-600 rounded-lg hover:bg-indigo-700">📊 View Progress</a>
          <button onclick="document.getElementById('results').classList.add('hidden'); return false;" class="w-full py-3 bg-slate-700 rounded-lg hover:bg-slate-600">✕ Close</button>
        </div>
      </div>
    </div>
  </div>
  
  <script>
    let score = 0;
    const total = {len(qs)};
    
    document.querySelectorAll('.opt').forEach(opt => {{
      opt.addEventListener('click', function() {{
        const question = this.closest('.question');
        const allOpts = question.querySelectorAll('.opt');
        const fb = question.querySelector('.feedback');
        const correct = parseInt(this.dataset.correct);
        const selected = parseInt(this.querySelector('input').value);
        
        allOpts.forEach(x => {{
          x.classList.remove('selected', 'correct', 'incorrect');
          x.querySelector('input').checked = false;
        }});
        
        this.classList.add('selected');
        this.querySelector('input').checked = true;
        fb.classList.remove('hidden');
        
        const fbText = fb.querySelector('.fb-text');
        const expText = fb.querySelector('.exp-text');
        
        if (selected === correct) {{
          this.classList.add('correct');
          fbText.textContent = '✅ Correct!';
          fbText.className = 'fb-text font-bold text-green-400';
          fb.className = 'feedback mt-4 p-4 rounded-lg bg-green-900/30 show';
          score++;
          document.getElementById('score').textContent = score;
        }} else {{
          this.classList.add('incorrect');
          allOpts[correct].classList.add('correct');
          fbText.textContent = '❌ Incorrect';
          fbText.className = 'fb-text font-bold text-red-400';
          expText.textContent = '{exp}';
          fb.className = 'feedback mt-4 p-4 rounded-lg bg-red-900/30 show';
        }}
      }});
    }});
    
    document.getElementById('quiz-form').addEventListener('submit', function(e) {{
      e.preventDefault();
      const pct = Math.round((score / total) * 100);
      const icon = document.getElementById('results-icon');
      const title = document.getElementById('results-title');
      const msg = document.getElementById('results-message');
      const scoreEl = document.getElementById('results-score');
      
      scoreEl.textContent = score + '/' + total;
      
      if (pct >= 80) {{
        icon.textContent = '🏆';
        title.textContent = 'Excellent!';
        msg.textContent = "You mastered this module!";
      }} else if (pct >= 60) {{
        icon.textContent = '👍';
        title.textContent = 'Good Job!';
        msg.textContent = 'Review flashcards to strengthen understanding.';
      }} else if (pct >= 40) {{
        icon.textContent = '📚';
        title.textContent = 'Keep Learning!';
        msg.textContent = 'Review material and try again.';
      }} else {{
        icon.textContent = '💪';
        title.textContent = "Don't Give Up!";
        msg.textContent = 'Study flashcards first, then retry.';
      }}
      
      document.getElementById('results').classList.remove('hidden');
    }});
  </script>
</body>
</html>'''
    return html

def make_progress():
    cards = ""
    for mid, m in MODULES.items():
        cards += f'''
        <div class="p-5 bg-slate-800 rounded-xl border border-slate-700 mb-4">
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center">
              <span class="text-2xl mr-3">📚</span>
              <div>
                <h3 class="font-bold text-lg">{m["title"]}</h3>
                <p class="text-sm text-slate-400">{m["duration"]}</p>
              </div>
            </div>
            <span class="text-xl font-bold text-yellow-400">0%</span>
          </div>
          <div class="w-full bg-slate-700 rounded-full h-3 mb-3">
            <div class="bg-gradient-to-r from-slate-600 to-slate-700 h-3 rounded-full" style="width: 0%"></div>
          </div>
          <div class="flex gap-2">
            <a href="flashcards-{mid}.html" class="flex-1 text-center py-2 bg-indigo-600/30 hover:bg-indigo-600/50 rounded-lg text-sm font-medium transition-colors">🧠 Flashcards</a>
            <a href="quiz-{mid}.html" class="flex-1 text-center py-2 bg-green-600/30 hover:bg-green-600/50 rounded-lg text-sm font-medium transition-colors">📝 Quiz</a>
          </div>
        </div>'''
    
    return f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Progress</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-slate-900 via-slate-800 to-indigo-900 min-h-screen text-white p-8">
  <div class="max-w-3xl mx-auto">
    <div class="text-center mb-8">
      <h1 class="text-4xl font-bold mb-2">📊 Your Learning Progress</h1>
      <p class="text-slate-400">Track your AI Upskill journey</p>
    </div>
    
    <div class="bg-slate-800 rounded-2xl p-6 mb-8 border border-slate-700 text-center">
      <p class="text-slate-400 mb-2">Overall Progress</p>
      <p class="text-5xl font-bold text-indigo-400">0%</p>
      <p class="text-slate-400 mt-2">0 of 5 modules completed</p>
    </div>
    
    <h2 class="text-xl font-bold mb-4">Modules</h2>
    {cards}
    
    <div class="mt-8 p-5 bg-yellow-900/30 rounded-xl border border-yellow-600/50">
      <h3 class="font-bold text-yellow-400 mb-2">🔔 Spaced Repetition Tip</h3>
      <p class="text-slate-300 text-sm">Review flashcards at optimal intervals for best retention: <strong>Day 1 → Day 3 → Day 7 → Day 14</strong></p>
    </div>
  </div>
</body>
</html>'''

def generate_all():
    for mid in MODULES:
        flash_file = OUTPUT_DIR / f"flashcards-{mid}.html"
        flash_file.write_text(make_flashcards(mid))
        print(f"✅ {flash_file.name}")
        
        quiz_file = OUTPUT_DIR / f"quiz-{mid}.html"
        quiz_file.write_text(make_quiz(mid))
        print(f"✅ {quiz_file.name}")
    
    progress_file = OUTPUT_DIR / "progress.html"
    progress_file.write_text(make_progress())
    print(f"✅ progress.html")
    print(f"\n🎉 Generated {len(MODULES)*2 + 1} files!")

if __name__ == "__main__":
    generate_all()
