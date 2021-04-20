import vtk


#source
cone=vtk.vtkConeSource()
cone.SetRadius(6)
cone.SetHeight(8)
cone.SetResolution(100)
cone.Update()

cube1=vtk.vtkCubeSource()
cube1.SetXLength(8)
cube1.SetYLength(8)
cube1.SetZLength(8)
cube1.Update()

cube2=vtk.vtkCubeSource()
cube2.SetXLength(4)
cube2.SetYLength(4)
cube2.SetZLength(4)
cube2.Update()

cube3=vtk.vtkCubeSource()
cube3.SetXLength(6)
cube3.SetYLength(3)
cube3.SetZLength(3)
cube3.Update()

manija=vtk.vtkSphereSource()
manija.SetRadius(0.7)
manija.Update()

#mapper
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputData(cone.GetOutput())

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputData(cube1.GetOutput())

mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputData(cube2.GetOutput())

mapper4 = vtk.vtkPolyDataMapper()
mapper4.SetInputData(cube3.GetOutput())

mapper5 = vtk.vtkPolyDataMapper()
mapper5.SetInputData(manija.GetOutput())




#actor
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.GetProperty().SetColor(1.0, 0.0, 0.0)
actor1.SetPosition(20,0,0)

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(1.0, 1.0, 0.0)
actor2.SetPosition(12,0,0)

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor3.GetProperty().SetColor(1.0, 1.0, 1.0)
actor3.SetPosition(12,2.5,0)

actor4 = vtk.vtkActor()
actor4.SetMapper(mapper4)
actor4.GetProperty().SetColor(1.0, 2.0, 1.0)
actor4.SetPosition(11,0,3)

actor5 = vtk.vtkActor()
actor5.SetMapper(mapper5)
actor5.GetProperty().SetColor(1.0, 0.0, 0.0)
actor5.SetPosition(10,0.8,4)


#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(actor4)
renderer.AddActor(actor5)


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

