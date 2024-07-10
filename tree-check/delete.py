def delete(self, r, data):
    if r is None:
        print('Error! Not Found Data')
        return r

    if data < r.data:
        r.left = self.delete(r.left, data)
    elif data > r.data:
        r.right = self.delete(r.right, data)
    else:
        if r.left == None:
            return r.right
        elif r.right == None:
            return r.left

        temp = Min(r.right)
        r.data = temp.data
        r.right = self.delete(r.right, temp.data)

    return r
