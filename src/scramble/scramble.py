from random import *

class Scramble:
    def __init__(self, input_file : str = "input.txt"):
        """
        initializes the Scramble object
        :param input_file: the file from which a random word is selected
        """
        #
        # opening the file and selecting a random line as the sentence
        #
        with open(input_file, "r") as f:
            input_sentences = f.readlines()
            self._sentence = input_sentences[randint(0, len(input_sentences) - 1)]
            f.close()
        #
        # the score is the length of the sentence without the spaces
        #
        self._score = len(self)

        #
        # shuffling the original sentence and getting a shuffled one
        #
        self._shuffled_sentence = self.shuffle_sentence()

        #
        # the stack in which the swap parameters are saved in order to call them again when an undo is made
        #
        self._stack_of_swaps = []

    @property
    def sentence(self):
        return self._sentence

    @property
    def score(self):
        return self._score

    @property
    def shuffled_sentence(self):
        return self._shuffled_sentence

    @sentence.setter
    def sentence(self, new_sentence : str):
        self._sentence = new_sentence

    @score.setter
    def score(self, new_score : int):
        self._score = new_score

    @shuffled_sentence.setter
    def shuffled_sentence(self, new_shuffled_sentence : str):
        self._shuffled_sentence = new_shuffled_sentence

    def shuffle_sentence(self):
        """
        shuffles the original sentence by making between 10 and 20 random swaps
        the first and last character is not taken in consideration
        :return: the shuffled sentence
        """
        sentence = self._sentence
        for i in range(randint(10, 20)):
            index1 = index2 = 0
            while index1 == 0 or index1 == len(sentence) - 2 or sentence[index1] == " ":
                index1 = randint(1, len(sentence) - 3)
            while index2 == 0 or index2 == len(sentence) - 2 or sentence[index2] == " ":
                index2 = randint(1, len(sentence) - 3)
            sentence = self.swap_characters(sentence, index1, index2)
        return sentence

    def swap(self, word1 : int, letter1 : int, word2 : int, letter2 : int):
        """
        swaps letter1 from word1 with letter2 from word2
        it changes the shuffled_sentence, the score and adds the parameters to stack_of_swaps
        :param word1: first word
        :param letter1: the letter from the first word
        :param word2: second word
        :param letter2: the letter from the second word
        :return: returns the modified sentence
        """
        words_in_sentence = self._shuffled_sentence.split(" ")
        if word1 >= len(words_in_sentence):
            raise Exception("there are not that many words! word1 doesn't exist!")
        if word2 >= len(words_in_sentence):
            raise Exception("there are not that many words! word2 doesn't exist!")
        if letter1 >= len(words_in_sentence[word1]):
            raise Exception("there are not that many letters in word1!")
        if letter2 >= len(words_in_sentence[word2]):
            raise Exception("there are not that many letters in word2!")
        self._stack_of_swaps.append([word1, letter1, word2, letter2])
        self._score -= 1

        if word1 != word2:
            [words_in_sentence[word1], words_in_sentence[word2]] = self.swap_characters_sentences(words_in_sentence[word1], letter1, words_in_sentence[word2], letter2)
        else:
            words_in_sentence[word1] = self.swap_characters(words_in_sentence[word1], letter1, letter2)

        sentence = ""
        for word in words_in_sentence:
            sentence += word
            sentence += " "
        # in the end, the sentence will have a whitespace in the end, so we're not taking that into consideration
        self._shuffled_sentence = sentence[:-1]
        return sentence[:-1]

    def undo(self):
        """
        undo the last operation (which can only be a swap) by taking the parameters from the stack and
        swapping again the characters and not changing the score
        :return: True
        """
        [word1, letter1, word2, letter2] = self._stack_of_swaps.pop()
        self.swap(word1, letter1, word2, letter2)
        self._score += 1
        return True

    def __str__(self):
        #
        # the string representation of the scramble sentence
        #
        return "score: " + str(self._score) + "\n" + self._shuffled_sentence

    def __len__(self):
        #
        # the length of the given sentence
        #
        length = 0
        for index in range(len(self._sentence)):
            if self._sentence[index] != " ":
                length += 1
        return length

    @staticmethod
    def swap_characters(sentence: str, index1: int, index2: int):
        """
        swaps 2 characters (having indexes index1 and index2) of a sentence
        :param sentence: the given sentence
        :param index1: the index of the first character to be swapped
        :param index2: the index of the second character to be swapped
        :return: the modified sentence
        """
        swapped_sentence = ""
        for i in range(len(sentence)):
            if i == index1:
                swapped_sentence += sentence[index2]
            elif i == index2:
                swapped_sentence += sentence[index1]
            else:
                swapped_sentence += sentence[i]
        return swapped_sentence

    @staticmethod
    def swap_characters_sentences(sentence1: str, index1: int, sentence2: str, index2: int):
        """
        swaps 2 characters from 2 different sentences
        :param sentence1: the first sentence
        :param index1: the index of the character in the first sentence
        :param sentence2: the second sentence
        :param index2: the index of the character in the second sentence
        :return: an array that contains the modified sentences
        """
        swapped_sentence1 = ""
        swapped_sentence2 = ""

        for i in range(len(sentence1)):
            if i == index1:
                swapped_sentence1 += sentence2[index2]
            else:
                swapped_sentence1 += sentence1[i]

        for i in range(len(sentence2)):
            if i == index2:
                swapped_sentence2 += sentence1[index1]
            else:
                swapped_sentence2 += sentence2[i]

        return [swapped_sentence1, swapped_sentence2]
