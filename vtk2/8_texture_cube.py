import vtk

#image for texture
reader = vtk.vtkJPEGReader()
reader.SetFileName("madera.jpg")

# Create texture object
texture = vtk.vtkTexture()
if vtk.VTK_MAJOR_VERSION <= 5:
    texture.SetInput(reader.GetOutput())
else:
    texture.SetInputConnection(reader.GetOutputPort())

texture.InterpolateOn()

# source
cube = vtk.vtkCubeSource()
cube.SetXLength(20)
cube.SetYLength(20)
cube.SetZLength(20)
cube.Update()

# Map texture coordinates
map_to_plane = vtk.vtkTextureMapToPlane()
if vtk.VTK_MAJOR_VERSION <= 5:
    map_to_plane.SetInput(cube.GetOutput())
else:
    map_to_plane.SetInputConnection(cube.GetOutputPort())

# Create mapper and set the mapped texture as input
mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(map_to_plane.GetOutput())
else:
    mapper.SetInputConnection(map_to_plane.GetOutputPort())

#actor
sphere_actor = vtk.vtkActor()
sphere_actor.SetMapper(mapper)
#sphere_actor.GetProperty().SetColor(0, 1, 0.0)
sphere_actor.SetTexture(texture)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(sphere_actor)


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

