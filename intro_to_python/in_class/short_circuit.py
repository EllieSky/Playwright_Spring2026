i = 0

def a():
     global i
     i += 1
     return True


def b():
    global i
    i += 1
    return False

def c():
    if a() or b():
        print("hello there")
    print(i)

c()

# will print 2 when a AND b
# will print 1 when b AND a
# will print "hello there" & print 1 when a OR b
