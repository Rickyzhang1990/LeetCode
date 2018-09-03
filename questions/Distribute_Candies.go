func distributeCandies(candies []int) int {
    var kind = make(map[int]bool)
    for _,i := range candies{
        if _,ok := kind[i];ok{
            continue
        }else{
            kind[i] = true
        }
    }
    getnu := len(candies)/2
    kinds := len(kind) 
    if(kinds <= getnu){return kinds}
    return getnu  
}
