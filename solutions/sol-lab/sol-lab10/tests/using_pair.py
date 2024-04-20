test = {
  'name': 'using-pair',
  'points': 0,
  'suites': [
      {
      'type': 'concept',
      'cases': [
        {
          'question': """
          Write out the Python expression that returns a `Pair` representing the given expression: (+ (- 2 4) 6 8)
          """,
          'choices': [
            "Pair('+', Pair('-', Pair(2, Pair(4, Pair(6, Pair(8, nil))))))",
            "Pair('+', Pair(Pair('-', Pair(2, Pair(4))), Pair(6, Pair(8))))",
            "Pair(+, Pair(Pair(-, Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))",
            "Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))",
            "None of these"
          ],
          'answer': "Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))",
          'hidden': False
        },
        {
        'question': """
        What is the operator of the call expression?
          """,
          'choices': [
            '-',
            '+',
            '(',
            '2',
            '6',
            'None of these'
          ],
          'answer': "+",
          'hidden': False
        },
        {
            'question': """
            If the `Pair` you constructed in the previous part was bound to the name `p`,
            how would you retrieve the operator?
            """,
            'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
            ],
            'answer': "p.first",
            'hidden': False
        },
        {
        'question': """
        If the `Pair` you constructed was bound to the name `p`, 
        how would you retrieve a list containing all of the operands?
          """,
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
            ],
          'answer': "p.rest",
          'hidden': False
        },
        {
        'question': """
        How would you retrieve only the first operand?
          """,
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
            ],
          'answer': "p.rest.first",
          'hidden': False
        },
        {
        'question': """
        What is the first operand of the call expression (prior to evaluation)?
          """,
          'choices': [
            "'-'",
            "'+'",
            "2",
            "4",
            "-2",
            "Pair('-', Pair(2, Pair(4, nil)))",
            "Pair(2, Pair(4, nil))"
            ],
          'answer': "Pair('-', Pair(2, Pair(4, nil)))",
          'hidden': False
        }
      ]
    }
    ]
}