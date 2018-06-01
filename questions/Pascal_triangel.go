func generate(numRows int) [][]int {
   list := make([][] int , numRows)
   switch {
       case numRows == 0:
        list = [] [] int {}
       case numRows == 1:
        list[0] =  [] int {1}
       case numRows > 1 :
        for i := 0;i < numRows;i++{
            if i == 0 || i== 1 {
                list[0] ,list[1] = [] int {1} ,[] int {1,1}
            }else {
            tmp := make([] int ,i+1)  
            for j := 0 ;j < i+1 ;j++{
                if j == 0 || j == i{
                    tmp[0] , tmp[i] = 1,1
                }else{
                    tmp[j] = list[i-1][j-1] + list[i-1][j]
                }
              }  
           list[i] = tmp
            }
          }
        }
    return list 
    }
