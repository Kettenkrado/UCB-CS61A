test = {
    "name": "Dictionaries",
    "points": 0,
    "suites": [
        {
            "type": "wwpp",
            "cases": [
                {
                    "code": """
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          25
          >>> len(pokemon)
          3
          >>> 'mewtwo' in pokemon
          False
          >>> 'pikachu' in pokemon
          True
          >>> 25 in pokemon
          False
          >>> 148 in pokemon.values()
          True
          >>> 151 in pokemon.keys()
          False
          >>> 'mew' in pokemon.keys()
          True
          """,
                }
            ],
        },
        # {
        #     "type": "wwpp",
        #     "cases": [
        #         {
        #             "code": """
        #   >>> letters = {'a': 1, 'b': 2, 'c': 3}
        #   >>> 'a' in letters
        #   True
        #   >>> 2 in letters
        #   False
        #   >>> sorted(list(letters.keys()))
        #   ['a', 'b', 'c']
        #   >>> sorted(list(letters.items()))
        #   [('a', 1), ('b', 2), ('c', 3)]
        #   """,
        #         }
        #     ],
        # },
    ],
}