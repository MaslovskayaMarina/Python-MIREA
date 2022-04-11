class FSM:
    def __init__(self):
        self.A = "A"
        self.B = "B"
        self.C = "C"
        self.D = "D"
        self.E = "E"
        self.F = "F"
        self.G = "G"

        self.start = self.A
        self.current_state = self.start

    def smash(self):
        if self.current_state == self.A:
            self.current_state = self.B
            return 0
        elif self.current_state == self.C:
            self.current_state = self.D
            return 4
        else:
            raise KeyError

    def sweep(self):
        if self.current_state == self.A:
            self.current_state = self.F
            return 1
        elif self.current_state == self.B:
            self.current_state = self.C
            return 3
        elif self.current_state == self.E:
            self.current_state = self.F
            return 7
        elif self.current_state == self.G:
            return 9
        else:
            raise KeyError

    def send(self):
        if self.current_state == self.A:
            self.current_state = self.E
            return 2
        elif self.current_state == self.C:
            self.current_state = self.A
            return 5
        elif self.current_state == self.D:
            self.current_state = self.E
            return 6
        elif self.current_state == self.F:
            self.current_state = self.G
            return 8
        else:
            raise KeyError


def main():
    state_machine = FSM()

    return state_machine


o = main()
print(o.smash()) # 0
print(o.sweep()) # 3
print(o.send()) # 5
print(o.smash()) # 0
print(o.sweep()) # 3
print(o.smash()) # 4
print(o.send()) # 6
print(o.sweep()) # 7
print(o.send()) # 8
print(o.sweep()) # 9
