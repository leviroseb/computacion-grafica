import vtk
import math

sphere_pos = [0,40,0]
floor_pos = [0,0,0]

def set_initial_position():
    sphere_actor.SetPosition(sphere_pos[0], sphere_pos[1], sphere_pos[2])
    floor_actor.SetPosition(floor_pos[0], floor_pos[1], floor_pos[2])

def callback_func(caller, timer_event):   
    sphere_pos[1] -= 0.2
    sphere_actor.SetPosition(sphere_pos[0], sphere_pos[1], sphere_pos[2])  
    render_window.Render()

# source
sphere = vtk.vtkSphereSource()
sphere.SetThetaResolution(50)
sphere.SetRadius(2)
sphere.Update()

floor = vtk.vtkCubeSource()
floor.SetXLength(40)
floor.SetYLength(1)
floor.SetZLength(40)
floor.Update()

# mapper
sphere_mapper = vtk.vtkPolyDataMapper()
sphere_mapper.SetInputData(sphere.GetOutput())
floor_mapper = vtk.vtkPolyDataMapper()
floor_mapper.SetInputData(floor.GetOutput())


#actor
sphere_actor = vtk.vtkActor()
sphere_actor.SetMapper(sphere_mapper)
sphere_actor.GetProperty().SetColor(0, 1, 0.0)

floor_actor = vtk.vtkActor()
floor_actor.SetMapper(floor_mapper)
floor_actor.GetProperty().SetColor(1, 1, 0.0)

#camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0,sphere_pos[1]/2,0)
camera.SetPosition(0,sphere_pos[1],sphere_pos[1]*2.7)

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

