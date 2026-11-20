import json,os,urllib.request as u
E=os.environ.get("MAKEFUN_ENV_URL")
V=[100,320,330,500,900,0]
C=[0,1,2,3,3,2,1,0]
N=[-21,-19,-12,-8,8,12,19,21]
K=[-11,-10,-9,-1,1,9,10,11]
D={'N':N,'B':(-11,-9,9,11),'R':(-10,-1,1,10),'Q':K,'K':K}
N_=0
SP=False
def vf(s):return(11-s//10)*10+s%10
def sq(x):return(10-int(x[1]))*10+ord(x[0])-96
def pv(c,s):
 t='PNBRQK'.index(c.upper());f=s%10-1;r=9-s//10;cc=C[f]+C[r]
 return V[t]+[12*r+3*C[f],8*cc,6*cc,4*cc,4*cc,-8*cc][t]
def fl(B):return''.join(B[i:i+10]for i in range(110,-1,-10)).swapcase()
def atk(B,s,w=1):
 U='PNBRQK'if w else'pnbrqk'
 for d in N:
  if B[s+d]==U[1]:return 1
 for d in K:
  t=s+d;n=1
  while B[t]!=' ':
   q=B[t]
   if q!='.':
    if n==1 and q==U[5]:return 1
    if n==1 and q==U[0]and d in((11,9)if w else(-11,-9)):return 1
    if d in(-11,-9,9,11)and q in U[2]+U[4]:return 1
    if d in(-10,-1,1,10)and q in U[3]+U[4]:return 1
    break
   t+=d;n+=1
 return 0
def gen(B,cp,ep,ca):
 ms=[]
 for s in range(120):
  p=B[s]
  if not p.isupper():continue
  if p=='P':
   pr=5 if s//10==3 else 0
   t=s-10
   if B[t]=='.':
    if pr or not cp:ms.append((s,t,pr))
    if s//10==8 and B[s-20]=='.'and not cp:ms.append((s,s-20,0))
   for d in(-11,-9):
    t=s+d;q=B[t]
    if q.islower():ms.append((s,t,pr))
    elif t==ep:ms.append((s,t,0))
  else:
   for d in D[p]:
    t=s
    while 1:
     t+=d;q=B[t]
     if q==' ':break
     if q=='.':
      if not cp:ms.append((s,t,0))
     elif q.islower():ms.append((s,t,0));break
     else:break
     if p in'NK':break
   if p=='K'and not cp and s==95:
    for z in((1,(96,97),(95,96,97),98,97),(2,(94,93,92),(95,94,93),91,93)):
     if ca&z[0]and all(B[x]=='.'for x in z[1])and B[z[3]]=='R'and all(not atk(B,x,0)for x in z[2]):ms.append((95,z[4],0))
 return ms
def mv(B,Sc,m,ep,ca):
 s,t,pr=m;p=B[s];q=B[t];e=p=='P'and q=='.'and s%10!=t%10
 d=pv('Q',t)-pv('P',s)if pr else pv(p,t)-pv(p,s)
 if q!='.':d+=pv(q,vf(t))
 if e:d+=pv('p',vf(t+10))
 nb=list(B);nb[t]='Q'if pr else p;nb[s]='.'
 if e:nb[t+10]='.'
 if p=='K'and abs(t-s)==2:
  a,b=(96,98)if t>s else(94,91);d+=pv('R',a)-pv('R',b);nb[a]='R';nb[b]='.'
 nep=(s+t)//2 if p=='P'and t==s-20 else-1
 nca=ca
 for x,y in((95,3),(91,2),(98,1),(21,8),(28,4)):
  if x in(s,t):nca&=~y
 rb=fl(''.join(nb))
 return rb,-(Sc+d),vf(nep)if~nep else-1,((nca&3)<<2)|(nca>>2)
def sr(B,Sc,ep,ca,a,b,d):
 global N_,SP
 N_+=1
 if N_>=50000:SP=True;return 0
 if d<=0:
  if Sc>=b:return b
  if Sc>a:a=Sc
  ms=gen(B,1,ep,ca)
  if atk(B,B.index('K'),0):ms=gen(B,0,ep,ca)
 else:
  chk=atk(B,B.index('K'),0)
  ms=gen(B,0,ep,ca)
 ms=[r for m in ms for r in[(m,)+mv(B,Sc,m,ep,ca)]if not atk(r[1],r[1].index('k'))]
 if d>0 and not ms:return-1000000 if chk else 0
 for m,rb,ns,rep,nca in ms:
  s=-sr(rb,ns,rep,nca,-b,-a,max(d-1,0))
  if SP:return 0
  if s>=b:return b
  if s>a:a=s
 return a
def th(B,Sc,ep,ca,ours):
 global N_,SP
 N_=0;SP=False;best=ours[0];a=-10000000;d=1
 while d<=9 and not SP:
  for m in ours:
   rb,ns,rep,nca=mv(B,Sc,m,ep,ca)
   if atk(rb,rb.index('k')):continue
   s=-sr(rb,ns,rep,nca,-10000000,-a,d-1)
   if SP:break
   if s>a:a=s;best=m
  if SP:break
  d+=1
 return best
def pf(f):
 p=f.split();B=list(' '*20+(' '+'.'*8+' ')*8+' '*20);Sc=0;i=21
 for ch in p[0]:
  if ch=='/':i+=2
  elif ch.isdigit():i+=int(ch)
  else:B[i]=ch;Sc+=pv(ch,i)if ch.isupper()else-pv(ch,vf(i));i+=1
 ca=sum(1<<'KQkq'.index(c)for c in p[2]if c in'KQkq')
 ep=-1
 if p[3]!='-':ep=sq(p[3])
 B=''.join(B)
 if p[1]=='b':B=fl(B);Sc=-Sc;ca=((ca&3)<<2)|(ca>>2);ep=vf(ep)if~ep else-1
 return B,Sc,ep,ca
def po(p,d):
 return u.urlopen(u.Request(E+p,data=json.dumps(d).encode())).read()
def ml():
 while 1:
  g=json.loads(po('/game',{}));s=g.get('status')
  if s=='done':return
  if s!='your_move':continue
  B,Sc,ep,ca=pf(g['fen'])
  blk=g['fen'].split()[1]=='b'
  ours=[(sq(x),sq(x[2:]),5 if len(x)>4 else 0)for x in g['legal_moves']]
  if blk:ours=[(vf(s),vf(t),p)for s,t,p in ours]
  m=th(B,Sc,ep,ca,ours)
  if blk:m=(vf(m[0]),vf(m[1]),m[2])
  po('/move',{'game':g['game'],'move':chr(97+m[0]%10-1)+str(10-m[0]//10)+chr(97+m[1]%10-1)+str(10-m[1]//10)+('q'if m[2]else'')})
ml()
