# TOOLS.md — AI Learning Orchestrator

## Orchestrator Workflow Commands

This document describes the integration points for all the supporting systems.

---

## 1. Student Data Management

### Creating a New Student

```bash
# Create student directory and profile
mkdir students/student-001
# Then populate profile.json using SCHEMA.md structure
```

### Loading Student Profile

```
Path: students/[student-id]/profile.json
Schema: See students/SCHEMA.md
```

---

## 2. Module Agent Invocation

### How to Invoke a Module Agent

```
Agent ID: module-1-agentic-revolution
Agent ID: module-2-tech-stack
Agent ID: module-3-openclaw
Agent ID: module-4-strategy-ethics
Agent ID: module-5-knowledge-check
```

### Content Flow

1. Load student profile for customization context
2. Load module content from modules/[module-id]/CONTENT.md
3. Send to module agent with context
4. Receive completion + quiz results
5. Update profile with progress

---

## 3. Spaced Repetition Integration

### Adding Concepts to Review Queue

After each module, add key concepts:

```python
# From learning/spaced-repetition/scheduler.py
# Usage:
python scheduler.py add <student_id> <concept_id> <concept_name> <module_id>

# Example:
python scheduler.py add student-001 agent-framework "AI Agent Framework 5 Core Capabilities" module-1
```

### Checking Due Reviews

```bash
# What's due today
python scheduler.py due student-001

# Record a review result (quality: 0-5)
python scheduler.py record student-001 agent-framework-5-capabilities 4

# View summary
python scheduler.py summary student-001
```

### Review Schedule

| Review | Timing |
|--------|--------|
| 1st | 1 day after learning |
| 2nd | 3 days after |
| 3rd | 7 days after |
| 4th | 14 days after |
| 5th | 30 days after |

---

## 4. Artifact Generation

### Generating Learning Materials

```bash
# Generate all artifacts for a student
python artifacts/artifact_generator.py generate student-001

# Generate specific artifact types
python artifacts/artifact_generator.py flashcards student-001 module-1
python artifacts/artifact_generator.py quiz student-001 module-1
python artifacts/artifact_generator.py progress student-001
```

### Output Locations

```
artifacts/generated/
├── progress.html
├── flashcards-module-1.html
├── flashcards-module-2.html
├── flashcards-module-3.html
├── flashcards-module-4.html
├── quiz-module-1.html
├── quiz-module-2.html
├── quiz-module-3.html
└── quiz-module-4.html
```

---

## 5. Knowledge Base Scraper

### Syncing OpenClaw Docs

```bash
# Fetch OpenClaw documentation
python knowledge/scraper.py --docs

# Check sync status
python knowledge/scraper.py --status
```

### Output

```
knowledge/ai-news/
├── index.json
├── getting-started.md
├── installation.md
├── ...
```

---

## 6. Full Student Journey Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     ORCHESTRATOR WORKFLOW                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  START                                                            │
│    │                                                              │
│    ▼                                                              │
│  ┌─────────────────┐                                             │
│  │ Discovery Phase │ ──► Create students/[id]/profile.json      │
│  └────────┬────────┘                                            │
│           │                                                       │
│           ▼                                                       │
│  ┌─────────────────┐                                             │
│  │ Generate        │ ──► Customized curriculum                  │
│  │ Curriculum      │                                             │
│  └────────┬────────┘                                            │
│           │                                                       │
│           ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ FOR EACH MODULE:                                          │   │
│  │  1. Invoke module agent (modules/[id]/AGENTS.md)        │   │
│  │  2. Deliver CONTENT.md                                   │   │
│  │  3. Run exercises & quiz                                  │   │
│  │  4. Score quiz                                            │   │
│  │  5. Update progress in profile.json                      │   │
│  │  6. Add concepts to spaced repetition                    │   │
│  │  7. Generate artifacts (flashcards, quiz)                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│           │                                                       │
│           ▼                                                       │
│  ┌─────────────────┐                                             │
│  │ Spaced          │ ──► Daily: scheduler.py due [id]          │
│  │ Repetition     │ ──► Review prompts                        │
│  └────────┬────────┘                                            │
│           │                                                       │
│           ▼                                                       │
│  ┌─────────────────┐                                             │
│  │ All Complete    │ ──► Certificate / Next steps               │
│  └─────────────────┘                                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Key Files Reference

| Purpose | File |
|---------|------|
| Student Profile Schema | students/SCHEMA.md |
| Module 1 Content | modules/module-1-agentic-revolution/CONTENT.md |
| Spaced Repetition Logic | learning/spaced-repetition/scheduler.py |
| Artifact Generator | artifacts/artifact_generator.py |
| Knowledge Scraper | knowledge/scraper.py |

---

## 8. Integration Checklist

- [x] Student profile creation
- [x] Module content loading
- [x] Progress tracking
- [x] Spaced repetition scheduling
- [x] Artifact generation
- [x] Knowledge base syncing
- [ ] Cron jobs for daily reviews (see knowledge/openclow-docs/CRON_SETUP.md)

---

*Tools for orchestration.*
