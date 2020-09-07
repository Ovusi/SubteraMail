#!/usr/bin/env python
from textsbanners.banner import Banner
from textsbanners.text import Text


class Subt:
    def st(self):
        userinput = input("[*] Type Option> ")
        if userinput == "1":
            from modules.sendmsg import Sendmsg
            sm = Sendmsg
            sm.start()
        else:
            print("\nOption does not exist. Please select from the options above.")
            Subt.st(Subt)


Subt.st(Subt)
