test = {
  'name': 'Lambda the Free',
  'points': 0,
  'suites': [
    {
      'type': 'concept',
      'cases': [
        {
          'answer': 'A lambda expression does not automatically bind the function that it returns to a name.',
          'choices': [
            'A lambda expression does not automatically bind the function that it returns to a name.',
            'A lambda expression cannot have more than two parameters.',
            'A lambda expression cannot return another function.',
            'A def statement can only have one line in its body.',
          ],
          'question': r"""
          Which of the following statements describes a difference between a def statement and a lambda expression?
          """
        },
        {
          'answer': 'two',
          'choices': [
            'one',
            'two',
            'three',
            'Not enough information',
          ],
          'question': r"""
          How many formal parameters does the following lambda expression have?
          lambda a, b: c + d
          """
        },
        {
          'answer': 'When the function returned by the lambda expression is called.',
          'choices': [
            'When the function returned by the lambda expression is called.',
            'When you assign the lambda expression to a name.',
            'When the lambda expression is evaluated.',
            'When you pass the lambda expression into another function.',
          ],
          'question': r"""
          When is the return expression of a lambda expression executed?
          """
        },
      ]
    },
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
          >>> lambda x: x  # A lambda expression with one parameter x
          Function
          >>> a = lambda x: x  # Assigning a lambda function to the name a
          >>> a(5)
          5
          >>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
          3
          >>> b = lambda x, y: lambda: x + y # Lambdas can return other lambdas!
          >>> c = b(8, 4)
          >>> c
          Function
          >>> c()
          12
          >>> d = lambda f: f(4)  # They can have functions as arguments as well
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          16
          """
        },
        # {
        #   'code': """
        #   >>> #
        #   >>> # Pay attention to the scope of variables
        #   >>> z = 3
        #   >>> e = lambda x: lambda y: lambda: x + y + z
        #   >>> e(0)(1)()
        #   4
        #   >>> f = lambda z: x + z
        #   >>> f(3)
        #   Error
        #   """
        # },
        # {
        #   'code': """
        #   >>> x, y, z = 1, 2, 3
        #   >>> a = lambda b: x + y + z
        #   >>> x += y
        #   >>> y -= z
        #   >>> a('lambdas are fun!')
        #   5
        #   """
        # },
        # {
        #   'code': """
        #   >>> x = None # remember to review the rules of WWPD given above!
        #   >>> x
        #   Nothing
        #   """
        # },
        {
          'code': """
          >>> # Try drawing an environment diagram if you get stuck!
          >>> higher_order_lambda = lambda f: lambda x: f(x)
          >>> g = lambda x: x * x
          >>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
          Error
          >>> higher_order_lambda(g)(2)
          4
          >>> call_thrice = lambda f: lambda x: f(f(f(x)))
          >>> call_thrice(lambda y: y + 1)(0)
          3
          >>> print_lambda = lambda z: print(z) # When is the return expression of a lambda expression executed?
          >>> print_lambda
          Function
          >>> one_thousand = print_lambda(1000)
          1000
          >>> one_thousand # What did the call to print_lambda return? If it displays nothing, write Nothing
          Nothing
          """
        },
        # {
        #   'code':"""
        #   >>> # Try drawing an environment diagram if you get stuck!
        #   >>> bar = lambda y: lambda x: pow(x, y)
        #   >>> bar()(15)
        #   Error
        #   >>> foo = lambda: 32
        #   >>> foobar = lambda x, y: x // y
        #   >>> a = lambda x: foobar(foo(), bar(4)(x))
        #   >>> a(2)
        #   2
        #   >>> b = lambda x, y: print('summer')
        #   Nothing
        #   >>> c = b(4, 'dog')
        #   summer
        #   >>> print(c)
        #   None
        #   """
        # },
      ]
    },
    # {
    #   'type': 'wwpp',
    #   'cases': [
    #     # {
    #     #   'code': """
    #     #   >>> a = lambda b: b * 2
    #     #   Nothing
    #     #   >>> a
    #     #   Function
    #     #   >>> a(a(a()))
    #     #   Error
    #     #   >>> a(a(a(2)))
    #     #   16
    #     #   >>> def d():
    #     #   ...     print(None)
    #     #   ...     print('whoo')
    #     #   >>> b = d()
    #     #   None
    #     #   whoo
    #     #   >>> b
    #     #   Nothing
    #     #   """
    #     # },
    #   ]
    # }
  ]
}