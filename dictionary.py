sample_dict = {}
details = {
    "name":"Anaadi",
    "age":12,
    "city":"mycity"
}

print(details)

sample_dict = ["Anaadi,12,mycity"]

print(details.keys())

print(details.values())

for key in details.keys():
    print(key, details [key])

if "country" in details:
    print(details["country"])
else:
    print("Not present")

if "city" in details:
    print(details["city"])
else:
    print("not there")

print(details["name"])

details["country"] = "mycountry"

del details["city"]

details["age"] = 13


print(len(details))

details["marks"] = [1,2,3,4,5]