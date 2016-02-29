"""
wm johnson
construction no. 1
finished 12142015

in this first piece using python to construct csound scores i worked by adding events sucessively. this caused difficulty when i wanted to make an instr react to something another instr and i hadn't previously been using that instr. i did verify the possibility of using a time index with the nosie--->reverb thing. 
"""

import csound
import random

# setup score
score = csound.Score()
duo = score.add_staff(1, 7) #amp, pan, root, rootvol, interval, intvol, wavform # 
noise = score.add_staff(2, 4) #amp, pan, freq, density
env = score.add_staff(3, 5)#amp, pan, attack, sustain, decay
reverb = score.add_staff(100, 3) #size, damp, amp

# materials
ratios = [9/float(7), 13/float(10)]
ratios2 = [9/float(7), 13/float(10), 4/float(3), 3/float(2), 14/float(9)]
rhythms = [0.1, 0.8, 0.1, 0.8, 0.5, 0.8, 0.1, 0.8, 0.1]

# event sequence
root = 300
notes = [r*root for r in ratios]
notes2 = [r*root for r in ratios2]

# duo events
duo.add_event(0, 0, [0.1 for i in range(7)])
for i in range(len(notes)*7):
    duo.add_event("+", 10, [(i+1)/float(14), (random.randrange(40)/float(100))+0.3, root, random.random(), ratios[i%len(ratios)], random.random(), 12])
for i in range(len(notes)*7):
    duo.add_event("+", 10, [0.2, random.random(), notes[i%len(notes)], 1, ratios[i%len(ratios)], 1, 8])

# noise events
t = 140
noise.add_event(t, 0, [0 for i in range(4)])
for i in range(100):
    t = t + (11/float(10))
    noise.add_event(t, (11/float(10)), [rhythms[i%len(rhythms)], 0.5, ratios2[i%len(notes2)], random.randrange(60, 1000)]) 

# reverb event
reverb.add_event(t, 45, [0.4, 0.1, 1])

# write to file
score.write_score_file('01.sco')
