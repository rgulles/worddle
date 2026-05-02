
def check_guess(guess, answer):
    result = ["grey"] * len(answer)
    answer_copy = answer.copy()

    for i in range(len(guess)):
        if guess[i] == answer[i]:
            result[i] = "green"
            answer_copy[i] = None 

    for i in range(len(guess)):
        if result[i] == "grey" and guess[i] in answer_copy:
            result[i] = "yellow"
            answer_copy[answer_copy.index(guess[i])] = None

    return result