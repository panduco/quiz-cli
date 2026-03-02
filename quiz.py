import argparse
import json
import os
import time
import random

FILENAME = "questions.json"
HIGHSCORE_FILE = "highscore.json"

def load_questions():
    if not os.path.exists(FILENAME):
        print("Error: questions.json file not found!")
        return []
    with open(FILENAME, 'r') as f:
        return json.load(f)

def load_highscore():
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    with open(HIGHSCORE_FILE, 'r') as f:
        data = json.load(f)
        return data.get('highscore', 0)

def save_highscore(score):
    with open(HIGHSCORE_FILE, 'w') as f:
        json.dump({'highscore': score}, f)

def run_quiz(hard_mode=False):
    questions = load_questions()
    if not questions:
        return

    # Feature 1: Shuffle questions for variety
    random.shuffle(questions)

    score = 0
    total = len(questions)
    time_limit = 5 
    
    # Load existing high score
    top_score = load_highscore()
    
    print("\n--- Welcome to the Quiz! ---")
    print(f"Current High Score: {top_score}/{total}")
    if hard_mode:
        print("MODE: HARD (5 seconds per question)")
    print("----------------------------\n")

    # To track wrong answers for summary
    wrong_answers = []

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        for idx, option in enumerate(q['options']):
            print(f"  {idx + 1}. {option}")
        
        start_time = time.time()
        
        try:
            choice = input("\nYour answer (1-4): ")
            end_time = time.time()
            duration = end_time - start_time
            
            # Hard Mode Logic
            if hard_mode and duration > time_limit:
                print(f"⏰ Too slow! You took {duration:.1f}s.")
                wrong_answers.append((q['question'], q['options'][q['answer']]))
                continue

            choice_idx = int(choice) - 1
            
            if choice_idx == q['answer']:
                print(f"✅ Correct! (Time: {duration:.1f}s)\n")
                score += 1
            else:
                correct_ans = q['options'][q['answer']]
                print(f"❌ Wrong! The correct answer was: {correct_ans}\n")
                wrong_answers.append((q['question'], correct_ans))
                
        except (ValueError, IndexError):
            print("Invalid input.\n")

    # --- SUMMARY & HIGH SCORE ---
    print("============================")
    print(f"FINAL SCORE: {score}/{total}")
    
    if score > top_score:
        print("🎉 NEW HIGH SCORE!")
        save_highscore(score)
    else:
        print(f"High Score to beat: {top_score}")

    # Feature 2: Detailed Summary of Wrong Answers
    if wrong_answers:
        print("\n--- Review Missed Questions ---")
        for q, ans in wrong_answers:
            print(f"Q: {q}")
            print(f"Correct Answer: {ans}\n")
            
    print("============================")

def main():
    parser = argparse.ArgumentParser(description="Run a CLI Quiz")
    parser.add_argument("--hard", action="store_true", help="Enable hard mode with time limits")
    args = parser.parse_args()

    run_quiz(hard_mode=args.hard)

if __name__ == "__main__":
    main()