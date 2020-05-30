
user_num = int(input("How many squares across would you like the board to be: "))

for i in range(user_num):
    print("---" * user_num + "\n" + "| " * (user_num+1))
    print("---" * user_num)

#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 
