epic_programmers_dict = {"tim berners-lee" : ['tbl@gmail.com', 111],
                         "guido van rossum" : ['gvr@gmail.com', 222],
                         "linus torvalds" : ['lt@gmail.com', 333],
                         "larry page" : ['lp.gmail.com', 444],
                         "sergey brin" : ['sb.gmail.com', 555]}

 
print epic_programmers_dict
print epic_programmers_dict['tim berners-lee']
print epic_programmers_dict['tim berners-lee'][1]
programmer = epic_programmers_dict['tim berners-lee']
print programmer[1]

personsName = raw_input("please enter a name: ").lower()
print personsName
try:
    personsInfo = epic_programmers_dict[personsName]
    print 'Name: ' + personsName
    print 'Email: ' + personsInfo[0]
    print 'number: ' + str(personsInfo[1])
    
except:
    print 'No information found for that name'


