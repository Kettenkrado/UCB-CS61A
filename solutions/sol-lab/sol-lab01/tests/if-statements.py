test = {
  'name': 'What If?',
  'points': 0,
  'suites': [
   # {
   #   'type': 'wwpp',
   #   'cases': [
   #     {
   #       'code': """
   #       >>> def so_big(x):
   #       ...     if x > 10:
   #       ...         print('huge')
   #       ...     if x > 5:
   #       ...         return 'big'
   #       ...     if x > 0:
   #       ...         print('small')
   #       ...     print("nothin'")
   #       >>> so_big(7)
   #       'big'
   #       >>> so_big(12)
   #       huge
   #       'big'
   #       >>> so_big(1)
   #       small
   #       nothin'
   #       """,
   #     }
   #   ]
   # },
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> def ab(c, d):
          ...     if c > 5:
          ...         print(c)
          ...     elif c > 7:
          ...         print(d)
          ...     print('foo')
          >>> ab(10, 20)
          10
          foo
          """,
        },
        {
          'code': """
          >>> def bake(cake, make):
          ...    if cake == 0:
          ...        cake = cake + 1
          ...        print(cake)
          ...    if cake == 1:
          ...        print(make)
          ...    else:
          ...        return cake
          ...    return make
          >>> bake(0, 29)
          1
          29
          29
          >>> bake(1, "mashed potatoes")
          mashed potatoes
          'mashed potatoes'
          """,
        },
      ]
    }
  ]
}