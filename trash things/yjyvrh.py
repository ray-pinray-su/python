import turtle as t
import random as r

t.tracer(0)
for i in range(100000):
    a = r.randrange(361)
    t.right(a)
    t.forward(r.randrange(5, 30))
t.update()
t.done()
