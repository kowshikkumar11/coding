l=list(map(int,input().split(' ')))
p=l[0]
c=l[1]
d=0
while(p!=0):
  r=p%c
  d+=r
  p=p//r
print(d+p)
