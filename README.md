# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The game is a number-guessing game where the player tries to guess a secret number within a limited number of attempts, with hints after each guess. The original AI-generated code had several bugs that made it unplayable. The hints were completely backwards — "Too High" told the player to go higher, and "Too Low" told them to go lower, meaning every hint pointed in the wrong direction. On every even-numbered attempt, the secret number was silently converted to a string, which caused Python's string comparison to return wrong results (e.g., "8" > "70" alphabetically, so guessing 8 against a secret of 70 would say "Too High"). The "New Game" button always picked a new secret from 1–100 regardless of the selected difficulty, ignoring the difficulty range entirely. The Hard difficulty range (1–50) was also smaller than Normal (1–100), making it easier rather than harder. When "New Game" was clicked after a win or loss, the game status was never reset to "playing", so the app would immediately stop again. Switching difficulty mid-game also left the old secret in place, so a secret outside the new range could persist. To fix all of these, `check_guess` was rewritten with clean integer comparison and correct hint directions, the string conversion was removed, the New Game handler was updated to reset all state including `status`, difficulty switching now generates a fresh in-range secret, and Hard was changed to range 1–500. The core logic was refactored into `logic_utils.py` and covered with 18 automated tests.

## 📸 Demo

![Screenshot of the fixed game after winning](assets/screenshot%20of%20the%20app%20after%20winning.png)

## 🚀 Stretch Features

- Color-coded hints: green for correct, red for too high, orange for too low.
- Guess history sidebar showing each past guess and its color-coded result, cleared on New Game.
