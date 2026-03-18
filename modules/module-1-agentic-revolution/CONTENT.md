# AGENTS.md — Module 1: The Agentic Revolution

## Role

Teach the fundamental concepts of AI Agents vs Chatbots

## Agent ID

`module-1-agentic-revolution`

## Duration

45 minutes

## Learning Objectives

By the end of this module, students will be able to:
1. Define what makes an AI "agentic"
2. Identify the 5 core capabilities of an AI Agent Framework
3. Compare and contrast chatbots vs agents
4. Explain why this shift in computing matters now

---

# LESSON CONTENT

## 1.1 Defining the AI Agent Framework (15 minutes)

### The Five Core Capabilities

An AI Agent Framework provides the **scaffolding** that allows an LLM to perform tasks beyond generating text.

```
┌─────────────────────────────────────────────────────────────────┐
│                  AI AGENT FRAMEWORK                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│    ┌─────────────┐   ┌─────────────┐   ┌─────────────┐       │
│    │  PERCEPTION │   │    PLANNING │   │   ACTION    │       │
│    │  (Sensors)  │──►│  (Reasoning)│──►│  (Tools)     │       │
│    └─────────────┘   └─────────────┘   └─────────────┘       │
│           │                 │                 │                 │
│           ▼                 ▼                 ▼                 │
│    ┌─────────────────────────────────────────────────────┐    │
│    │                    MEMORY                            │    │
│    │  ┌───────────┐  ┌───────────┐  ┌───────────┐        │    │
│    │  │ Working   │  │ Semantic  │  │ Episodic  │        │    │
│    │  │ Memory    │  │ Memory    │  │ Memory    │        │    │
│    │  └───────────┘  └───────────┘  └───────────┘        │    │
│    └─────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Core Capability 1: Autonomous Execution

**Definition:** The ability to complete multi-step tasks without continuous human intervention.

**Example:**
- ❌ Chatbot: "What's the weather?" → "It's 72°F and sunny"
- ✅ Agent: "Plan my weekend" → Books camping site, checks weather, suggests routes, sets calendar

**Why it matters:** Agents can work while you're sleeping.

---

### Core Capability 2: Tool Use

**Definition:** Calling external functions, APIs, and services to interact with the real world.

**The Tool Spectrum:**
```
┌──────────────────────────────────────────────────────────────┐
│                     TOOL USE CATEGORIES                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  🔧 BUILT-IN TOOLS           🔌 EXTERNAL APIs               │
│  ├── Web search               ├── Calendar                   │
│  ├── Calculator              ├── Email                      │
│  ├── Code interpreter        ├── CRM                        │
│  └── File operations         ├── Database                   │
│                              ├── Slack                       │
│                              └── Custom APIs                 │
│                                                              │
│  🌐 WEBHOOKS (Event-driven)   ⚡ FUNCTION CALLING           │
│  ├── Stripe payments          ├── OpenAI functions          │
│  ├── Form submissions         ├── OpenClaw tools            │
│  └── Database triggers        └── Custom functions           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

### Core Capability 3: Memory & Context

**Definition:** Maintaining state across interactions and learning from past interactions.

**Three Types of Memory:**

| Type | What It Stores | Example |
|------|----------------|---------|
| **Working** | Current conversation | "We were discussing the marketing campaign..." |
| **Semantic** | Learned knowledge | "User prefers morning meetings" |
| **Episodic** | Past experiences | "Last time we tried X, it failed" |

**Analogy:** Think of memory like a human brain:
- Working memory = short-term (what you just thought)
- Semantic memory = facts you know
- Episodic memory = experiences you've had

---

### Core Capability 4: Decision Making

**Definition:** Evaluating options and choosing actions based on goals, constraints, and context.

**The Decision Loop:**
```
┌────────────────────────────────────────────────────────────┐
│                   THE AGENT LOOP                          │
├────────────────────────────────────────────────────────────┤
│                                                            │
│    ┌─────────┐                                            │
│    │  THINK  │ ◄─── Observe environment                    │
│    └────┬────┘         + Retrieve memory                 │
│         │                                                 │
│         ▼                                                 │
│    ┌─────────┐                                            │
│    │ DECIDE  │ ◄─── Evaluate options                       │
│    └────┬────┘         + Consider constraints            │
│         │                                                 │
│         ▼                                                 │
│    ┌─────────┐                                            │
│    │  ACT    │ ◄─── Execute tool                           │
│    └────┬────┘         + Update memory                    │
│         │                                                 │
│         ▼                                                 │
│    ┌─────────┐                                            │
│    │ OBSERVE │ ◄─── Get results                            │
│    └────┬────┘         + Check success                    │
│         │                                                 │
│         └──────── (repeat until goal complete)            │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

### Core Capability 5: Action Chaining

**Definition:** Breaking complex tasks into sequences of smaller actions that achieve a larger goal.

**Example Chain:**
```
User Request: "Book me a flight to NYC next Friday"

CHAIN BREAKDOWN:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 1: Check calendar    → Find open Friday
Step 2: Search flights   → Find NYC flights  
Step 3: Compare prices   → Sort by price
Step 4: Check weather    → NYC weather forecast
Step 5: Book flight      → Purchase ticket
Step 6: Add to calendar  → Create travel event
Step 7: Notify user      → Send confirmation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total: 7 actions chained together automatically
```

---

## 1.2 Chatbots vs Agents (15 minutes)

### The Fundamental Shift

This is NOT just a better chatbot. It's a fundamentally different computing paradigm.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CHATBOT                          AGENT              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│    INPUT                    OUTPUT                    INPUT            │
│  ┌────────┐              ┌─────────┐              ┌────────┐           │
│  │ "Hello" │───────────►│ "Hello!" │              │Goal: X │           │
│  └────────┘              └─────────┘              └────┬────┘           │
│                                                         │                │
│     ▲                                                    ▼                │
│     │                                              ┌─────────┐           │
│     │                                              │Action 1 │──┐        │
│     │                                              └────┬────┘  │        │
│     │                                                   │       ▼        │
│     │                                              ┌────▼────┐           │
│     │                                              │Action 2 │──┐        │
│     │                                              └────┬────┘  │        │
│     │                                                   │       ▼        │
│     │                                              ┌────▼────┐           │
│     │                                              │Result Y │           │
│     │                                              └─────────┘           │
│     │                                                    ▲                │
│     │                                                    │                │
│     └──────────── ONE-TO-ONE MAPPING                    │                │
│                                                         │                │
│                  One request → One response            └────────────────┘
│                                                         Multi-step execution
│                                                         to achieve goal
└─────────────────────────────────────────────────────────────────────────┘
```

### Comparison Table

| Dimension | Chatbot | Agent |
|-----------|---------|-------|
| **Initiative** | Reactive - waits for prompt | Proactive - takes initiative |
| **Connectivity** | Isolated - no external access | Connected - uses tools/APIs |
| **Memory** | Session-only | Persistent across sessions |
| **Scope** | Single response | Multi-step workflows |
| **Goal** | Answer questions | Accomplish tasks |
| **Autonomy** | None | High |
| **Learning** | Static | Improves from feedback |

### Real-World Examples

#### Chatbot Example: Customer Service Bot
```
User: "Where's my order?"
Bot: "I can help with that! Can you provide your order number?"
User: "It's 12345"
Bot: "Your order #12345 is currently in transit. 
       Expected delivery: March 20th."
```

#### Agent Example: Executive Assistant Agent
```
User: "I need to schedule a Q1 strategy meeting with the team"

Agent does:
1. Check everyone's calendar via API
2. Find 2-hour slot with all attendees free
3. Create video conference
4. Send calendar invites
5. Prepare agenda template
6. Book meeting room
7. Add to follow-up: "Send meeting notes"

User receives: "Done! Strategy meeting scheduled for 
                Tuesday 2pm. Video link and agenda template 
                attached."
```

---

## 1.3 The Shift in Computing (10 minutes)

### Why This Matters NOW

```
┌─────────────────────────────────────────────────────────────────────┐
│                  THE CONVERGENCE                                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│       ┌─────────────┐        ┌─────────────┐                      │
│       │  Powerful   │        │  Reliable   │                      │
│       │    LLMs     │   +    │    APIs     │                      │
│       │  (GPT-4,    │        │  (REST,     │                      │
│       │   Claude,   │        │   Webhooks) │                      │
│       │   Gemini)   │        │             │                      │
│       └─────────────┘        └─────────────┘                      │
│              │                       │                             │
│              │                       │                             │
│              ▼                       ▼                             │
│       ┌─────────────────────────────────────────────┐             │
│       │                                             │             │
│       │         AUTONOMOUS AGENTS                   │             │
│       │                                             │             │
│       └─────────────────────────────────────────────┘             │
│                                                                     │
│                    PREVIOUSLY: Sci-Fi    NOW: Reality              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### The Three Waves of AI

| Wave | What | When | Example |
|------|------|------|---------|
| **Wave 1** | Rules-based | 1960s-1990s | "If A, then B" |
| **Wave 2** | Machine Learning | 2010s-2022 | Spam filters, recommendations |
| **Wave 3** | Generative + Agents | 2023+ | Claude, GPT-4, AutoGPT |

### Why Agents Are Different

**Traditional Software:**
```
Input → [Fixed Rules] → Output
        (Programmer's
         intelligence)
```

**LLM-powered Software:**
```
Input → [Trained Model] → Output
        (Learned 
         intelligence)
```

**Agent-powered Software:**
```
Input → [Model + Tools + Memory + Goals] → Accomplished Task
                  ↑
           (Autonomous
            execution)
```

### The Business Impact

```
┌─────────────────────────────────────────────────────────────────────┐
│                     AGENT ADOPTION TIMELINE                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  2024              2025              2026              2027+        │
│  ┌───┐            ┌───┐            ┌───┐            ┌───┐         │
│  │   │            │   │            │   │            │   │         │
│  │ E │            │   │            │   │            │   │         │
│  │ A │            │   │            │   │            │   │         │
│  │ R │            │   │            │   │            │   │         │
│  │ L │            │   │            │   │            │   │         │
│  │ Y │            │   │            │   │            │   │         │
│  └───┘            └───┘            └───┘            └───┘         │
│                                                                     │
│  Innovators        Early           Majority        Laggards        │
│  (You!)           Adopters                                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

# EXERCISES

## Exercise 1: Identify the Capabilities (5 minutes)

For each scenario, identify which of the 5 core capabilities is being demonstrated:

1. **Scenario:** An agent remembers that you prefer morning meetings and schedules your meeting at 9am.
   - **Capability:** _______________

2. **Scenario:** An agent searches the web for current stock prices before recommending a portfolio.
   - **Capability:** _______________

3. **Scenario:** An agent breaks down "plan my marketing campaign" into 12 separate tasks.
   - **Capability:** _______________

4. **Scenario:** An agent notices you're running late and proactively reschedules your meetings.
   - **Capability:** _______________

---

## Exercise 2: Chatbot vs Agent Classification (5 minutes)

Classify each as chatbot or agent:

| # | Description | Chatbot | Agent |
|---|-------------|---------|-------|
| 1 | "Hi, I'm here to help. What do you need?" | | |
| 2 | Books flight, adds to calendar, notifies contacts | | |
| 3 | "The weather tomorrow is 72°F" | | |
| 4 | Researches competitors, writes report, emails it to you | | |
| 5 | "I don't understand. Can you rephrase?" | | |

---

## Exercise 3: Design Your Own Agent (10 minutes)

**Task:** Design an agent for a real-world use case in YOUR context.

**Template:**
```
Use Case: [What task should the agent handle?]

Target User: [Who is this for?]

Required Capabilities:
1. _______________
2. _______________
3. _______________

Tools Needed:
- _______________
- _______________

Chain of Actions:
1. _______________
2. _______________
3. _______________
4. _______________

Memory Needed:
- _______________
```

---

# DISCUSSION QUESTIONS

1. **Reflection:** What's a task you do repeatedly that an agent could automate? What capabilities would it need?

2. **Ethics:** If an agent makes a mistake (books wrong flight, sends email to wrong person), who is responsible - the user, the developer, or the AI company?

3. **Future:** What happens to "chatbot" jobs as agents become more capable? What new jobs might emerge?

4. **Privacy:** Agents need access to your data (email, calendar, files) to be useful. What are the privacy implications?

---

# QUIZ

## Quiz: Module 1 - The Agentic Revolution

### Question 1 (1 point)
What are the 5 core capabilities of an AI Agent Framework?

A) Reading, Writing, Math, Logic, Creativity  
B) Autonomous Execution, Tool Use, Memory, Decision Making, Action Chaining  
C) Input, Processing, Output, Storage, Network  
D) Language, Vision, Audio, Action, Planning

**Correct Answer:** B

---

### Question 2 (1 point)
What's the main difference between a chatbot and an agent?

A) Chatbots use AI, agents use rules  
B) Chatbots are reactive, agents are proactive  
C) Agents are slower than chatbots  
D) Chatbots can see, agents cannot

**Correct Answer:** B

---

### Question 3 (1 point)
Which type of memory stores learned facts about user preferences?

A) Working Memory  
B) Episodic Memory  
C) Semantic Memory  
D) Short-term Memory

**Correct Answer:** C

---

### Question 4 (1 point)
In the agent loop, what happens after "ACT"?

A) Think again  
B) Observe results  
C) Decide next action  
D) End

**Correct Answer:** B

---

### Question 5 (1 point)
What makes 2023+ different from previous AI waves?

A) AI can now read  
B) Generative AI + Agents combined  
C) AI is faster  
D) AI is cheaper

**Correct Answer:** B

---

### Question 6 (1 point)
What's "action chaining" in agent terms?

A) Linking multiple agents together  
B) Breaking complex tasks into sequences of smaller actions  
C) Connecting tools to APIs  
D) Sequencing API calls

**Correct Answer:** B

---

### Question 7 (2 points)
A user asks an agent to "plan my vacation to Japan." 

List 3 actions the agent might chain together:

1. _______________
2. _______________
3. _______________

**Sample Answers:**
1. Search flights and hotels
2. Check visa requirements
3. Create daily itinerary

---

### Question 8 (2 points)
Why is "autonomous execution" important for business use cases?

**Sample Answer:** 
It allows agents to complete multi-step tasks without requiring constant human oversight, enabling 24/7 productivity and freeing up human time for higher-value work.

---

## Quiz Answer Key

| Q | Answer |
|---|--------|
| 1 | B |
| 2 | B |
| 3 | C |
| 4 | B |
| 5 | B |
| 6 | B |
| 7 | (Open) |
| 8 | (Open) |

---

# VISUAL AIDS SUMMARY

## Key Diagrams (for reference)

1. **AI Agent Framework** - Perception, Planning, Action, Memory
2. **The Agent Loop** - Think → Decide → Act → Observe
3. **Chatbot vs Agent** - Reactive vs Proactive
4. **The Convergence** - LLMs + APIs = Agents
5. **Agent Adoption Timeline** - Innovators to Laggards

---

# SUMMARY

## Key Takeaways

✅ **AI Agent Framework** = scaffolding that gives LLMs tools, memory, and action capabilities

✅ **5 Core Capabilities:**
1. Autonomous Execution
2. Tool Use  
3. Memory & Context
4. Decision Making
5. Action Chaining

✅ **Chatbot vs Agent:** Reactive vs Proactive

✅ **The Shift:** We're moving from "ask for answer" to "give task, get result"

✅ **Why Now:** Powerful LLMs + Reliable APIs = Practical Agents

---

# NEXT STEPS

After completing this module:

1. ✅ You understand agent fundamentals
2. ⏭️ Move to **Module 2: The Tech Stack of 2026**
3. 🔄 Schedule spaced repetition review (1 day, 3 days, 7 days)

---

*Module 1 complete. You're ready for the technical deep dive!*
