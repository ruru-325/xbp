import random
import datetime
ALP = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

r = random.choice(ALP)
alp =""
for i in ALP:
    if i != r:
        alp= alp + i
print(alp)
st= datetime.datetime.now()
ans = input("欠けているアルファベットは？")
if ans == r:
    print("正解")
    
else:
    print("違います")
    