import vtk
import numpy as np
import math

class MySphere:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius    
        self.velocity = [0,-10,0] # la esfera cae, por eso tiene una velocida hacia abajo
        self.last_velocity = [0,-10,0]
        self.actor = None

class MyFloor:
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height    
        self.velocity = np.array([0,0,0])
        self.actor = None

sphere = MySphere([0,40,0], 2)
floor = MyFloor([0,0,0], 1)
time = 0
g = 9
height = abs(floor.pos[1] - sphere.pos[1]) 
  
def set_initial_position():
    sphere_actor.SetPosition(sphere.pos[0], sphere.pos[1], sphere.pos[2])
    floor_actor.SetPosition(floor.pos[0], floor.pos[1], floor.pos[2])

def callback_func(caller, timer_event):
    global time
    print("velocity", sphere.velocity, "last velocity", sphere.last_velocity )
    #print("pos", sphere.pos, "\n")

    sphere.pos[1] =  sphere.pos[1] + sphere.velocity[1]*time    
    # distancia = velocidad * tiempo
    # new_position =  old_position + velocidad * tiempo

    sphere.last_velocity[1] = sphere.velocity[1]
    
    if (sphere.pos[1] - sphere.radius) < (floor.pos[1] + floor.height/2):        
        sphere.velocity[1] = abs(sphere.velocity[1]/1.3)  #con cada rebote, se libera energia(calor, vibracion, etc) y se pierde velocidad      
    else:
        sphere.velocity[1] = sphere.velocity[1] - g*time

        if sphere.last_velocity[1]*sphere.velocity[1] < 0: #si cambio la dirección de la velocidad, cuando empieza a caer
            #print("\nrestart time\n")
            time = 0

    sphere.actor.SetPosition(sphere.pos[0], sphere.pos[1], sphere.pos[2])  
    time += 0.001
    render_window.Render()

# source
source1 = vtk.vtkSphereSource()
source1.SetThetaResolution(50)
source1.SetRadius(sphere.radius)
source1.Update()

source2 = vtk.vtkCubeSource()
source2.SetXLength(40)
source2.SetYLength(floor.height)
source2.SetZLength(40)
source2.Update()

# mapper
sphere_mapper = vtk.vtkPolyDataMapper()
sphere_mapper.SetInputData(source1.GetOutput())
floor_mapper = vtk.vtkPolyDataMapper()
floor_mapper.SetInputData(source2.GetOutput())

#actor
sphere_actor = vtk.vtkActor()
sphere_actor.SetMapper(sphere_mapper)
sphere_actor.GetProperty().SetColor(0, 1, 0.0)
#sphere_actor.GetProperty().SetOpacity(0.5)
sphere.actor = sphere_actor

floor_actor = vtk.vtkActor()
floor_actor.SetMapper(floor_mapper)
floor_actor.GetProperty().SetColor(1, 1, 0.0)
#sphere_actor.GetProperty().SetOpacity(0.7)
floor.actor = floor_actor

#camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0,sphere.pos[1]/2,0)
#camera.SetPosition(0,sphere.pos[1],sphere.pos[1]*2.7)
camera.SetPosition(0,sphere.pos[1],sphere.pos[1]*2.7)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(sphere_actor)
renderer.AddActor(floor_actor)
renderer.SetActiveCamera(camera)

#renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(1200, 1200)
render_window.AddRenderer(renderer)

#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()

set_initial_position()

interactor.CreateRepeatingTimer(1)
interactor.AddObserver("TimerEvent", callback_func)
interactor.Start()

