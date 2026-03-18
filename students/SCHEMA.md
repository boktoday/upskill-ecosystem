# JSON Schema — Student Progress Tracking

## Overview

This schema tracks individual student progress through the AI Upskill curriculum, including module completion, quiz scores, and spaced repetition review schedules.

## Schema Version

`1.0.0`

---

## Student Profile Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["studentId", "createdAt", "discovery", "progress"],
  "properties": {
    "studentId": {
      "type": "string",
      "pattern": "^student-[0-9]{3,}$",
      "example": "student-001"
    },
    "createdAt": {
      "type": "string",
      "format": "date-time",
      "example": "2024-01-15T10:30:00Z"
    },
    "updatedAt": {
      "type": "string",
      "format": "date-time"
    },
    "discovery": {
      "$ref": "#/definitions/DiscoveryAnswers"
    },
    "progress": {
      "$ref": "#/definitions/ProgressTracker"
    },
    "settings": {
      "$ref": "#/definitions/StudentSettings"
    }
  },
  "definitions": {
    "DiscoveryAnswers": {
      "type": "object",
      "required": ["currentRole", "targetRole", "learningStyle", "timeAvailable", "priorKnowledge"],
      "properties": {
        "currentRole": {
          "type": "string",
          "enum": ["entrepreneur", "employee-tech", "employee-non-tech", "student", "parent", "educator", "consultant", "other"]
        },
        "targetRole": {
          "type": "string",
          "enum": ["agent-developer", "ai-consultant", "product-manager", "technical-lead", "business-integration", "personal-use", "personal-development", "teaching", "other"]
        },
        "businessContext": {
          "type": "object",
          "properties": {
            "hasBusiness": { "type": "boolean" },
            "businessType": {
              "type": "string",
              "enum": ["ai-agency", "saas", "consulting", "content-creator", "other", "none"]
            },
            "businessGoals": {
              "type": "array",
              "items": { "type": "string" }
            }
          }
        },
        "personalContext": {
          "type": "object",
          "properties": {
            "isPersonal": { "type": "boolean" },
            "forFamily": { "type": "boolean" },
            "forDevelopment": { "type": "boolean" }
          }
        },
        "learningStyle": {
          "type": "string",
          "enum": ["visual", "reading", "auditory", "hands-on", "mixed"]
        },
        "timeAvailable": {
          "type": "string",
          "enum": ["15min", "30min", "1hour", "weekend", "intensive"]
        },
        "priorKnowledge": {
          "type": "string",
          "enum": ["beginner", "some-exposure", "regular-user", "developer", "expert"]
        }
      }
    },
    "ProgressTracker": {
      "type": "object",
      "properties": {
        "curriculum": {
          "$ref": "#/definitions/Curriculum"
        },
        "modules": {
          "type": "object",
          "additionalProperties": {
            "$ref": "#/definitions/ModuleProgress"
          }
        },
        "assessments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/AssessmentResult"
          }
        },
        "projects": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ProjectCompletion"
          }
        }
      }
    },
    "Curriculum": {
      "type": "object",
      "properties": {
        "generatedAt": {
          "type": "string",
          "format": "date-time"
        },
        "moduleOrder": {
          "type": "array",
          "items": { "type": "string" }
        },
        "customizations": {
          "type": "object"
        }
      }
    },
    "ModuleProgress": {
      "type": "object",
      "required": ["status", "startedAt"],
      "properties": {
        "status": {
          "type": "string",
          "enum": ["not-started", "in-progress", "completed", "needs-review"]
        },
        "startedAt": {
          "type": "string",
          "format": "date-time"
        },
        "completedAt": {
          "type": "string",
          "format": "date-time"
        },
        "timeSpentMinutes": {
          "type": "integer"
        },
        "quizScore": {
          "type": "integer",
          "minimum": 0,
          "maximum": 100
        },
        "keyConcepts": {
          "type": "array",
          "items": { "type": "string" }
        },
        "notes": {
          "type": "string"
        }
      }
    },
    "AssessmentResult": {
      "type": "object",
      "required": ["moduleId", "score", "completedAt"],
      "properties": {
        "assessmentId": {
          "type": "string"
        },
        "moduleId": {
          "type": "string"
        },
        "score": {
          "type": "integer",
          "minimum": 0,
          "maximum": 100
        },
        "questionsCorrect": {
          "type": "integer"
        },
        "questionsTotal": {
          "type": "integer"
        },
        "completedAt": {
          "type": "string",
          "format": "date-time"
        },
        "areasForImprovement": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },
    "ProjectCompletion": {
      "type": "object",
      "required": ["projectId", "completedAt"],
      "properties": {
        "projectId": {
          "type": "string"
        },
        "title": {
          "type": "string"
        },
        "difficulty": {
          "type": "string",
          "enum": ["beginner", "intermediate", "advanced", "expert"]
        },
        "completedAt": {
          "type": "string",
          "format": "date-time"
        },
        "submission": {
          "type": "string"
        }
      }
    },
    "StudentSettings": {
      "type": "object",
      "properties": {
        "notificationsEnabled": {
          "type": "boolean",
          "default": true
        },
        "reminderTime": {
          "type": "string",
          "example": "09:00"
        },
        "difficulty": {
          "type": "string",
          "enum": ["standard", "accelerated", "comprehensive"]
        }
      }
    }
  }
}
```

---

## Spaced Repetition Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["studentId", "reviewQueue"],
  "properties": {
    "studentId": {
      "type": "string"
    },
    "reviewQueue": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/ReviewItem"
      }
    },
    "lastReviewDate": {
      "type": "string",
      "format": "date-time"
    }
  },
  "definitions": {
    "ReviewItem": {
      "type": "object",
      "required": ["conceptId", "moduleId", "nextReviewDate", "interval", "easeFactor"],
      "properties": {
        "conceptId": {
          "type": "string",
          "example": "agent-framework-5-capabilities"
        },
        "conceptName": {
          "type": "string",
          "example": "AI Agent Framework 5 Core Capabilities"
        },
        "moduleId": {
          "type": "string",
          "example": "module-1"
        },
        "learnedAt": {
          "type": "string",
          "format": "date-time"
        },
        "nextReviewDate": {
          "type": "string",
          "format": "date-time"
        },
        "interval": {
          "type": "integer",
          "description": "Days until next review",
          "example": 1
        },
        "repetitions": {
          "type": "integer",
          "minimum": 0,
          "example": 0
        },
        "easeFactor": {
          "type": "number",
          "minimum": 1.3,
          "maximum": 2.5,
          "default": 2.5,
          "description": "SM-2 algorithm ease factor"
        },
        "lastQuality": {
          "type": "integer",
          "minimum": 0,
 5,
                   "maximum": "description": "Quality of last recall (0-5)"
        }
      }
    }
  }
}
```

---

## Example: Complete Student Profile

```json
{
  "studentId": "student-001",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-20T14:22:00Z",
  "discovery": {
    "currentRole": "employee-non-tech",
    "targetRole": "agent-developer",
    "businessContext": {
      "hasBusiness": true,
      "businessType": "consulting",
      "businessGoals": ["automate-operations", "offer-ai-services"]
    },
    "personalContext": {
      "isPersonal": false,
      "forFamily": false,
      "forDevelopment": false
    },
    "learningStyle": "hands-on",
    "timeAvailable": "30min",
    "priorKnowledge": "some-exposure"
  },
  "progress": {
    "curriculum": {
      "generatedAt": "2024-01-15T10:35:00Z",
      "moduleOrder": ["module-1", "module-2", "module-3", "module-4", "module-5"],
      "customizations": {
        "examples": ["consulting-workflows"],
        "delivery": "exercises-first"
      }
    },
    "modules": {
      "module-1": {
        "status": "completed",
        "startedAt": "2024-01-15T11:00:00Z",
        "completedAt": "2024-01-15T11:50:00Z",
        "timeSpentMinutes": 48,
        "quizScore": 87,
        "keyConcepts": [
          "agent-framework-5-capabilities",
          "chatbot-vs-agent",
          "computing-paradigm-shift"
        ],
        "notes": "Good understanding of autonomy, need more practice with memory types"
      }
    },
    "assessments": [
      {
        "assessmentId": "quiz-m1-001",
        "moduleId": "module-1",
        "score": 87,
        "questionsCorrect": 7,
        "questionsTotal": 8,
        "completedAt": "2024-01-15T11:50:00Z",
        "areasForImprovement": ["action-chaining-examples"]
      }
    ],
    "projects": []
  },
  "settings": {
    "notificationsEnabled": true,
    "reminderTime": "09:00",
    "difficulty": "standard"
  }
}
```

---

## Example: Spaced Repetition Queue

```json
{
  "studentId": "student-001",
  "lastReviewDate": "2024-01-18T09:00:00Z",
  "reviewQueue": [
    {
      "conceptId": "agent-framework-5-capabilities",
      "conceptName": "AI Agent Framework 5 Core Capabilities",
      "moduleId": "module-1",
      "learnedAt": "2024-01-15T11:50:00Z",
      "nextReviewDate": "2024-01-19T00:00:00Z",
      "interval": 1,
      "repetitions": 1,
      "easeFactor": 2.5,
      "lastQuality": 4
    },
    {
      "conceptId": "agent-loop",
      "conceptName": "The Agent Loop (Think, Decide, Act, Observe)",
      "moduleId": "module-1",
      "learnedAt": "2024-01-15T11:50:00Z",
      "nextReviewDate": "2024-01-16T00:00:00Z",
      "interval": 1,
      "repetitions": 0,
      "easeFactor": 2.5,
      "lastQuality": null
    }
  ]
}
```

---

## Storage Location

```
students/
├── student-001/
│   ├── profile.json          # Student profile
│   ├── spaced-repetition.json # Review queue
│   └── notes.md              # Free-form notes
├── student-002/
│   └── ...
```
