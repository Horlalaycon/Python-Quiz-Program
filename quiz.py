# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon

import random
import time
from questions import quiz

welcome = """
                    ++++++++++++++++++++++++++++++++++++++
                    ++++++++++++++++++++++++++++++++++++++
                    |||                                |||
                    |||  python and hacking related    |||
                    |||          quiz program          |||
                    |||                                |||
                    |||                                |||
                    ++++++++++++++++++++++++++++++++++++++
                    ++++++++++++++++++++++++++++++++++++++
                                  +++++++++
                                +++++++++++++
"""


def pick_question():
    questions = [quiz['question1']['question'], quiz['question2']['question'], quiz['question3']['question'], quiz['question4']['question'], quiz['question5']['question'], quiz['question6']['question'], quiz['question7']['question'], quiz['question8']['question'], quiz['question9']['question'], quiz['question10']['question'], quiz['question11']['question'], quiz['question12']['question'], quiz['question13']['question'], quiz['question14']['question'], quiz['question15']['question'], quiz['question16']['question'], quiz['question17']['question'], quiz['question18']['question'], quiz['question19']['question'], quiz['question20']['question']]

    rand_question = random.choice(questions)

    return rand_question


if __name__ == "__main__":
    scores = 0
    number_of_questions = 20

    print(welcome)

    for number in range(number_of_questions):
        number += 1

        question = pick_question()
        print(str(number) + ". " + question)

        reply = input("Answer: ")

        time.sleep(2)

        # conditions(random_question, answer, scores)
        if reply.lower() == quiz['question1']['answer'] and question == quiz['question1']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question2']['answer'] and question == quiz['question2']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question3']['answer'] and question == quiz['question3']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question4']['answer'] and question == quiz['question4']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question5']['answer'] and question == quiz['question5']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question6']['answer'] and question == quiz['question6']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question7']['answer'] and question == quiz['question7']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question8']['answer'] and question == quiz['question8']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question9']['answer'] and question == quiz['question9']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question10']['answer'] and question == quiz['question10']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question11']['answer'] and question == quiz['question11']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question12']['answer'] and question == quiz['question12']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question13']['answer'] and question == quiz['question13']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question14']['answer'] and question == quiz['question14']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question15']['answer'] and question == quiz['question15']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question16']['answer'] and question == quiz['question16']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question17']['answer'] and question == quiz['question17']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question18']['answer'] and question == quiz['question18']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question19']['answer'] and question == quiz['question19']['question']:
            print("Correct")
            scores += 1

        elif reply.lower() == quiz['question20']['answer'] and question == quiz['question20']['question']:
            print("Correct")
            scores += 1

        else:
            print("Sorry! wrong Answer")

        print(f'score: {str(scores)}')
        print('\n')

    print(f'Total percentage is: {str(int(scores/number_of_questions * 100))}%')
