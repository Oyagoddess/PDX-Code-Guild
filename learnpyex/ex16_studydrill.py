from sys import argv


script, filename = argv  # will use test.txt that was created in ex16

txt = open(filename) # opens test.txt that we just created

print txt.read()




