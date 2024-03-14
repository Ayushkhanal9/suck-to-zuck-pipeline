    #inorder traversal using reccursion
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    arr=[]
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        arr.append(root.val)
        inorder(root.right)
    inorder(root)
    return arr
    # preorder traversal
def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    arr=[]
    def preorder(root):
        if not root:
            return
        arr.append(root.val)
        preorder(root.left)
        preorder(root.right)
    preorder(root)
    return arr
    #post order traversal
def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    arr=[]
    def postorder(root):
        if not root:
            return
        postorder(root.left)
        postorder(root.right)
        arr.append(root.val)
    postorder(root)
    return arr

