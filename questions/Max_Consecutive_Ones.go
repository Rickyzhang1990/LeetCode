func findMaxConsecutiveOnes(nums []int) int {
    var lenght = 0
    var len_list [] int 
    for _,j := range(nums){
        switch {
            case j == 0 :
            len_list = append(len_list ,lenght)
            lenght = 0
            case j == 1 :
            lenght++
        }
        len_list = append(len_list ,lenght)
    }
    return max(len_list)
}

func max(list [] int ) int {
    first := list[0]
    for _ , n := range(list){
        if first < n{
            first = n 
        }
    }
    return first 
}
