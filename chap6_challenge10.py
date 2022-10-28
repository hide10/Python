from distutils.command.build_scripts import first_line_re


sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
first_index = sentence.index(",")
slce = sentence[0:first_index]
print(slce)