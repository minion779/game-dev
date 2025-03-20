#tuple

my_tuple = ("Anaadi",12)

#packing

address = (54, "Seed Lane","UK","WK23DJI")

#unpacking

housenumber, street, country, post_code = address
print(housenumber)

colours = ("red","blue","black","grey","green")
colours_1 = "red","blue","black","grey","green"

print(colours_1)

#nested tuple

ldetail = ("Anaadi",12,"football",["89%", "98%", "90%", "88%"])
print(ldetail[3][1])

'''
ldetail[1]=13
print(ldetail[1])
'''

ldetail[3][1]="100%"
print(ldetail[3][1])