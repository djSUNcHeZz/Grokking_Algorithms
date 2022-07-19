# Countdown recursion

def countdown(i):
    if i >= 0:
        print(i, end=" ")
    else:
        return
    countdown(i - 1)


countdown(10)
