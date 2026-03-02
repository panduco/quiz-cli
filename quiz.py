import time
import argparse
import json
import os 

FILENAME = "questions.json"

def load_questions():
    if not os.path.exists(FILENAME):
        print("Error: questions.json file not found!")
        return []
    with open(FILENAME, 'r') as f:
        return json.load(f)

import time 
# ... other imports

def run_quiz(hard_mode=False):
    questions = load_questions()
    if not questions:
        return

    score = 0
    total = len(questions)
    time_limit = 5 # Seconds for hard mode
    
    print("\n--- Welcome to the Quiz! ---")
    if hard_mode:
        print(f"MODE: HARD ({time_limit} seconds per question)")
    print("----------------------------\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        for idx, option in enumerate(q['options']):
            print(f"  {idx + 1}. {option}")
        
        start_time = time.time()
        
        # In standard Python, we can't easily kill an input prompt cross-platform
        # without complex threading. 
        # For this exercise, we will measure the time taken.
        # If they exceed the limit in Hard Mode, we mark it wrong.
        
        try:
            choice = input("\nYour answer (1-4): ")
            end_time = time.time()
            duration = end_time - start_time
            
            # Hard Mode Logic
            if hard_mode and duration > time_limit:
                print(f"⏰ Too slow! You took {duration:.1f}s (Limit: {time_limit}s)")
                continue # Skip checking answer, it's automatically wrong

            choice_idx = int(choice) - 1
            
            if choice_idx == q['answer']:
                print(f"✅ Correct! (Time: {duration:.1f}s)\n")
                score += 1
            else:
                correct_ans = q['options'][q['answer']]
                print(f"❌ Wrong! The correct answer was: {correct_ans}\n")
                
        except (ValueError, IndexError):
            print("Invalid input.\n")

    print("============================")
    print(f"FINAL SCORE: {score}/{total}")
    print("============================")
    
def main():
    parser = argparse.ArgumentParser(description="Run a CLI Quiz")
    parser.add_argument("--hard", action="store_true", help="Enable hard mode with time limits")
    args = parser.parse_args()

    run_quiz(hard_mode=args.hard)

if __name__ == "__main__":
    main()