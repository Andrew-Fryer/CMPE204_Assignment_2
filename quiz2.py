from lib204 import wff, semantic_interface
P, Q, R, S, T = map(wff.Variable, 'PQRST')

s5 = ((S>>R)>>(Q|(~S&R)))
print(" s5: %s" % s5)
print("s5 = %s" % s5.dump('python'))

# (b) Copy s5 and s6 formulae into the first steps below, and show the steps to
#     convert to negation normal form. An example is given, but it is the wrong
#     starting formula. You /must/ provide an explanation for each step. Possible
#     explanations might include (exact wording is not required)...
#      - starting formula
#      - de Morgans
#      - distribution
#      - replace implications
#      - double negation
#      - etc.
s5nnf = [
    [(S>>R)>>(Q|(~S&R)), 'starting formula'],
    [(~S|R)>>(Q|(~S&R)), 'replace implication'],
    [~(~S|R)|(Q|(~S&R)), 'replace implication'],
    [(~~S|~R)|(Q|(~S&R)), 'de Morgans'],
    [(S|~R)|(Q|(~S&R)), 'double negation'],
    [(S|~R)|(Q|(~S&R)), 'double negation'],
]

# (c) Copy s5 and s6 formulae into the first steps below, and show the steps to
#     convert to CNF using distribution, de Morgan's, implication removal, etc.
#     An example is given, but it is for the wrong formula. You /must/ provide
#     an explanation for each step. Possible explanations are listed above.
s5cnf = [
    [(S>>R)>>(Q|(~S&R)), 'starting formula'],
    [(~S|R)>>(Q|(~S&R)), 'replace implication'],
    [~(~S|R)|(Q|(~S&R)), 'replace implication'],
    [(~~S|~R)|(Q|(~S&R)), 'de Morgans'],
    [(S|~R)|(Q|(~S&R)), 'double negation'],
    [(S|~R)|(Q|(~S&R)), 'double negation'],
    [(S|~R)|((~Q|S)&(Q|R)), 'distribution'],
    [((S|~R)|(~Q|S))&((S|~R)|(Q|R)), 'distribution'],
]

# (d) Build the Tseitin encoding of both s5 and s6 using the semantic_interface
#     library to create auxiliary variables as necessary. Examples for different
#     formulae are given. There is a limit of one operator per auxiliary variable,
#     and you may re-use auxiliary variables as necessary.
s5tseitin = semantic_interface.Encoding()
x1 = s5tseitin.tseitin(S>>R, 'x1')
x2 = s5tseitin.tseitin(~S, 'x2')
x3 = s5tseitin.tseitin(x2&R, 'x3')
x4 = s5tseitin.tseitin(Q|x3, 'x4')
x5 = s5tseitin.tseitin(x1>>x4, 'x5')
s5tseitin.finalize(x5)

assert isinstance(x1, wff.WFF)
print(s5tseitin, dir(s5tseitin), s5tseitin.dump())
