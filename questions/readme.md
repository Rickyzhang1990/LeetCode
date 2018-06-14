# 1、**平衡树**  
判断平衡树的问题，对于二叉树的问题，一般都涉及到递归和迭代，使用递归的方法如本次的解决方法。通过对这道题的学习，学习到了如何使用递归去解决问题  
# 2、**反转整数**  
在python中解决比较简单，主要运用到列表的操作，反转列表后转化成整数。对于golang,使用golang不如使用python熟练，想到另外一种解决方法。理想中python代码如下  
以435为例，构建两个列表，  
```python
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
```
# 3、**最大连续1的个数**  
思路：列表中有元素为0/1的元素，我们要找到最大连续出现1的长度。如
>*输入: [1,1,0,1,1,1]*  
*输出: 3*  
*解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.*
>
思路：将列表转化为字符串，然后将字符串按照“0”为分隔符进行分隔，得到一个“1\*N”的列表，统计列表中长度最大的几位最长连续1的次数。
对于Go的解法，使用遍历切片的方法，判断条件使用初次尝试使用switch语句，
```golang
count := 0 
switch{
  case i == 0 :
  len_list = append(len_list ,count)
  count = 0 
  case i == 1 :
  count++
  }
  len_list = append(len_list ,count)
  ```
  最终取len_list的最大值即为最大1的连续次数,总体来说与.python.解决方法思路最后相同  
 # 4、**杨辉三角**  
帕斯卡三角，在我国被称为杨辉三角，整体题目如下题
>给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
>在杨辉三角中，每个数是它左上方和右上方的数的和。  
>示例:  
>输入: 5  
>输出:  
>[  
     [1],  
    [1,1],  
   [1,2,1],  
  [1,3,3,1],  
 [1,4,6,4,1]  
]  
>
思路仿照百度百科，下一行的第二个元素等于上一行第一个与第二个的和，第三个元素等于上一行第三个与第二个元素的和。具体解法见脚本。    
尝试使用go解决该问题，发现无法照搬python的思路去完成。  
>**1、golang为静态语言，多维数组需声明,而python则不需要  
2、在golang的切片内，元素的索引为0,1,2,3.....，不存在-1，-2，如果出现这种下标则会给出下标越界的错误，而python的索引-1指的是最后一个元素  
3、python的二维列表可以通过list [1] [2] = x 赋值，而如果同样方法操作golang，则也会报错下标越界**    

# 5、**宝石与石头**  
>You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".  
>>Example 1:  
``Input: J = "aA", S = "aAAbbbb"``
``Output: 3``  
>>Example 2:  
``Input: J = "z", S = "ZZ"``
``Output: 0`` 
>
go的解法与学习经验  
## **1、Go中对于字符串的遍历分为两种方法，如下**  
```golang
func main() {
    str := "Hello,世界"
    /*utf-8遍历 遍历的为字节码，为byte,只能填充int8的值*/
    for i := 0; i < len(str); i++ {
        ch := str[i]
        fmt.Println(ch)
    }
    fmt.Println("=============>Unicode遍历")
    //Unicode遍历 为rune 底层类型为一个是uint32，只能填充uint32的值
    for _, ch1 := range str {
        fmt.Println(ch1)
    }
}
```
Go语言中byte和rune实质上就是uint8和int32类型。byte用来强调数据是raw data，而不是数字；而rune用来表示Unicode的code point。  
## **2、对于声明的变量，必须要使用，如果没有使用则会编译不通过，参考以下代码**  
```golang
func numJewelsInStones(J string, S string) int {
  var jMap = map[rune]bool{}
  cnt := 0
  for _, x := range J {
    jMap[x] = true
   }
   for _, y := range S {
      _, ok := jMap[y]
      if ok {
      fmt.Println(y) /*对于声明的变量y,必须要有对应的操作，只是判断的话并不算used，对于自己是golang的初学者，感觉是个特别脑残的设定*/
      cnt += 1}
    }
return cnt
}
```
参考discuss中的写法，非常巧妙，直接将没有宝石类别放置到map内，map[jewel] = 1没有类别为1.
然后遍历自己的石头，使用count += map[自己石头],字符串中字节在map中出现一次，count+1，特别巧妙  
# **6、键盘同一行**  
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。  
>Example 1:
```
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
```
Note:

    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.
>  
python思路： 判断每个单词的每个字母是否在三个列表内，如果在A列表内，resultA添加元素1，如果不在A内添加0，同理判断B和C列表内的情况，最后判断三个列表的情况，如果其中一个列表全部1，则返回该单词。具体见脚本  
# **7、根据字符出现频率排序**  
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

**示例 1:**
>**输入**:  
"tree"  
**输出**：  
"eert"  
**解释**：  
'e'出现两次，'r'和't'都只出现一次。  
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。  
>
**示例 2：**
>**输入**：    
"cccaaa"  
 **输出**：  
 "cccaaa"  
 **解释**：  
 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。  
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
>
**示例3：**
>**输入**：
"Aabb"  
**输出**：  
"bbAa"  
**解释**：  
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。  
注意'A'和'a'被认为是两种不同的字符。  
>  
具体思路参见脚本内注释*Sort_Characters_By_Frequency.py*  
golang版本的还在构思中，争取本周完成  
# **8、出现一次的字母**  
使用hash中键值对唯一的特性，提取单词出现的字符，思路简单。go实现也很容易，应该有更好的思路，以后待优化。  
# **9、快乐数**  
编写一个算法来判断一个数是不是“快乐数”.  
一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。  

**示例:**  
>**输入**: 19  
**输出**: true  
**解释**:   
1^2 + 9^2 = 82  
8^2 + 2^2 = 68  
6^2 + 8^2 = 100  
1^2 + 0^2 + 0^2 = 1
>  
思路:基于递归的方法，对每个数据递归求每个位置的平方和，直到最后数字变为<10的数字，小于10的数字中，只有1和7为欢乐数，如果得到1或者7则返回true,如果  
得不到这两个数字，则返回false  。总体来说我的解决方法是为了通过测试才写的,属于投机取巧的写法，应该还有正确的解法。  
# **10、最长非重复子字符串**  
给定一个字符串，找出不含有重复字符的最长子串的长度。  
**示例：**
>给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。  
给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。  
给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。  
>
思路：最开始想着使用字典的方法，统计出每个独立的子字符，然后按照子字符串的位置去重构子串，但是将字符串拆开比较简单，将子字符按照index重新组合会有很大问题，而且以目前个人水平实现比较困难。因而放弃第一种思路。
第二种思路则类似于动态规划的方法，遍历字符串，初始子串为""，如果字符不在初始串中，则添加入初始子串。依次判断。但是遇到三类问题。
第一个问题：当字符串为空时，需要加上为空的判断，因为在脚本中添加语句  
```python  
if len(s) == 0：  return 0 
```    
第二个问题：当字符串为长度为1时，最终子串的列表没有成功添加结果，因而在循环后添加语句  
```
python result.append(substr)
```
第三个问题：字符串为“dvdf”和“ckilbkd”时，第二个“d”和第二个“k”均存在之前的字符串中，需要将遇到重复之前的字符串保留，然后截取“dv”中的“d”以及“ckilb”中的“ck”,加上后出现的重复字符串。  
最后得到了最后的结果，详细见脚本

