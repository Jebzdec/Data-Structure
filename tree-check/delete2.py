def delete(self,r,data):
    if r == None:
        print('dont have')
        return r

    if data > r.data:
        r.right = self.delete(r.right,data)
    elif data < r:
        r.left = self.delete(r.left,data)
    else:
        if r.left == None:
            return r.right
        elif r.right == None:
            return r.left

        temp = Min(r.right)
        r.data = temp.data
        r.right = self.delelte(r.right,temp)
    return r
        


def Min(node):
    if node.left == None:
        return node
    return Min(node.left)