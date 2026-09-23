word_list = [
    {"puzzle": "P_th_n", "answer": "python"},
    {"puzzle": "C_mp_t_r", "answer": "computer"},
    {"puzzle": "Pr_gr_m", "answer": "program"},
    {"puzzle": "S_ftw_r_", "answer": "software"},
    {"puzzle": "D_t_b_s_", "answer": "database"},
    {"puzzle": "K_yb__rd", "answer": "keyboard"},
    {"puzzle": "M_n_t_r", "answer": "monitor"},
    {"puzzle": "I_nt_rn_t", "answer": "internet"},
    {"puzzle": "B_r_ws_r", "answer": "browser"},
    {"puzzle": "N_tw_rk", "answer": "network"}
]

score = 0
correct_answers = 0
incorrect_answers = 0

print("Welcome to the Missing Letter Word Puzzle!")
print("-" * 40)

for i in range(10):
    current_word = word_list[i]
    print(f"Word {i+1} of 10: {current_word['puzzle']}")
    
    guess = input("Your guess: ").strip().lower()
    
    if guess == current_word['answer']:
        print("Result: Correct!\n")
        score += 10 
        correct_answers += 1
    else:
        print(f"Result: Incorrect! The correct answer was '{current_word['answer'].capitalize()}'.\n")
        incorrect_answers += 1

print("-" * 40)
print("Game Over! Here are your final statistics:")
print(f"Correct Answers: {correct_answers}")
print(f"Incorrect Answers: {incorrect_answers}")
print(f"Total Score: {score} / 100")