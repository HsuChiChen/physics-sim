from vpython import*
scene=canvas(title="assignment",width=1200,height=1000,center=vector(5,5,5),background=vector(0.5,0.5,0),range=(5))

mybox=box(pos=vector(0,2,0),axis=vector(0,0,1),length=12,height=20,width=1,color=vector(10,0,0))
mybox=box(pos=vector(20,0,0),axis=vector(1,0,0),length=40,height=4,width=10,color=vector(0,15,10))
spring=helix(pos=vector(0,10,0),axis=vector(25,0,0),thickness=1,radius=1,color=vector(30,0,30))
mybox=box(pos=vector(25,10,0),axis=vector(0,0,1),length=4,height=4,width=4,color=vector(20,20,0))
