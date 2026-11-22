import numpy as np, sys
from PIL import Image, ImageFilter
W,H=1080,1920
rng=np.random.default_rng(23)
gw,gh=270,480                      # work at quarter res
def facets(npts,seed_off):
    r=np.random.default_rng(100+seed_off)
    pts=np.stack([r.random(npts)*gw,r.random(npts)*gh],1)
    tilt=r.normal(0,1,(npts,2))
    off=r.normal(0,1,npts)
    yy,xx=np.mgrid[0:gh,0:gw].astype('float32')
    d=np.stack([np.hypot(xx-p[0],yy-p[1]) for p in pts],0)
    idx=np.argsort(d,0)
    d1=np.take_along_axis(d,idx[:1],0)[0]; d2=np.take_along_axis(d,idx[1:2],0)[0]
    cell=idx[0]
    dx=xx-pts[cell,0]; dy=yy-pts[cell,1]
    plane=(tilt[cell,0]*dx+tilt[cell,1]*dy)/np.maximum(d1.max(),1)*0.9+off[cell]*0.6
    crease=np.exp(-((d2-d1)/2.2))
    return plane,crease
p1,c1=facets(40,1)
p2,c2=facets(110,2)
plane=0.8*p1+0.45*p2
crease=np.clip(0.8*c1+0.5*c2,0,1)
def up(a):
    im=Image.fromarray(((a-a.min())/(a.max()-a.min())*255).astype('uint8')).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(2.0))
    return np.asarray(im,dtype='float32')/255
P=up(plane); Cr=up(crease)
shade=1+(P-0.5)*0.10-Cr*0.065+Cr**2*0.02
fine=rng.random((H//3+2,W//3+2)).astype('float32')
fine=np.asarray(Image.fromarray((fine*255).astype('uint8')).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(0.8)),dtype='float32')/255
shade+= (fine-0.5)*0.05
shade+= (rng.random((H,W)).astype('float32')-0.5)*0.02
base=np.array([float(x) for x in (sys.argv[2] if len(sys.argv)>2 else "212,230,204").split(",")],dtype="float32")
img=base[None,None,:]*np.clip(shade,0.85,1.08)[:,:,None]
yy,xx=np.mgrid[0:H,0:W]
v=1-0.09*(((xx-W/2)/(W/2))**2+((yy-H/2)/(H/2))**2)/2
img=img*v[:,:,None]
Image.fromarray(np.clip(img,0,255).astype('uint8')).save(sys.argv[1],quality=90)
print('paper ok')
