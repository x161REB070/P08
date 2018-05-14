# Programmu veidoja: Karlis Reinis Ulmanis */
print 'Ievadi bumbas atrumu:'
vs = raw_input()    #s jo raw ir string
v = int(vs)
g = 9.81
print 'Ievadi laika momentu:'
ts = raw_input()    #s jo raw ir string
t = int(ts)
y = (v * t)-((g * t ** 2) / 2)
print 'Pec %.3f sekundem bumba bus %.2f metru augstuma \n' %(t,y)
