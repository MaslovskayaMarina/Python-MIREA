class FSM:
    def __init__(self):
        self.A = "A"
        self.B = "B"
        self.C = "C"
        self.D = "D"
        self.E = "E"
        self.F = "F"

        self.start = self.A
        self.current_state = self.start
    def rush(self):
        if self.current_state == self.A:
            self.current_state = self.B
            return 0
        elif self.current_state == self.D:
            self.current_state = self.A
            return 5
        else:
            raise KeyError
    def daub(self):
        if self.current_state == self.B:
            self.current_state = self.C
            return 1
        elif self.current_state == self.C:
            self.current_state = self.D
            return 2
        elif self.current_state == self.D:
            return 4
        elif self.current_state == self.E:
            return 7
        else:
            raise KeyError
    def smash(self):
        if self.current_state == self.F:
            self.current_state = self.B
            return 8
        elif self.current_state == self.E:
            self.current_state = self.F
            return 6
        elif self.current_state == self.D:
            self.current_state = self.E
            return 3
        else:
            raise KeyError
    
def main():
    state_machine = FSM()
    return state_machine


o = main()
o.rush() # 0
o.daub() # 1
o.daub() # 2
o.smash() # 3
o.daub() # 7
o.smash() # 6
o.smash() # 8
o.daub() # 1
o.daub() # 2
o.daub() # 4
o.rush() # 5
