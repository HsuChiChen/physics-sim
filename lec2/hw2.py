from vpython import*
t=0
dt=0.01
R=3
P=vector(0,5,0)
V=vector(10,10,0)

sence=canvas(title='a',width=1000,height=1000,center=vector(0,0,0),background=vector(0.4,0.4,0.8),range=60)
xaxis=arrow(pos=vector(0,-5,0),axis=vector(3,0,0),color=vector(1,0,0))
yaxis=arrow(pos=vector(0,-5,0),axis=vector(0,3,0),color=vector(1,1,0))
zaxis=arrow(pos=vector(0,-5,0),axis=vector(0,0,3),color=vector(1,1,1))
ball=sphere(color=color.red,radius=R,pos=P,v=V)
mybox=box(pos=vector(0,0,0),axis=vector(1,0,0),length=50,height=2,width=10)
mybox2=box(pos=vector(-25,25,0),axis=vector(0,1,0),length=50,height=2,width=10)
mybox3=box(pos=vector(25,25,0),axis=vector(0,1,0),length=50,height=2,width=10)
mybox4=box(pos=vector(0,50,0),axis=vector(1,0,0),length=50,height=2,width=10)
mybox5=box(pos=vector(0,25,-5),axis=vector(0,0,1),length=1,height=50,width=50)

plot_figurel=graph(x=800,y=0,xtitle='time',ytitle='y',xmin=0,xmax=10000,ymin=0,ymax=1000)
yt=gcurve(graph=plot_figurel,color=color.red)
while t<10000:
    rate(100)
    ball.pos=ball.pos+ball.v*dt
    yt.plot(pos=(t,abs(ball.pos.y)))
    t=t+dt
    if ball.pos.x>21:
        ball.v.x=-ball.v.x
    if ball.pos.x<-21:
        ball.v.x=-ball.v.x
    if ball.pos.y>46:
        ball.v.y=-ball.v.y
    if ball.pos.y<4:
        ball.v.y=-ball.v.y
