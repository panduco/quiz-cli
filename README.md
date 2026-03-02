# 🧠 Interactive Quiz CLI

A command-line trivia tool that tests your knowledge with multiple-choice questions. Features a "Hard Mode" for experts and persistent high scores.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **Dynamic Questions:** Loads questions from a simple JSON file.
- **Randomized Order:** Questions are shuffled every time you play.
- **Hard Mode:** A time limit (5 seconds) per question. Too slow? It counts as wrong!
- **High Score Tracking:** Your best score is saved locally.
- **Review Mode:** At the end of the game, review the questions you missed.

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/quiz-cli.git
   cd quiz-cli
   ```

2. **Add Questions:**
   Create a file named `questions.json` and add your questions in the following format:
   ```json
   [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "answer": 2
        }
   ]
   ```
   *(Note: `answer` is the index of the correct option, starting at 0).*

## 💻 Usage

**Start a normal game:**
```bash
python quiz.py
```

**Start a Hard Mode game (5s time limit):**
```bash
python quiz.py --hard
```

## 📂 Project Structure

```
quiz-cli/
├── quiz.py           # Main application logic
├── questions.json    # Your question bank
├── highscore.json    # Saved high score (auto-generated)
└── README.md
```

## 🔧 Customization

You can easily edit `questions.json` to add your own trivia categories (History, Science, Pop Culture, etc.).

## 📜 License

This project is licensed under the MIT License.
```

### Final Commit

```bash
git add .
git commit -m "Feat: Add question shuffling, high scores, and end-game review"
git push origin main