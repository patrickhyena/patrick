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

#part two
#number one
degrees_number = 150

radians_number = degrees_number * (180/(3/14))  

print("Degrees:" + str(degrees_number))  

print("Radians:" + str(radians_number)) 

 
#number two
class1 = 32 

class2 = 45 

class3 = 51 

class1_groups = 32//5 

class2_groups = 45//7 

class3_groups = 51//6 

leftovers1 = (class1 - (class1_groups * 5)) 

leftovers2 = (class2 - (class2_groups * 7)) 

leftovers3 = (class3 - (class3_groups * 6)) 

print("Number of Groups:") 

print("Class 1: " + str(class1_groups)) 

print("Class 2: " + str(class2_groups)) 

print("Class 3: " + str(class3_groups)) 

print("Number of Leftovers:") 

print("Class 1: " + str(leftovers1)) 

print("Class 2: " + str(leftovers2)) 

print("Class 3: " + str(leftovers3)) 

#number two
student1 = 80.0

student2 = 90.0

student3 = 66.5

average_score = ( student1 + student2 + student3 ) / 3 

print("Student scores:") 

print(student1) 

print(student2) 

print(student3) 

print("Average: " + str(average_score)) 

#number three
class1 = 32 

class2 = 45 

class3 = 51 

class1_groups = 32//5 

class2_groups = 45//7 

class3_groups = 51//6 

leftovers1 = (class1 - (class1_groups * 5)) 

leftovers2 = (class2 - (class2_groups * 7)) 

leftovers3 = (class3 - (class3_groups * 6)) 

print("Number of Groups:") 

print("Class 1: " + str(class1_groups)) 

print("Class 2: " + str(class2_groups)) 

print("Class 3: " + str(class3_groups)) 

print("Number of Leftovers:") 

print("Class 1: " + str(leftovers1)) 

print("Class 2: " + str(leftovers2)) 

print("Class 3: " + str(leftovers3)) 

#number four
pi = 3.14 

pie_diameter = 55.4 

pie_radius = pie_diameter / 2 

circumference = 2 * pi * pie_radius 

circumference_msg = "Jimmy’s pie has a circumference: " 

print(circumference_msg, circumference) 

#number five
meters = 20580 

speed = meters / 60 

frequency = 256 

wavelength = speed / frequency 

print("The speed (m/s): " + str(speed)) 

print("The frequency (Hz): " + str(frequency)) 

print("The wavelength (m): " + str(wavelength)) 