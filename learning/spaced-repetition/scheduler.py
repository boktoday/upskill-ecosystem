#!/usr/bin/env python3
"""
Spaced Repetition Scheduler
===========================
Implements SM-2 algorithm for optimal review scheduling.

Schedule: 1 day → 3 days → 7 days → 14 days → 30 days
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

# Base directory for student data
BASE_DIR = Path(__file__).parent.parent / "students"

# SM-2 Algorithm constants
MIN_EASE_FACTOR = 1.3
DEFAULT_EASE_FACTOR = 2.5
INTERVALS = [1, 3, 7, 14, 30]  # Days


def get_student_dir(student_id: str) -> Path:
    """Get the directory for a student's data."""
    student_dir = BASE_DIR / student_id
    student_dir.mkdir(parents=True, exist_ok=True)
    return student_dir


def load_profile(student_id: str) -> Optional[dict]:
    """Load student profile."""
    profile_path = get_student_dir(student_id) / "profile.json"
    if profile_path.exists():
        with open(profile_path) as f:
            return json.load(f)
    return None


def save_profile(student_id: str, profile: dict) -> None:
    """Save student profile."""
    profile_path = get_student_dir(student_id) / "profile.json"
    profile["updatedAt"] = datetime.now().isoformat()
    with open(profile_path, 'w') as f:
        json.dump(profile, f, indent=2)


def load_spaced_repetition(student_id: str) -> dict:
    """Load or initialize spaced repetition data."""
    sr_path = get_student_dir(student_id) / "spaced-repetition.json"
    if sr_path.exists():
        with open(sr_path) as f:
            return json.load(f)
    return {
        "studentId": student_id,
        "reviewQueue": [],
        "lastReviewDate": None
    }


def save_spaced_repetition(student_id: str, sr_data: dict) -> None:
    """Save spaced repetition data."""
    sr_path = get_student_dir(student_id) / "spaced-repetition.json"
    with open(sr_path, 'w') as f:
        json.dump(sr_data, f, indent=2)


def calculate_next_review(
    current_interval: int,
    ease_factor: float,
    quality: int
) -> tuple[int, float]:
    """
    SM-2 Algorithm: Calculate next review interval and ease factor.
    
    Args:
        current_interval: Current interval in days
        ease_factor: Current ease factor (default 2.5)
        quality: Quality of recall (0-5)
            0 - Complete blackout
            1 - Incorrect, but remembered upon seeing answer
            2 - Incorrect, but answer seemed easy to recall
            3 - Correct with serious difficulty
            4 - Correct after hesitation
            5 - Perfect recall
    
    Returns:
        Tuple of (new_interval, new_ease_factor)
    """
    if quality < 3:
        # Failed recall - reset to beginning
        return INTERVALS[0], ease_factor
    
    # Calculate new ease factor
    # EF' = EF + (0.1 - (5-q) * (0.08 + (5-q) * 0.02))
    new_ef = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    new_ef = max(MIN_EASE_FACTOR, new_ef)
    
    # Calculate new interval
    if current_interval == 0:
        new_interval = INTERVALS[0]
    else:
        new_interval = int(current_interval * new_ef)
    
    # Cap at 30 days max
    new_interval = min(new_interval, 30)
    
    return new_interval, new_ef


def add_concept_for_review(
    student_id: str,
    concept_id: str,
    concept_name: str,
    module_id: str
) -> None:
    """
    Add a new concept to the review queue.
    
    First review is scheduled for 1 day after learning.
    """
    sr_data = load_spaced_repetition(student_id)
    
    # Check if already in queue
    for item in sr_data["reviewQueue"]:
        if item["conceptId"] == concept_id:
            return  # Already being reviewed
    
    now = datetime.now()
    review_item = {
        "conceptId": concept_id,
        "conceptName": concept_name,
        "moduleId": module_id,
        "learnedAt": now.isoformat(),
        "nextReviewDate": (now + timedelta(days=INTERVALS[0])).isoformat(),
        "interval": INTERVALS[0],
        "repetitions": 0,
        "easeFactor": DEFAULT_EASE_FACTOR,
        "lastQuality": None
    }
    
    sr_data["reviewQueue"].append(review_item)
    save_spaced_repetition(student_id, sr_data)
    
    print(f"✅ Added '{concept_name}' to review queue")
    print(f"   First review: {INTERVALS[0]} day(s) from now")


def get_due_reviews(student_id: str) -> list[dict]:
    """
    Get all reviews due today.
    
    Returns list of concepts that should be reviewed now.
    """
    sr_data = load_spaced_repetition(student_id)
    now = datetime.now()
    
    due = []
    for item in sr_data["reviewQueue"]:
        next_review = datetime.fromisoformat(item["nextReviewDate"])
        if next_review <= now:
            due.append(item)
    
    return due


def record_review_result(
    student_id: str,
    concept_id: str,
    quality: int
) -> None:
    """
    Record the result of a review and schedule the next one.
    
    Args:
        student_id: The student's ID
        concept_id: The concept that was reviewed
        quality: Recall quality (0-5)
    """
    sr_data = load_spaced_repetition(student_id)
    
    for item in sr_data["reviewQueue"]:
        if item["conceptId"] == concept_id:
            # Calculate new interval and ease factor
            new_interval, new_ef = calculate_next_review(
                item["interval"],
                item["easeFactor"],
                quality
            )
            
            # Update the item
            item["interval"] = new_interval
            item["easeFactor"] = new_ef
            item["repetitions"] += 1
            item["lastQuality"] = quality
            
            # Schedule next review
            now = datetime.now()
            item["nextReviewDate"] = (now + timedelta(days=new_interval)).isoformat()
            
            print(f"📚 Review recorded for '{item['conceptName']}'")
            print(f"   Quality: {quality}/5")
            print(f"   Next review: {new_interval} day(s)")
            
            break
    
    # Update last review date
    sr_data["lastReviewDate"] = datetime.now().isoformat()
    save_spaced_repetition(student_id, sr_data)


def get_review_summary(student_id: str) -> str:
    """
    Get a summary of review status for a student.
    
    Returns a human-readable string.
    """
    sr_data = load_spaced_repetition(student_id)
    due = get_due_reviews(student_id)
    
    total = len(sr_data["reviewQueue"])
    due_count = len(due)
    
    summary = f"""
📚 Spaced Repetition Status for {student_id}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total concepts in review: {total}
Due for review today: {due_count}

"""
    
    if due:
        summary += "🔔 DUE NOW:\n"
        for item in due:
            summary += f"  • {item['conceptName']}\n"
    
    # Show upcoming reviews
    now = datetime.now()
    upcoming = []
    for item in sr_data["reviewQueue"]:
        next_review = datetime.fromisoformat(item["nextReviewDate"])
        if next_review > now:
            days_until = (next_review - now).days
            if days_until <= 7:
                upcoming.append((item["conceptName"], days_until))
    
    if upcoming:
        summary += "\n📅 UPCOMING:\n"
        for name, days in sorted(upcoming, key=lambda x: x[1]):
            summary += f"  • {name} (in {days} day{'s' if days != 1 else ''})\n"
    
    return summary


def what_to_review_today(student_id: str) -> list[dict]:
    """
    Main function: Returns what the student should review today.
    
    This is the primary entry point for the review scheduler.
    """
    due = get_due_reviews(student_id)
    
    if not due:
        # No reviews due - check if we should learn new concepts
        profile = load_profile(student_id)
        if profile:
            # Could trigger new content learning here
            pass
        return []
    
    return due


def create_sample_student() -> str:
    """Create a sample student for testing."""
    import uuid
    
    student_id = f"student-{uuid.uuid4().hex[:3]}"
    profile = {
        "studentId": student_id,
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
        "discovery": {
            "currentRole": "employee-non-tech",
            "targetRole": "agent-developer",
            "learningStyle": "mixed",
            "timeAvailable": "30min",
            "priorKnowledge": "beginner"
        },
        "progress": {
            "curriculum": {
                "generatedAt": datetime.now().isoformat(),
                "moduleOrder": ["module-1", "module-2", "module-3", "module-4", "module-5"],
                "customizations": {}
            },
            "modules": {},
            "assessments": [],
            "projects": []
        },
        "settings": {
            "notificationsEnabled": True,
            "reminderTime": "09:00",
            "difficulty": "standard"
        }
    }
    
    save_profile(student_id, profile)
    print(f"✅ Created sample student: {student_id}")
    
    return student_id


# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("""
Spaced Repetition Scheduler
===========================
Usage:
  python spaced_repetition.py due <student_id>     - Show what's due today
  python spaced_repetition.py add <student_id> <concept_id> <concept_name> <module_id>
  python spaced_repetition.py record <student_id> <concept_id> <quality>
  python spaced_repetition.py summary <student_id>
  python spaced_repetition.py create               - Create sample student
        """)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "due" and len(sys.argv) >= 3:
        student_id = sys.argv[2]
        due = what_to_review_today(student_id)
        if due:
            print("📚 Due for review:")
            for item in due:
                print(f"  • {item['conceptName']}")
        else:
            print("✅ No reviews due today!")
    
    elif command == "add" and len(sys.argv) >= 6:
        student_id = sys.argv[2]
        concept_id = sys.argv[3]
        concept_name = sys.argv[4]
        module_id = sys.argv[5]
        add_concept_for_review(student_id, concept_id, concept_name, module_id)
    
    elif command == "record" and len(sys.argv) >= 5:
        student_id = sys.argv[2]
        concept_id = sys.argv[3]
        quality = int(sys.argv[4])
        record_review_result(student_id, concept_id, quality)
    
    elif command == "summary" and len(sys.argv) >= 3:
        student_id = sys.argv[2]
        print(get_review_summary(student_id))
    
    elif command == "create":
        create_sample_student()
    
    else:
        print("Invalid command. Run without args for usage.")
