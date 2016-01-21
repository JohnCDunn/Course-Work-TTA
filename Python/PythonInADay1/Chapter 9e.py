epic_programmers_dict = {"Tim Berners-lee" : 'tbl@gmail.com',
                         "Guido van Rossum" : 'gvr@gmail.com',
                         "Linus Torvalds" : 'lt@gmail.com', }
epic_programmers_dict["Larry Page"]='lp.gmail.com'
epic_programmers_dict["Sergey Brin"]='sb.gmail.com'
print 'before delete'
print epic_programmers_dict

del epic_programmers_dict['Sergey Brin']
print 'after delete'
print epic_programmers_dict

