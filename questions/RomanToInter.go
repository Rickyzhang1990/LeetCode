func romanToInt(s string) int {
    dic := map[string]int{"IV":4,"IX":9,"XL":40,"XC":90,"CM":900,"CD":400,"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    var result [] string
    for {
        if len([]rune(s)) >1 {
            if _,ok := dic[s[0:2]];ok{
                result = append(result ,s[0:2])
                s = s[2:]
            }else{
                result = append(result ,s[0:1])
                s = s[1:]}
        }else{
            result = append(result ,s)
            break 
        }
    }
    total := 0 
    for _, x := range result{
        if x != ""{
            total += dic[x]
        }
    }
    return total 
}
