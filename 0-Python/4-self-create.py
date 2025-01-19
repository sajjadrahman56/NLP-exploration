nums = 5

for i in range(1,nums+1):
    space = " " * (nums-i)
    star = "*" * (2*i - 1)
    space1 = " " * (nums-i)
    star1 = "*" * (2*i - 1)
    print(space+star+space1+star1)

'''
      *      *
     ***     ***
    *****    *****
   *******   *******
  *********  *********
 *********** ***********
**************************
''' 