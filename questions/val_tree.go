/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    if root == nil {return true}
    return iss_child(root.Left , root.Right)
}

func iss_child(left, right *TreeNode) bool {
    if (left == nil && right == nil){return true}
    if (left == nil || right == nil){return false}
    if (left.Val == right.Val){return iss_child(left.Left,right.Right) && iss_child(left.Right,right.Left)}
    return false
}
