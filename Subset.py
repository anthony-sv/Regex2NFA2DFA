from AFD import Afd
from FSM import Fsm
from Alphabet import Alphabet
from Transition import Transition
from State import State
from PlotAutomaton import PlotAutomaton
class Subset:
    def __init__(self, nfa):
        self.nfa = nfa
        self.dfa = Afd([], Fsm([], None, Alphabet()), Transition({}))

    def epsilonClosure(self, root):
        if not isinstance(root, set):
            visiteddict = dict()
            for x in self.nfa.Nfa.automata.Fsm.Q:
                visiteddict[x] = False
            queue = []
            queue.append(root)
            visiteddict[root] = True
            while queue:
                s = queue.pop(0)
                g = self.nfa.Nfa.automata.Transition.dict[(s, 'Ɛ')] if (s, 'Ɛ') in self.nfa.Nfa.automata.Transition.dict.keys() else None
                if (s, 'Ɛ') in self.nfa.Nfa.automata.Transition.dict.keys():
                    for i in g:
                        if i in visiteddict.keys() and visiteddict[i] == False:
                            queue.append(i)
                            visiteddict[i] = True
                else:
                    pass
            return {key for key,value in visiteddict.items() if value== True}
        else:
            states = set()
            for x in root:
                ec = self.epsilonClosure(x)
                for y in ec:
                    states.add(y)
            return states

    def precalcmove(self, symbol):
        precal= dict()
        for key, value in self.nfa.Nfa.automata.Transition.dict.items():
            if key[1] == symbol.getCharacter():
                for x in value:
                    precal[key[0]] = x
        return precal

    def move(self,DFAstate, symbol):
        Temp = set()
        g = self.precalcmove(symbol)
        for x in DFAstate:
            if x in g.keys():
                Temp.add(g[x])
        return Temp

    def getAFD(self, listofstates):
        pass

    def subsetConstruction(self):
        inits = self.epsilonClosure(self.nfa.Nfa.automata.Fsm.q0)
        initsfafd= State(inits, True, False)
        self.dfa.Fsm.q0 = initsfafd
        kerneldict = dict()
        markedstates = dict()
        markedstates[frozenset(inits)] = False
        afdprovlistofstates = [inits]
        isfinaldict = dict()
        queue = []
        queue.append(inits)
        markedstates[frozenset(inits)] = True
        while queue:
            state = queue.pop()
            markedstates[frozenset(state)] = True
            for x in self.nfa.Nfa.automata.Fsm.Sigma.sigma:
                Temp = self.move(set(state), x)
                if len(Temp)==0:
                    pass
                else:
                    if frozenset(Temp) not in kerneldict.keys():
                        newState = self.epsilonClosure(Temp)
                        kerneldict[frozenset(Temp)] = newState
                        if newState not in afdprovlistofstates:
                            afdprovlistofstates.append(newState)
                            queue.append(newState)
                            markedstates[frozenset(newState)] = False
                        else:
                            pass
                        self.dfa.Transition.dict[(State(state), x)] = State(newState)
                    else:
                        ns = kerneldict[frozenset(Temp)]
                        nsafd = State(ns)
                        self.dfa.Transition.dict[(State(state), x)] = nsafd
        fs = self.nfa.Nfa.automata.F
        for x in afdprovlistofstates:
            if fs in x:
                t = State(x, False, True)
            else:
                t = State(x)
            self.dfa.Fsm.Q.append(t)
        self.dfa.Fsm.Sigma.sigma = self.nfa.Nfa.automata.Fsm.Sigma.sigma
        # 10. Marcamos como estados finales del AFD, a los que contegan estados finales del AFN
        for x in self.dfa.Fsm.Q:
            if x.getIsFinalState():
                self.dfa.F.append(x)
    def printAutomaton(self):
        print()
        print("El AFD para el AFN es:")
        Afd.printDFAStates(self.dfa.Fsm.Q)
        Afd.printAlphabet(self.dfa.Fsm.Sigma.sigma)
        print("q0:", Afd.printDFAState(self.dfa.Fsm.q0))
        Afd.printFinalStates(self.dfa.F)
        print("δ:")
        Afd.printDFATransition(self.dfa.Transition.dict)
        P = PlotAutomaton(self.dfa)
        P.plotDFA(self.nfa.Nfa.regex)
