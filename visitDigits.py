class SevenSegmentDisplay:
    def __init__(self, number, top_left, top, top_right, bottom_right, bottom, bottom_left, middle) -> None:
        self.top_left = top_left
        self.top = top
        self.top_right = top_right
        self.bottom_right = bottom_right
        self.bottom = bottom
        self.bottom_left = bottom_left
        self.middle = middle
        self.number = number

    def getSegments(self):
        return [self.top_left, self.top, self.top_right, self.bottom_right, self.bottom, self.bottom_left, self.middle]

    def __repr__(self) -> str:
        return str(self.number)
    
    def __str__(self) -> str:
        return str(self.number)
    
    def __eq__(self, other) -> bool:
        return self.top_left == other.top_left and self.top == other.top and self.top_right == other.top_right and self.bottom_right == other.bottom_right and self.bottom == other.bottom and self.bottom_left == other.bottom_left and self.middle == other.middle


zero = SevenSegmentDisplay(0, True, True, True, True, True, True, False)
one = SevenSegmentDisplay(1, False, False, True, True, False, False, False)
two = SevenSegmentDisplay(2, False, True, True, False, True, True, True)
three = SevenSegmentDisplay(3, False, True, True, True, True, False, True)
four = SevenSegmentDisplay(4, True, False, True, True, False, False, True)
five = SevenSegmentDisplay(5, True, True, False, True, True, False, True)
six = SevenSegmentDisplay(6, True, True, False, True, True, True, True)
seven = SevenSegmentDisplay(7, False, True, True, True, False, False, False)
eight = SevenSegmentDisplay(8, True, True, True, True, True, True, True)
nine = SevenSegmentDisplay(9, True, True, True, True, True, False, True)

numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
smol_numbers = [zero, one, two, three, four, five, six, seven]
chosen_numbers = [zero, eight, six, five]

def calculateDegreesOfDifference(num1: SevenSegmentDisplay, num2: SevenSegmentDisplay):
    degreeOfDifference = 0
    for segment_index in range(7):
        if num1.getSegments()[segment_index] != num2.getSegments()[segment_index]:
            degreeOfDifference += 1
    return degreeOfDifference

def visitDigits(sequence):
    total_moves = 0
    for index in range(len(sequence) - 1):
        total_moves += calculateDegreesOfDifference(sequence[index], sequence[index + 1])
    return(total_moves)

def generateAllSequences(numbers_remaining, sequence=[], master_list=[]):
    if len(numbers_remaining) == 0:
        master_list.append(sequence)
        return 
    for number in numbers_remaining:
        new_sequence = list(sequence)
        new_sequence.append(number)
        new_numbers_remaining = list(numbers_remaining)
        new_numbers_remaining.remove(number)
        generateAllSequences(new_numbers_remaining, new_sequence)
    return master_list

def findSequenceWithFewestMoves(numbers_remaining, sequence=[], master_dictionary={}):
    if len(numbers_remaining) == 0:
        master_dictionary[visitDigits(sequence)] = sequence
        return 
    for number in numbers_remaining:
        new_sequence = list(sequence)
        new_sequence.append(number)
        new_numbers_remaining = list(numbers_remaining)
        new_numbers_remaining.remove(number)
        findSequenceWithFewestMoves(new_numbers_remaining, new_sequence)
    return [min(master_dictionary), master_dictionary[min(master_dictionary)]]



print(findSequenceWithFewestMoves(numbers))