# Module 3: Building Agents 🏗️

*A comprehensive guide to creating, configuring, and managing OpenClaw agents*

---

## Overview

In this module, you'll learn how to build intelligent agents from scratch using OpenClaw's file-based agent system. By the end, you'll understand the complete agent lifecycle—from creating configuration files to spawning working agents that can interact with tools and maintain memory.

**Duration:** ~45 minutes  
**Prerequisites:** Module 1 & 2 (understanding of AI agents and OpenClaw basics)

---

## Table of Contents

1. [The Agent File Structure](#31-the-agent-file-structure)
2. [Spawning and Managing Agents](#32-spawning-and-managing-agents)
3. [Tool Use and Integration](#33-tool-use-and-integration)
4. [Memory and Context Management](#34-memory-and-context-management)
5. [Hands-On Exercises](#hands-on-exercises)
6. [Discussion Questions](#discussion-questions)
7. [Quiz](#quiz)

---

## 3.1 The Agent File Structure

OpenClaw agents are defined by a collection of markdown files that together define who the agent is, what it knows, what tools it can access, and how it remembers things. This is OpenClaw's declarative approach to agent configuration.

### The Four Core Files

Every OpenClaw agent requires these four configuration files:

```
agent-workspace/
├── SOUL.md      # Agent's personality and behavior
├── USER.md      # Context about the user
├── TOOLS.md     # Available tools and configurations
└── MEMORY.md    # Agent's persistent memory
```

### SOUL.md — The Agent's Personality

**Purpose:** Defines the agent's core identity, personality, values, and behavioral guidelines.

The SOUL.md is the most important file—it shapes how the agent thinks and responds. It contains:

- **Core Truths:** Fundamental beliefs and guiding principles
- **Boundaries:** What the agent should and shouldn't do
- **Vibe:** The overall tone and communication style
- **Continuity:** How the agent persists between sessions

#### Example SOUL.md

```markdown
# SOUL.md — Research Assistant

## Core Truths

**Be thorough but concise.** Prioritize accuracy over speed. When unsure, say so instead of guessing.

**Have opinions.** You're allowed to disagree with the user if you have good reasoning.

**Be resourceful.** Try to figure things out yourself before asking for help.

## Boundaries

- Never make up facts—always verify
- When in doubt, ask before acting
- Respect privacy—don't share what you learn about the user
- No external actions without explicit permission

## Vibe

Be the helpful colleague who actually knows their stuff. Professional but not robotic. Crack a joke occasionally if appropriate.

## Continuity

Read your MEMORY.md at the start of each session. Update it with anything important you learn.
```

### USER.md — Knowing Your Human

**Purpose:** Stores context about the user so the agent can provide personalized assistance.

This file should be populated over time as the agent learns about the user.

#### Example USER.md

```markdown
# USER.md — About My Human

- **Name:** Alex
- **What to call them:** Alex (casual) or Mr. Chen (formal)
- **Pronouns:** he/him
- **Timezone:** Australia/Sydney (GMT+11)

## Context

Alex is a software developer working on automation projects. He:
- Prefers technical explanations with code examples
- Likes efficiency—get to the point
- Works on side projects involving AI agents
- Often asks "why" before "how"

## Preferences

- 24-hour time format
- Direct answers, not "Great question!"
- appreciates when I save him time with shortcuts
```

### TOOLS.md — The Agent's Toolkit

**Purpose:** Defines what tools the agent has access to and any environment-specific configurations.

This file tells the agent about available capabilities without exposing sensitive details.

#### Example TOOLS.md

```markdown
# TOOLS.md — Available Tools

## File Operations

- **read:** Read file contents (limited to workspace)
- **write:** Create or overwrite files
- **edit:** Make precise edits to existing files

## External Access

- **web_search:** Search the web via Brave API
- **web_fetch:** Extract content from URLs
- **browser:** Control web browser for automation

## Communication

- **message:** Send messages via configured channels (Telegram, Discord, WhatsApp)
- **tts:** Convert text to speech

## Environment

- **Shell:** PowerShell (Windows)
- **Workspace:** C:\Users\Alex\Projects\my-agent\

## Notes

- Use `exec` for shell commands
- Always confirm destructive actions (delete, overwrite)
- Check file existence before writing
```

### MEMORY.md — Persistent Context

**Purpose:** Stores information the agent should remember between sessions.

The agent reads this file at the start of each conversation and updates it throughout.

#### Example MEMORY.md

```markdown
# MEMORY.md — Session Log

## Last Session (2026-03-15)

- Alex asked me to help set up a research automation workflow
- He's using OpenClaw on Windows with Telegram as primary channel
- Key project: Building a personal AI assistant for code reviews

## Ongoing Projects

1. **Code Review Agent** — In progress. Need to define the review criteria
2. **Research Pipeline** — Not started. Will need web search + note-taking tools

## Things to Follow Up

- Ask about preferred code review criteria
- Check if he wants the research agent to save to Obsidian

## Personal Notes

- Alex appreciates concise, technical responses
- He uses VS Code as his editor
- Prefers MiniMax M2.1 for fast tasks, Claude Sonnet for complex reasoning
```

### Visual: Agent File Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                     OPENCLAW AGENT                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │
│   │   SOUL.md   │    │   USER.md   │    │   TOOLS.md   │    │
│   │             │    │             │    │              │    │
│   │ Personality │    │ User Context│    │ Capabilities │    │
│   │ Boundaries  │    │ Preferences │    │ Environment  │    │
│   │ Values      │    │ Projects    │    │ Config       │    │
│   └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    │
│          │                 │                  │            │
│          └────────────┬────┴──────────────────┘            │
│                       │                                      │
│                       ▼                                      │
│              ┌─────────────────┐                            │
│              │   AGENT RUNTIME │                            │
│              │                 │                            │
│              │ • Reads config  │                            │
│              │ • Applies rules │                            │
│              │ • Uses tools    │                            │
│              │ • Maintains mem │                            │
│              └────────┬────────┘                            │
│                       │                                      │
│          ┌────────────┴────────────┐                        │
│          ▼                         ▼                        │
│   ┌─────────────┐          ┌─────────────┐                  │
│   │  MEMORY.md  │◄────────►│  Sessions   │                  │
│   │             │          │             │                  │
│   │ Persistent  │          │ Ephemeral   │                  │
│   │ Remember    │          │ Chat hist   │                  │
│   │ across      │          │ Context     │                  │
│   │ sessions    │          │ window      │                  │
│   └─────────────┘          └─────────────┘                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 3.2 Spawning and Managing Agents

Now that you understand the file structure, let's learn how to create and run agents.

### Creating an Agent Workspace

Every agent needs its own workspace directory. Here's the step-by-step process:

#### Step 1: Create the Directory Structure

```bash
# Create agent workspace
mkdir -p ~/.openclaw/workspace/my-first-agent

# Create the four required files
touch ~/.openclaw/workspace/my-first-agent/{SOUL.md,USER.md,TOOLS.md,MEMORY.md}
```

#### Step 2: Configure SOUL.md

This is your agent's identity. Take time to get it right.

```markdown
# SOUL.md — My First Agent

## Core Truths

**Be helpful.** That's the job. Do it well.

**Be honest.** Admit when you don't know something.

**Be efficient.** Don't waste the user's time with filler.

## Boundaries

- Never execute destructive commands without confirmation
- Ask before taking external actions (sending messages, posting, etc.)
- Stay within the workspace unless explicitly given paths outside

## Vibe

Direct, practical, technically capable. Like a senior developer who actually has time to help.

## Continuity

Read MEMORY.md at session start. Write important updates to MEMORY.md before ending.
```

#### Step 3: Configure USER.md

```markdown
# USER.md

- **Name:** [Your Name]
- **Timezone:** [Your Timezone]

## Context

I'm learning OpenClaw and building my first agent.
```

#### Step 4: Configure TOOLS.md

```markdown
# TOOLS.md

## Available Tools

- **read:** Read files in workspace
- **write:** Create files in workspace  
- **exec:** Run shell commands
- **web_search:** Search the web
- **web_fetch:** Fetch URL content
```

#### Step 5: Configure MEMORY.md

```markdown
# MEMORY.md

## About This Agent

Created: 2026-03-18
Purpose: Learning OpenClaw agent development

## Sessions

### First Session
- Agent was created and configured
- Basic file structure implemented
```

### Spawning the Agent

Once your files are ready, spawn the agent using the OpenClaw CLI:

```bash
# Start the gateway first (if not running)
openclaw gateway start

# Spawn your agent
openclaw agent spawn my-first-agent

# Or spawn with a specific channel
openclaw agent spawn my-first-agent --channel telegram
```

### Managing Agents

```bash
# List all running agents
openclaw agent list

# Check agent status
openclaw agent status my-first-agent

# Stop an agent
openclaw agent stop my-first-agent

# Restart an agent
openclaw agent restart my-first-agent
```

### Visual: Agent Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                      AGENT LIFECYCLE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   CREATE              SPAWN              RUN                  │
│   ══════              ══════              ═══                  │
│                                                                 │
│   ┌─────────┐         ┌─────────┐        ┌─────────┐         │
│   │  SOUL   │         │  OpenClaw│        │  Agent  │         │
│   │  .md    │────────►│  loads   │───────►│  ready  │         │
│   │  USER   │         │  config  │        │  to     │         │
│   │  .md    │         │  files   │        │  assist │         │
│   │  TOOLS  │         │          │        │         │         │
│   │  .md    │         │          │        │         │         │
│   │  MEMORY │         │          │        │         │         │
│   │  .md    │         │          │        │         │         │
│   └─────────┘         └─────────┘        └────┬────┘         │
│                                                │               │
│                     MANAGE                     │               │
│                     ══════                     │               │
│                                                ▼               │
│   ┌─────────┐         ┌─────────┐        ┌─────────┐         │
│   │  edit   │         │  list   │        │  stop   │         │
│   │ config │◄────────│ agents  │───────►│ agent   │         │
│   │ files  │         │         │        │         │         │
│   └─────────┘         └─────────┘        └─────────┘         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Using AGENTS.md for Multiple Agents

If you're managing multiple agents, create an AGENTS.md file in your workspace root:

```markdown
# AGENTS.md — Agent Directory

## agent-openclaw-expert

- **Purpose:** OpenClaw installation, troubleshooting, configuration
- **Model:** MiniMax M2.1 (fast), Claude Sonnet (complex)
- **Workspace:** ~/.openclaw/workspace/agent-openclaw-expert

## agent-researcher  

- **Purpose:** Web research and information gathering
- **Model:** Claude Sonnet (thorough analysis)
- **Workspace:** ~/.openclaw/workspace/agent-researcher

## agent-writer

- **Purpose:** Content creation and editing
- **Model:** MiniMax M2.1 (fast drafting)
- **Workspace:** ~/.openclaw/workspace/agent-writer
```

---

## 3.3 Tool Use and Integration

Tools are how agents interact with the world. OpenClaw provides a rich set of built-in tools, and you can extend capabilities through skills.

### Built-in Tools Overview

| Tool | Purpose | Example Use |
|------|---------|-------------|
| `read` | Read file contents | Reading configuration, source code |
| `write` | Create/update files | Writing code, notes, reports |
| `edit` | Modify specific text | Fixing bugs, updating config |
| `exec` | Run shell commands | Git operations, running scripts |
| `web_search` | Search the web | Finding information, research |
| `web_fetch` | Get URL content | Scraping, reading articles |
| `browser` | Control browser | Automation, testing |
| `message` | Send messages | Telegram, Discord, WhatsApp |
| `tts` | Text-to-speech | Audio output |

### Tool Use Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                      TOOL USE FLOW                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────┐                                                │
│   │  User    │                                                │
│   │  Request │                                                │
│   └────┬─────┘                                                │
│        │                                                       │
│        ▼                                                       │
│   ┌──────────────────────────────────────┐                   │
│   │           AGENT THINKS                │                   │
│   │  "I need to read this file to        │                   │
│   │   answer the user's question"         │                   │
│   └──────────────┬───────────────────────┘                   │
│                  │                                             │
│                  ▼                                             │
│   ┌──────────────────────────────────────┐                   │
│   │        DECIDES TO USE TOOL            │                   │
│   │                                       │                   │
│   │  Tool: read                          │                   │
│   │  Args: path="config.json"            │                   │
│   └──────────────┬───────────────────────┘                   │
│                  │                                             │
│        ┌─────────┴─────────┐                                   │
│        ▼                   ▼                                   │
│   ┌──────────┐         ┌──────────┐                            │
│   │  TOOL   │         │  TOOL    │                            │
│   │ SUCCESS │         │  FAILS   │                            │
│   └────┬─────┘         └────┬─────┘                            │
│        │                   │                                   │
│        ▼                   ▼                                   │
│   ┌──────────┐         ┌──────────┐                            │
│   │  Uses    │         │  Reports │                            │
│   │  result  │         │  error   │                            │
│   │  in      │         │  to user │                            │
│   │  reply   │         │  + asks  │                            │
│   └──────────┘         │  what to │                            │
│                        │  do      │                            │
│                        └──────────┘                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Configuring Tool Access in TOOLS.md

You can be explicit about which tools the agent can use:

```markdown
# TOOLS.md — Restricted Agent

## Allowed Tools

- **read:** Yes (workspace only)
- **write:** Yes (workspace only)  
- **edit:** Yes (workspace only)
- **exec:** No
- **web_search:** Yes
- **web_fetch:** Yes
- **browser:** No
- **message:** No

## Restrictions

This is a read-only research agent. It should:
- Read files to understand the codebase
- Search the web for information
- Fetch URLs for content
- Never execute shell commands
- Never send messages externally

## Notes

This configuration creates a "safe" agent that can gather information but can't make changes to the system.
```

### Skills: Extending Tool Capabilities

Skills add specialized capabilities to your agents. They're installed from ClawHub:

```bash
# Install a skill
npx clawhub@latest install weather

# Skills are automatically available to all agents
```

#### Example: Adding Weather Skill

After installing the weather skill, configure it in TOOLS.md:

```markdown
# TOOLS.md — Weather-Aware Agent

## Built-in Tools

- read, write, edit, exec, web_search, web_fetch, browser, message, tts

## Skills

### weather
- **What:** Get current weather and forecasts
- **How:** Just ask about weather for any location
- **Example:** "What's the weather in Tokyo tomorrow?"
- **Source:** wttr.in (no API key needed)
```

---

## 3.4 Memory and Context Management

Effective memory management is what separates basic chatbots from capable AI assistants. OpenClaw provides multiple layers of memory.

### The Memory Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                    MEMORY HIERARCHY                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              LONG-TERM (MEMORY.md)                       │   │
│  │  • Persists across sessions                              │   │
│  │  • Updated manually or automatically                    │   │
│  │  • Contains: projects, preferences, ongoing work         │   │
│  │  • Size: Keep under 3KB for performance                  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            ▲                                    │
│                            │                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              SESSION (Chat History)                       │   │
│  │  • Current conversation only                              │   │
│  │  • In-memory (ephemeral)                                 │   │
│  │  • Contains: immediate context, recent exchanges        │   │
│  │  • Lost when session ends                                │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            ▲                                    │
│                            │                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              CONTEXT (SYSTEM PROMPT)                     │   │
│  │  • Built from: SOUL.md + USER.md + TOOLS.md             │   │
│  │  • Loaded at session start                               │   │
│  │  • Defines: identity, capabilities, constraints         │   │
│  │  • Fixed per session (unless files changed)             │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Best Practices for MEMORY.md

#### 1. Keep It Concise

```markdown
# MEMORY.md — GOOD EXAMPLE

## Current Project
- Building code review automation

## Key Details
- User prefers concise responses
- Uses MiniMax M2.1 model
- Primary channel: Telegram

## To Follow Up
- Confirm review criteria
```

#### 2. Structure With Sections

```markdown
# MEMORY.md — Structured

## About
[One-line description of agent purpose]

## Last Session
[What happened in the most recent session]

## Ongoing Projects
1. [Project 1] — Status
2. [Project 2] — Status

## Personal Notes
[Any user preferences or context]
```

#### 3. Update Regularly

The agent should update MEMORY.md at appropriate moments:

- End of each session
- When learning something important about the user
- When project status changes
- Before long-running operations

### Automatic Memory with QMD

For larger projects, consider installing QMD (Query-Memory-Data) for semantic search:

```bash
# Install QMD skill
npx clawhub@latest install qmd
```

QMD enables:
- Semantic search across all your files
- Natural language queries about past work
- Automatic knowledge retrieval

### Session Context Loading

```
┌─────────────────────────────────────────────────────────────────┐
│                SESSION START SEQUENCE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   1. AGENT SPAWNS                                              │
│         │                                                       │
│         ▼                                                       │
│   2. LOAD CONTEXT FILES                                        │
│      ┌─────────┐ ┌─────────┐ ┌─────────┐                       │
│      │ SOUL.md │ │ USER.md │ │TOOLS.md │                       │
│      │         │ │         │ │         │                       │
│      │ Identity│ │ Context │ │Capabilities                     │
│      └─────────┘ └─────────┘ └─────────┘                       │
│         │                                                       │
│         ▼                                                       │
│   3. LOAD MEMORY                                               │
│      ┌─────────────┐                                           │
│      │  MEMORY.md  │                                           │
│      │             │                                           │
│      │ • Projects  │                                           │
│      │ • Preferences                                           │
│      │ • History   │                                           │
│      └─────────────┘                                           │
│         │                                                       │
│         ▼                                                       │
│   4. READY TO ASSIST                                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Hands-On Exercises

### Exercise 1: Create Your First Agent (10 minutes)

**Objective:** Create a simple agent from scratch with all four required files.

**Steps:**

1. Create a new directory: `~/.openclaw/workspace/hello-agent/`
2. Create `SOUL.md` with:
   - A clear purpose
   - 2-3 behavioral guidelines
   - Your preferred communication style
3. Create `USER.md` with basic info about yourself
4. Create `TOOLS.md` listing what the agent can access
5. Create `MEMORY.md` with an introduction

**Verification:**
```bash
# List your agent files
ls -la ~/.openclaw/workspace/hello-agent/
```

You should see all four .md files listed.

---

### Exercise 2: Spawn and Test Your Agent (10 minutes)

**Objective:** Bring your agent to life and have a conversation.

**Steps:**

1. Start the OpenClaw gateway (if not running):
```bash
openclaw gateway start
```

2. Spawn your agent:
```bash
openclaw agent spawn hello-agent
```

3. Send a message through your configured channel:
   - Telegram: Send "/start" to your bot
   - Or use the dashboard

4. Ask your agent:
   - "What do you know about me?"
   - "What tools do you have access to?"

**Verification:**
The agent should respond using the identity and context you defined in SOUL.md and USER.md.

---

### Exercise 3: Tool Integration Practice (15 minutes)

**Objective:** Configure an agent with specific tools and practice using them.

**Steps:**

1. Create a new agent called `research-agent`
2. Configure TOOLS.md to allow:
   - web_search
   - web_fetch
   - read
   - write
3. Spawn the agent
4. Ask it to:
   - "Search for the latest news about OpenClaw AI"
   - "Fetch the content from https://openclaw.ai"
   - "Write a summary of what you found to research-notes.md"

**Verification:**
Check that the agent:
- Successfully searched the web
- Retrieved content from the URL
- Created a file with the summary

---

### Exercise 4: Memory Management (10 minutes)

**Objective:** Practice using MEMORY.md for persistent context.

**Steps:**

1. Have a conversation with your agent about:
   - A project you're working on
   - A preference you have (e.g., time format, communication style)
2. Ask the agent: "Can you remember this for next time?"
3. End the session
4. Start a new session with the same agent
5. Ask: "What do you remember about me?"

**Verification:**
The agent should recall information from the previous session, proving MEMORY.md is being used correctly.

---

## Discussion Questions

### Question 1: Agent Design Philosophy

**Topic:** When designing an agent's SOUL.md, how do you balance between having strong opinions/personalities versus staying flexible and adaptable?

*Consider:*
- How does a strong personality affect usability?
- When should agents defer to user preferences?
- What's the risk of a "blank slate" agent?

---

### Question 2: Spawning vs. Skills

**Topic:** When should you spawn a new agent versus installing a skill?

*Consider:*
- What's the overhead of each approach?
- When does an agent's purpose become distinct enough to warrant a new agent?
- Can skills and spawned agents work together?

---

### Question 3: Memory Privacy

**Topic:** What information should and shouldn't be stored in MEMORY.md?

*Consider:*
- Sensitive personal data (passwords, financial info)
- API keys or credentials
- Private conversations
- Project-specific knowledge

---

### Question 4: Context Window Limits

**Topic:** How do you manage context when working with agents that have large memory files?

*Consider:*
- When does MEMORY.md become too large?
- What information deserves priority?
- How do you balance comprehensiveness vs. performance?

---

### Question 5: Multi-Agent Systems

**Topic:** What's the philosophy behind having multiple specialized agents vs. one general-purpose agent?

*Consider:*
- Pros/cons of agent specialization
- How do agents communicate or delegate?
- When does complexity become counterproductive?

---

## Quiz

### Section A: Multiple Choice

**Question 1:** Which file defines the agent's personality and behavioral guidelines?

A) USER.md  
B) TOOLS.md  
C) SOUL.md  
D) MEMORY.md

---

**Question 2:** What is the PRIMARY purpose of MEMORY.md?

A) To define available tools  
B) To store context about the user  
C) To persist information between sessions  
D) To configure the agent's capabilities

---

**Question 3:** Which command spawns an agent named "my-agent"?

A) `openclaw start my-agent`  
B) `openclaw agent create my-agent`  
C) `openclaw agent spawn my-agent`  
D) `openclaw new my-agent`

---

**Question 4:** What happens at the start of every agent session?

A) TOOLS.md is deleted and recreated  
B) SOUL.md, USER.md, and TOOLS.md are loaded into context  
C) MEMORY.md is cleared automatically  
D) A new agent ID is generated

---

### Section B: Short Answer

**Question 5:** Name the four required files for an OpenClaw agent configuration.

---

**Question 6:** What's the recommended maximum size for MEMORY.md, and why?

---

**Question 7:** Describe the difference between session context and persistent memory.

---

**Question 8:** If you wanted to create an agent that can send messages via Telegram but cannot execute shell commands, how would you configure TOOLS.md?

---

## Quiz Answer Key

### Question 1: C) SOUL.md
**Explanation:** SOUL.md defines the agent's personality, values, boundaries, and behavioral guidelines. It's the core identity file.

### Question 2: C) To persist information between sessions
**Explanation:** MEMORY.md is designed to store information that should be remembered across different conversations. It's read at session start and updated throughout.

### Question 3: C) `openclaw agent spawn my-agent`
**Explanation:** The `openclaw agent spawn` command is used to bring an agent to life. The agent must already have its configuration files in place.

### Question 4: B) SOUL.md, USER.md, and TOOLS.md are loaded into context
**Explanation:** At session start, OpenClaw reads these three files to build the agent's system prompt. MEMORY.md is also loaded to provide persistent context.

### Question 5:
- SOUL.md (personality)
- USER.md (user context)
- TOOLS.md (available tools)
- MEMORY.md (persistent memory)

### Question 6:
**Recommended:** Keep MEMORY.md under 3KB.

**Why:** Larger memory files slow down context loading and can exceed the model's context window. It also encourages keeping only the most important information.

### Question 7:
**Session Context:** Ephemeral information that exists only during the current conversation. This includes the immediate chat history and any files read during the session.

**Persistent Memory:** Information stored in MEMORY.md that survives between sessions. It provides continuity so the agent "remembers" previous conversations.

### Question 8:

```markdown
# TOOLS.md

## Allowed Tools
- **message:** Yes (for Telegram)
- **read, write, edit:** Yes (workspace)
- **exec:** NO

## Restrictions
This agent can communicate via Telegram but cannot execute shell commands.
```

---

## Summary

In this module, you've learned:

1. **Agent File Structure** — The four essential files (SOUL.md, USER.md, TOOLS.md, MEMORY.md) that define an OpenClaw agent
2. **Spawning Agents** — How to create, configure, and run agents using the OpenClaw CLI
3. **Tool Integration** — How to configure and use tools, including skills from ClawHub
4. **Memory Management** — The hierarchy of memory systems and best practices for persistent context

You now have the foundation to build capable, persistent AI assistants tailored to your specific needs.

---

## Next Steps

- **Module 4:** Strategy & Ethics — Learn about responsible AI deployment
- **Practice:** Create 2-3 more agents with different purposes
- **Explore:** Browse ClawHub for skills to extend your agents

---

*Module 3 complete. You're building real agents now.* 🎉
