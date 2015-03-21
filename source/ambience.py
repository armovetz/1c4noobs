# <AMB_PAYERS> is list of non-empty unique strings, one string per payer
AMB_PAYERS = [ \
"Саша", \
"Маша"  \
]

# <AMB_SPECIAL_PURPOSES> is list of non-empty unique strings, one string per purpose
# these purposes are ignored later for creditors
AMB_SPECIAL_PURPOSES = [    \
"особое",   \
"квартира"  \
]


# <AMB_PURPOSE> is list of non-empty unique strings, one string per purpose
AMB_PURPOSES = [    \
"еда",      \
"общие",    \
"Саша",     \
"Маша"      \
]

AMB_PURPOSES += AMB_SPECIAL_PURPOSES

# Proportions set how much each of payer pays for corresponding purpose
# <AMB_PROPORTIONS> var must be list with next restrictions:
# 1. length of <AMB_PROPORTIONS> == length of <AMB_PURPOSES>
# 2. <AMB_PROPORTIONS> is list of *prop*, and:
#       a. *prop* is list of integer/float values
#       b. length of *prop* == length of <AMB_PAYERS>
#       c. elements of *prop* are non-negative and their sum is 1.0;
#          OR *prop* is list of <-1> values, which mean corresponding purpose
#          must be treated specially and it won't be taken into account later
#          when computing debts
AMB_PROPORTIONS = [     \
[   0.75,    0.25   ],  \
[   0.5,     0.5    ],  \
[   1.0,     0.0    ],  \
[   0.0,     1.0    ],  \
[   -1,      -1     ],  \
[   -1,      -1     ]   \
]

def checkAmbience():
    """ Checks settings according to restrictions described above. """ 

    try:
        assert type(AMB_PAYERS) is list                 # AMB_PAYERS is list
        assert len(AMB_PAYERS) > 0                      # non-empty
        assert len(set(AMB_PAYERS)) == len(AMB_PAYERS)  # with unique elements
        for payer in AMB_PAYERS:                        # elements are non-empty strings
            assert (type(payer) is str) and (payer != "")
    except AssertionError:
        raise Exception("[GAG ASSERT] bad AMB_PAYERS")
    
    try:
        assert type(AMB_PURPOSES) is list                   # AMB_PURPOSES is list
        assert len(AMB_PURPOSES) > 0                        # non-empty
        assert len(set(AMB_PURPOSES)) == len(AMB_PURPOSES)  # with unique elements
        for purpose in AMB_PURPOSES:                        # elements are non-empty strings
            assert (type(purpose) is str) and (purpose != "")    
    except AssertionError:
        raise Exception("[GAG ASSERT] bad AMB_PURPOSES")
    
    #try:
    assert type(AMB_PROPORTIONS) is list                # AMB_PROPORTIONS is list
    assert len(AMB_PROPORTIONS) == len(AMB_PURPOSES)    # length == length of AMB_PURPOSES
    for prop in AMB_PROPORTIONS:                        # each *prop* must :
        assert (type(prop) is list) and (len(prop) == len(AMB_PAYERS))  # - be list with length == length of AMB_PAYERS
        for p in prop:
            assert (type(p) is int) or (type(p) is float)               # - be list of integers/floats
    
        if prop != ( [-1] * len(AMB_PAYERS) ):                          # - be rather [-1, ... -1]
            assert sum(prop) == 1.0                                     # - or list of positives with sum == 1.0
            for p in prop:
                assert p >= 0
    #except AssertionError:
    #    raise Exception("[GAG ASSERT] bad AMB_PROPORTIONS")

checkAmbience()




