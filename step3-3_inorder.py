# 1st: 13:14

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            raise ValueError()
        if len(preorder) != len(inorder):
            raise ValueError()

        preorder_index = {}
        for i in range(len(preorder)):
            preorder_index[preorder[i]] = i

        right_unresolved = []
        def resolve_decendants(pivot_index):
            if not right_unresolved:
                return None
            child = None
            while right_unresolved:
                node = right_unresolved[-1]
                if preorder_index[node.val] < pivot_index:
                    break
                node.right = child
                child = node
                right_unresolved.pop()
            return child

        
        for node_value in inorder:
            node = TreeNode(node_value)
            node.left = resolve_decendants(preorder_index[node_value])
            right_unresolved.append(node)
        
        return resolve_decendants(float("-inf"))