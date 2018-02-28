# coding: utf-8

# Test for: Rohde&Schwarz HMC8042

import vxi11
instr = vxi11.Instrument("10.101.54.172")

print(instr.ask("*IDN?"))

# Apply 5V and 1A
instr.write("INST OUT1")
instr.write("APPLy 5,1")

# Current settings check
print("V and I now: ")
print(instr.ask("APPLy?"))
