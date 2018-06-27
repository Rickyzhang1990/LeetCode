func isIsomorphic(s string, t string) bool {
    var tn,sn [] int 
    s_dic := make(map[rune] int)
    t_dic := make(map[rune] int)
    for i, j := range s{
        if _,ok := s_dic[j];ok{
            sn = append(sn , s_dic[j])
            continue}
        s_dic[j] = i
        sn = append(sn , i)
    }
    for m,n := range t {
        if _,ok := t_dic[n];ok{
            tn = append(tn,t_dic[n])
            continue }
        t_dic[n] = m
        tn =append(tn,m)
    }
    var temp = 0 
    for x := range sn{
        if sn[x] == tn[x]{
            temp++
        }
    }
    return temp == len(sn)
}
