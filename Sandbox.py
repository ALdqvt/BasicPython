import numpy as np

import cellpylib as cpl

size = 201
rule = 105
simple = True
#103, 105, 109

if simple:
    cellular_automaton = cpl.init_simple(size)
else:
    cellular_automaton = cpl.init_random(size)


cellular_automaton = cpl.evolve(cellular_automaton, timesteps=int(size*1.5), memoize=True,
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, rule))
cpl.plot(cellular_automaton)