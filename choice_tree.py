class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

#Preorder Node Left Right

def Preorder_traversal(root):
    print(root.value)
    if root.left!=None:
        Preorder_traversal(root.left)
    if root.right!=None:
        Preorder_traversal(root.right)

#Postorder Left Right Node

def Postorder_traversal(root):
    if root.left!=None:
        Postorder_traversal(root.left)
    if root.right!=None:
        Postorder_traversal(root.right)
    print(root.value)

#Inorder Left Node Right

def Inorder_traversal(root):
    if root.left!=None:
        Inorder_traversal(root.left)
    print(root.value)
    if root.right!=None:
        Inorder_traversal(root.right)

def create_tree():
    root_choice=input("Enter a number for the root:")
    root=Node(root_choice)
    root_left=input("Enter a number for the left branch:")
    root.left(root_left)
    root_right=input("Enter a number for the right branch:")
    root.right(root_right)
    return root


def menu():
    #root=None
    while True:
        print("1. Create Tree")
        print("2. Preorder Traversal")
        print("3. Postorder Traversal")
        print("4. Inorder Traversal")
        print("5. Expansion of left branch")
        print("6. Expansion of right branch")
        print("7. Exit")

        choice=input("Enter your choice: ")

        if choice=='1':
                root = create_tree()
                print("Tree created successfully.")
        elif choice=='2':
            if root:
                print("Preorder Traversal:")
                Preorder_traversal(root)
                print()
            else:
                print("Tree is not created yet. Please create a tree first.")
        elif choice=='3':
            if root:
                print("Postorder Traversal:")
                Postorder_traversal(root)
                print()
            else:
                print("Tree is not created yet. Please create a tree first.")
        elif choice=='4':
            if root:
                print("Inorder Traversal:")
                Inorder_traversal(root)
                print()
            else:
                print("Tree is not created yet. Please create a tree first.")
        elif choice == '5':
                branch=input("Left or right branch of the left branch?")
                if branch == "left":
                    num_l=input("Enter a value:")
                    root.left.left(num_l)
                elif branch == "right":
                    num_r=input("Enter a value:")
                    root.left.right(num_r)    
        elif choice == '6':
                branch=input("Left or right branch of the right branch?")
                if branch == "left":
                    num_l=input("Enter a value:")
                    root.right.left(num_l)
                elif branch == "right":
                    num_r=input("Enter a value:")
                    root.right.right(num_r)            
        elif choice=='7':
                print("Exiting program.")
                break

menu()