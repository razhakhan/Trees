#User function Template for python3

'''
Example:
Input:
2
2
1 2 L 1 -1 N
6
1 2 L 1 3 R 2 -1 N 2 -1 N 3 3 L 3 -1 N
Output:
3
9



'''
    
def sumBT(root):
    if not root:
        return 0
    else:
        return root.data+sumBT(root.left)+sumBT(root.right)

#{ 
 # Driver Code Starts
from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def make_tree():
    n=int(input())
    l=list(map(str,input().split()))
    head=None
    q=deque()
    i=0
    while(n>0):
        a,b,c=l[i],l[i+1],l[i+2]
        if(not head):
            head=Node(int(a))
            q.append(head)
        pick=q[0]
        q.popleft()
        if(c=='L'):
            pick.left=Node(int(b))
            q.append(pick.left)
        n=n-1
        if(not n):
            break
        a,b,c=l[i+3],l[i+4],l[i+5]
        if(c=='R'):
            pick.right=Node(int(b))
            q.append(pick.right)
        i=i+6
        n=n-1
    return head
            
    

if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        head=make_tree()
        k=sumBT(head)
        print(k)


# } Driver Code Ends
