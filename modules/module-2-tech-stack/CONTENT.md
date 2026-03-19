# AGENTS.md — Module 2: The Tech Stack of 2026

## Role

Teach technical foundations: AI orchestration components, evolution of AI systems, and the modern AI tooling landscape

## Agent ID

`module-2-tech-stack`

## Duration

45 minutes

## Learning Objectives

By the end of this module, students will be able to:
1. Identify the core components of an AI orchestration system
2. Explain the evolution from basic chatbots to agentic AI systems
3. Differentiate between various AI API providers and their strengths
4. Build a basic understanding of how AI tools connect together

---

# LESSON CONTENT

## 2.1 The AI Orchestration Stack (15 minutes)

### What Is AI Orchestration?

AI orchestration is the **coordination layer** that connects AI models, tools, memory, and actions into a coherent system. Think of it as the conductor of an AI orchestra.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AI ORCHESTRATION STACK                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                    USER INTERFACE                            │  │
│   │         (Chat, Voice, API, Webhook, Dashboard)              │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                              │                                       │
│                              ▼                                       │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                  ORCHESTRATION LAYER                        │  │
│   │    (Agent Framework, Workflow Engine, Task Planner)         │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                              │                                       │
│          ┌──────────────────┼──────────────────┐                   │
│          ▼                  ▼                  ▼                   │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐           │
│   │   MEMORY    │    │    TOOLS    │    │    MODEL   │           │
│   │  (Vector DB,│    │  (APIs,     │    │  (LLM,     │           │
│   │   Sessions) │    │  Functions) │    │   Embed)   │           │
│   └─────────────┘    └─────────────┘    └─────────────┘           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Core Components

| Component | Purpose | Examples |
|-----------|---------|----------|
| **Orchestration Layer** | Coordinates tasks and workflows | OpenClaw, LangChain, AutoGen |
| **LLM Provider** | Generates text and reasoning | OpenAI, Anthropic, Google, MiniMax |
| **Vector Database** | Stores embeddings for semantic search | Pinecone, Weaviate, Chroma |
| **Tool Connectors** | Integrates with external services | APIs, Webhooks, Functions |
| **Memory System** | Maintains state and context | Session storage, semantic memory |

---

## 2.2 Evolution of AI Systems (15 minutes)

### The Four Eras of AI

```
┌─────────────────────────────────────────────────────────────────────┐
│                    EVOLUTION OF AI SYSTEMS                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ERA 1: Rules-Based          ERA 2: Machine Learning              │
│   ┌─────────────┐             ┌─────────────┐                      │
│   │ IF/THEN    │             │  Training   │                      │
│   │  Logic     │──────►      │   Data      │                      │
│   │             │             │    Models    │                      │
│   └─────────────┘             └─────────────┘                      │
│   1960s-1990s                 2010s-2022                            │
│                                                                     │
│   ERA 3: Generative AI       ERA 4: Agentic AI                     │
│   ┌─────────────┐             ┌─────────────┐                      │
│   │   Large    │             │  Autonomous │                      │
│   │   Language │──────►      │   Agents    │                      │
│   │   Models   │             │  + Tools    │                      │
│   └─────────────┘             └─────────────┘                      │
│   2022-2024                   2024+                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Era 1: Rules-Based Systems
- Explicit programming
- No learning capability
- Limited to programmed rules
- Example: Early chatbots, ELIZA

### Era 2: Machine Learning
- Models trained on data
- Pattern recognition
- Limited to training data
- Example: Spam filters, recommendation systems

### Era 3: Generative AI
- Large Language Models
- Creates new content
- General-purpose capabilities
- Example: ChatGPT, Claude, Gemini

### Era 4: Agentic AI
- Autonomous execution
- Tool use and actions
- Persistent memory
- Example: OpenClaw agents, AutoGPT

---

## 2.3 AI Provider Landscape (10 minutes)

### Major LLM Providers

| Provider | Flagship Models | Strengths | Best For |
|----------|-----------------|-----------|----------|
| **OpenAI** | GPT-4o, o1 | First mover, API maturity | General purpose, code |
| **Anthropic** | Claude 3.5, 4 | Safety, long context | Writing, analysis |
| **Google** | Gemini 1.5, 2.0 | Multimodal, context | Research, integration |
| **Meta** | Llama 3.3 | Open source | Custom fine-tuning |
| **MiniMax** | M2.1, M2.5 | Cost-effective | High-volume tasks |

### Emerging Providers

| Provider | Specialty | Notes |
|----------|-----------|-------|
| **DeepSeek** | Reasoning, coding | Open weights, strong performance |
| **Mistral** | European AI | Open source options |
| **Cohere** | Enterprise | Focus on business APIs |

### Choosing the Right Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MODEL SELECTION GUIDE                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Need long context?    → Claude 200K, Gemini 2M                  │
│   Need coding help?    → OpenAI o1, DeepSeek                      │
│   Need safety focus?   → Claude, Gemini                            │
│   Need low cost?       → MiniMax, Llama, DeepSeek                 │
│   Need offline?        → Llama, Mistral (self-hosted)              │
│   Need Australian?     → MiniMax (data residency)                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2.4 Building Blocks Deep Dive (5 minutes)

### Tool Categories

| Category | Function | Examples |
|----------|----------|----------|
| **Search** | Web research | Brave Search, SerpAPI |
| **Browser** | Web automation | Playwright, Selenium |
| **Database** | Data storage | PostgreSQL, MongoDB |
| **Communication** | Messaging | Slack, Discord, Email |
| **Productivity** | Office work | Calendar, Docs, Sheets |
| **Payment** | Transactions | Stripe, PayPal |

### Memory Types

| Type | Purpose | Implementation |
|------|---------|----------------|
| **Session** | Current conversation | In-memory, Redis |
| **Semantic** | Learned knowledge | Vector databases |
| **Episodic** | Past interactions | Event stores |
| **Working** | Active task context | Context window |

---

# EXERCISES

## Exercise 1: Identify the Stack (5 minutes)

For each scenario, identify which component of the orchestration stack would be used:

1. **Scenario:** An agent needs to remember user preferences across sessions
   - **Component:** _______________

2. **Scenario:** An agent needs to search the web for current information
   - **Component:** _______________

3. **Scenario:** An agent needs to decide the order of tasks
   - **Component:** _______________

---

## Exercise 2: Era Classification (5 minutes)

Classify each AI system by era:

| # | Description | Era |
|---|-------------|-----|
| 1 | A spam filter that learns from user reports | |
| 2 | ChatGPT that writes creative stories | |
| 3 | An agent that books flights and hotels automatically | |
| 4 | A calculator that follows BEDMAS rules | |

---

## Exercise 3: Provider Selection (5 minutes)

Match the use case to the best provider:

**Use Cases:**
A) Need 100K token context for analysing long documents
B) Building a safety-focused customer service bot
C) Need the cheapest option for high-volume simple queries
D) Want to fine-tune my own model

**Providers:**
1) Claude 3.5
2) MiniMax
3) Llama 3
4) Gemini 2.0

---

# DISCUSSION QUESTIONS

1. **Technical:** How does the orchestration layer differ from simply calling an LLM API directly?

2. **Strategic:** What are the trade-offs between using a single provider vs. multiple providers in an AI system?

3. **Future:** How might the AI tooling landscape change in the next 12-18 months?

4. **Practical:** What factors should influence your choice of vector database for a project?

---

# QUIZ

## Quiz: Module 2 - The Tech Stack of 2026

### Question 1 (1 point)
What is the primary role of the orchestration layer in an AI system?

A) Generating text responses  
B) Coordinating tasks, tools, and memory  
C) Storing user data  
D) Creating user interfaces

**Correct Answer:** B

---

### Question 2 (1 point)
Which era of AI is characterized by autonomous agents with tool use?

A) Era 1: Rules-Based  
B) Era 2: Machine Learning  
C) Era 3: Generative AI  
D) Era 4: Agentic AI

**Correct Answer:** D

---

### Question 3 (1 point)
What is a vector database primarily used for?

A) Storing plain text documents  
B) Semantic search and embeddings  
C) Running SQL queries  
D) Caching API responses

**Correct Answer:** B

---

### Question 4 (1 point)
Which provider is known for the largest context window?

A) OpenAI  
B) Anthropic  
C) MiniMax  
D) Meta

**Correct Answer:** B (Claude 200K) - Note: Contexts vary by model version

---

### Question 5 (1 point)
What distinguishes Era 3 (Generative AI) from Era 4 (Agentic AI)?

A) Era 3 uses neural networks, Era 4 doesn't  
B) Era 3 creates content, Era 4 takes autonomous actions  
C) Era 3 is cheaper than Era 4  
D) Era 3 requires more data than Era 4

**Correct Answer:** B

---

### Question 6 (1 point)
Which component connects an AI agent to external services like calendars or email?

A) Memory System  
B) Orchestration Layer  
C) User Interface  
D) Tool Connectors

**Correct Answer:** D

---

### Question 7 (2 points)
Name three categories of tools an AI agent might use:

1. _______________
2. _______________
3. _______________

**Sample Answers:**
1. Search tools (web research)
2. Communication tools (email, Slack)
3. Productivity tools (calendar, docs)

---

### Question 8 (2 points)
Why might a business choose to use multiple LLM providers instead of just one?

**Sample Answer:**
Different providers excel at different tasks, cost varies by usage, redundancy for reliability, and some providers offer better safety or data residency for specific use cases.

---

## Quiz Answer Key

| Q | Answer |
|---|--------|
| 1 | B |
| 2 | D |
| 3 | B |
| 4 | B |
| 5 | B |
| 6 | D |
| 7 | (Open) |
| 8 | (Open) |

---

# SUMMARY

## Key Takeaways

✅ **AI Orchestration** = Coordination layer connecting models, tools, and memory

✅ **Four Eras of AI:**
1. Rules-Based (1960s-1990s)
2. Machine Learning (2010s-2022)
3. Generative AI (2022-2024)
4. Agentic AI (2024+)

✅ **Core Stack Components:**
- Orchestration Layer
- LLM Provider
- Vector Database
- Tool Connectors
- Memory System

✅ **Provider Selection** depends on: context needs, cost, safety, offline capability

---

# NEXT STEPS

After completing this module:

1. ✅ You understand the technical AI stack
2. ⏭️ Move to **Module 3: OpenClaw Deep Dive**
3. 🔄 Schedule spaced repetition review

---

*Module 2 complete. Ready for the hands-on technical work!*
