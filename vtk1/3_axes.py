import vtk

# source
cylinder = vtk.vtkCylinderSource()
cylinder.SetRadius(0.2)
cylinder.SetHeight(0.5)
cylinder.SetResolution(10)
cylinder.Update()

# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(cylinder.GetOutput())

#actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0.0, 1.0, 0.0)
actor.SetPosition(-0.5,0.5,0.0)

#axes
transform = vtk.vtkTransform()
transform.Translate(0.0, 0.0, 0.0) 
axes = vtk.vtkAxesActor()
axes.SetUserTransform(transform)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(actor)
renderer.AddActor(axes)

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