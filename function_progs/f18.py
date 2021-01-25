#def test(a,b,c,/,x,y=200,*,p=1000,q,r=3000):
#def test(a,b,c,/,x=100,y,*,p=1000,q,r=3000): <== not allowed 
#def test(a,b,c=3,/,x,y=200,*,p=1000,q,r=3000): <== not allowed 
def test(a,b,c=3,/,x=100,y=200,*,p=1000,q,r=3000):
	print(a,b,c,x,y,p,q,r)

#test(1,2,3,100,200,p=9,q=99,r=999)
test(1,2,30000,100,200,p=9,q=99,r=999)