from vpython import*


m1=1
m2=20
t=0
dt=0.01
k=2
b=0.3
springlength=15

scene=canvas(title="彈性碰撞",center=vector(20,0,0),width=1200,height=800,background=vector(0.5,0.6,0.7),range=50)
cube1=box(pos=vector(-2.5,0,0),axis=vector(1,0,0),length=5,width=5,height=5,color=color.blue)
cube2=box(pos=vector(20,0,0),axis=vector(1,0,0),length=5,width=5,height=5,color=color.yellow)
spring=helix(pos=vector(0,0,0),axis=vector(springlength,0,0),color=color.white)
floor=box(pos=vector(20,-3,0),axis=vector(1,0,0),length=100,width=50,height=1)

cube1.v=vector(5,0,0)
cube2.v=vector(0,0,0)
cube1.a=vector(0,0,0)
cube2.a=vector(0,0,0)
dis12=(cube2.pos-vector(2.5,0,0))-(cube1.pos+vector(2.5,0,0))

while(t<10):
    rate(300)
    spring.pos.x=cube1.pos.x+2.5
    dis12=(cube2.pos-vector(2.5,0,0))-(cube1.pos+vector(2.5,0,0))
    if(mag(dis12)<=springlength):   #彈簧開始壓縮
        spring.axis=dis12
        f=-k*(vector(springlength,0,0)-spring.axis)-b*(cube1.v-cube2.v) #彈簧對木塊1所做的力+阻尼力
        cube1.a=f/m1
        cube2.a=-f/m2
    else:
        cube1.a=vector(0,0,0)
        cube2.a=vector(0,0,0)
    cube1.v=cube1.v+cube1.a*dt
    cube1.pos=cube1.pos+cube1.v*dt
    cube2.v=cube2.v+cube2.a*dt
    cube2.pos=cube2.pos+cube2.v*dt
    t=t+dt
