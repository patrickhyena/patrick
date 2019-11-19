guest_list = ["dad", "mom", "invisible tom","nga"]
del guest_list[0]
guest_list.append("coon")
for i in range(4):
     print(guest_list)
guest_list.insert(0, "crook")
guest_list.insert(2, "crock")
guest_list.append("dog")
for i in range(7):
    print("Hey " + guest_list[i] + ", you're invited to dinner")
print("A bigger table has been found")

print("i can only invite two people lol")
while len(guest_list) !=2:
   guest_popped = guest_list.pop()
   print(guest_popped + ", you're not invited")
for i in range(2):
 print(guest_list[i] + ", hey you're cool, you're still invited dawg")

del guest_list[0]

print(guest_list)

del guest_list[0]

print(guest_list)




locations = ["london", "atlanta", "germany", "home", "your home"]
print(locations)
print(sorted(locations))
print(sorted(locations))
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

