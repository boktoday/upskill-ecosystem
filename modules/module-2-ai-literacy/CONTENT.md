# AGENTS.md — Module 2: AI Literacy

## Role

Teach foundational AI concepts: how LLMs work, prompt engineering, context management, and tool selection

## Agent ID

`module-2-ai-literacy`

## Duration

45 minutes

## Learning Objectives

By the end of this module, students will be able to:
1. Explain how LLMs generate text through token prediction
2. Apply basic prompt engineering techniques to improve AI responses
3. Understand context windows and manage memory effectively
4. Select appropriate tools for different AI tasks

---

# LESSON CONTENT

## 2.1 Understanding LLMs (12 minutes)

### What Is an LLM?

A **Large Language Model (LLM)** is a type of AI trained on massive amounts of text data. It learns patterns in language and uses those patterns to predict what comes next.

Think of it like autocomplete on steroids — but instead of completing a word, it can complete paragraphs, code, or entire conversations.

**Key Players:**
- **OpenAI:** GPT-4, GPT-4o
- **Anthropic:** Claude 3.5, Claude 3
- **Google:** Gemini 1.5
- **Meta:** Llama 3
- **MiniMax:** M2.1, M2.5

---

### How LLMs Actually Work

```
┌─────────────────────────────────────────────────────────────────────┐
│                    HOW AN LLM GENERATES TEXT                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   INPUT: "The capital of France is"                                │
│              │                                                     │
│              ▼                                                     │
│   ┌─────────────────────────────────────────────────────────┐     │
│   │                    TOKENIZATION                           │     │
│   │  "The" → [1, 2]    "capital" → [3, 4, 5, 6, 7]          │     │
│   │  "of" → [8]        "France" → [9, 10, 11]              │     │
│   │  "is" → [12]                                           │     │
│   └─────────────────────────────────────────────────────────┘     │
│                          │                                          │
│                          ▼                                          │
│   ┌─────────────────────────────────────────────────────────┐     │
│   │                 NEURAL NETWORK                           │     │
│   │                                                          │     │
│   │   [1,2] ──┐                                              │     │
│   │   [3,4,5]─┼──►  Predict next token probabilities       │     │
│   │   [6,7]  ─┘                                              │     │
│   │   ...    ──┬                                              │     │
│   │            │                                              │     │
│   │   Output: "Paris" (87%)  "Lyon" (5%)  "Nice" (2%) ...   │     │
│   └─────────────────────────────────────────────────────────┘     │
│                          │                                          │
│                          ▼                                          │
│   ┌─────────────────────────────────────────────────────────┐     │
│   │                  SAMPLING                                 │     │
│   │                                                          │     │
│   │   Select next token based on:                           │     │
│   │   • Temperature (creativity vs precision)              │     │
│   │   • Top-p (nucleus sampling)                            │     │
│   │   • Top-k (top k candidates)                            │     │
│   └─────────────────────────────────────────────────────────┘     │
│                          │                                          │
│                          ▼                                          │
│   OUTPUT: "The capital of France is Paris."                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Tokens: The Building Blocks

LLMs don't understand words — they understand **tokens**. A token is typically:
- ~4 characters of English text
- 1 word on average
- A portion of code or other languages

**Why this matters:**
- **Context limits** are measured in tokens, not words
- Longer prompts = fewer tokens for the response
- Some languages use more tokens than others

```
┌─────────────────────────────────────────────────────────────────┐
│                        TOKEN EXAMPLES                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   "Hello"     →  1 token                                         │
│   "world"     →  1 token                                         │
│   "Hello world" →  2 tokens                                      │
│   "AI"        →  1 token                                         │
│   "🤖"        →  1-2 tokens (emoji is complex!)                 │
│   "12345"     →  1 token                                         │
│   "$50.00"    →  1 token                                         │
│                                                                 │
│   📝 Rule of thumb: 1 token ≈ ¾ of a word                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### Temperature: Creativity vs Precision

The **temperature** setting controls how "random" the model's output is.

```
┌─────────────────────────────────────────────────────────────────────┐
│                      TEMPERATURE SETTINGS                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Temperature = 0                                                 │
│   ┌─────────────────────────────────────────────────────────────┐ │
│   │ "What is 2+2?" → "4"     (Deterministic, always same)       │ │
│   └─────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   Temperature = 0.7 (Recommended for most tasks)                  │
│   ┌─────────────────────────────────────────────────────────────┐ │
│   │ "Write a poem about cats" → Varies each time, creative      │ │
│   └─────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   Temperature = 1.0+                                              │
│   ┌─────────────────────────────────────────────────────────────┐ │
│   │ "What is 2+2?" → Could say "5", "window", "purple"          │ │
│   │                  (High randomness, may not make sense)      │ │
│   └─────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   📝 Best Practice:                                               │
│   • Math/Coding: temperature = 0                                  │
│   • Writing/Creative: temperature = 0.7-0.9                       │
│   • General use: temperature = 0.7                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2.2 Prompt Engineering Basics (12 minutes)

### What Is Prompt Engineering?

**Prompt engineering** is the art and science of crafting inputs that get the best outputs from AI models.

It's like learning to ask better questions — the quality of your prompt directly affects the quality of the response.

```
┌─────────────────────────────────────────────────────────────────────┐
│                   PROMPT ENGINEERING SPECTRUM                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   BAD PROMPT                      GOOD PROMPT                      │
│   ┌─────────────┐                ┌─────────────────────────────┐   │
│   │ "Write about │                │ "Write a 300-word blog post │   │
│   │  AI"        │                │  about how AI improves      │   │
│   │             │                │  productivity. Include:     │   │
│   │             │                │  • 3 specific examples      │   │
│   │             │                │  • 1 caution about overuse  │   │
│   │             │                │  Tone: professional but      │   │
│   │             │                │  accessible. Format: intro, │   │
│   │             │                │  body, conclusion."          │   │
│   └─────────────┘                └─────────────────────────────┘   │
│                                                                     │
│   Result: Vague,                  Result: Focused, useful,        │
│   generic response                actionable content              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Core Prompting Techniques

#### 1. Be Specific

```
┌─────────────────────────────────────────────────────────────────┐
│                      BE SPECIFIC                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ❌ "Write about Python"                                      │
│                                                                 │
│   ✅ "Explain Python list comprehensions to a beginner.        │
│      Include 3 code examples: one simple, one with filter,    │
│      one nested. Keep explanations under 50 words each."      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 2. Give Role/Context

```
┌─────────────────────────────────────────────────────────────────┐
│                      GIVE ROLE/CONTEXT                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ❌ "How do I fix this bug?"                                  │
│                                                                 │
│   ✅ "You are a senior Python developer with 10 years of       │
│      experience. I'm a beginner who encountered this error     │
│      in my first Django project. Explain what's wrong and     │
│      how to fix it in simple terms."                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 3. Structure Your Request

```
┌─────────────────────────────────────────────────────────────────┐
│                   STRUCTURE YOUR REQUEST                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Use formatting to make your intent clear:                    │
│                                                                 │
│   ❌ "Give me a workout plan eat better feel better"          │
│                                                                 │
│   ✅ """                                                        │
│      Goal: Feel better and lose 5 lbs                          │
│      Constraints: Vegetarian, no gym access, 30 min/day        │
│      Format:                                                    │
│      - Morning routine                                         │
│      - Evening routine                                          │
│      - 3 meal ideas per day                                    │
│      """                                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 4. Few-Shot Examples

Show the model what you want by example:

```
┌─────────────────────────────────────────────────────────────────┐
│                     FEW-SHOT PROMPTING                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ❌ "Convert these to JSON"                                   │
│                                                                 │
│   ✅ "Convert these to JSON:                                    │
│                                                                 │
│      Example:                                                   │
│      Input: Apple, Red, Round                                  │
│      Output: {\"fruit\": \"Apple\", \"color\": \"Red\",        │
│               \"shape\": \"Round\"}                              │
│                                                                 │
│      Now convert:                                               │
│      Banana, Yellow, Long                                       │
│   """                                                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### OpenClaw Prompt Example

Here's how you might prompt an OpenClaw agent:

```
┌─────────────────────────────────────────────────────────────────────┐
│                 OPENCLAW PROMPT EXAMPLE                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   """                                                              │
│   Task: Research latest AI news and summarize in 3 bullet points  │
│                                                                     │
│   Role: Tech journalist who writes for business executives        │
│                                                                     │
│   Context: I need to prepare for a board meeting in 2 hours        │
│                                                                     │
│   Constraints:                                                     │
│   - Focus on business impact, not technical details               │
│   - Include any major announcements from big tech companies       │
│   - Maximum 3 sentences per bullet point                           │
│                                                                     │
│   Tools to use:                                                    │
│   - web_search (search for "AI news March 2026")                  │
│   - Read and summarize the top 5 results                          │
│                                                                     │
│   Output format:                                                   │
│   - Date of news                                                   │
│   - Key development (1-2 sentences)                               │
│   - Business implication (1 sentence)                            │
│   """                                                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Common Prompt Patterns

| Pattern | When to Use | Example |
|---------|-------------|---------|
| **Role** | Get domain-specific responses | "You are a lawyer..." |
| **Template** | Structured output | "Write in this format..." |
| **Chain of Thought** | Complex reasoning | "Think step by step..." |
| **Few-Shot** | Show examples | "Example: X → Y" |
| **Constraints** | Limit output | "Don't mention..." |
| **Style** | Match tone | "Write like a pirate..." |

---

## 2.3 Context Windows and Memory (10 minutes)

### What Is a Context Window?

A **context window** is the maximum amount of text (measured in tokens) an LLM can consider at once. It's like the model's "attention span."

```
┌─────────────────────────────────────────────────────────────────────┐
│                      CONTEXT WINDOW VISUALIZATION                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Model: Claude 3.5           Context Window: 200K tokens          │
│   ┌─────────────────────────────────────────────────────────────┐ │
│   │  ┌─────────────────────────────────────────────────────────┐ │ │
│   │  │                    CONTEXT WINDOW                       │ │ │
│   │  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐      │ │ │
│   │  │  │Token│ │Token│ │Token│ │Token│ │Token│ │ ... │      │ │ │
│   │  │  │  1  │ │  2  │ │  3  │ │  4  │ │  5  │ │     │      │ │ │
│   │  │  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘      │ │ │
│   │  │     │       │       │       │       │       │          │ │ │
│   │  │     ▼       ▼       ▼       ▼       ▼       ▼          │ │ │
│   │  │  ┌───────────────────────────────────────────────┐    │ │ │
│   │  │  │            ATTENTION MECHANISM                 │    │ │ │
│   │  │  │  (Model "attends" to all tokens at once)       │    │ │ │
│   │  │  └───────────────────────────────────────────────┘    │ │ │
│   │  │                      │                                 │ │ │
│   │  │                      ▼                                 │ │ │
│   │  │              ┌──────────────┐                         │ │ │
│   │  │              │ Output Token │                         │ │ │
│   │  │              │  Prediction  │                         │ │ │
│   │  │              └──────────────┘                         │ │ │
│   │  └─────────────────────────────────────────────────────────┘ │ │
│   └─────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   📝 If your prompt is 100K tokens, you have 100K for context    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Current Context Limits by Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                   CONTEXT WINDOWS BY MODEL                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Model                Context Window    ~Words                    │
│   ─────────────────────────────────────────────────────────────     │
│   GPT-4o               128K tokens        ~96,000 words              │
│   Claude 3.5 Sonnet    200K tokens       ~150,000 words             │
│   Gemini 1.5 Pro      2M tokens          ~1.5M words               │
│   Llama 3 70B         8K tokens          ~6,000 words              │
│   MiniMax M2.5        1M+ tokens         ~750,000 words            │
│                                                                     │
│   📝 Note: Larger contexts are slower and more expensive           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Memory Types in AI Systems

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TYPES OF AI MEMORY                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌───────────────────────────────────────────────────────────┐    │
│   │  1. CONTEXT WINDOW (Working Memory)                       │    │
│   │  ─────────────────────────────────────────────             │    │
│   │  • What's currently in the conversation                  │    │
│   │  • Disappears when session ends                           │    │
│   │  • Example: "We were discussing the marketing plan..."     │    │
│   └───────────────────────────────────────────────────────────┘    │
│                    │                                                │
│                    ▼                                                │
│   ┌───────────────────────────────────────────────────────────┐    │
│   │  2. SYSTEM PROMPT (Instructions)                          │    │
│   │  ─────────────────────────────────────────────             │    │
│   │  • Fixed instructions you provide at start               │    │
│   │  • Examples: "You are a helpful assistant...",            │    │
│   │              "Always respond in Spanish..."               │    │
│   └───────────────────────────────────────────────────────────┘    │
│                    │                                                │
│                    ▼                                                │
│   ┌───────────────────────────────────────────────────────────┐    │
│   │  3. EXTERNAL MEMORY (Files, Database)                     │    │
│   │  ─────────────────────────────────────────────             │    │
│   │  • Persistent storage beyond sessions                     │    │
│   │  • Example: Read your notes, reference documents         │    │
│   │  • OpenClaw can read/write files, access knowledge bases  │    │
│   └───────────────────────────────────────────────────────────┘    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Managing Context Effectively

**The "Summary" Technique:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONTEXT MANAGEMENT                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   LONG CONVERSATION PROBLEM:                                   │
│   ┌─────────────────────────────────────────────────────┐     │
│   │ Message 1: "Help me write code"                     │     │
│   │ Message 2: "Make it more efficient"                 │     │
│   │ Message 3: "Actually, use Python not JS"           │     │
│   │ ...                                                  │     │
│   │ Message 50: "Wait, what are we building again?"    │     │
│   └─────────────────────────────────────────────────────┘     │
│                                                                 │
│   SOLUTION: Periodically summarize                              │
│   ┌─────────────────────────────────────────────────────┐     │
│   │ "So far we've created a Python script that:         │     │
│   │  - Scrapes product prices from Amazon               │     │
│   │  - Stores prices in a CSV file                       │     │
│   │  - Runs daily via cron                               │     │
│   │  Current task: Add email notifications"             │     │
│   └─────────────────────────────────────────────────────┘     │
│                                                                 │
│   📝 OpenClaw Tip: Keep your MEMORY.md updated so the         │
│      agent remembers important context across sessions        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2.4 Tool Selection and Integration (11 minutes)

### Why Tools Matter

LLMs are powerful but limited — they can only generate text. **Tools** extend their capabilities to interact with the real world.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LLM + TOOLS = SUPERPOWER                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   LLM ALONE:                                                       │
│   ┌─────────────┐                                                 │
│   │             │    Input: "What's the weather?"               │
│   │  Generate   │ ──────────────────────► "Let me check..."     │
│   │   Text      │    (Can only guess or say "I can't")         │
│   │             │                                                 │
│   └─────────────┘                                                 │
│                                                                     │
│   LLM + TOOLS:                                                     │
│   ┌─────────────┐     ┌──────────────┐                         │
│   │             │     │  WEATHER API  │                         │
│   │  Generate   │ ───►│  + Search     │ ──► "It's 72°F"       │
│   │   Text      │     │  + Calculator │                         │
│   │             │     │  + Browser    │                         │
│   └─────────────┘     └──────────────┘                         │
│                                                                     │
│   📝 Tools turn "I don't know" into "Let me find out"             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Tool Categories

```
┌─────────────────────────────────────────────────────────────────────┐
│                      TOOL CATEGORIES                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   📡 INFORMATION GATHERING                                         │
│   ├── web_search      → Find current information                  │
│   ├── web_fetch      → Read specific pages                        │
│   ├── browser        → Interact with websites                     │
│   └── pdf            → Analyze documents                           │
│                                                                     │
│   💻 COMPUTATION & CODE                                            │
│   ├── exec           → Run shell commands                         │
│   ├── code_interpreter → Execute code safely                       │
│   └── ai_model       → Use other AI models                        │
│                                                                     │
│   📝 COMMUNICATION                                                  │
│   ├── message        → Send messages (Telegram, Discord, WA)      │
│   ├── email          → Send/receive emails                        │
│   └── tts            → Text to speech                             │
│                                                                     │
│   💾 DATA & FILES                                                  │
│   ├── read           → Read files                                 │
│   ├── write          → Create/update files                        │
│   ├── edit           → Modify files                               │
│   └── memory         → Store/retrieve memories                    │
│                                                                     │
│   🎨 MEDIA & CREATIVE                                              │
│   ├── canvas         → Generate images, UI                        │
│   ├── image_generation → Create images from text                  │
│   └── video          → Video analysis/generation                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Tool Selection Flowchart

```
┌─────────────────────────────────────────────────────────────────────┐
│                  WHICH TOOL SHOULD I USE?                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────┐                                             │
│   │ What do you     │                                             │
│   │ need to do?     │                                             │
│   └────────┬────────┘                                             │
│            │                                                       │
│            ▼                                                       │
│   ┌─────────────────────────────────────────────────────────┐      │
│   │                                                         │      │
│   │  Need current info?  ────►  web_search                 │      │
│   │         │                                                │      │
│   │  Need to read a page?  ───► web_fetch                  │      │
│   │         │                                                │      │
│   │  Need to run code/commands?  ──► exec                  │      │
│   │         │                                                │      │
│   │  Need to send a message?  ────► message                │      │
│   │         │                                                │      │
│   │  Need to create/edit file?  ──► read/write/edit       │      │
│   │         │                                                │      │
│   │  Need to remember for later?  ──► write to MEMORY.md   │      │
│   │         │                                                │      │
│   │  Need AI to analyze image?  ──► vision-capable model   │      │
│   │         │                                                │      │
│   │  Need image generation?  ─────► canvas/image_gen       │      │
│   │         │                                                │      │
│   │  Not sure?  ──────────────────► web_search first!      │      │
│   │                                                         │      │
│   └─────────────────────────────────────────────────────────┘      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### OpenClaw Tool Examples

```
┌─────────────────────────────────────────────────────────────────────┐
│                    OPENCLAW TOOL EXAMPLES                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   📡 WEB SEARCH                                                    │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ web_search({query: "OpenClaw vs LangChain 2026"})          │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│   📄 READ FILE                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ read({path: "~/projects/my-app/README.md"})                │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│   💬 SEND MESSAGE (Telegram)                                       │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ message({                                                   │  │
│   │   channel: "telegram",                                     │  │
│   │   action: "send",                                          │  │
│   │   target: "@mychat",                                       │  │
│   │   message: "Meeting starting in 5 minutes!"               │  │
│   │ })                                                         │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│   💻 RUN COMMAND                                                   │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ exec({command: "npm run build", workdir: "~/projects/web"})│  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│   🎨 GENERATE IMAGE                                                │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ canvas({                                                    │  │
│   │   action: "present",                                      │  │
│   │   fn: "generate",                                         │  │
│   │   prompt: "A friendly robot teaching humans about AI"     │  │
│   │ })                                                         │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Tool Integration in Practice

```
┌─────────────────────────────────────────────────────────────────────┐
│               TOOL CHAINING EXAMPLE                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Task: "Find the latest OpenClaw version and check if my          │
│          installation is up to date"                               │
│                                                                     │
│   ┌───────────────────────────────────────────────────────────┐    │
│   │ STEP 1: web_search                                        │    │
│   │ Query: "OpenClaw latest version 2026"                     │    │
│   │ → Returns: "OpenClaw 3.2.0 released March 2026"         │    │
│   └───────────────────────────────────────────────────────────┘    │
│                           │                                        │
│                           ▼                                        │
│   ┌───────────────────────────────────────────────────────────┐    │
│   │ STEP 2: exec                                              │    │
│   │ Command: "openclaw --version"                             │    │
│   │ → Returns: "OpenClaw 3.1.8"                               │    │
│   └───────────────────────────────────────────────────────────┘    │
│                           │                                        │
│                           ▼                                        │
│   ┌───────────────────────────────────────────────────────────┐    │
│   │ STEP 3: ANALYZE & RESPOND                                 │    │
│   │ Compare: 3.2.0 vs 3.1.8                                   │    │
│   │ → "Your installation is out of date. Run:                │    │
│   │    npm install -g openclaw@latest"                        │    │
│   └───────────────────────────────────────────────────────────┘    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

# EXERCISES

## Exercise 1: Prompt Engineering Practice (8 minutes)

Improve these weak prompts:

| # | Weak Prompt | Improved Version |
|---|-------------|-------------------|
| 1 | "Write about dogs" | |
| 2 | "Help me with code" | |
| 3 | "What's the news?" | |

**Then test your improved prompts!**

---

## Exercise 2: Token Counting (5 minutes)

Estimate how many tokens each input uses:

```
"The cat sat on the mat." → ~______ tokens

"Artificial intelligence is transforming how we work, live, and interact 
with technology. From chatbots to autonomous agents, AI is becoming 
ubiquitous in modern society." → ~______ tokens
```

---

## Exercise 3: Tool Selection (7 minutes)

Match the task to the right tool:

| Task | Best Tool |
|------|-----------|
| Find current stock price | |
| Read a PDF report | |
| Send a Telegram message | |
| Create a new file | |
| Run Python code | |
| Generate an image | |

**Tools:** web_search, pdf, message, write, exec, canvas

---

## Exercise 4: Context Management (5 minutes)

You're having a long conversation with an AI assistant. The context is getting full. What can you do?

1. _______________
2. _______________
3. _______________

---

# DISCUSSION QUESTIONS

1. **Limitations:** LLMs can "hallucinate" — make up information that sounds true but isn't. How can prompt engineering help reduce hallucinations? What are the risks of relying on AI-generated information?

2. **Context Ethics:** AI systems can now read entire books in context. What are the implications for copyright? Should AI be allowed to "read" copyrighted works for training?

3. **Tool Power:** As AI gets better tools, it becomes more capable. What happens when AI can access your bank accounts, send emails, and make purchases? What safeguards are needed?

4. **Memory & Privacy:** OpenClaw can remember things across sessions. What happens if it remembers sensitive information (passwords, health data)? How should AI memory be managed?

5. **The Future:** Some predict we'll have 1M+ token contexts soon. What becomes possible when an AI can "read" your entire life — emails, messages, files, photos — and remember everything?

---

# QUIZ

## Quiz: Module 2 - AI Literacy

### Question 1 (1 point)
What does an LLM actually "predict" when generating text?

A) The correct answer to a question  
B) The next token in a sequence  
C) What the user wants to hear  
D) Whether the user is telling the truth

**Correct Answer:** B

---

### Question 2 (1 point)
What is "temperature" in LLM settings?

A) How fast the model responds  
B) How "hot" or excited the model gets  
C) The balance between random and predictable output  
D) The amount of computing power used

**Correct Answer:** C

---

### Question 3 (1 point)
What's the recommended temperature for coding tasks?

A) 0.0 (deterministic)  
B) 0.7 (balanced)  
C) 1.0+ (creative)  
D) Doesn't matter

**Correct Answer:** A

---

### Question 4 (1 point)
Which prompting technique involves showing examples?

A) Role-playing  
B) Chain of thought  
C) Few-shot prompting  
D) Constraint-based

**Correct Answer:** C

---

### Question 5 (1 point)
What is a "context window"?

A) The UI where you type prompts  
B) The maximum tokens an LLM can consider at once  
C) The amount of memory on your computer  
D) The chat history displayed on screen

**Correct Answer:** B

---

### Question 6 (1 point)
Which tool would you use to find current information on the web?

A) read  
B) web_search  
C) exec  
D) canvas

**Correct Answer:** B

---

### Question 7 (2 points)
Name 3 techniques to manage a long conversation that exceeds the context limit:

1. _______________
2. _______________
3. _______________

**Sample Answers:**
1. Summarize the conversation periodically
2. Start new sessions with context from previous ones
3. Use external files/MEMORY.md to store important info

---

### Question 8 (2 points)
Why is "being specific" important in prompt engineering?

**Sample Answer:**
Specific prompts give the AI clearer guidance on what output is expected, reducing ambiguity and improving the relevance and quality of responses. Vague prompts lead to generic or unrelated answers.

---

## Quiz Answer Key

| Q | Answer |
|---|--------|
| 1 | B |
| 2 | C |
| 3 | A |
| 4 | C |
| 5 | B |
| 6 | B |
| 7 | (Open) |
| 8 | (Open) |

---

# VISUAL AIDS SUMMARY

## Key Diagrams (for reference)

1. **LLM Text Generation** - Tokenization → Neural Network → Sampling → Output
2. **Temperature Settings** - 0 (precise) vs 0.7 (balanced) vs 1.0+ (random)
3. **Context Window** - Attention mechanism visualization
4. **Memory Types** - Context, System Prompt, External Memory
5. **Tool Categories** - Information, Computation, Communication, Files, Media
6. **Tool Selection Flowchart** - Decision tree for choosing tools

---

# SUMMARY

## Key Takeaways

✅ **LLMs** predict tokens (not words), trained on massive text data

✅ **Temperature** controls creativity vs precision:
- 0 = deterministic (coding, math)
- 0.7 = balanced (general use)
- 1.0+ = creative (writing, brainstorming)

✅ **Prompt Engineering** improves outputs through:
- Being specific
- Giving role/context
- Providing structure
- Using few-shot examples

✅ **Context Window** = max tokens the model can see at once
- Manage by summarizing, external memory, or starting fresh

✅ **Tools** extend AI capabilities:
- web_search → current info
- read/write → files
- exec → run commands
- message → send communications

✅ **Tool Selection** depends on your goal — pick the right tool for the task

---

# NEXT STEPS

After completing this module:

1. ✅ You understand how LLMs work
2. ✅ You can write effective prompts
3. ✅ You know how to manage context
4. ⏭️ Move to **Module 3: OpenClaw Deep Dive**
5. 🔄 Schedule spaced repetition review (1 day, 3 days, 7 days)

---

*Module 2 complete. You now have foundational AI literacy!*