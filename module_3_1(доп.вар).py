calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(x):
    global calls
    count_calls()
    string = (len(x), x.upper(), x.lower())
    return string


def is_contains(y, z):
    global calls
    count_calls()
    string = y.lower()
    a = False
    for i in range(0, len(z)):
        if z[i].lower() != string:
            continue
        else:
            return True
    for j in range(0, len(z)):
        if z[j].lower() == string:
            continue
        else:
            return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
