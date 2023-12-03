from src.scramble.scramble import Scramble

class UI:
    def __init__(self, scramble : Scramble = None):
        if scramble is None:
            scramble = Scramble()
        self._scramble = scramble

    def start(self):
        print("the scrambled word: " + self._scramble.shuffled_sentence)
        while True:
            command = input("")
            params = command.split(" ")
            if params[0] == "undo":
                self._scramble.undo()
                print(self._scramble)
            elif params[0] == "swap":
                if len(params) == 6:
                    if params[1].isdigit() and params[2].isdigit() and params[4].isdigit() and params[5].isdigit() and params[3] == "-":
                        try:
                            self._scramble.swap(int(params[1]), int(params[2]), int(params[4]), int(params[5]))
                            print(self._scramble)

                            if self._scramble.sentence == self._scramble.shuffled_sentence:
                                print("victory! the word was indeed " + self._scramble.sentence + " and your score is " + str(self._scramble.score))
                                exit()
                            elif self._scramble.score == 0:
                                print("defeat! the word was " + self._scramble.sentence)
                                exit()
                        except Exception as e:
                            print(e)
                    else:
                        print("incorrect swap command!")
                else:
                    print("incorrect swap command!")
            else:
                print("invalid command")