import vtk

# source
cube1 = vtk.vtkCubeSource()
cube1.SetXLength(10)
cube1.SetYLength(20)
cube1.SetZLength(10)
cube1.Update()

cube2 = vtk.vtkCubeSource()
cube2.SetXLength(5)
cube2.SetYLength(7)
cube2.SetZLength(8)
cube2.Update()

cube3 = vtk.vtkCubeSource()
cube3.SetXLength(10)
cube3.SetYLength(7)
cube3.SetZLength(10)
cube3.Update()

# mapper
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputData(cube1.GetOutput())

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputData(cube2.GetOutput())

mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputData(cube3.GetOutput())

#actor
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.GetProperty().SetColor(1.0, 0.0, 0.0)
actor1.SetPosition(10,0,0)

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(0.0, 1.0, 0.0)
actor2.SetPosition(10,10,0)

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor3.GetProperty().SetColor(0.0, 0.0, 1.0)
actor3.SetPosition(10,10,10)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)

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
interactor.Start()