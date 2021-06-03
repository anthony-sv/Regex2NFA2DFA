from Acceptor import Acceptor
from Transition import Transition
class Afn(Acceptor):
    def __init__(self, F, Fsm, T):
        super().__init__(F,Fsm)
        self.Transition = T
    @staticmethod
    def printAutomata(automata):
        states = set(sorted([x.getName() for x in automata.Fsm.Q]))
        qstates = ', '.join(states)
        print("")
        print("El AFN para la expresión regular es:")
        print(f"Q: {{{qstates}}}")
        alpha = set(sorted([x.getCharacter() for x in automata.Fsm.getAlphabet()]))
        salpha = ', '.join(alpha)
        print(f"Σ: {{{salpha}}}")
        print("q0:", automata.Fsm.q0.getName())
        print(f"F: {{{automata.F.getName()}}}")
        print("δ:")
        Transition.printTransition(automata.Transition.dict)
