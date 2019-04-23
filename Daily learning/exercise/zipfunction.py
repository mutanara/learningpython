source_names = ["fourth_ex", "second_ex", "first_ex", "third_ex"]

source_ps = [ "I never considered you a nice guy.", " You are insane boo, you know that?",
 "I regret 2016, I should have been more nice with you!", "Be careful, you might only be good at programming."]

#First_way to do it:
zip (source_names, source_ps)
for x in zip (source_names, source_ps):
    print(x)


#Second_way to do it: 
for x, y in zip(source_names,source_ps):
    print(x,y)

#Third_way to do it:
for x,y in zip(source_names, source_ps):
    zipped = (x,y)
    print (zipped)

