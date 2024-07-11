Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88}

Keymax = max(Tv, key= lambda x: Tv[x])

max_value = max(Tv.values())
print(f"Keymax: {Keymax}")
print(f"max_value: {max_value}")
