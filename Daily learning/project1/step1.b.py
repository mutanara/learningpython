 
source_names = ["Plante Niyomugenga", " Narcisse Mutabaruka", "Silas Gasasira", "Jean Luc Abayo"]

source_ps = [ "I never considered you a nice guy.", " You are insane boo, you know that?",
 "I regret 2016, I should have been more nice with you!", "Be careful, you might only be good at programming."]

source_message = """

Dear %s;

It has been a pleasure meeting you, and knowing for you from 2016. 
You have been a blessing and an asshole to me in some many wasy.
I enjoyed each laughter, lies, and adventures we shared. I hope you will let it go,
I have now found a hubby and we are about to get married. 
 
Thanks bro!

P.S. %s

Delice Fatiro.

"""

def make_messages(list_a, list_b):

    if len(list_a) == len(list_b):
        for x,y in zip (list_a, list_b):
            zipped = (x,y)
            print(source_message %(zipped))

make_messages(source_names, source_ps)
