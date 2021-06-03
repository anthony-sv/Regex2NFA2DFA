import sys
from AskAutomaton import AskAutomaton
from Subset import Subset
afn = AskAutomaton(sys.argv[1])
afn.Nfa.printAutomaton()
afd = Subset(afn)
afd.subsetConstruction()
afd.printAutomaton()