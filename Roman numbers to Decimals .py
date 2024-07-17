tallies ={
    'I':1,
    'v':5,
    'x':10,
    'L':50,
    'c':100,
    'D':500,
    'M':1000,
    #specify more numerals if you wish
}
def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral)-1):
        left = romanNumeral[i]
        right = romanNumeral[i+1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]
    return sum