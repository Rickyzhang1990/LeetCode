func twoSum(nums []int, target int) []int {
    dic := make(map[int] int)
    for idx , num := range nums{
        num2 := target - num 
        if _ ,ok := dic[num2] ; ok && idx != dic[num2]{
            return [] int {dic[num2] ,idx} 
        }
        dic[num] = idx
    }
    return [] int {-1,-1}
}
