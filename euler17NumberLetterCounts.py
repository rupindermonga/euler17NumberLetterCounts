#counting and summing number of letters in the number (up to that number - including boundaries)
#pip3 install num2words
from num2words import num2words
def NumberLetterCounts(n):
    total_length = 0
    for i in range(1, n+1):
        total_length += len(num2words(i).replace(" ","").replace("-",""))
    return total_length

final = NumberLetterCounts(1000)
print(final)

        
