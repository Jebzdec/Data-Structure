class TorKham:

    def __init__(self):

        self.words = []

    def restart(self):

        self.words = []
        return "game restarted"

    def play(self, word):

        n = len(self.words)
        if n == 0:
            self.words.append(word)
            return f'\'{word}\' -> {self.words}'
        elif word[0].lower() == self.words[-1][-2].lower() \
                and word[1].lower() == self.words[-1][-1].lower():
            self.words.append(word)
            return f'\'{word}\' -> {self.words}'
        else:
            return f'\'{word}\' -> game over'


torkham = TorKham()

print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')

for i in range(len(S)):
    try:
        Key, Word = S[i].split()
    except:
        Key = S[i][0]
    if Key == 'P':
        print(torkham.play(Word))
    elif Key == 'R':
        print(torkham.restart())
    elif Key == 'X':
        exit()
    else:
        print(f'\'{S[i]}\' is Invalid Input !!!')
        exit()
