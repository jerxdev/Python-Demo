
def replace(s, old, new):

    return new.join(s.split(old))

print(replace('Mississippi', 'i', 'I'))


replace('Mississippi', 'i', 'I'), 

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
print (replace(s, 'om', 'am')),

print (replace(s, 'o', 'a')),
