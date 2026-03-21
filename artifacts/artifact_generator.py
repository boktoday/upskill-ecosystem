#!/usr/bin/env python3
"""
Artifact Generator V2
====================
Generates interactive learning materials for all 5 modules.
Features:
- Flashcards with flip animation
- Interactive quizzes with instant feedback
- Progress tracking
"""

import json
import random
from pathlib import Path

# Module content
MODULE_CONCEPTS = {
    "module-1": {"title": "The Agentic Revolution", "duration": "45 min", "concepts": [
        {"term": "AI Agent Framework", "definition": "The scaffolding that allows an LLM to perform tasks beyond generating text."},
        {"term": "Autonomous Execution", "definition": "Ability to complete multi-step tasks without continuous human intervention."},
        {"term": "Tool Use", "definition": "Calling external functions, APIs, and services to interact with the real world."},
        {"term": "Memory & Context", "definition": "Maintaining state across interactions. Types: Working, Semantic, Episodic."},
        {"term": "Decision Making", "definition": "Evaluating options and choosing actions based on goals and context."},
        {"term": "Action Chaining", "definition": "Breaking complex tasks into sequences of smaller actions."},
        {"term": "Chatbot vs Agent", "definition": "Chatbots are reactive, agents are proactive."},
        {"term": "The Agent Loop", "definition": "Think → Decide → Act → Observe → repeat until goal is complete."}
    ]},
    "module-2": {"title": "The Tech Stack of 2026", "duration": "45 min", "concepts": [
        {"term": "LLM", "definition": "Large Language Model - AI trained on vast text data."},
        {"term": "API", "definition": "You ask, it answers. Pull-based communication."},
        {"term": "Webhook", "definition": "It notifies you when something happens. Push-based."},
        {"term": "Function Calling", "definition": "AI calling custom functions/APIs during generation."},
        {"term": "Prompt Engineering", "definition": "Designing effective inputs to get desired outputs."},
        {"term": "Context Window", "definition": "Amount of text an LLM can consider at once."},
        {"term": "Temperature", "definition": "Controls randomness. Low = focused, High = creative."},
        {"term": "Token", "definition": "Basic unit of text. ~4 characters = 1 token."}
    ]},
    "module-3": {"title": "Deep Dive into OpenClaw", "duration": "60 min", "concepts": [
        {"term": "Gateway", "definition": "Central hub connecting agents to channels and tools."},
        {"term": "Skill", "definition": "Pre-built capability package extending agent functionality."},
        {"term": "Agent", "definition": "AI entity with defined role, tools, and behaviors."},
        {"term": "Memory System", "definition": "4-layer system: Working, Short-term, Long-term, Semantic."},
        {"term": "Channel", "definition": "Platform (Telegram, Discord, WhatsApp) where agents interact."},
        {"term": "Jentic", "definition": "Security framework for managing credentials."},
        {"term": "Cron Jobs", "definition": "Scheduled tasks running automatically at set times."},
        {"term": "Model Routing", "definition": "Sending requests to different AI models."}
    ]},
    "module-4": {"title": "Strategy, Ethics, Application", "duration": "30 min", "concepts": [
        {"term": "AI Ethics", "definition": "Moral principles: fairness, transparency, privacy, safety."},
        {"term": "Hallucination", "definition": "AI generating false information presented as fact."},
        {"term": "Prompt Injection", "definition": "Malicious input to make AI ignore instructions."},
        {"term": "Data Privacy", "definition": "Protecting user data. GDPR, consent, minimal collection."},
        {"term": "Human Oversight", "definition": "Keeping humans in the loop for important decisions."},
        {"term": "Practical Use Cases", "definition": "Real applications: customer service, content, data."}
    ]},
    "module-5": {"title": "Knowledge Check & Practice", "duration": "Variable", "concepts": [
        {"term": "Mastery Quiz", "definition": "Assessment covering all modules."},
        {"term": "Hands-On Exercises", "definition": "Practical tasks: creating prompts, mapping workflows."},
        {"term": "SKILL.md Creation", "definition": "Creating skill definition files for OpenClaw."},
        {"term": "Action Chain Mapping", "definition": "Designing AI agent task sequences."},
        {"term": "Integration Design", "definition": "Planning AI connections to tools/workflows."}
    ]}
}

# Quiz questions
QUIZ_QUESTIONS = {
    "module-1": [
        {"q": "What is the primary difference between a chatbot and an AI agent?", "o": ["Chatbots are smarter", "Agents are proactive, chatbots are reactive", "Agents can't use tools", "Chatbots have better memory"], "a": 1, "e": "Agents take initiative, chatbots only respond."},
        {"q": "Which is NOT a core capability of AI agents?", "o": ["Autonomous Execution", "Tool Use", "Writing Novels", "Decision Making"], "a": 2, "e": "Core capabilities are: Execution, Tool Use, Memory, Decision, Action Chaining."},
        {"q": "What is Action Chaining?", "o": ["Linking agents", "Breaking tasks into steps", "Connecting APIs", "Storing history"], "a": 1, "e": "Breaking complex goals into logical action sequences."},
        {"q": "What is the Agent Loop?", "o": ["A programming language", "Think → Decide → Act → Observe → repeat", "A type of chatbot", "A security protocol"], "a": 1, "e": "Continuous cycle until goal completion."},
        {"q": "What stores facts and general knowledge?", "o": ["Working Memory", "Episodic Memory", "Semantic Memory", "Procedural Memory"], "a": 2, "e": "Semantic Memory stores facts and world knowledge."}
    ],
    "module-2": [
        {"q": "API vs Webhook?", "o": ["APIs are faster", "APIs pull, Webhooks push", "Webhooks are secure", "No difference"], "a": 1, "e": "APIs = pull (you ask), Webhooks = push (they notify)."},
        {"q": "What is Temperature?", "o": ["Processing speed", "Server temperature", "Controls output randomness", "Model size"], "a": 2, "e": "Low = focused/deterministic, High = creative/varied."},
        {"q": "What is a Token?", "o": ["API password", "Cryptographic key", "~4 chars = 1 token", "AI model type"], "a": 2, "e": "Basic text unit. ~4 characters ≈ 1 token."},
        {"q": "What is Function Calling?", "o": ["Writing code", "Emergency calls", "AI calling APIs", "A chatbot type"], "a": 2, "e": "Ability for AI to invoke external tools/APIs."},
        {"q": "What is Prompt Engineering?", "o": ["Building AI", "Designing effective inputs", "Writing code", "Creating chatbots"], "a": 1, "e": "Crafting inputs to get better outputs from LLMs."}
    ],
    "module-3": [
        {"q": "Which file defines agent persona?", "o": ["SOUL.md", "AGENTS.md", "TOOLS.md", "USER.md"], "a": 0, "e": "SOUL.md defines identity, voice, and behaviors."},
        {"q": "What are the 4 memory layers?", "o": ["Input, Process, Output, Store", "Working, Short, Long, Semantic", "Fast, Medium, Slow, Archive", "User, Agent, Tool, Channel"], "a": 1, "e": "Working, Short-term, Long-term, Semantic."},
        {"q": "What does the Gateway do?", "o": ["Connects to internet", "Security, routing, cron", "Stores memories", "Creates agents"], "a": 1, "e": "Central hub handling security, sessions, and scheduling."},
        {"q": "What is a Channel?", "o": ["TV channel", "YouTube video", "Communication platform", "Memory type"], "a": 2, "e": "Platforms like Telegram, Discord, WhatsApp."},
        {"q": "What is Jentic?", "o": ["A chatbot", "A programming language", "Security for credentials", "An AI model"], "a": 2, "e": "Security framework managing credentials without exposure."}
    ],
    "module-4": [
        {"q": "What is Hallucination?", "o": ["AI dreaming", "AI generating false info", "Error message", "Security feature"], "a": 1, "e": "Plausible-sounding but false/fabricated information."},
        {"q": "What is Prompt Injection?", "o": ["Injecting code", "Malicious input to bypass instructions", "Improving prompts", "A chatbot"], "a": 1, "e": "Security threat trying to make AI ignore its instructions."},
        {"q": "What is Human Oversight?", "o": ["AI watching humans", "Humans in the loop for important decisions", "Humans overseeing companies", "AI supervising humans"], "a": 1, "e": "Keeping humans involved in critical AI decisions."},
        {"q": "Practical use cases include?", "o": ["Gaming, Entertainment", "Customer service, Content, Data analysis", "Cooking, Sports", "Fashion, Music"], "a": 1, "e": "Automating service, generating content, analyzing data."},
        {"q": "Data Privacy is?", "o": ["Making data bigger", "Protecting user data", "Storing all conversations", "Sharing publicly"], "a": 1, "e": "Protection through consent, minimal collection, GDPR."}
    ],
    "module-5": [
        {"q": "What goes in SKILL.md?", "o": ["Only the name", "Description, Templates, Resources, Steps", "Just code", "A list of users"], "a": 1, "e": "Include description, templates, resources, instructions."},
        {"q": "When mapping Action Chains, start with?", "o": ["Code to write", "Final goal, work backwards", "AI model", "Budget"], "a": 1, "e": "Start with final goal, identify steps backwards."},
        {"q": "How handle complex IEP documents?", "o": ["All at once", "Chunk into smaller steps", "Print it out", "Ignore it"], "a": 1, "e": "Break into smaller, actionable chunks."},
        {"q": "Best hands-on exercise?", "o": ["Just reading", "Creating real workflows", "Memorizing", "Watching videos"], "a": 1, "e": "Build actual solutions that solve real problems."},
        {"q": "Design AI integration by?", "o": ["Copying others", "Starting with the problem", "Most expensive tools", "Avoiding planning"], "a": 1, "e": "Understand the problem first, then design."}
    ]
}

OUTPUT_DIR = Path(__file__).parent / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def gen_flashcards(module_id):
    m = MODULE_CONCEPTS.get(module_id)
    if not m: return "<p>Unknown module</p>"
    cards = ""
    for c in m["concepts"]:
        cards += f'''
    <div class="card cursor-pointer w-full h-48 mb-4" onclick="this.classList.toggle('flipped')">
      <div class="card-inner relative w-full h-full">
        <div class="card-front absolute w-full h-full bg-gradient-to-br from-indigo-600 to-purple-600 rounded-xl p-6 flex items-center justify-center shadow-lg">
          <p class="text-2xl font-bold text-center">{c["term"]}</p>
        </div>
        <div class="card-back absolute w-full h-full bg-gradient-to-br from-green-600 to-teal-600 rounded-xl p-6 flex items-center justify-center">
          <p class="text-lg text-center">{c["definition"]}</p>
        </div>
      </div>
    </div>'''
    return f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Flashcards - {m["title"]}</title><script src="https://cdn.tailwindcss.com"></script>
<style>.card{{perspective:1000px}}.card-inner{{transition:transform .6s;transform-style:preserve-3d}}.card.flipped .card-inner{{transform:rotateY(180deg)}}.card-front,.card-back{{backface-visibility:hidden}}.card-back{{transform:rotateY(180deg)}}</style>
</head><body class="bg-gradient-to-br from-slate-900 via-slate-800 to-indigo-900 min-h-screen text-white p-8">
<div class="max-w-2xl mx-auto text-center mb-8">
<h1 class="text-4xl font-bold mb-2">🧠 {m["title"]}</h1>
<p class="text-slate-400">{m["duration"]} • Click cards to flip</p></div>
<div class="max-w-2xl mx-auto">{cards}</div>
<div class="text-center mt-8"><a href="progress.html" class="px-6 py-3 bg-slate-700 rounded-lg">📊 Progress</a></div>
</body></html>'''

def gen_quiz(module_id):
    qs = QUIZ_QUESTIONS.get(module_id)
    m = MODULE_CONCEPTS.get(module_id, {"title": module_id})
    if not qs: return "<p>No quiz available</p>"
    
    html = ""
    for i, q in enumerate(qs, 1):
        opts = ""
        for j, o in enumerate(q["o"]):
            opts += f'<label class="opt flex items-center p-3 rounded-lg border-2 border-slate-600 hover:border-indigo-400 cursor-pointer mb-2" data-a="{q["a"]}"><input type="radio" name="q{i}" value="{j}" class="hidden"><span class="w-8 h-8 rounded-full bg-slate-700 flex items-center justify-center mr-3 font-bold">{chr(65+j)}</span>{o}</label>'
        html += f'<div class="q mb-6 p-6 bg-slate-800 rounded-xl border border-slate-700"><p class="text-lg font-bold mb-4">Q{i}. {q["q"]}</p><div class="opts space-y-2">{opts}</div><div class="fb mt-4 p-4 rounded-lg hidden"><p class="fb-txt font-bold"></p><p class="exp mt-2 text-sm text-slate-300"></p></div></div>'
    
    return f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Quiz - {m["title"]}</title><script src="https://cdn.tailwindcss.com"></script>
<style>.opt.correct{{border-color:#22c55e;background:rgba(34,197,94,.2)}}.opt.incorrect{{border-color:#ef4444;background:rgba(239,68,68,.2)}}.opt.selected{{border-color:#6366f1;background:rgba(99,102,241,.1)}}.fb.show{{display:block!important}}</style>
</head><body class="bg-gradient-to-br from-slate-900 via-slate-800 to-green-900 min-h-screen text-white p-8">
<div class="max-w-3xl mx-auto"><div class="text-center mb-8"><h1 class="text-4xl font-bold mb-2">📝 {m["title"]}</h1><p class="text-slate-400">Instant feedback on each answer!</p></div>
<div class="fixed top-4 right-4 bg-slate-800 rounded-xl p-4 border border-slate-700"><p class="text-slate-400 text-sm">Score</p><p id="s" class="text-3xl font-bold text-green-400">0</p><p class="text-slate-400 text-sm">/ {len(qs)}</p></div>
<form id="quiz">{html}<div class="text-center mt-8"><button type="submit" class="px-8 py-4 bg-gradient-to-r from-green-600 to-teal-600 rounded-xl font-bold text-lg shadow-lg">🎯 See Results</button></div></form>
<div id="results" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50 p-4"><div class="bg-slate-800 rounded-2xl p-8 max-w-md w-full text-center border border-slate-700"><div id="icon" class="text-6xl mb-4">🎉</div><h2 id="title" class="text-3xl font-bold mb-4">Great Job!</h2><p id="msg" class="text-slate-400 mb-6"></p><p id="score" class="text-5xl font-bold text-green-400 mb-6"></p><a href="progress.html" class="block py-3 bg-indigo-600 rounded-lg mb-2">📊 Progress</a><button onclick="document.getElementById('results').classList.add('hidden')" class="w-full py-3 bg-slate-700 rounded-lg">✕ Close</button></div></div>
</div><script>
let score=0;const qCount={len(qs)};
document.querySelectorAll('.opt').forEach(o=>o.addEventListener('click',function(){{
const p=this.closest('.q');const fb=p.querySelector('.fb');const correct=parseInt(this.dataset.a);const sel=parseInt(this.querySelector('input').value);
p.querySelectorAll('.opt').forEach(x=>{{x.classList.remove('selected','correct','incorrect');x.querySelector('input').checked=false}});
this.classList.add('selected');this.querySelector('input').checked=true;fb.classList.remove('hidden');
if(sel===correct){{this.classList.add('correct');fb.querySelector('.fb-txt').textContent='✅ Correct!';fb.querySelector('.fb-txt').className='fb-txt font-bold text-green-400';fb.className='fb mt-4 p-4 rounded-lg bg-green-900/30 show';score++;document.getElementById('s').textContent=score}}
else{{this.classList.add('incorrect');p.querySelectorAll('.opt')[correct].classList.add('correct');fb.querySelector('.fb-txt').textContent='❌ Incorrect';fb.querySelector('.fb-txt').className='fb-txt font-bold text-red-400';fb.querySelector('.exp').textContent='{chr(123)}0}.exp';fb.className='fb mt-4 p-4 rounded-lg bg-red-900/30 show'}}}}));
document.getElementById('quiz').addEventListener('submit',function(e){{e.preventDefault();const pct=Math.round((score/qCount)*100);
document.getElementById('score').textContent=score+'/'+qCount;
if(pct>=80){{document.getElementById('icon').textContent='🏆';document.getElementById('title').textContent='Excellent!';document.getElementById('msg').textContent="You mastered this module!"}}
else if(pct>=60){{document.getElementById('icon').textContent='👍';document.getElementById('title').textContent='Good Job!';document.getElementById('msg').textContent='Review flashcards to strengthen understanding.'}}
else if(pct>=40){{document.getElementById('icon').textContent='📚';document.getElementById('title').textContent='Keep Learning!';document.getElementById('msg').textContent='Review material and try again.'}}
else{{document.getElementById('icon').textContent='💪';document.getElementById('title').textContent="Don't Give Up!";document.getElementById('msg').textContent='Study flashcards first, then retry.'}}
document.getElementById('results').classList.remove('hidden')}});
</script></body></html>'''

def gen_progress():
    cards = ""
    for mid, m in MODULE_CONCEPTS.items():
        cards += f'''
        <div class="p-4 bg-slate-800 rounded-xl border border-slate-700 mb-4">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xl">📚</span>
            <span class="text-yellow-400 font-bold">0%</span>
          </div>
          <h3 class="font-bold mb-1">{m["title"]}</h3>
          <p class="text-sm text-slate-400 mb-3">{m["duration"]}</p>
          <div class="flex gap-2">
            <a href="flashcards-{mid}.html" class="flex-1 text-center py-2 bg-indigo-600/30 hover:bg-indigo-600/50 rounded-lg text-sm">🧠 Flashcards</a>
            <a href="quiz-{mid}.html" class="flex-1 text-center py-2 bg-green-600/30 hover:bg-green-600/50 rounded-lg text-sm">📝 Quiz</a>
          </div>
        </div>'''
    
    return f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Your Progress</title><script src="https://cdn.tailwindcss.com"></script>
</head><body class="bg-gradient-to-br from-slate-900 via-slate-800 to-indigo-900 min-h-screen text-white p-8">
<div class="max-w-3xl mx-auto"><div class="text-center mb-8"><h1 class="text-4xl font-bold mb-2">📊 Your Learning Progress</h1><p class="text-slate-400">Track your AI Upskill journey</p></div>
<div class="bg-slate-800 rounded-2xl p-6 mb-8 border border-slate-700 text-center"><h2 class="text-xl mb-2">Overall</h2><p class="text-4xl font-bold text-indigo-400">0%</p></div>
<h2 class="text-xl font-bold mb-4">Modules</h2>{cards}
<div class="mt-8 p-4 bg-yellow-900/30 rounded-xl border border-yellow-600/50"><h3 class="font-bold text-yellow-400 mb-2">🔔 Spaced Repetition</h3><p class="text-slate-300 text-sm">Review at: Day 1, Day 3, Day 7, Day 14 for best retention!</p></div>
</div></body></html>'''

def generate_all():
    for mid in MODULE_CONCEPTS:
        (OUTPUT_DIR / f"flashcards-{mid}.html").write_text(gen_flashcards(mid))
        (OUTPUT_DIR / f"quiz-{mid}.html").write_text(gen_quiz(mid))
        print(f"✅ Generated {mid}")
    (OUTPUT_DIR / "progress.html").write_text(gen_progress())
    print("✅ Generated progress.html")

if __name__ == "__main__":
    generate_all()
