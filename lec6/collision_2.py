from vpython import*

m1=1
m2=20
t=0
b=1
dt=0.005
k=0.5

scene=canvas(width=1200,height=800,center=vector(20,0,0),background=vector(0,0,0.1))
xaxis=arrow(pos=vector(0,7,7), axis=vector(3,0,0), color=color.green)
yaxis=arrow(pos=vector(0,7,7), axis=vector(0,3,0), color=color.red)
zaxis=arrow(pos=vector(0,7,7), axis=vector(0,0,3), color=color.orange)
figure1=graph(xtitle="t",ytitle="P",xmin=0,xmax=15)
p1t=gcurve(graph=figure1,color=color.red)
p2t=gcurve(graph=figure1,color=color.blue)
ptotalt=gcurve(graph=figure1,color=color.green)

figure2=graph(xtitle="t",ytitle="E",xmin=0,xmax=15)
e1t=gcurve(graph=figure2,color=color.red)
e2t=gcurve(graph=figure2,color=color.blue)
espringt=gcurve(graph=figure2,color=color.black)
etotalt=gcurve(graph=figure2,color=color.green)


spring=helix(radius=2, pos=vector(0,0,0), axis=vector(15,0,0),color=color.red, thickness=0.5,coils=6)
floor=box(pos=vector(25,-5,0),axis=vector(0,1,0),length=1,height=70,width=13)

block1=box(pos=vector(0,0,0),axis=vector(1,0,0),length=8.8,height=8.8,width=8.8, color=color.green)
block2=box(pos=vector(40,0,0),axis=vector(1,0,0),length=8.8,height=8.8,width=8.8, color=color.yellow)

block1.v=vector(10,0,0)
block2.v=vector(0,0,0)
block1.a=vector(0,0,0)
block2.a=vector(0,0,0)
dis12=(block2.pos-vector(4.4,0,0))-(block1.pos+vector(4.4,0,0))
Ektotal=0.5*m1*(mag(block1.v))**2
work=0

while(t<15):
    rate(300)
    Ek1=0.5*m1*block1.v.x**2
    Ek2=0.5*m2*block2.v.x**2
    spring.pos.x=block1.pos.x+2.5
    dis12=(block2.pos-vector(2.5,0,0))-(block1.pos+vector(2.5,0,0))
    if(mag(dis12)<=15): 
        spring.axis=dis12
        f=-k*(vector(15,0,0)-spring.axis)-b*(block1.v-block2.v) 
        block1.a=f/m1
        block2.a=-f/m2
        work=work-b*mag(block1.v-block2.v)**2*dt
    else:
        block1.a=vector(0,0,0)
        block2.a=vector(0,0,0)
    block1.v=block1.v+block1.a*dt
    block1.pos=block1.pos+block1.v*dt
    block2.v=block2.v+block2.a*dt
    block2.pos=block2.pos+block2.v*dt
    Ek1=0.5*m1*block1.v.x**2 
    Ek2=0.5*m2*block2.v.x**2 
    Uspring=0.5*k*(mag(vector(15,0,0)-spring.axis))**2
    p1t.plot(pos=(t,m1*block1.v.x))
    p2t.plot(pos=(t,m2*block2.v.x))
    ptotalt.plot(pos=(t,m1*block1.v.x+m2*block2.v.x))
    e1t.plot(pos=(t,Ek1))
    e2t.plot(pos=(t,Ek2))
    espringt.plot(pos=(t,0.5*k*(mag(vector(15,0,0)-spring.axis))**2))
    etotalt.plot(pos=(t,Ek1+Ek2+Uspring))
    t=t+dt
dE=Ektotal-(Ek1+Ek2+Uspring) 
print(dE)
print(work)

