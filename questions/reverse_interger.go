func reverse(x int) int {  
    var a [] int  
    var number int 
    for {
        count := x%10
        x /= 10 
        a = append([]int{count},a[0:]...)
        if x == 0{ 
            break }
    }
    for i,j := range(a) {
        number += j * (power(10,i))
    }
    if number > -1*(power(2,31)) && number < power(2,31){return number}
    return 0
}

func power(x int, n int) int {
    ans := 1

    for n != 0 {
        if n%2 == 1 {
            ans *= x
        }
        x *= x
        n /= 2
    }
    return ans
}
