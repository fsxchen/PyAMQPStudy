#!/usr/bin/env python


import stomper

ch = stomper.connect("", "", "172.17.5.194")

stomper.send(ch, "hello")

print ch