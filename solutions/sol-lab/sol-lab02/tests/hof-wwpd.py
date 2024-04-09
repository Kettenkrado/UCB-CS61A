test = {
  'name': 'Higher Order Functions',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        # {
        #   'code': """
        #   >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
        #   >>> def even(f):
        #   ...     def odd(x):
        #   ...         if x < 0:
        #   ...             return f(-x)
        #   ...         return f(x)
        #   ...     return odd
        #   >>> steven = lambda x: x
        #   >>> stewart = even(steven)
        #   >>> stewart
        #   Function
        #   >>> stewart(61)
        #   61
        #   >>> stewart(-4)
        #   4
        #   """,
        # },
        {
          'code': """
          >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
          >>> def cake():
          ...    print('beets')
          ...    def pie():
          ...        print('sweets')
          ...        return 'cake'
          ...    return pie
          >>> chocolate = cake()
          beets
          >>> chocolate
          Function
          >>> chocolate()
          sweets
          'cake'
          >>> more_chocolate, more_cake = chocolate(), cake
          sweets
          >>> more_chocolate
          'cake'
          >>> # Reminder: cake, more_cake, and chocolate were defined/assigned in the code above! 
          >>> # It might be helpful to refer to their definitions on the assignment website so you don't have to scroll as much!
          >>> def snake(x, y):
          ...    if cake == more_cake:
          ...        return chocolate
          ...    else:
          ...        return x + y
          >>> snake(10, 20)
          Function
          >>> snake(10, 20)()
          sweets
          'cake'
          >>> cake = 'cake'
          >>> snake(10, 20)
          30
          """,
        }
      ]
    }
  ]
}