mylist = [1,2,3,4, ["adadadad"],5]

details = {
    "name":"Anaadi",
    "age":12,
    "city":"mycity"

}

classroom = {
    "Anaadi": {
        "age":12,
        "city":"mycity",
        "marks":[1,2,3,4,5]
    },
        "Nishiv": {
            "age":11,
            "city":"hiscity",
            "marks":[2,3,4,5,6]
    }
}

print(classroom["Anaadi"]["city"])
print(classroom["Nishiv"]["marks"][3])

#length of nested dictionary
var = classroom["Anaadi"]
print(len(var))