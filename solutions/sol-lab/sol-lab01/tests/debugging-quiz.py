test = {
  'name': 'debugging-quiz',
  'points': 0,
  'suites': [
      {
      'type': 'concept',
      'cases': [
        {
          'question': """
          In the following traceback, what is the most recent function call?
          Traceback (most recent call last):
              File "temp.py", line 10, in <module>
                f("hi")
              File "temp.py", line 2, in f
                return g(x + x, x)
              File "temp.py", line 5, in g
                return h(x + y * 5)
              File "temp.py", line 8, in h
                return x + 0
            TypeError: must be str, not int
          """,
          'choices': [
            'f("hi")',
            'g(x + x, x)',
            'h(x + y * 5)',
          ],
          'answer': "h(x + y * 5)",
          'hidden': False
        },
          {
            'question': """
            In the following traceback, what is the cause of this error?
            Traceback (most recent call last):
                File "temp.py", line 10, in <module>
                  f("hi")
                File "temp.py", line 2, in f
                  return g(x + x, x)
                File "temp.py", line 5, in g
                  return h(x + y * 5)
                File "temp.py", line 8, in h
                  return x + 0
              TypeError: must be str, not int
            """,
            'choices': [
              'the code attempted to add a string to an integer',
              'the code looped infinitely',
              'there was a missing return statement',
            ],
            'answer': "the code attempted to add a string to an integer",
            'hidden': False
          },
        {
          'question': """
          How do you write a doctest asserting that square(2) == 4?
          """,
          'choices': [
            """
            def square(x):
                '''
                doctest: (2, 4)
                '''
                return x * x
            """,
            """
            def square(x):
                '''
                input: 2
                output: 4
                '''
                return x * x
            """,
            """
            def square(x):
                '''
                square(2)
                4
                '''
                return x * x
            """,
            """
            def square(x):
                '''
                >>> square(2)
                4
                '''
                return x * x
            """
          ],
          'answer': """
          def square(x):
              '''
              >>> square(2)
              4
              '''
              return x * x
          """,
          'hidden': False
        },
        {
          'question': "When should you use print statements?",
          'choices': [
            "For permanant debugging so you can have long term confidence in your code",
            "To ensure that certain conditions are true at certain points in your code",
            "To investigate the values of variables at certain points in your code"
          ],
          'answer': "To investigate the values of variables at certain points in your code",
          'hidden': False
        },
        {
          'question': "How do you prevent the ok autograder from interpreting print statements as output?",
          'choices': [
            "You don't need to do anything, ok only looks at returned values, not printed values",
            "Print with 'DEBUG:' at the front of the outputted line",
            "Print with # at the front of the outputted line",
          ],
          'answer': "Print with 'DEBUG:' at the front of the outputted line",
          'hidden': False
        },
        {
          'question': "What is the best way to open an interactive terminal to investigate a failing test for question sum_digits in assignment lab01?",
          'choices': [
            "python3 ok -q sum_digits -i",
            "python3 ok -q sum_digits --trace",
            "python3 ok -q sum_digits",
            "python3 -i lab01.py"
          ],
          'answer': "python3 ok -q sum_digits -i",
          'hidden': False
        },
        # TODO: Figure out why --trace isn't working
        # {
        #   'question': "What is the best way to look at an environment diagram to investigate a failing test for question sum_digits in assignment lab01?",
        #   'choices': [
        #     "python3 ok -q sum_digits -i",
        #     "python3 ok -q sum_digits --trace",
        #     "python3 ok -q sum_digits",
        #     "python3 -i lab01.py"
        #   ],
        #   'answer': "python3 ok -q sum_digits --trace",
        #   'hidden': False
        # },
        {
          'question': "Which of the following is NOT true?",
          'choices': [
            "Code that returns a wrong answer instead of crashing is generally better as it at least works fine",
            "Testing is very important to ensure robust code",
            "Debugging is not a substitute for testing",
            "It is generally bad practice to release code with debugging print statements left in",
            "It is generally good practice to release code with assertion statements left in",
          ],
          'answer': "Code that returns a wrong answer instead of crashing is generally better as it at least works fine",
          'hidden': False
        },
      ]
    }
    ]
}