import turtle as t

t.speed(0)
import time

for i in range(100):
    t.right(i * 6)
    t.forward(100)
    time.sleep(1)
    t.home()
    t.clear()
