# TOOLS.md — AI Learning Orchestrator

## Discovery Questions

### 1. Current Role
```
What is your current role?
- Entrepreneur/Business Owner
- Employee (Tech)
- Employee (Non-Tech)
- Student
- Parent/Caregiver
- Educator
- Consultant
- Other
```

### 2. Future Role/Goal
```
What role or goal are you working toward?
- AI Agent Developer
- AI Consultant
- AI Product Manager
- Technical Lead
- Business Integration Lead
- Personal Use (Family)
- Personal Development
- Teaching Others
- Other
```

### 3. Business/Side Hustle
```
Do you have a business or side hustle?
- Yes - AI Agency
- Yes - SaaS/Product
- Yes - Consulting
- Yes - Content Creator
- Yes - Other
- No - Just learning
- No - For my employer
```

### 4. Business Goals
```
What are your business goals? (Select up to 3)
- Automate operations
- Build AI products
- Offer AI services
- Reduce costs
- Improve customer experience
- Scale team
- Other
```

### 5. Personal Context
```
Is this for personal use?
- Yes - Family (managing kids, household)
- Yes - Personal development
- Yes - Both
- No - Purely business
```

### 6. Learning Style
```
What's your preferred learning style?
- Visual (diagrams, videos)
- Reading (text, articles)
- Auditory (podcasts, discussions)
- Hands-on (exercises, projects)
- Mixed (varied approach)
```

### 7. Time Availability
```
How much time can you dedicate?
- 15 min/day (micro-learning)
- 30 min/day
- 1 hour/day
- Weekend warrior
- Intensive (full day)
```

### 8. Prior Knowledge
```
What's your prior AI knowledge?
- Complete beginner
- Some exposure
- Regular user
- Developer experience
- Expert level
```

## Customization Logic

### Role → Content Priority

| Current Role | Priority Modules |
|--------------|----------------|
| Non-Tech | Module 1, 4, 5 first |
| Tech | Module 2, 3, 5 first |
| Parent | Module 4 (neurodiversity), 5 |
| Educator | All modules + teaching approach |
| Entrepreneur | Module 4 (business use cases) |

### Business → Examples

| Business Type | Customized Examples |
|---------------|--------------------|
| AI Agency | Client workflows, service delivery |
| SaaS | Product integration, automation |
| Consulting | Assessment, delivery frameworks |
| Content | Content creation, distribution |
| Personal | Family use, productivity |

### Learning Style → Delivery

| Style | Format |
|-------|--------|
| Visual | Diagrams, videos, infographics |
| Reading | Detailed text, articles |
| Auditory | Discussion, voice notes |
| Hands-on | Exercises, projects |

## Module Agents

Each module has its own specialized agent:

### Module 1: Agentic Revolution
- Focus: Concept understanding
- Duration: 45 minutes

### Module 2: Tech Stack of 2026
- Focus: Technical foundations
- Duration: 45 minutes

### Module 3: Deep Dive into OpenClaw
- Focus: Technical mastery
- Duration: 60 minutes

### Module 4: Strategy, Ethics, Application
- Focus: Practical implementation
- Duration: 30 minutes

### Module 5: Knowledge Check
- Focus: Assessment and practice
- Duration: Variable

## Learning Techniques

### Spaced Repetition Schedule
- Review after 1 day
- Review after 3 days
- Review after 7 days
- Review after 14 days
- Review after 30 days

### Project Options

| Level | Project |
|-------|---------|
| Beginner | Create a simple prompt |
| Intermediate | Build a 2-step workflow |
| Advanced | Design a full agent system |
| Expert | Deploy to production |

---

*Tools to orchestrate your learning.*
