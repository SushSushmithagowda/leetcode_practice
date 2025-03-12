#Tree Traversal: Perform preorder traversal of a binary tree using iterative approach

def binary_tree_traversal(root):
  result = []
  stack = []
  if root is not None:
    stack.append(root)


  while len(stack) > 0:
    node = stack.pop()
    result.append(node.value)
    if node.left is not None:
      result.append(node.left)
    if node.right is not None:
      result.append(node.right)
  return result
