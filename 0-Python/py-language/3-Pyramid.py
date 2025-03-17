nums = 7

for i in range(1,nums+1):
    space = " " * (nums-i)
    star = "*" * (2*i - 1)
    print(space+star)


'''
      *
     ***
    *****
   *******
  *********
 ***********
*************
'''