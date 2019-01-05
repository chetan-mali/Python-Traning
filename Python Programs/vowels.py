state_name =['Alabama','California','Oklahoma','Florida']
for a in  ['a','e','i','o','u','A','E','I','O','U']:
    state_name=[word.replace(a,"") for word in state_name]
print(state_name)