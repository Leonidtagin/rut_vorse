calls = 0
def count_calls():
    global calls
    calls += 0
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [item.lower() for item in list_to_search]
info = string_info("URBAN.")
print(info)
contains = is_contains("UrBaN", ["URBAN"])
print(contains)
print(calls)

