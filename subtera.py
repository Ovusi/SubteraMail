from textsbanners.banner import Banner
from textsbanners.text import Text

Banner()
Text()


class Subt:
    def st(self):
        userinput = input("[*] Type Option> ")
        if userinput == "1":
            import modules.sendmsg
            sm = modules.sendmsg
            sm.Sendmsg()
        else:
            print("\nOption does not exist. Please select from the options above.")
            Subt.st(Subt)


Subt.st(Subt)
