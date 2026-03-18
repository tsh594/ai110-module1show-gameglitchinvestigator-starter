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

I used Claude (Claude Code) and GitHub Copilot as AI assistants throughout this project. For finding bugs, I asked Claude to read the code and identify issues, and it correctly spotted the string-conversion bug and the backwards hints immediately. For one correct suggestion, Copilot suggested removing the if/else block that cast the secret to a string on even attempts and simply using `secret = st.session_state.secret` — I verified this by running the game and confirming hints were consistent on every turn, then confirmed with a pytest test. For a misleading suggestion, Copilot at one point recommended expanding the Hard difficulty range to 1–1000 to make it "truly hard," but that wasn't the actual bug causing the hints to fail, and changing the range wouldn't have fixed anything — the real issue was the type mismatch in the comparison.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed when both a manual game test and an automated pytest test agreed the behavior was correct. For the hints bug, I wrote `test_too_high_message_says_go_lower` and `test_too_low_message_says_go_higher` — these failed before the fix and passed after, confirming the direction was corrected. I also manually played the game with the Developer Debug Info expander open so I could see the secret and verify the hints matched. For the string-conversion bug, I wrote a test that checks `check_guess(8, 70)` returns `"Too Low"`, which would have failed under the original string comparison. Claude helped me think through edge cases like negative numbers, decimals, and `None` input, which I turned into eight additional pytest tests.

---

## 4. What did you learn about Streamlit and state?

The secret appeared to change because the code was converting it to a string (`secret = str(st.session_state.secret)`) on even-numbered attempts. This didn't actually change the stored value, but it changed what was being compared — Python string comparison gave completely different results than integer comparison, so the hints seemed to contradict each other from one guess to the next, as if the secret had shifted. Streamlit reruns the entire Python script from top to bottom every time the user interacts with the page (clicks a button, types in a box, etc.). Without `st.session_state`, every variable would reset to its initial value on each rerun — so the secret would be re-rolled on every click. Session state is like a dictionary that survives across reruns, letting you store values that should persist. The fix was simple: remove the if/else entirely and always pass `st.session_state.secret` (the integer) directly to `check_guess`.

---

## 5. Looking ahead: your developer habits

The habit I want to carry forward is writing tests that check the *message direction*, not just the outcome label. In this project, `check_guess` returned the right outcome string (`"Too High"`) but the wrong message (`"Go HIGHER!"`), and a test that only checked the outcome would have missed that bug entirely. Next time I work with AI on a coding task, I would ask it to explain *why* it is making each change, not just what to change — Copilot sometimes produced correct-looking diffs that fixed the symptom without addressing the root cause, and asking for a reason would have helped me catch that faster. This project made me realize that AI-generated code can be subtly wrong in ways that only show up at runtime: the code compiles, the tests pass if you don't look closely, but the behavior is still broken — so treating AI output as a first draft that needs verification, not a finished product, is the right mindset.
