func majorityElement(nums []int) int {
    sc := make(map[int]int)
    for _ , j := range nums{
        if _,ok := sc[j];ok{sc[j]++
        }else{sc[j] = 1}
    }    
    for k ,v := range sc{
        if v > (len(nums)/2){
            return k
        }
    }
    return 0
}
