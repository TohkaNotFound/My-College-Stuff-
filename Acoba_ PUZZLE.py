# Word Puzzle Game

words = [
    ("P_THON", "PYTHON"),
    ("PR_GR_M", "PROGRAM"),
    ("COMPU_ER", "COMPUTER"),
    ("KEYBO_RD", "KEYBOARD"),
    ("MON_TOR", "MONITOR"),
    ("MOU_E", "MOUSE"),
    ("SOFT_ARE", "SOFTWARE"),
    ("HARDW_RE", "HARDWARE"),
    ("NETW_RK", "NETWORK"),
    ("INTERN_T", "INTERNET")
]

correct = 0
incorrect = 0

for i, (puzzle, target) in enumerate(words, start=1):
    print(f"\nWord {i}: {puzzle}")
    answer = input("Complete the word: ").strip().upper()

    if answer == target:
        print("Correct!")
        correct += 1
    else:
        print("Incorrect!")
        print("Answer:", target)
        incorrect += 1

print("\n===== RESULT =====")
print("Correct Answers:", correct)
print("Incorrect Answers:", incorrect)
print(f"Score: {correct}/10")