import numpy as np, wave, sys
import sys; SR=44100; DUR=float(sys.argv[2]); BPM=float(sys.argv[3]); beat=60/BPM
N=int(SR*DUR); L=np.zeros(N); R=np.zeros(N)
def mtof(m): return 440*2**((m-69)/12)
def add(sig,t0,pan=0.5,g=1.0):
    i=int(t0*SR)
    if i>=N: return
    e=min(N,i+len(sig)); s=sig[:e-i]*g
    L[i:e]+=s*(1-pan)*1.4; R[i:e]+=s*pan*1.4
def env(n,a,d,s,r):
    t=np.arange(n)/SR; e=np.ones(n)
    e*=np.minimum(1,t/a)
    e*=np.where(t>a,s+(1-s)*np.exp(-(t-a)/d),1)
    tail=np.minimum(1,np.maximum(0,(n/SR-t)/r)); return e*tail
chords=[(48,[60,64,67]),(43,[59,62,67]),(45,[60,64,69]),(41,[60,65,69])]  # C G Am F
rng=np.random.default_rng(int(sys.argv[5])); chords=chords[int(sys.argv[4]):]+chords[:int(sys.argv[4])]
bar=4*beat; nbars=int(DUR/bar)+1
for b in range(nbars):
    t0=b*bar; root,tri=chords[b%4]
    n=int(bar*SR*1.05); t=np.arange(n)/SR
    # pad: detuned soft saw-ish via harmonics
    for m in tri:
        f=mtof(m); sig=sum(np.sin(2*np.pi*f*h*t+ph)/h**1.6 for h,ph in ((1,0),(2,.3),(3,.9),(4,1.4)))
        sig+=sum(np.sin(2*np.pi*f*1.004*h*t)/h**1.6 for h in (1,2))
        add(sig*env(n,.25,9,1.0,.5)*0.035,t0,0.35+0.3*rng.random())
    # bass
    nb=int(beat*2*SR); tb=np.arange(nb)/SR
    for k in (0,2):
        bs=np.sin(2*np.pi*mtof(root)*tb)+0.3*np.sin(2*np.pi*mtof(root)*2*tb)
        add(bs*env(nb,.01,.5,.4,.1)*0.22,t0+k*beat,0.5)
    # arpeggio plucks, 8th notes
    seq=[tri[0],tri[1],tri[2],tri[1]+12,tri[2],tri[1],tri[0]+12,tri[1]]
    for k,m in enumerate(seq):
        npk=int(beat*1.6*SR); tp=np.arange(npk)/SR; f=mtof(m+12)
        sig=np.sin(2*np.pi*f*tp)+.5*np.sin(2*np.pi*f*2*tp)*np.exp(-tp*8)+.25*np.sin(2*np.pi*f*3*tp)*np.exp(-tp*14)
        add(sig*np.exp(-tp*5.5)*0.11,t0+k*beat/2,0.25+0.5*((k%4)/3))
    # kick on beats, hat on offbeats, clap on 2 & 4
    for k in range(4):
        nk=int(.25*SR); tk=np.arange(nk)/SR
        kick=np.sin(2*np.pi*(55+90*np.exp(-tk*30))*tk)*np.exp(-tk*12)
        add(kick*0.5,t0+k*beat,0.5)
        nh=int(.05*SR); hat=rng.standard_normal(nh)*np.exp(-np.arange(nh)/SR*70)
        hat=np.diff(hat,prepend=0)
        add(hat*0.10,t0+k*beat+beat/2,0.62)
        if k in (1,3):
            nc=int(.12*SR); cl=rng.standard_normal(nc)*np.exp(-np.arange(nc)/SR*35)
            add(np.diff(cl,prepend=0)*0.13,t0+k*beat,0.45)
# gentle reverb-ish echo
def echo(x,d,g):
    y=x.copy(); k=int(d*SR); y[k:]+=x[:-k]*g; return y
L=echo(L,.19,.28); R=echo(R,.23,.28)
fade=np.minimum(1,np.arange(N)/(SR*1.0))*np.minimum(1,(N-np.arange(N))/(SR*5.0))
L*=fade; R*=fade
pk=max(abs(L).max(),abs(R).max()); L/=pk; R/=pk
out=np.stack([L,R],1)*0.85
pcm=(out*32767).astype('<i2')
w=wave.open(sys.argv[1],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()
print('ok')
