epic_programmers_dict = {"Tim Berners-lee" : ['tbl@gmail.com', 111],
                         "Guido van Rossum" : ['gvr@gmail.com', 222],
                         "Linus Torvalds" : ['lt@gmail.com', 333],
                         "Larry Page" : ['lp.gmail.com', 444],
                         "Sergey Brin" : ['sb.gmail.com', 555]}

 
print epic_programmers_dict
print epic_programmers_dict['Tim Berners-lee']
print epic_programmers_dict['Tim Berners-lee'][1]
programmer = epic_programmers_dict['Tim Berners-lee']
print programmer[1]

personsName = raw_input("please enter a name: ")
print personsName
