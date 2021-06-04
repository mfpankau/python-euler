x = 20
isAnswer = True
while True:
    for i in range(1, 21):
        if isAnswer and x % i == 0: continue 
        else: 
            isAnswer = False
            break
    if isAnswer: 
        print(x)
        break
    isAnswer = True
    x = x + 20
    
