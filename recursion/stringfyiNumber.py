def stringifyNumbers(obj):
    for key in obj:
        if type(obj[key]) is int:
            obj[key] = str(obj[key])
        if type(obj[key]) is dict:
            obj[key] = stringifyNumbers(obj[key])
    return obj


obj = {
    "num": 1,
    "test": [],
    "data": {"val": 4, "info": {"isRight": True, "random": 66}},
}

print(stringifyNumbers(obj))

{
    "num": "1",
    "test": [11],
    "data": {"val": "4", "info": {"isRight": True, "random": "66"}},
}
print(stringifyNumbers(obj))
