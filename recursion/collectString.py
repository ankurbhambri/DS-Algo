# collectStrings Solution


def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    return resultArr


obj = {
    "stuff": "foo",
    "data": {
        "val": {
            "thing": {
                "info": "bar",
                "moreInfo": {"evenMoreInfo": {"weMadeIt": "baz"}},
            }
        }
    },
}

# TC: O(n)
# SC: O(n)
print(collectStrings(obj))  # ['foo', 'bar', 'baz'])
