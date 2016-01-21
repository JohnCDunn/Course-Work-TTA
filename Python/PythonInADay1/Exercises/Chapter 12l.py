epic_programmers_dict = {"tim berners-lee" : ['tbl@gmail.com', 111],
                         "guido van rossum" : ['gvr@gmail.com', 222],
                         "linus torvalds" : ['lt@gmail.com', 333],
                         "larry page" : ['lp.gmail.com', 444],
                         "sergey brin" : ['sb.gmail.com', 555]}

 
def searchPeople(personsName):
    try:
        personsInfo = epic_programmers_dict[personsName]
        print 'Name: ' + personsName.title()
        print 'Email: ' + personsInfo[0]
        print 'number: ' + str(personsInfo[1])
    
    except:
        print 'No information found for that name'


userWantsMore = True
while userWantsMore == True:
    
    personsName = raw_input("please enter a name: ").lower()
    searchPeople(personsName)
    userWantsMore = False
    searchAgain = raw_input('Search afain? (y/n)')
    if searchAgain == 'y':
        userWantsMore = True
    elif searchAgain == 'n':
        userWantsMore = False
    else:
        print "I don't understand what you mean, quitting"
        userWantsMore = False
        
