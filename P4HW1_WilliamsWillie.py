# Willie C. Williams Jr.
# 2025-11-03
# P4HW1 - Score List with Grade
# This program asks the user how many test scores they want to enter, validates each
# score (must be between 0 and 100), stores them in a list, drops the lowest score,
# calculates the average of the remaining scores, and outputs the corresponding letter grade.

"""
Pseudocode (Detailed Algorithm)
-------------------------------
1) Display program title/brief instructions (optional).
2) Prompt user: "How many scores would you like to enter?" -> num_scores (int).
   WHILE num_scores <= 0:
       - Print error message
       - Re-prompt for a positive integer

3) Initialize an empty list "scores".
4) FOR i from 1 to num_scores:
       - LOOP:
           - Prompt: "Enter score #i:" -> value (float)
           - IF value < 0 or value > 100:
                 print "INVALID score entered! Score must be between 0 and 100."
                 continue loop (ask again)
             ELSE:
                 append value to "scores"
                 break out of validation loop

5) After collecting all scores:
       - Find the lowest score: lowest = min(scores)
       - Make a copy of scores into "modified_scores"
       - Remove ONE occurrence of the lowest score from modified_scores

6) Compute average of modified_scores:
       - IF length of modified_scores > 0:
             avg = sum(modified_scores) / len(modified_scores)
         ELSE:
             avg = 0.0   # (Edge case if user only entered 1 score)

7) Determine letter grade using standard scale:
       - IF avg >= 90: grade = 'A'
         ELIF avg >= 80: grade = 'B'
         ELIF avg >= 70: grade = 'C'
         ELIF avg >= 60: grade = 'D'
         ELSE: grade = 'F'

8) Display results:
       - "-------------- Results --------------"
       - "Lowest Score  : <lowest>"
       - "Modified List : <modified_scores>"
       - "Scores Average: <avg formatted to 2 decimals>"
       - "Letter Grade  : <grade>"
       - "-------------------------------------"
"""

def get_positive_int(prompt):
    """Prompt until the user enters a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive whole number greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 3).")

def get_valid_score(prompt):
    """Prompt until the user enters a float between 0 and 100 inclusive."""
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("INVALID score entered! Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 87.5).")

def determine_letter_grade(average):
    """Return a letter grade based on the numeric average."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("P4HW1 - Score List with Grade")
    print("-" * 40)
    num_scores = get_positive_int("How many scores would you like to enter? ")

    scores = []
    for i in range(1, num_scores + 1):
        score = get_valid_score(f"Enter score #{i}: ")
        scores.append(score)

    lowest = min(scores)
    modified_scores = scores.copy()
    modified_scores.remove(lowest)

    if len(modified_scores) > 0:
        average = sum(modified_scores) / len(modified_scores)
    else:
        average = 0.0

    grade = determine_letter_grade(average)

    print("\n-------------- Results --------------")
    print(f"Lowest Score  : {lowest:.2f}")
    print(f"Modified List : {modified_scores}")
    print(f"Scores Average: {average:.2f}")
    print(f"Letter Grade  : {grade}")
    print("-------------------------------------")

if __name__ == "__main__":
    main()
