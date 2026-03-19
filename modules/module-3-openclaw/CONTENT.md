# AGENTS.md — Module 3: OpenClaw Technical Mastery

## Role

Teach technical mastery of OpenClaw: architecture, configuration, agents, skills, and practical deployment

## Agent ID

`module-3-openclaw`

## Duration

60 minutes

## Learning Objectives

By the end of this module, students will be able to:
1. Explain the OpenClaw architecture and core components
2. Configure agents with custom prompts, tools, and behaviours
3. Create and manage skills for reusable capabilities
4. Set up automation workflows with cron jobs and webhooks
5. Deploy and run a personal AI assistant

---

# LESSON CONTENT

## 3.1 OpenClaw Architecture (15 minutes)

### What Is OpenClaw?

OpenClaw is an **open-source AI assistant framework** that enables you to build, deploy, and manage autonomous AI agents. It's designed for personal and business automation.

```
┌─────────────────────────────────────────────────────────────────────┐
│                      OPENCLAW ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                      GATEWAY                                │  │
│   │         (Message routing, Auth, Channels)                  │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                              │                                       │
│          ┌──────────────────┼──────────────────┐                   │
│          ▼                  ▼                  ▼                   │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐           │
│   │   AGENTS    │    │   SKILLS    │    │   TOOLS     │           │
│   │  (Prompts,  │    │  (Reusable  │    │  (Browser,  │           │
│   │   Tools,    │    │   Actions)  │    │   Search,   │           │
│   │   Memory)   │    │             │    │   TTS, etc) │           │
│   └─────────────┘    └─────────────┘    └─────────────┘           │
│          │                  │                  │                   │
│          └──────────────────┼──────────────────┘                   │
│                             ▼                                       │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                    ORCHESTRATION                             │  │
│   │      (Task Planning, Execution, Tool Calling)               │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                             │                                       │
│                             ▼                                       │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                   LLM PROVIDERS                              │  │
│   │        (OpenAI, Anthropic, MiniMax, Local, etc.)           │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Core Components

| Component | Description |
|-----------|-------------|
| **Gateway** | Message routing across Telegram, WhatsApp, Discord, Signal |
| **Agents** | Configurable AI assistants with custom prompts and tools |
| **Skills** | Reusable capability modules (search, browser, etc.) |
| **Orchestration** | Task planning and tool execution |
| **Providers** | Multi-LLM support (OpenAI, Anthropic, MiniMax, local) |

---

## 3.2 Agents Deep Dive (15 minutes)

### Agent Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│                      AGENT CONFIGURATION                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   AGENT: "Sales Assistant"                                         │
│   ─────────────────────────────────────────                        │
│                                                                     │
│   PROMPT:                                                          │
│   "You are a friendly sales assistant. Help customers find        │
│    products. Be concise and persuasive. Always end with:          │
│    'Can I help you with anything else?'"                          │
│                                                                     │
│   TOOLS:                                                           │
│   ├── search-products (search the product catalog)                │
│   ├── get-pricing (fetch current prices)                          │
│   ├── create-order (process a purchase)                            │
│   └── send-email (email confirmation)                             │
│                                                                     │
│   MEMORY:                                                          │
│   ├── session: Current conversation                                │
│   └── semantic: Customer preferences                               │
│                                                                     │
│   SETTINGS:                                                        │
│   ├── model: minimax/MiniMax-M2.5                                  │
│   ├── temperature: 0.7                                             │
│   └── max_tokens: 2000                                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Agent Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | Agent identity, role, and instructions |
| `SOUL.md` | Personality and communication style |
| `TOOLS.md` | Available tools and configurations |
| `MEMORY.md` | Long-term memory and learnings |

### Creating Your First Agent

```markdown
# AGENTS.md — My Sales Agent

## Role
Help customers find and purchase products

## Goals
1. Understand customer needs
2. Recommend suitable products
3. Process orders smoothly

## Constraints
- Always be polite and helpful
- Never share internal pricing formulas
- Escalate to human for complex issues
```

---

## 3.3 Skills System (10 minutes)

### What Are Skills?

Skills are **reusable capability modules** that agents can use to perform specific actions. Think of them as plugins that extend what your agents can do.

```
┌─────────────────────────────────────────────────────────────────────┐
│                      SKILLS ECOSYSTEM                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│   │   SEARCH    │  │  BROWSER    │  │    TTS      │              │
│   │   SKILL     │  │   SKILL     │  │   SKILL     │              │
│   ├─────────────┤  ├─────────────┤  ├─────────────┤              │
│   │ Brave       │  │ Playwright  │  │ ElevenLabs  │              │
│   │ SearXNG     │  │ Browser     │  │ MiniMax     │              │
│   │ Jina AI     │  │ Relay       │  │             │              │
│   └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                     │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│   │   EMAIL     │  │  CALENDAR   │  │   SOCIAL    │              │
│   │   SKILL     │  │   SKILL     │  │   SKILL     │              │
│   ├─────────────┤  ├─────────────┤  ├─────────────┤              │
│   │ Gmail       │  │ Google      │  │ LinkedIn    │              │
│   │ SendFox     │  │ Calendar    │  │ Bluesky     │              │
│   │             │  │             │  │ X (Twitter) │              │
│   └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Available Skills (Examples)

| Skill | Capabilities |
|-------|-------------|
| **brave-search** | Web search with Brave API |
| **browser** | Web automation via Playwright |
| **minimax-tts** | Text-to-speech generation |
| **gmail-send** | Send emails via Gmail |
| **linkedin** | LinkedIn automation |
| **bluesky** | Bluesky social posting |
| **weather** | Current weather and forecasts |
| **google-tasks** | Google Tasks management |

---

## 3.4 Automation: Cron Jobs & Webhooks (10 minutes)

### Cron Jobs

Schedule recurring tasks to run automatically:

```json
{
  "name": "Morning Report",
  "schedule": "0 7 * * *",
  "enabled": true,
  "task": "Generate and send morning report",
  "channels": ["telegram", "whatsapp"]
}
```

**Cron Format:**
```
┌───────────── minute (0-59)
│ ┌─────────── hour (0-23)
│ │ ┌───────── day of month (1-31)
│ │ │ ┌─────── month (1-12)
│ │ │ │ ┌───── day of week (0-6, Sunday=0)
│ │ │ │ │
* * * * *
```

**Common Examples:**
| Schedule | Meaning |
|----------|---------|
| `0 7 * * *` | Daily at 7am |
| `0 9 * * 1` | Every Monday at 9am |
| `0 8 * * 1-5` | Weekdays at 8am |

### Webhooks

Trigger actions based on external events:

```
┌─────────────────────────────────────────────────────────────────────┐
│                         WEBHOOK FLOW                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   External Event          OpenClaw Gateway         Agent Action   │
│   ─────────────          ─────────────────         ───────────   │
│                                                                     │
│   ┌──────────┐          ┌──────────────┐         ┌──────────┐   │
│   │ GitHub   │───────►│  Receive     │────────►│  Agent   │   │
│   │ Push     │          │  Webhook     │         │  Triggers│   │
│   └──────────┘          └──────────────┘         └──────────┘   │
│                                                                     │
│   ┌──────────┐          ┌──────────────┐         ┌──────────┐   │
│   │ Form     │───────►│  Parse       │────────►│  Agent   │   │
│   │ Submit   │          │  Data        │         │  Process │   │
│   └──────────┘          └──────────────┘         └──────────┘   │
│                                                                     │
│   ┌──────────┐          ┌──────────────┐         ┌──────────┐   │
│   │ Schedule │───────►│  Time Event   │────────►│  Agent   │   │
│   │ Trigger  │          │              │         │  Runs    │   │
│   └──────────┘          └──────────────┘         └──────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3.5 Channels & Communication (10 minutes)

### Supported Channels

| Channel | Capabilities |
|---------|-------------|
| **Telegram** | Messages, buttons, polls, voice |
| **WhatsApp** | Messages, media, status |
| **Discord** | Commands, embeds, threads |
| **Signal** | Encrypted messaging |
| **Slack** | Messages, workflows |
| **Web** | Custom chat UI |

### Multi-Channel Configuration

```yaml
channels:
  telegram:
    enabled: true
    bot_token: "${TELEGRAM_BOT_TOKEN}"
    
  whatsapp:
    enabled: true
    phone_number: "+61490393533"
    
  discord:
    enabled: true
    guild_id: "123456789"
```

---

# EXERCISES

## Exercise 1: Architecture Mapping (5 minutes)

Match each OpenClaw component to its function:

| Component | Function |
|-----------|----------|
| 1. Gateway | A) Reusable capability modules |
| 2. Agents | B) Message routing across channels |
| 3. Skills | C) Configurable AI assistants |
| 4. Orchestration | D) Task planning and execution |

---

## Exercise 2: Create an Agent (10 minutes)

Design an agent configuration for a "Research Assistant" that:
- Searches the web for information
- Summarises findings
- Saves to a database

**Template:**
```markdown
# AGENTS.md — Research Assistant

## Role:
[Your answer]

## Goals:
1. [Your answer]
2. [Your answer]

## Tools needed:
- [Your answer]
```

---

## Exercise 3: Cron Schedule (5 minutes)

Write the cron expression for:
1. Every day at 6am _______________
2. Every Monday at 9am _______________
3. Every hour _______________

---

# DISCUSSION QUESTIONS

1. **Technical:** How does OpenClaw compare to other agent frameworks like LangChain or AutoGen?

2. **Practical:** What are the security considerations when giving agents access to tools like email or calendar?

3. **Design:** How would you structure an agent team for a small business (sales, support, operations)?

4. **Future:** How might voice-first interfaces change how we interact with AI agents?

---

# QUIZ

## Quiz: Module 3 - OpenClaw Technical Mastery

### Question 1 (1 point)
What is the primary role of the Gateway in OpenClaw?

A) Running AI models  
B) Message routing across channels  
C) Storing agent memories  
D) Scheduling cron jobs

**Correct Answer:** B

---

### Question 2 (1 point)
Which file defines an agent's core identity and role?

A) TOOLS.md  
B) SOUL.md  
C) AGENTS.md  
D) MEMORY.md

**Correct Answer:** C

---

### Question 3 (1 point)
What are Skills in OpenClaw?

A) Training data for agents  
B) Reusable capability modules  
C) Configuration files  
D) User preferences

**Correct Answer:** B

---

### Question 4 (1 point)
If you want a task to run every Monday at 9am, what cron expression would you use?

A) `0 9 * * 1`  
B) `0 9 * 1 *`  
C) `9 0 * * 1`  
D) `1 9 * * 0`

**Correct Answer:** A

---

### Question 5 (1 point)
Which component handles tool execution and task planning?

A) Gateway  
B) Skills  
C) Orchestration  
D) Memory

**Correct Answer:** C

---

### Question 6 (1 point)
What is the purpose of semantic memory in an agent?

A) Store current conversation  
B) Remember learned facts about users  
C) Cache API responses  
D) Log system events

**Correct Answer:** B

---

### Question 7 (2 points)
Name three communication channels OpenClaw supports:

1. _______________
2. _______________
3. _______________

**Sample Answers:**
1. Telegram
2. WhatsApp
3. Discord

---

### Question 8 (2 points)
Why would you use multiple agents instead of one general-purpose agent?

**Sample Answer:**
Specialised agents can be optimised for specific tasks, have tailored prompts, use different tools, and are easier to maintain and debug than a single complex agent.

---

## Quiz Answer Key

| Q | Answer |
|---|--------|
| 1 | B |
| 2 | C |
| 3 | B |
| 4 | A |
| 5 | C |
| 6 | B |
| 7 | (Open) |
| 8 | (Open) |

---

# SUMMARY

## Key Takeaways

✅ **OpenClaw Architecture:** Gateway → Agents → Skills → Tools → Orchestration → LLMs

✅ **Agent Files:**
- AGENTS.md: Identity and role
- SOUL.md: Personality
- TOUL.md: Available tools
- MEMORY.md: Long-term memory

✅ **Skills:** Reusable capability modules (search, browser, TTS, email, etc.)

✅ **Automation:**
- Cron: Scheduled recurring tasks
- Webhooks: Event-driven triggers

✅ **Channels:** Telegram, WhatsApp, Discord, Signal, Slack, Web

---

# NEXT STEPS

After completing this module:

1. ✅ You understand OpenClaw architecture
2. ⏭️ Move to **Module 4: Strategy & Ethics**
3. 🔄 Set up your own OpenClaw instance
4. 🔄 Create your first custom agent

---

*Module 3 complete. You're ready to build real agents!*
