# -*- coding: utf-8 -*-
import threading
import time

from werkzeug.local import Local, LocalStack

a = LocalStack()

a.push({'n':123})

def func():
    a.push({'c':456})
    print(a)
    print(a.top)

thread = threading.Thread(target=func)
thread.start()

time.sleep(1)

print(a)
print(a.top)

