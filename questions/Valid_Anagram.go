func isAnagram(s string, t string) bool {
    if len([]rune(s)) != len([]rune(t)) {return false }
    s_l := make(map[rune] int)
    t_l := make(map[rune] int)
    var count int
    for _,j  :=  range s{
        if _ ,ok := s_l[j];ok{s_l[j]++
        }else{s_l[j] = 1}
    }
    for  _, n := range t {
        if _, ok := t_l[n]; ok{t_l[n]++
        }else{t_l[n] = 1}
    }
    if len(s_l) != len(t_l){return false}
    for key := range s_l{
        if s_l[key] == t_l[key]{count++}
    }
    return count == len(s_l)
}
/* 脑残之我见：对于range遍历有了新的认识，当使用range遍历字符串时，直接打印出来的是数字码，需要经过string()转换才能打印出来我们想要看到的字符。
本来这道题目思路比较简单，但是对于golang的不熟悉导致中间除了一些错误，提交了3次才接受而且效率低下，哎，学习需要继续啊*/
