# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

When I first ran the game it looked normal however there were some bugs while playing it.
Here are the bugs I found:

1. The hints were backwards. Too high told me to go higher and too low told me to go lower.
2. The attempt counter started at 1 instead of 0 so the attempts left display was always off by one.
3. Clicking New Game did not reset your score, status, or guess history so old data carried over.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
I used GitHub Copilot Chat in VS Code as my main AI tool for this project. One example of 
a correct suggestion was when I highlighted the check_guess function and asked Copilot to 
explain the logic. It correctly identified that the hint messages were swapped and suggested 
flipping the return values, which I verified by running the game and confirming the hints 
now matched my guesses. One example of a misleading suggestion was when I asked Copilot to 
help me fix the New Game button. It initially only suggested resetting the attempts and 
secret number, which looked complete but missed resetting the score, status, and history. 
I caught this by starting a new game after a loss and noticing the game was still locked, 
which told me the status reset was missing.


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I decided a bug was really fixed when the game behavior matched what I expected both in 
the live app and in a passing pytest test. For example after fixing the swapped hints I 
manually played a round and confirmed that guessing too high now correctly told me to go 
lower. I also ran pytest after adding three new test cases targeting each of the bugs I 
fixed, all three passed which confirmed the logic was correct. Copilot helped me write the 
pytest cases by generating assertions based on the expected behavior I described, which 
saved time and helped me understand what a good test for each bug should actually check.



## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---


The secret number kept changing in the original app because Streamlit reruns the entire 
script from top to bottom every time the user interacts with anything, so without session 
state the secret would get reassigned to a new random number on every rerun. Streamlit 
reruns are basically Streamlit re-executing your whole script every time you click a button 
or type something, and session state is like a small memory that persists between those 
reruns so your variables do not get wiped. The fix was wrapping the secret number 
initialization in a check like "if secret not in session state" so it only gets generated 
once at the start of a new game and stays the same for the rest of that game.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is committing after every individual fix instead of making all 
the changes at once. It made it really easy to track what changed and why, and if something 
broke I could pinpoint exactly which commit caused it. One thing I would do differently 
next time is test the app manually before asking AI to audit the code, so I have my own 
observations to compare against what the AI finds rather than just taking its word for it. 
This project changed the way I think about AI generated code because I used to assume that 
if code runs without crashing it is probably correct, but this game ran fine and still had 
so many bugs that made it behave completely wrong.