from banner import Banner
from text import Text

Banner()
Text()


class Subt:
    def st(self):
        userinput = input("[*] Type Option> ")
        if userinput == "1":
            import sendmsg
            sm = sendmsg
            sm.Sendmsg()
        else:
            print("\nOption does not exist. Please select from the options above.")
            Subt.st(Subt)


Subt.st(Subt)