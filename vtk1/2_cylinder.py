import vtk

# source
cylinder = vtk.vtkCylinderSource()
cylinder.SetRadius(20)
cylinder.SetHeight(50)
cylinder.SetResolution(50)
cylinder.Update()

# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(cylinder.GetOutput())

#actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0.0, 1.0, 0.0)
actor.RotateX(60.0)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(actor)

#renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(800, 800)
render_window.AddRenderer(renderer)

#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()