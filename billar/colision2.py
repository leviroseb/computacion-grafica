import vtk
import numpy as np
import math
import matplotlib.pyplot as plt

class MySphere:
    def __init__(self, pos, radius,velocidad,aceleracion):
        self.pos = pos
        self.radius = radius    
        self.velocity = velocidad # la esfera cae, por eso tiene una velocida hacia abajo
        self.aceleracion=aceleracion
        self.last_velocity = [0.000,-10.000,0.000]
        self.actor = None
        self.rebote=True
        self.velMin=10
        self.movimientoXZ=True
        self.anguloX=0
        self.anguloZ=0

class MyFloor:
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height
        self.longitudX=99
        self.longitudY=198    
        self.velocity = np.array([0,0,0])
        self.actor = None


m=170 #masa de la bola gramos


C=0.47   #coeficiente de arrastre de una esfera
radio=5.715/2
A=radio*2 #Area Transversal
P=0.00129  #densidad del aire g/cm^3
k=(C*A*P)/(2*m)

friccion=0.0000006


#ax=0-k*v*vx
#ay=-10-10-k*v*vy


h=0.001


vx=400
vy=0
vz=200
v=math.sqrt(vx**2+vy**2+vz**2)


sphere = MySphere([0,0,0], radio,[vx,vy,vz], [-k*v*vx,-980-k*v*vy,-k*v*vz])##0-k*v*vx,-10-10-k*v*vy,0-k*v*vz])
floor = MyFloor([0,-sphere.radius,0], 1)


vxs=[]
vys=[]
vzs=[]
tt=[]
sum=0
  
def set_initial_position():
    sphere_actor.SetPosition(sphere.pos[0], sphere.pos[1], sphere.pos[2])
    actor1.SetPosition(floor.pos[0], floor.pos[1], floor.pos[2])

def callback_func(caller, timer_event):
    global h
    global k
    global vxs
    global vys
    global vzs
    global tt
    global sum
    global m
    global radio

    
    vxs.append(sphere.velocity[0])
    vys.append(sphere.velocity[1])
    vzs.append(sphere.velocity[2])
    sum=sum+h
    tt.append(sum+h)

    XX=math.sqrt((sphere.velocity[0]**2)+(sphere.velocity[2]**2))
    print(sphere.pos[2])

    if(math.sqrt((sphere.velocity[0]**2)+(sphere.velocity[2]**2))<sphere.velMin):
        
        sphere.movimientoXZ=False

        sphere.velocity[0]=0
        sphere.velocity[1]=0
        sphere.velocity[2]=0
        sphere.aceleracion[0]=0
        sphere.aceleracion[1]=0
        sphere.aceleracion[2]=0
        sphere.anguloZ=0
        sphere.anguloX=0
    
    if sphere.movimientoXZ is True:

        vi=math.sqrt((sphere.velocity[0]**2)+(sphere.velocity[1]**2)+(sphere.velocity[2]**2))

        #Aceleraciones:
        #Resistencia Aire
        sphere.aceleracion[0]=-1*k*vi*sphere.velocity[0]-(sphere.velocity[0]*friccion*m*(-980)*-1)
        sphere.aceleracion[1]=-10-1*k*vi*sphere.velocity[1]-(sphere.velocity[1]*friccion*m*(-980)*-1)
        sphere.aceleracion[2]=-1*k*vi*sphere.velocity[2]-(sphere.velocity[2]*friccion*m*(-980)*-1)

        


        #Eje x
        distanciaX=sphere.pos[0]
        sphere.pos[0]=round(sphere.pos[0]+sphere.velocity[0]*h,4)
        sphere.velocity[0]=round(sphere.velocity[0]+sphere.aceleracion[0]*h,4)

        distanciaX=sphere.pos[0]-distanciaX #S
        print(distanciaX)

        sphere.anguloZ=(-1*(distanciaX/radio)*180/math.pi)#(sphere.anguloX+distanciaX/radio)%6.28
        #print("X:",sphere.anguloZ)



        #Eje Y
        sphere.pos[1]=round(sphere.pos[1]+sphere.velocity[1]*h,4)
        sphere.velocity[1]=round(sphere.velocity[1]+sphere.aceleracion[1]*h,4)

        #Eje Z
        distanciaZ=sphere.pos[2]
        sphere.pos[2]=round(sphere.pos[2]+sphere.velocity[2]*h,4)
        sphere.velocity[2]=round(sphere.velocity[2]+sphere.aceleracion[2]*h,4)

        distanciaZ=sphere.pos[2]-distanciaZ #S
        #print("distancia:",distanciaZ)

        
        sphere.anguloX=((distanciaZ/radio)*180/math.pi)#(sphere.anguloZ+distanciaZ/radio)%6.28
        
        

        #Colissiones

        #Eje x
        if abs(sphere.pos[0]) + sphere.radius>floor.longitudX/2:
            sphere.velocity[0] = sphere.velocity[0]/1.3
            sphere.velocity[0] = sphere.velocity[0]*-1
            if(sphere.pos[0]>0):
                sphere.pos[0]=(floor.longitudX/2)-sphere.radius
            else:
                sphere.pos[0]=(-floor.longitudX/2)+sphere.radius
            

        #Eje Z
        if abs(sphere.pos[2]) + sphere.radius>floor.longitudY/2:
            sphere.velocity[2] = sphere.velocity[2]/1.3
            sphere.velocity[2] = sphere.velocity[2]*-1
            
            if(sphere.pos[2]>0):
                sphere.pos[2]=(floor.longitudY/2)-sphere.radius
            else:
                sphere.pos[2]=(-floor.longitudY/2)+sphere.radius


        #Eje Y

        if(sphere.pos[1]< 0):
            sphere.pos[1]=0 
            if sphere.rebote is True:
                if(abs(sphere.velocity[1])<sphere.velMin):
                    sphere.rebote=False
                    sphere.velocity[1]=0
                    
                else:
                    sphere.velocity[1] = sphere.velocity[1]/1.3 #con cada rebote, se libera energia(calor, vibracion, etc) y se pierde velocidad      
                    sphere.velocity[1] = sphere.velocity[1]*-1
                
                
            else:
                sphere.velocity[1]=0
                sphere.pos[1]=0 


        

    #vi=math.sqrt((sphere.velocity[0]**2)+(sphere.velocity[1]**2)+(sphere.velocity[2]**2))

    

    



    
    #print("velocidad->",sphere.velocity[1])
    #print("pos->",sphere.pos[1])


    
    
    
        
    


    
    
    

    sphere.actor.SetPosition(sphere.pos[0], sphere.pos[1], sphere.pos[2])  
    sphere.actor.RotateX(sphere.anguloX)
    sphere.actor.RotateZ(sphere.anguloZ)
    
    #print("vel",sphere.velocity[1])
    #print("pos",sphere.pos[1])
    render_window.Render()



############################################  source  ##################################################






cube1 = vtk.vtkCubeSource()
cube1.SetXLength(99)
#cube1.SetYLength(5)
cube1.SetZLength(198)
cube1.Update()

lateral2Source=vtk.vtkCubeSource()
lateral2Source.SetXLength(137)
lateral2Source.SetYLength(20)
lateral2Source.SetZLength(19)
lateral2Source.Update()


lateral1Source=vtk.vtkCubeSource()
lateral1Source.SetXLength(19)
lateral1Source.SetYLength(20)
lateral1Source.SetZLength(236)
lateral1Source.Update()


# esfera
source1 = vtk.vtkSphereSource()
source1.SetThetaResolution(50)
source1.SetRadius(sphere.radius)
source1.Update()


# Load ball texture
reader = vtk.vtkJPEGReader()
reader.SetFileName("bola.jpg")
# Create texture object
sphereTexture = vtk.vtkTexture()
if vtk.VTK_MAJOR_VERSION <= 5:
    sphereTexture.SetInput(reader.GetOutput())
else:
    sphereTexture.SetInputConnection(reader.GetOutputPort())


# Map texture coordinates
map_to_sphere = vtk.vtkTextureMapToSphere()
if vtk.VTK_MAJOR_VERSION <= 5:
    map_to_sphere.SetInput(source1.GetOutput())
else:
    map_to_sphere.SetInputConnection(source1.GetOutputPort())
map_to_sphere.PreventSeamOn()



############################################  mapper  ######################################################
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputData(cube1.GetOutput())

lateral1Mapper = vtk.vtkPolyDataMapper()
lateral1Mapper.SetInputData(lateral1Source.GetOutput())

lateral2Mapper = vtk.vtkPolyDataMapper()
lateral2Mapper.SetInputData(lateral2Source.GetOutput())

# mapper esfera
sphere_mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    sphere_mapper.SetInput(map_to_sphere.GetOutput())
else:
    sphere_mapper.SetInputConnection(map_to_sphere.GetOutputPort())

'''
floor_mapper = vtk.vtkPolyDataMapper()
floor_mapper.SetInputData(source2.GetOutput())
'''

###########################################  actor  ########################################################
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.GetProperty().SetColor(1/255, 152/255, 101/255)
actor1.SetPosition(0, 0, 0)



actor2 = vtk.vtkActor()
actor2.SetMapper(mapper1)
actor2.GetProperty().SetColor(147/255, 102/255, 8/255)
actor2.SetPosition(0, -7.50, 0)

lateral11actor= vtk.vtkActor()
lateral11actor.SetMapper(lateral1Mapper)
lateral11actor.GetProperty().SetColor(147/255, 102/255, 8/255)
lateral11actor.SetPosition(-59, 0, 0)

lateral12actor= vtk.vtkActor()
lateral12actor.SetMapper(lateral1Mapper)
lateral12actor.GetProperty().SetColor(147/255, 102/255, 8/255)
lateral12actor.SetPosition(59, 0, 0)

lateral21actor= vtk.vtkActor()
lateral21actor.SetMapper(lateral2Mapper)
lateral21actor.GetProperty().SetColor(147/255, 102/255, 8/255)
lateral21actor.SetPosition(0, 0, -108.5)

lateral22actor= vtk.vtkActor()
lateral22actor.SetMapper(lateral2Mapper)
lateral22actor.GetProperty().SetColor(147/255, 102/255, 8/255)
lateral22actor.SetPosition(0, 0, 108.5)



#actor
sphere_actor = vtk.vtkActor()
sphere_actor.SetMapper(sphere_mapper)
#sphere_actor.GetProperty().SetColor(0, 1, 0.0)
#sphere_actor.GetProperty().SetOpacity(0.5)
sphere_actor.SetTexture(sphereTexture)
sphere.actor = sphere_actor

'''
floor_actor = vtk.vtkActor()
floor_actor.SetMapper(floor_mapper)
floor_actor.GetProperty().SetColor(1, 1, 0.0)
#sphere_actor.GetProperty().SetOpacity(0.7)

'''
floor.actor = actor1

#camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0,sphere.pos[1]/2,0)
#camera.SetPosition(0,sphere.pos[1]*5,sphere.pos[1]*10.7)
camera.SetPosition(400,200,400)

# axes
transform = vtk.vtkTransform()
transform.Translate(0.0, 0.0, 0.0)
axes = vtk.vtkAxesActor()
axes.SetTotalLength(200, 200, 200)
axes.SetUserTransform(transform)



#############################################  renderer  #########################################################
renderer = vtk.vtkRenderer()
renderer.AddActor(sphere_actor)
renderer.AddActor(actor1)
renderer.SetActiveCamera(camera)
renderer.SetBackground(219/255, 228/255, 235/255)
renderer.AddActor(axes)
renderer.AddActor(actor2)
renderer.AddActor(lateral11actor)
renderer.AddActor(lateral12actor)
renderer.AddActor(lateral21actor)
renderer.AddActor(lateral22actor)

############################################  renderWindow  #############################################################
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(1200, 1200)
render_window.AddRenderer(renderer)

############################################   interactor  ##############################################################
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()

set_initial_position()

interactor.CreateRepeatingTimer(1)
interactor.AddObserver("TimerEvent", callback_func)
interactor.Start()

#print(tt)
plt.plot(tt,vys)
plt.show()
