# AI Upskill Ecosystem 🤖

An **OpenClaw agent ecosystem** for teaching AI Agents and OpenClaw — personalized to each learner.

---

## The Vision

A groundbreaking learning system where:
1. An **AI Orchestrator** works with the human to understand their context
2. Generates a **personalized curriculum** based on their profile
3. Coordinates **module agents** for content delivery
4. Uses **spaced repetition** for retention
5. Includes **project-based learning** for practical skills
6. **Assesses** understanding through quizzes

---

## The Curriculum (5 Modules)

### Module 1: The Agentic Revolution (45 min)
- AI Agent Framework
- Five Core Capabilities
- Chatbots vs Agents

### Module 2: The Tech Stack of 2026 (45 min)
- LLMs, APIs, Webhooks
- Authentication
- Prompt Engineering

### Module 3: Deep Dive into OpenClaw (60 min)
- The 6 Pillars of OpenClaw
- Technical mastery
- Hands-on skills

### Module 4: Strategy, Ethics, Application (30 min)
- Benefits & Challenges
- Practical Use Cases
- Implementation

### Module 5: Knowledge Check & Practice (variable)
- Quiz questions
- Hands-on exercises

---

## The Agents

### 🎯 Orchestrator
```
orchestrator/
├── SOUL.md     # Your AI learning guide
├── AGENTS.md   # Workflow
├── TOOLS.md    # Discovery questions
└── USER.md     # Your profile & progress
```

### 📚 Modules (5)
```
modules/
├── module-1-agentic-revolution/
├── module-2-tech-stack/
├── module-3-openclaw/
├── module-4-strategy-ethics/
└── module-5-knowledge-check/
```

### 🔄 Learning Support
```
learning/
├── spaced-repetition/    # Review scheduling
└── project-based/      # Hands-on projects
```

### 📝 Assessment
```
assessment/
└── quiz-agent/         # Knowledge checks
```

### 📋 Generation
```
generation/
└── curriculum-generator/  # Creates personalized paths
```

---

## How It Works

```
┌─────────────┐
│   Human     │
│  (You)      │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Orchestrator│ ◄─── Discovers your context
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ Curriculum Generator│ ◄─── Creates personalized path
└──────┬─────────────┘
       │
       ▼
┌──────────────────────────────────┐
│  Module Agents (1-5)             │ ◄─── Deliver content
│  • spaced-repetition             │
│  • project-based                 │
│  • quiz-agent                    │
└──────────────────────────────────┘
       │
       ▼
┌─────────────┐
│   GitHub    │ ◄─── Push completed ecosystem
└─────────────┘
```

---

## Personalization

The system customizes based on:

| Factor | I Adjust |
|--------|----------|
| Current Role | Content priority |
| Future Goal | Examples |
| Business | Use cases |
| Learning Style | Delivery format |
| Time Available | Pacing |
| Prior Knowledge | Depth |

---

## Learning Techniques

### Spaced Repetition
- Review at optimal intervals (1, 3, 7, 14, 30 days)
- Active recall over re-reading

### Project-Based Learning
- Real-world exercises
- Portfolio building
- Progressive difficulty

### Adaptive Pacing
- Speed up familiar topics
- Slow down complex ones
- Skip if proficient

---

## Installation

```bash
git clone https://github.com/boktoday/upskill-ecosystem.git ~/.openclaw/agents/upskill
```

---

## Usage

1. **Start with the Orchestrator** — It will discover your context
2. **Receive your personalized curriculum** — Generated based on your profile
3. **Learn module by module** — Each module agent delivers content
4. **Practice with projects** — Apply what you learn
5. **Review with spaced repetition** — Retain knowledge

---

## The Curriculum Content

This ecosystem delivers the following AI Upskill curriculum:

### Module 1: The Agentic Revolution
- AI Agent Framework definition
- Five core capabilities
- Chatbots vs Agents comparison

### Module 2: The Tech Stack of 2026
- Components: LLMs, APIs, Webhooks, Auth
- Evolution timeline

### Module 3: Deep Dive into OpenClaw
- Gateway, Skills, Agents
- Memory System (4 layers)
- Tools and Channels

### Module 4: Strategy, Ethics, Application
- Benefits and challenges
- Practical use cases

### Module 5: Knowledge Check
- Quiz questions
- Hands-on exercises

---

## OpenClaw Format

Each agent follows the 4-file OpenClaw structure:
- **SOUL.md** — Identity
- **AGENTS.md** — Role
- **TOOLS.md** — Capabilities
- **USER.md** — Context

---

## Credits

Built with [OpenClaw](https://openclaw.ai/)

---

**License**: MIT
