
# DO NOT EDIT

# Assignment for 17atf4

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')
s1 = (~P|(~T|S))
s2 = (P|(T|~S))
s3 = ((S|T)&(T|~S))
s4 = ((T|P)&(T|~P))

s5 = ((S>>R)>>(Q|(~S&R)))
s6 = ((~R>>(Q&~S))|~(S|~R))
