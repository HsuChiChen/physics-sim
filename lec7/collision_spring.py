from vpython import*

massratio=20
m1=1
m2=massratio*m1
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


figure1=graph(xtitle="t",ytitle="P",xmin=0,xmax=15) #動量時間圖P-t圖
p1t=gcurve(graph=figure1,color=color.red)
p2t=gcurve(graph=figure1,color=color.blue)
ptotalt=gcurve(graph=figure1,color=color.green)

figure2=graph(xtitle="t",ytitle="E",xmin=0,xmax=15) #能量時間圖E-t圖
e1t=gcurve(graph=figure2,color=color.red)
e2t=gcurve(graph=figure2,color=color.blue)
espringt=gcurve(graph=figure2,color=color.black)
etotalt=gcurve(graph=figure2,color=color.green)

cube1.v=vector(5,0,0)
cube2.v=vector(0,0,0)
cube1.a=vector(0,0,0)
cube2.a=vector(0,0,0)
dis12=(cube2.pos-vector(2.5,0,0))-(cube1.pos+vector(2.5,0,0))
Ektotal=0.5*m1*(mag(cube1.v))**2   #原總能量
work=0

while(t<20):
    rate(300)
    Ek1=0.5*m1*cube1.v.x**2
    Ek2=0.5*m2*cube2.v.x**2
    spring.pos.x=cube1.pos.x+2.5
    dis12=(cube2.pos-vector(2.5,0,0))-(cube1.pos+vector(2.5,0,0))
    if(mag(dis12)<=springlength):   #彈簧開始壓縮
        spring.axis=dis12
        f=-k*(vector(springlength,0,0)-spring.axis)-b*(cube1.v-cube2.v) #彈簧對木塊1所做的力+阻尼力
        cube1.a=f/m1
        cube2.a=-f/m2
        work=work-b*mag(cube1.v-cube2.v)*mag(cube1.v-cube2.v)*dt    #fb阻尼力對dx做積分即阻尼力所做的功:work=fb*dx
    else:
        cube1.a=vector(0,0,0)
        cube2.a=vector(0,0,0)
    cube1.v=cube1.v+cube1.a*dt
    cube1.pos=cube1.pos+cube1.v*dt
    cube2.v=cube2.v+cube2.a*dt
    cube2.pos=cube2.pos+cube2.v*dt
    Ek1=0.5*m1*cube1.v.x**2 #木塊1的動能
    Ek2=0.5*m2*cube2.v.x**2 #木塊2的動能
    Uspring=0.5*k*(mag(vector(springlength,0,0)-spring.axis))**2
    p1t.plot(pos=(t,m1*cube1.v.x))
    p2t.plot(pos=(t,m2*cube2.v.x))
    ptotalt.plot(pos=(t,m1*cube1.v.x+m2*cube2.v.x))
    e1t.plot(pos=(t,Ek1))
    e2t.plot(pos=(t,Ek2))
    espringt.plot(pos=(t,0.5*k*(mag(vector(springlength,0,0)-spring.axis))**2)) #彈簧的彈力位能
    etotalt.plot(pos=(t,Ek1+Ek2+Uspring))
    t=t+dt
dE=Ektotal-(Ek1+Ek2+Uspring) #原總能量-末總能量
print(dE)
print(work)
