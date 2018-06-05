/*借鉴了讨论中一个非常巧妙的方法，见readme*/
func numJewelsInStones(J string, S string) int {
    Jewel := make(map[rune]int)
    for _, word := range J{
        Jewel[word] = 1
    }
    count := 0 
    for _, letter  := range S{
         count += Jewel[letter]
    }
    return count 
}
