def delete(self,r,data):
    if r == None:
        print('dont hav')
        return r
    else:
        if data>r.data:
            r.right = self.delete(r.right,data)
        elif data<r.data:
            r.left = self.delete(r.left)
        else:
            if r.right ==None:
                return r.left
            elif r.left ==None:
                return r.right

            temp = Min(r.right)
            r.data = temp.data
            r.right = self.delete(r.right,temp)
    return r