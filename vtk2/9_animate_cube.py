import vtk

def callback_func(caller, timer_event):
    cube_actor.RotateZ(1)
    render_window.Render()

# source
cube = vtk.vtkCubeSource()
cube.Update()

# mapper
cube_mapper = vtk.vtkPolyDataMapper()
cube_mapper.SetInputData(cube.GetOutput())

#actor
cube_actor = vtk.vtkActor()
cube_actor.SetMapper(cube_mapper)
cube_actor.GetProperty().SetColor(0.5, 0.5, 0.0)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(cube_actor)

#renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(400, 400)
render_window.AddRenderer(renderer)

#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()


interactor.CreateRepeatingTimer(1)
interactor.AddObserver("TimerEvent", callback_func)
interactor.Start()

