# 🤖 AI Upskill Ecosystem

A groundbreaking **OpenClaw agent ecosystem** for teaching AI Agents and OpenClaw — personalized to each learner.

---

## The Vision

A complete learning system where:
1. An **AI Orchestrator** works with the human to understand their context
2. Generates a **personalized curriculum** based on their profile
3. Coordinates **module agents** for content delivery
4. Uses **spaced repetition** for retention
5. Includes **project-based learning** for practical skills
6. **Assesses** understanding through quizzes
7. Stores **student data** for multi-student support
8. Maintains **local knowledge base** with daily OpenClaw docs sync

---

## Quick Start

### Install

```bash
git clone https://github.com/boktoday/upskill-ecosystem.git ~/.openclaw/agents/upskill
```

### Run

Start a session with the **Orchestrator** agent to begin personalized learning.

---

## The Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI UPSKILL ECOSYSTEM                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────┐                                              │
│   │   Human     │                                              │
│   │  (Student)  │                                              │
│   └──────┬──────┘                                              │
│          │                                                       │
│          ▼                                                       │
│   ┌─────────────┐    ┌──────────────────┐                      │
│   │ Orchestrator│───►│Curriculum Generator│                     │
│   └──────┬──────┘    └──────────────────┘                      │
│          │                                                       │
│          ▼                                                       │
│   ┌─────────────────────────────────────────────┐              │
│   │           MODULE AGENTS (5)                 │              │
│   │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐  │              │
│   │  │ M1  │ │ M2  │ │ M3  │ │ M4  │ │ M5  │  │              │
│   │  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘  │              │
│   └─────────────────────────────────────────────┘              │
│          │                                                       │
│          ▼                                                       │
│   ┌─────────────────────────────────────────────┐              │
│   │         LEARNING SUPPORT                     │              │
│   │  ┌─────────────────┐ ┌──────────────────┐  │              │
│   │  │ Spaced          │ │ Project-Based    │  │              │
│   │  │ Repetition     │ │ Learning         │  │              │
│   │  └─────────────────┘ └──────────────────┘  │              │
│   └─────────────────────────────────────────────┘              │
│          │                                                       │
│          ▼                                                       │
│   ┌─────────────────────────────────────────────┐              │
│   │            ASSESSMENT                        │              │
│   │  ┌─────────────────────────────────────┐   │              │
│   │  │        Quiz Agent                    │   │              │
│   │  └─────────────────────────────────────┘   │              │
│   └─────────────────────────────────────────────┘              │
│                                                                 │
│   ┌─────────────────────────────────────────────┐              │
│   │            ARTIFACTS                        │              │
│   │  ┌─────────────────────────────────────┐   │              │
│   │  │   Canvas/Artifacts Builder          │   │              │
│   │  │   (Flashcards, Quizzes, Progress)  │   │              │
│   │  └─────────────────────────────────────┘   │              │
│   └─────────────────────────────────────────────┘              │
│                                                                 │
│   ┌─────────────────────────────────────────────┐              │
│   │            KNOWLEDGE                         │              │
│   │  ┌─────────────────────────────────────┐   │              │
│   │  │   OpenClaw Docs (Daily Sync)       │   │              │
│   │  └─────────────────────────────────────┘   │              │
│   └─────────────────────────────────────────────┘              │
│                                                                 │
│   ┌─────────────────────────────────────────────┐              │
│   │            STUDENTS                         │              │
│   │  ┌─────────────────────────────────────┐   │              │
│   │  │   Student Data (Multi-Student)      │   │              │
│   │  └─────────────────────────────────────┘   │              │
│   └─────────────────────────────────────────────┘              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## The Agents

### 🎯 Orchestrator
```
orchestrator/
├── SOUL.md     # Your AI learning guide
├── AGENTS.md   # Workflow
├── TOOLS.md    # Discovery questions
└── USER.md     # Student profile
```

### 📚 Modules (5)
```
modules/
├── module-1-agentic-revolution/     # 45 min
├── module-2-tech-stack/            # 45 min
├── module-3-openclaw/              # 60 min
├── module-4-strategy-ethics/      # 30 min
└── module-5-knowledge-check/       # Variable
```

### 🔄 Learning
```
learning/
├── spaced-repetition/    # Review scheduling
└── project-based/       # Hands-on projects
```

### 📝 Assessment
```
assessment/
└── quiz-agent/         # Knowledge checks
```

### 🎨 Artifacts
```
artifacts/
├── canvas-builder/     # Build visual tools
└── examples/           # Ready-to-use
    ├── flashcards.html
    ├── quiz.html
    └── progress.html
```

### 📖 Knowledge
```
knowledge/
└── openclow-docs/      # Local OpenClaw docs
    ├── scraper.py      # Downloads docs
    └── CRON_SETUP.md  # Daily sync config
```

### 👥 Students
```
students/               # Multi-student support
└── README.md          # Structure documentation
```

---

## The Curriculum (5 Modules)

### Module 1: The Agentic Revolution (45 min)
- AI Agent Framework definition
- Five Core Capabilities
- Chatbots vs Agents comparison

### Module 2: The Tech Stack of 2026 (45 min)
- LLMs, APIs, Webhooks
- Authentication
- Prompt Engineering

### Module 3: Deep Dive into OpenClaw (60 min)
- The 6 Pillars of OpenClaw
- Gateway, Skills, Agents
- Memory System (4 layers)

### Module 4: Strategy, Ethics, Application (30 min)
- Benefits & Challenges
- Practical Use Cases

### Module 5: Knowledge Check & Practice (Variable)
- Quiz questions
- Hands-on exercises

---

## Personalization

The system customizes based on:

| Factor | Adjusts |
|--------|----------|
| Current Role | Content priority |
| Future Goal | Examples |
| Business | Use cases |
| Learning Style | Delivery format |
| Time Available | Pacing |
| Prior Knowledge | Depth |

---

## Discovery Questions (8)

1. Current Role
2. Future Goal
3. Business/Side Hustle
4. Business Goals
5. Personal Context
6. Learning Style
7. Time Available
8. Prior Knowledge

---

## Learning Techniques

### Spaced Repetition
- Review at optimal intervals (1, 3, 7, 14, 30 days)
- Active recall over re-reading
- Quick refreshers

### Project-Based Learning
- Real-world exercises
- Portfolio building
- Progressive difficulty

### Adaptive Pacing
- Speed up familiar topics
- Slow down complex ones
- Skip if proficient

---

## Multi-Student Support

Each student gets their own data folder:
- Discovery answers
- Module progress
- Quiz scores
- Spaced repetition schedule
- Notes

---

## OpenClaw Knowledge Base

Daily sync with docs.openclaw.ai:

```bash
# Setup daily cron
crontab -e

# Add: Daily at 2am
0 2 * * * cd /path/to/knowledge/openclow-docs && python3 scraper.py
```

---

## Example Artifacts

### Flashcards
- Click to flip
- Review key terms

### Interactive Quiz
- Multiple choice
- Instant feedback
- Score tracking

### Progress Tracker
- Module completion
- Visual progress bars

---

## File Structure Summary

```
upskill-ecosystem/
├── README.md                    # This file
├── orchestrator/                # Main orchestrator
│   ├── SOUL.md
│   ├── AGENTS.md
│   ├── TOOLS.md
│   └── USER.md
├── modules/                     # 5 learning modules
│   ├── module-1-*/
│   ├── module-2-*/
│   ├── module-3-*/
│   ├── module-4-*/
│   └── module-5-*/
├── learning/                   # Learning techniques
│   ├── spaced-repetition/
│   └── project-based/
├── assessment/                 # Quiz & assessment
│   └── quiz-agent/
├── artifacts/                 # Visual learning tools
│   ├── canvas-builder/
│   └── examples/
├── knowledge/                 # OpenClaw docs
│   └── openclow-docs/
│       ├── scraper.py
│       └── CRON_SETUP.md
└── students/                 # Student data
    └── README.md
```

---

## Installation

```bash
# Clone the repo
git clone https://github.com/boktoday/upskill-ecosystem.git

# Copy to OpenClaw agents
cp -r upskill-ecosystem ~/.openclaw/agents/upskill

# Restart OpenClaw
openclaw gateway restart
```

---

## Usage

1. **Start with Orchestrator** — It will discover your context
2. **Receive personalized curriculum** — Generated based on your profile
3. **Learn module by module** — Each module agent delivers content
4. **Practice with projects** — Apply what you learn
5. **Review with spaced repetition** — Retain knowledge
6. **Take quizzes** — Test understanding

---

## Requirements

- **OpenClaw** — Core platform for running agents
- **Python 3.8+** — For knowledge scraper and utilities
  - Uses only Python standard library (no pip install needed)
- **Local OpenClaw docs** — For knowledge base (path configured in `knowledge/scraper.py`)

### Dependencies

This project is designed to work with **zero external Python packages**:

| Component | Dependencies |
|-----------|--------------|
| Orchestrator | OpenClaw only |
| Module Agents | OpenClaw only |
| Knowledge Scraper | Python 3.8+ stdlib only |
| Spaced Repetition | Python 3.8+ stdlib only |
| Artifact Generator | Python 3.8+ stdlib only |

All Python scripts use built-in modules: `os`, `json`, `hashlib`, `re`, `datetime`, `pathlib`, `typing`, `argparse`.

### Running the Knowledge Scraper

**Windows:**
```powershell
# Update OpenClaw docs in knowledge base
cd knowledge
py scraper.py

# Check scraper status
py scraper.py --status
```

**macOS/Linux:**
```bash
# Update OpenClaw docs in knowledge base
cd knowledge
python3 scraper.py

# Check scraper status
python3 scraper.py --status
```

The scraper reads from your local OpenClaw installation (at `C:\Users\Brendan\OneDrive\Downloads\ClawLauncher-Windows\myclaw\node_modules\openclaw\docs` on Windows) and outputs to `knowledge/openclaw_docs.json`.

**Note:** On first run, the scraper will process all 22 documentation files. Subsequent runs only process changed files.

---

## Contributing

This ecosystem is designed to be extended. To add:
- New modules: Add to `modules/`
- New learning techniques: Add to `learning/`
- New artifacts: Add to `artifacts/`

---

## Credits

Built with [OpenClaw](https://openclaw.ai/)

Curriculum based on the AI Upskill program.

---

**License**: MIT
