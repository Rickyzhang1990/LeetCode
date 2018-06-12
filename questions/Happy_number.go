func isHappy(n int) bool {
    if add(n) == 1 || add(n) == 7  {return true}
    return false}

func add(n int ) int { 
    var tem_nu int 
    if n < 10 {
        return  n
    }else{
        for{
            a := n%10
            tem_nu += a*a
            if n/10 == 0 {
                break }
            n /= 10 
        }
    }
    return add(tem_nu)
}
