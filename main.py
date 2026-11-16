import json as j,os,urllib.request as u
U=os.environ['MAKEFUN_ENV_URL']
def P(p,b):return j.load(u.urlopen(U+p,j.dumps(b).encode()))
B=bytearray(128)
V=(0,)+(1,3,3,5,9,0)*2
KN=(-33,-31,-18,-14,14,18,31,33)
KG=(-17,-15,15,17,-16,-1,1,16)
C={112:2,119:1,116:3,0:8,7:4,4:12}
PT=[[0]*128 for _ in range(13)]
def pv(t,r,f):
 c=min(f,7-f)+min(r,7-r)
 return(0,100+r*r,300+6*c,322+4*c,500,894,-15*r)[t]
for s in range(128):
 r=s>>4;f=s&7
 for t in range(1,7):PT[t][s]=pv(t,7-r,f);PT[t+6][s]=-pv(t,r,f)
G=[1,15,-1,0,116,4]
ST=[];ND=[0]*3;M=9999
def A(q,w):
 for o in(15,17):
  t=q+o if w else q-o
  if not t&136 and B[t]==7-6*w:return 1
 for o in KN+KG:
  t=q+o
  if not t&136 and B[t]==(2,6)[o in KG]+6-6*w:return 1
 for d in KG:
  t=q+d
  while not t&136:
   c=B[t]
   if c:
    if c-6+6*w in((3,5)if abs(d)in(15,17)else(4,5)):return 1
    break
   t+=d
 return 0
def IC():return A(G[4+(G[0]<0)],G[0]<0)
def GN(c):
 ms=[];w=G[0]>0;sr=6 if w else 1;lr=0 if w else 7
 def pm(o):
  if(o>>4)==lr:ms.extend(s|o<<7|p<<14 for p in(5,4,3,2))
  else:ms.append(s|o<<7)
 for s in range(128):
  c0=B[s]
  if not c0 or(c0<7)!=w:continue
  t=(c0-1)%6+1
  if t==1:
   d=-16 if w else 16;o=s+d
   if not B[o]and not c:
    pm(o)
    if(s>>4)==sr and not B[o+d]:ms.append(s|(o+d)<<7)
   for o in(s+d-1,s+d+1):
    if not o&136 and(B[o]and(B[o]<7)!=w or o==G[2]):pm(o)
  else:
   ds=(KN,KG[:4],KG[4:],KG,KG)[t-2];sl=2<t<6
   for d in ds:
    o=s+d
    while not o&136:
     x=B[o]
     if(x<7)!=w if x else not c:ms.append(s|o<<7)
     if x or not sl:break
     o+=d
   if t==6 and not c:
    for r,t2 in((1,118),(2,114),(4,6),(8,2)):
     if G[1]&r and not(B[(s+t2)//2]|B[t2])and all(not A(x,not w)for x in(s,(s+t2)//2,t2))and(t2>s or not B[t2-1]):ms.append(s|t2<<7)
 return ms
def MK(m):
 fr=m&127;to=m>>7&127;pr=m>>14;pc=B[fr];cp=B[to];cs=-1
 if pc%6==1 and to==G[2]and not cp:cs=to+16-32*(pc>6);cp=B[cs]
 ST.append((m,cp,cs,pc,G[:]));B[to]=pr+6*(pc>6)if pr else pc;B[fr]=0
 if cs>=0:B[cs]=0
 if pc in(6,12):
  if to-fr==2:B[to-1]=B[to+1];B[to+1]=0
  elif fr-to==2:B[to+1]=B[to-2];B[to-2]=0
  G[4+(pc>6)]=to
 G[1]&=~(C.get(fr,0)|C.get(to,0));G[2]=(fr+to)//2 if pc%6==1 and abs(to-fr)==32 else-1;G[0]=-G[0]
 if A(G[4+(pc>6)],pc>6):UM();return 0
 return 1
def UM():
 m,cp,cs,pc,g=ST.pop();fr=m&127;to=m>>7&127;B[fr]=pc
 if cs>=0:B[cs]=cp;B[to]=0
 else:B[to]=cp
 if pc in(6,12)and abs(to-fr)==2:
  rs=to-1 if to>fr else to+1;B[rs+2 if to>fr else rs-3]=B[rs];B[rs]=0
 G[:]=g
def EV():return sum(PT[x][i]for i,x in enumerate(B)if x)*G[0]
def N(d,a,b):
 ND[0]+=1
 if ND[0]>=ND[2]:ND[1]=1;return 0
 if d<=0:
  ch=IC();bs=EV()
  if ch:bs=1-M
  elif bs>=b:return bs
  elif bs>a:a=bs
  ms=GN(0)if ch else GN(1)
 else:
  if IC():d+=1
  elif d>2:
   G[0]=-G[0];s=-N(d-3,-b,-b+1);G[0]=-G[0]
   if s>=b:return b
  ms=GN(0);bs=-M
 ms.sort(key=lambda m:V[B[m>>7&127]]+V[m>>14],reverse=1);lg=0
 for m in ms:
  if not MK(m):continue
  lg+=1
  if d>2 and lg>3 and ST[-1][1]<1:s=-N(d-2,-a-1,-a)
  else:s=-N(d-1,-b,-a)
  UM()
  if ND[1]:return 0
  if s>bs:bs=s
  if s>a:a=s
  if s>=b:break
 if not lg:
  if d<=0:return 1-M if ch else bs
  return 1-M if IC()else 0
 return bs
def R(ms):
 bs=ms[0]
 for d in range(1,65):
  ND[1]=0;ND[0]=0;ND[2]=65000
  al=-M
  for m in ms:
   MK(m);s=-N(d-1,-M,-al);UM()
   if ND[1]:break
   if s>al:al=s;bs=m
  if ND[1]:break
  ms.remove(bs);ms.insert(0,bs)
 return bs
def PU(u):
 fr,to=[(8-int(u[i+1]))*16+ord(u[i])-97 for i in(0,2)];pr="  nbrq".find(u[4:])
 return fr|to<<7|pr<<14
def UU(m):return q(m&127)+q(m>>7&127)+("  nbrq"[m>>14]if m>>14 else"")
def q(x):return chr(97+(x&7))+str(8-(x>>4))
def SY(g):
 B[:]=bytearray(128)
 B[0:8]=b'\n\10\11\13\14\11\10\n';B[16:24]=b'\7'*8;B[96:104]=b'\1'*8;B[112:120]=b'\4\2\3\5\6\3\2\4'
 G[:]=[1,15,-1,0,116,4];ST.clear()
 for u in g['moves']:MK(PU(u))
 ST.clear()
while 1:
 g=P('/game',{})
 if g['status'][0]=='d':break
 SY(g);gm=g['game']
 while 1:
  lg=g['legal_moves']
  if not lg:g=P('/resign',{'game':gm});break
  try:m=R([PU(x)for x in lg])
  except:m=PU(lg[0])
  g=P('/move',{'game':gm,'move':UU(m)})
  if g['status'][0]!='y':break
  SY(g)
