class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.combinations = []
        self.index = 0

        def backT(i, subset):
            if (len(subset) == combinationLength):
                self.combinations.append(subset)
                return
            if (i == len(characters)):
                return
            backT(i + 1, subset + self.characters[i])
            backT(i + 1, subset)

        backT(0, "")

    def next(self) -> str:
        if self.index < len(self.combinations):
            result = self.combinations[self.index]
            self.index += 1
            return result
        return ""

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()