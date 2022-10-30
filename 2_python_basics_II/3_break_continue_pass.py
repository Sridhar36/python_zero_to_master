'''break vs continue vs pass
break - breaks the loop
continue - to continue for that iteration
pass - very rare - good way to have a place holder
'''

a = list(range(20))
for i in a:
    if i == 10:
        break
    # This loop breaks if i is 10, so, only i from 1 to 10 gets printed
    print(i)
