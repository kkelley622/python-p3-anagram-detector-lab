# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        matching = []

        for x in list:
            if(sorted([letter for letter in x]) == sorted([letter for letter in self.word])):
                matching.append(x)
                
        
        return matching