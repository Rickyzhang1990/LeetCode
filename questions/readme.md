1、平衡树  
判断平衡树的问题，对于二叉树的问题，一般都涉及到递归和迭代，使用递归的方法如本次的解决方法。通过对这道题的学习，学习到了如何使用递归去解决问题  
2、反转整数  
在python中解决比较简单，主要运用到列表的操作，反转列表后转化成整数。对于golang,使用golang不如使用python熟练，想到另外一种解决方法。代码如下  
以435为例，构建两个列表，  
>>
list1,list2 = [],[]  
number = 435  
while 1：  
  n = 0  
  if number != 0 :  
    n += 1  
    x = number%10  
    list1.append(n)  
    list2.append(x)  
    number /=10   
  else:  
    break   
#最后反转list1进行计算  
>>
