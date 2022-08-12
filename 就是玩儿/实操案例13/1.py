class Instrument():
    def make_sound(self):
        pass

class Erhu(Instrument):
    def make_sound(self):
        print('二胡在演奏')

class Piano(Instrument):
    def make_sound(self):
        print('钢琴在演奏')

class Volin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')

class Bird(Instrument):
    def make_sound(self):
        print('小鸟在唱歌')

def play(instrument):
    instrument.make_sound()

if __name__ == '__main__':
    play(Erhu())
    play(Piano())
    play(Volin())
    play(Bird())