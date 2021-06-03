from Thompson import Thompson
class AskAutomaton:
    def __init__(self, string):
        t = Thompson(string)
        t.ThompsonContruction()
        self.Nfa = t