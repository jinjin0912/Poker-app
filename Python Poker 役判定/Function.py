# 0を2 .... A=12として定義
#numbersは並び変えられた後のモノを代入する
def poker_yaku_first(suits,numbers):
    if suits[0]==suits[1]==suits[2]==suits[3]==suits[4] :
        if numbers==[8,9,10,11,12]:
            return 9
        elif (numbers[1]==numbers[0]+1 and numbers[2]==numbers[1]+1 and numbers[3]==numbers[2]+1 and numbers[4]==numbers[3]+1) or (numbers==[0,1,2,3,12]) : 
            return 8
        else:
            return 5
    dup=[x for x in set(numbers) if numbers.count(x)==4]

    if len(dup)==1 :
        return 7
    dup=[x for x in set(numbers) if numbers.count(x)==3]
    dup2=[x for x in set(numbers) if numbers.count(x)>=2]
    if len(dup)==1 and len(dup2)==2:
        return 6
    
    if (numbers[1]==numbers[0]+1 and numbers[2]==numbers[1]+1 and numbers[3]==numbers[2]+1 and numbers[4]==numbers[3]+1) or (numbers==[0,1,2,3,12]) :
        return 4
    
    if len(dup)==1 :
        return 3
    
    if len(dup2)==2 :
        return 2

    if len(dup2)==1 :
        return 1
    else:
        return 0