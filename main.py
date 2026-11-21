import os,json,urllib.request as u
V=[0,100,320,330,500,900,0]
J='TToo]f]^TV\\L]ZTT092T<^=f<f=^2U09CKLTL]M]L]M]MTCKTT]]TTTTTTTTTTTUCLLTL]T]T]M]L\\CL80808080A8JBfTf\\'
Z=[-40,-30,-20,-10,0,5,20,50]
KN=[-33,-31,-18,-14,14,18,31,33]
KG=[-17,-16,-15,-1,1,15,16,17]
BD=[-17,-15,15,17]
RD=[-16,-1,1,16]
W=[0,0,KN,BD,RD,BD+RD,KG]
RM={0:2,7:1,112:8,119:4}
P=[0]*1664
for c in range(-6,7):
 t=abs(c)
 for q in range(128):
  if q&136==0:
   f=q&7;r=q>>4;i=(7-r if c>0 else r)*4+min(f,7-f)
   P[c*128+q+768]=(V[t]+Z[divmod(ord(J[(t-1)*16+i//2])-48,8)[i%2]])*(1 if c>0 else -1)
Q=lambda c,q:P[c*128+q+768]
G=int(os.getenv('BUDGET')or 15e4)
O=1e5
N=0
T={}
K=[(0,0)]*512
def F(f):
 B=[0]*128;C=0;p=f.split();q=112
 for ch in p[0]:
  if ch=='/':q-=24
  elif ch.isdigit():q+=int(ch)
  else:
   c=('PNBRQK'.index(ch.upper())+1)*((ch<'a')*2-1);B[q]=c;C+=Q(c,q);q+=1
 s=2*(p[1]=='w')-1
 a=sum(1<<i for i,h in enumerate('KQkq') if h in p[2])
 e=-1 if p[3]=='-' else (int(p[3][1])-1)*16+ord(p[3][0])-97
 return B,s,e,a,C
def A(B,s,q):
 for d in(-17,-15):
  t=q+d*s
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
 m=[];o=m.append
 def X(q,w,sc):o(((sc+900,q|w<<7|5<<14) if w>>4==7*(s+1)//2 else (sc,q|w<<7)))
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
     if x*s<0 and abs(x)<6:X(q,w,10*V[abs(x)])
     elif w==e and not x:X(q,w,1900)
  else:
   for z in W[t]:
    w=q+z
    while w&136==0:
     x=B[w]
     if x:
      if x*s<0 and abs(x)<6:o((10*V[abs(x)],q|w<<7))
      break
     o((0,q|w<<7))
     if t%4==2:break
     w+=z
 k=60-56*s
 for d in(1,-1):
  b=1<<(s<0)*2+(d<0)
  if a&b and B[k+d]|B[k+2*d]==0 and(d>0 or B[k+3*d]==0)and all(not A(B,-s,k+i*d)for i in(0,1,2)):o((0,k|(k+2*d)<<7))
 m.sort(reverse=1)
 return m
def M(B,s,m,e,a,C):
 n=B[:];f=m&127;t=(m>>7)&127;r=(m>>14)&7;p=B[f];c=C-Q(p,f);x=B[t]
 if x:c-=Q(x,t)
 elif p==s and t==e:
  w=t-16*s;c-=Q(-s,w);n[w]=0
 v=r*s or p
 n[f]=0;n[t]=v;c+=Q(v,t)
 if p==6*s and abs(t-f)==2:
  u=f+3*(t>f)-4*(t<f);y=f+(t>f)-(t<f)
  z=n[u];c-=Q(z,u);n[u]=0;n[y]=z;c+=Q(z,y)
 w=f+16*s if p==s and t-f==32*s else -1
 a&=~RM.get(f,0)&~RM.get(t,0)
 if p==6*s:a&=(12,3)[s<0]
 return n,c,w,a
def S(B,s,e,a,C,d,x,y,p):
 global N;N+=1
 if N>G:raise StopIteration
 c=A(B,-s,B.index(6*s));q=d<=0 and not c
 if d>2 and not c:
  v=-S(B,-s,-1,a,C,d-3,-y,1-y,p+1)
  if v>=y:return v
 t=T.get(k:=(tuple(B),s,e,a));h=0
 if t and t[0]>=d and not(t[2]==1 and t[1]<y or t[2]==2 and t[1]>x):return t[1]
 if t:h=t[3]
 if q:
  v=C*s
  if v>=y:return v
  if v>x:x=v
 z=E(B,s,e,a);f=g=0;a0=x
 z.sort(key=lambda t:2*(t[1]==h)+(t[1] in K[p]),reverse=1)
 for u,m in z:
  if q and u<=0:continue
  n,D,w,i=M(B,s,m,e,a,C)
  if A(n,-s,n.index(6*s)):continue
  f=1;v=-S(n,-s,w,i,D,max(d-1,0),-y,-x,p+1)
  if v>x:x=v;g=m
  if x>=y:
   if u<=0:K[p]=(m,K[p][0])
   break
 if not f:
  if c:return -O+p
  return x if q else 0
 if abs(x)<9e4:T[k]=(d,x,(x>=y)+2*(x<=a0),g)
 return x
def H(B,s,e,a,C,m):
 global N;N=0;T.clear();b=m[0][1]
 for d in range(1,64):
  try:
   x=-O;g=b
   for v,n in [(0,b)]+m:
    j,d2,h,i=M(B,s,n,e,a,C)
    if A(j,-s,j.index(6*s)):continue
    v=-S(j,-s,h,i,d2,d-1,-O,-x,1)
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
   B,s,e,a,C=F(g['fen']);m=E(B,s,e,a);v=H(B,s,e,a,C,m);z=''.join(chr(97+(v>>k&7))+chr(49+(v>>(k+4)&7)) for k in(0,7))+('nbrq'[(v>>14)-2] if v>>14 else '')
   w=g['legal_moves']
   if z not in w:z=w[0]
   g=P('/move',{'game':g['game'],'move':z})
L()
