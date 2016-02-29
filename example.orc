sr = 44100
kr = 441
ksmps = 100
nchnls = 2

ga1 init 0

;duophone, produces interval given [amp, pan, root, rootvol, ratio above root, uppervol,  wav (vco2)]
instr 1
a1 vco2 5000, p6, p10
a2 vco2 5000, p6*p8, p10
aenv expseg 0.01, 0.01, p4, p3-0.02, p4, 0.01, 0.01
amix = (a1*p7)+(a2*p9)
al, ar pan2 amix, p5
outs al*aenv, ar*aenv
ga1 = ga1 + amix
endin

;original chaotic noise generator [amp, pan, root, nfactor]
instr 2
adel init 0
anoise1 noise 100, 0.5 
anoise2 dust 5000, p7 
aosc oscil anoise1, p6
afil lowres anoise1, p6, 0.9
amix = anoise2*0.2 + afil
amix = amix * p4
al, ar pan2 amix, p5
outs al, ar
ga1 = ga1 + al + ar
endin

;eveloped sin wav [amp, pan, a, s, r]
instr 3 
a1 expseg 0.001, p6, 1, p7, 1, p8, 0.001
a2 oscil 5000, p4
amix = a1*a2
al, ar pan2 amix, p5
outs al, ar
ga1 = ga1 + al + ar
endin

;reverb [roomsize, hfdamp, amp]
instr 100
a1, a2 freeverb ga1, ga1, p4, p5
a3 = a1 *p6
a4 = a1 *p6
outs, a3, a4
ga1 = 0
endin

