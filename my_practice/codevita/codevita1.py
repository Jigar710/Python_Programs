def sw(lst1,x,y,effort):
    mi = lst1.index(min1)
    xi = lst1.index(x)
    yi = lst1.index(y)
    lst1[mi], lst1[xi] = lst1[xi], lst1[mi]
    effort += min1 * x
    print(lst1)
    mi = lst1.index(min1)
    xi = lst1.index(x)
    yi = lst1.index(y)
    lst1[mi], lst1[yi] = lst1[yi], lst1[mi]
    effort += min1 * y
    print(lst1)
    mi = lst1.index(min1)
    xi = lst1.index(x)
    yi = lst1.index(y)
    lst1[mi], lst1[xi] = lst1[xi], lst1[mi]
    effort += min1 * x
    print(lst1)
    print(effort)



'''
n, k = input().split()
n, k = int(n), int(k)
lst1 = list(map(int,input().split()))[:n]
print(lst1)
'''
n = 6
k = 3
lst1 = [30,20,40,80,70,60]
lst = lst1.copy()
m = max(lst)
min1 = min(lst1)
lst.remove(m)
lst.sort()
lst.insert(k-1,m)
effort = 0
for i in range(len(lst1)):
    if lst[i]!=lst1[i]:
        x = lst[i]
        y = lst1[i]
        xi = lst1.index(x)
        yi = lst1.index(y)
        if x == min(lst1):
            lst1[xi],lst1[yi] = lst1[yi],lst1[xi]
            effort += x*y
            print(lst1)
        else:
            e1 = x*y
            if x>y:
                e2 = x*min1 + 2*y*min1
            else:
                e2 = 2*x*min1 + y*min1
            if e1 < e2 :
                lst1[xi], lst1[yi] = lst1[yi], lst1[xi]
                effort += x*y
                print(lst1)
            else:
                if x > y :
                    mi = lst1.index(min1)
                    xi = lst1.index(x)
                    yi = lst1.index(y)
                    lst1[mi], lst1[yi] = lst1[yi], lst1[mi]
                    effort += min1 * y
                    print(lst1)
                    mi = lst1.index(min1)
                    xi = lst1.index(x)
                    yi = lst1.index(y)
                    lst1[mi],lst1[xi] = lst1[xi], lst1[mi]
                    effort += min1 * x
                    print(lst1)
                    mi = lst1.index(min1)
                    xi = lst1.index(x)
                    yi = lst1.index(y)
                    lst1[mi], lst1[yi] = lst1[yi], lst1[mi]
                    effort += min1 * y
                    print(lst1)
                if x > y :
                    sw(lst1,y,x,effort)
                else:
                    sw(lst1,x,y,effort)






