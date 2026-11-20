import os,json,urllib.request as u
V=[0,100,320,330,500,900,0]
J="6666====88:<778;666:754678836666012213662689279:269:27891367012234444666467847784688488847663444"+"66667888"+"5666"*5+"6667"+"34454666467756776677477746763445"+"2110"*4+"32214333::66:<86"
Z=[-50,-40,-30,-20,-10,-5,0,5,10,15,20,25,30,50]
KN=[-33,-31,-18,-14,14,18,31,33]
KG=[-17,-16,-15,-1,1,15,16,17]
BD=[-17,-15,15,17]
RD=[-16,-1,1,16]
W=[0,0,KN,BD,RD,BD+RD,KG]
RM={0:2,7:1,112:8,119:4}
P=[0]*1664
for c in range(-6,7):
 if c:
  t=abs(c)
  for q in range(128):
   if q&136==0:
    f=q&7;r=q>>4;h=f if f<4 else 7-f;i=(7-r if c>0 else r)*4+h
    P[c*128+q+768]=(V[t]+Z[ord(J[(t-1)*32+i])-48])*(1 if c>0 else -1)
G=int(os.getenv('BUDGET',15e4))
O=1e5
N=0
T={}
def F(f):
 B=[0]*128;C=0;p=f.split();q=112
 for ch in p[0]:
  if ch=='/':q-=24
  elif ch.isdigit():q+=int(ch)
  else:
   c=('PNBRQK'.index(ch.upper())+1)*((ch<'a')*2-1);B[q]=c;C+=P[c*128+q+768];q+=1
 s=2*(p[1]=='w')-1
 a=sum(1<<'KQkq'.index(h) for h in p[2] if h in 'KQkq')
 e=-1 if p[3]=='-' else (int(p[3][1])-1)*16+ord(p[3][0])-97
 return B,s,e,a,C
def A(B,s,q):
 for d in(-17*s,-15*s):
  t=q+d
  if t&136==0 and B[t]==s:return 1
 for v in(2,3,4,6):
  for d in W[v]:
   t=q+d
   while t&136==0:
    x=B[t]
    if x:
     if x==v*s or 2<v<5 and x==5*s:return 1
     break
    if v%4==2:break
    t+=d
 return 0
def E(B,s,e,a):
 m=[];l=7*(s+1)//2
 def X(q,w,sc):m.append(((sc+900,q|w<<7|5<<14) if w>>4==l else (sc,q|w<<7)))
 for q in range(128):
  p=B[q]
  if not p or p*s<=0:continue
  t=abs(p)
  if t==1:
   d=16*s;j=(7-5*s)//2
   w=q+d
   if w&136==0 and B[w]==0:
    X(q,w,0)
    if q>>4==j:
     x=w+d
     if x&136==0 and B[x]==0:X(q,x,0)
   for z in(d-1,d+1):
    w=q+z
    if w&136==0:
     x=B[w]
     if x and x*s<0 and abs(x)<6:X(q,w,10*V[abs(x)])
     elif w==e and not x:X(q,w,1900)
  else:
   for z in W[t]:
    w=q+z
    while w&136==0:
     x=B[w]
     if x:
      if x*s<0 and abs(x)<6:m.append((10*V[abs(x)],q|w<<7))
      break
     m.append((0,q|w<<7))
     if t%4==2:break
     w+=z
 k=60-56*s
 if B[k]==6*s:
  for d in(1,-1):
   b=(1,2,4,8)[(s<0)*2+(d<0)]
   if a&b and B[k+d]==0 and B[k+2*d]==0 and (d>0 or B[k+3*d]==0) and all(not A(B,-s,k+i*d) for i in(0,1,2)):m.append((0,k|(k+2*d)<<7))
 m.sort(reverse=1)
 return m
def M(B,s,m,e,a,C):
 n=B[:];f=m&127;t=(m>>7)&127;r=(m>>14)&7;p=B[f];c=C-P[p*128+f+768];x=B[t]
 if x:c-=P[x*128+t+768]
 elif p==s and t==e:
  w=t-16*s;c-=P[-s*128+w+768];n[w]=0
 v=r*s or p
 n[f]=0;n[t]=v;c+=P[v*128+t+768]
 if p==6*s and abs(t-f)==2:
  u=f+3 if t>f else f-4;y=f+1 if t>f else f-1
  z=n[u];c-=P[z*128+u+768];n[u]=0;n[y]=z;c+=P[z*128+y+768]
 w=f+16*s if p==s and t-f==32*s else -1
 a=a&~RM.get(f,0)&~RM.get(t,0)
 if p==6*s:a&=(12,3)[s<0]
 return n,c,w,a
def S(B,s,e,a,C,d,x,y):
 global N;N+=1
 if N>G:raise StopIteration
 c=A(B,-s,B.index(6*s));q=d<=0 and not c
 if d>2 and not c:
  v=-S(B,-s,-1,a,C,d-3,-y,1-y)
  if v>=y:return v
 if q:
  t=C*s
  if t>=y:return t
  if t>x:x=t
 z=E(B,s,e,a);f=0;k=(tuple(B),s)
 if k in T and T[k][0]>=d:return T[k][1]
 for v,m in z:
  if q and v<=0:continue
  n,D,w,h=M(B,s,m,e,a,C)
  if A(n,-s,n.index(6*s)):continue
  f=1;v=-S(n,-s,w,h,D,max(d-1,0),-y,-x)
  if v>x:x=v
  if x>=y:break
 if not f:
  if c:return -O
  return x if q else 0
 if len(T)<1e5:T[k]=(d,x)
 return x
def H(B,s,e,a,C,m):
 global N;N=0;b=m[0][1]
 for d in range(1,64):
  try:
   x=-O;g=b
   for v,n in m:
    j,d2,h,i=M(B,s,n,e,a,C)
    if A(j,-s,j.index(6*s)):continue
    v=-S(j,-s,h,i,d2,d-1,-O,-x)
    if v>x:x=v;g=n
   b=g
  except StopIteration:break
 return b
def L():
 T=os.getenv('MAKEFUN_ENV_URL')
 def P(p,b):return json.load(u.urlopen(u.Request(T+p,data=json.dumps(b).encode(),headers={'content-type':'application/json'})))
 while True:
  g=P('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   B,s,e,a,C=F(g['fen']);m=E(B,s,e,a);v=H(B,s,e,a,C,m);z=''.join(chr(97+(v>>k&7))+str(((v>>k&127)>>4)+1) for k in(0,7))+('nbrq'[(v>>14)-2] if v>>14 else '')
   if z not in g['legal_moves']:z=g['legal_moves'][0]
   g=P('/move',{'game':g['game'],'move':z})
L()
