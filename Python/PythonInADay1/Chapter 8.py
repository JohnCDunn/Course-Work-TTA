print ('Part 1')
# creat a list of programmers

epic_programmers_list = ["Tim Berners-lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "larry Page",
                        "Sergey Brin",]


print "Epic programmers: " + epic_programmers_list[0]
print "Epic programmers: " + epic_programmers_list[1]
print "Epic programmers: " + epic_programmers_list[2]
print "Epic programmers: " + epic_programmers_list[3]
print "Epic programmers: " + epic_programmers_list[4]

print ('Part 2')
epic_programmers_list = ["Tim Berners-lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "larry Page",
                        "Sergey Brin",]
epic_programmers_list[4] = 'Me'

print "Epic programmers: " + epic_programmers_list[0]
print "Epic programmers: " + epic_programmers_list[1]
print "Epic programmers: " + epic_programmers_list[2]
print "Epic programmers: " + epic_programmers_list[3]
print "Epic programmers: " + epic_programmers_list[4]

print ('Part 3')
epic_programmers_list = ["Tim Berners-lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "larry Page",
                        "Sergey Brin",]

epic_programmers_list.append("me")
print "Epic programmers: " + epic_programmers_list[0]
print "Epic programmers: " + epic_programmers_list[1]
print "Epic programmers: " + epic_programmers_list[2]
print "Epic programmers: " + epic_programmers_list[3]
print "Epic programmers: " + epic_programmers_list[4]
print "Epic programmers: " + epic_programmers_list[5]

print ('Part 4')
print ('Loop through the list')
epic_programmers_list = ["Tim Berners-lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "larry Page",
                        "Sergey Brin",]
for programmer in epic_programmers_list:
    print programmer


print ('Part 5')
print ('Loop through the list again')
epic_programmers_list = ["Tim Berners-lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "larry Page",
                        "Sergey Brin",]
for programmer in epic_programmers_list:
    print "An epic programmer: " + programmer

print ('Part 6')
print ('New List process')
number_list = [1,2,3,4,5]
empty_number_list = []

for x in number_list:
    empty_number_list.append(x**2)

print empty_number_list
