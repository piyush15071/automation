from subprocess import Popen, PIPE

control_c_sequence = '''keydown Control_L
key C
keyup Control_L
'''

def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)

print("Will print")
keypress(control_c_sequence)
print("Will not print")
