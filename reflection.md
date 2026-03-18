# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").

### Bugs found in the starter code

**Bug 1 — Hints are backwards (`app.py`, lines 37–40)**
In `check_guess`, when `guess > secret` the message says `"📈 Go HIGHER!"`, but if your guess is already too high, you should go *lower*. Likewise, `guess < secret` says `"📉 Go LOWER!"` when it should say higher. Every direction hint misleads the player.

**Bug 2 — Secret is randomly converted to a string on even attempts (`app.py`, lines 158–161)**
On every even-numbered attempt the code does `secret = str(st.session_state.secret)`. This makes `check_guess` compare an integer guess against a string secret using Python's cross-type string comparison. For example, if the secret is `70` and you guess `8`, `"8" > "70"` is `True` alphabetically, so the game says "Too High" when 8 is actually lower than 70. Hints are wrong on every other turn.

**Bug 3 — "Hard" difficulty has a smaller (easier) range than "Normal" (`app.py`, lines 8–10)**
`get_range_for_difficulty` returns `(1, 50)` for Hard but `(1, 100)` for Normal. A range of 1–50 is *easier* to guess, not harder. Hard should have the largest range (e.g., 1–500) to be genuinely more difficult.

**Bug 4 — New Game ignores the selected difficulty (`app.py`, line 136)**
When the "New Game" button is clicked, the secret is always reset with `random.randint(1, 100)` regardless of which difficulty is selected. A player on Easy or Hard mode still gets a 1–100 secret instead of the correct range for their difficulty.

**Bug 5 — Attempt counter starts at 1, not 0 (`app.py`, line 96)**
`st.session_state.attempts` is initialized to `1` instead of `0`. Because the counter is incremented *before* evaluating the guess, the player effectively starts with one attempt already consumed, losing one full guess on the very first turn.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
