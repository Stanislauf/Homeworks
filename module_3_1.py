calls = 0


def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    string = str(string)
    result = (len(string), string.upper(), string.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('KaVabanGa'))
print(string_info('Uno, DuE, TRE, quattro'))
print(is_contains('tRe', ['UnO', 'DuE', 'TRE', 'quattro']))
print(is_contains('POMOdoro', ['UnO', 'DuE', 'TRE', 'POmmoDoro']))
print(calls)