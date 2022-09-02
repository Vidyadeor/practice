def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

#@make_pretty
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)

#Generator
def simple():
    for i in range(10):
        if (i % 2 == 0):
            yield i
            # Successive Function call using for loop
for i in simple():
    print(i)