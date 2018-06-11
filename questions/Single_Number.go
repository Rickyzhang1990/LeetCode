func singleNumber(nums []int) int {
    var count map[int] int 
    count = make(map[int] int)
    for _ ,j := range nums{
        if _ ,ok := count[j];ok {
            count[j]++
        } else{
            count[j] = 1 
        }
    }
    for key , value := range count{
        if value == 1 {
            return key 
        }
    }
    return 0
}
