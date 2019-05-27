 
source_names = ["foure_x", "second_ex", "first_ex", "third_ex"]

source_ps = [ "I never considered you a nice guy.", " You are insane boo, you know that?",
 "I regret 2016, I should have been more nice with you!", "Be careful, you might only be good at programming."]

source_message = """

Dear {person};

It has been a pleasure meeting you, and knowing for you from 2016. 
You have been a blessing and an asshole to me in some many wasy.
I enjoyed each laughter, lies, and adventures we shared. I hope you will let it go,
I have now found a hubby and we are about to get married. 
 
Thanks bro!

P.S. {takeaway}

The Girl.

"""

def make_messages(list_a=None, list_b=None):
        if (list_a, list_b) is not None:
                if len(list_a) == len(list_b):
                        i = 0
                        for name in list_a:
                                ps = list_b[i]
                                new_msg = source_message.format(person=name,takeaway=ps)
                                i += 1
                                print(new_msg)
                        return new_msg

def send ():
    make_messages (source_names, source_ps)

if __name__ == "__main__": send()
