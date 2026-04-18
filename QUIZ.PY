# Login Function
def login():
    print("----- Login -----")

    correct_username = "admin"
    correct_password = "1234"

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful\n")
        return True
    else:
        print("Invalid Login Credentials")
        return False


# Display Questions Function
def display_questions():
    print("----- Enter Quiz Questions -----")

    n = int(input("Enter number of questions: "))
    score = 0

    for i in range(n):
        print("\nEnter Question", i + 1)
        question = input("Question: ")
        correct_answer = input("Correct Answer: ")

        print("\n", question)
        user_answer = input("Enter your answer: ")

        if user_answer.lower() == correct_answer.lower():
            print("Correct Answer")
            score += 1
        else:
            print("Wrong Answer")

    return score, n


# Calculate Total Marks
def calculate_total_marks(score):
    return score


# Calculate Percentage
def calculate_percentage(score, total_questions):
    return (score / total_questions) * 100


# Calculate Average
def calculate_average(score, total_questions):
    return score / total_questions


# Score List Analysis
def score_list_module(scores):
    print("\n----- Score List Analysis -----")

    highest_score = max(scores)
    lowest_score = min(scores)
    average_score = sum(scores) / len(scores)

    print("Scores List:", scores)
    print("Highest Score:", highest_score)
    print("Lowest Score:", lowest_score)
    print("Average Score:", average_score)


# Main Function
def main():
    scores = []   # score list

    status = login()

    if status:
        score, total_questions = display_questions()

        scores.append(score)

        total_marks = calculate_total_marks(score)
        percentage = calculate_percentage(score, total_questions)
        average = calculate_average(score, total_questions)

        print("\nTotal Marks:", total_marks)
        print("Percentage:", percentage)
        print("Average:", average)

        score_list_module(scores)


# Program Start
main()
