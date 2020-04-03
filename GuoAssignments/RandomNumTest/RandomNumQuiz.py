from random import randint

lsAnswers = []
lsNums = []
lsQuestions = []
plus = ' + '
equal = ' = '
for i in range(1, 11, 1):
    ranNum = int(randint(0,100))
    ranNum2 = int(randint(0,100))
    print(ranNum, '+' ,ranNum2, '=')
    input1 = int(input())
    answer = ranNum + ranNum2
    if input1 == answer:
        lsAnswers.append('Correct')
    else:
        lsAnswers.append('Incorrect, the answer was:')
        lsNums.append(answer)
    #Questions= ranNum, plus, ranNum2, equal, input1
    Questions = str(ranNum) + plus + str(ranNum2) + equal + str(input1)
    lsQuestions.append(Questions)

for i in range (0, 10, 1):
    print(lsQuestions[i], lsAnswers[i], lsNums[i])