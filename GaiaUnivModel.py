from turtle import position
from ursina import *
import math
from ursina.prefabs.first_person_controller import FirstPersonController
#installing necessary packages and controls

# creating keyboard controls for x and y axis
def camera_control():
	camera.x += held_keys["d"] * time.dt * 5
	camera.x -= held_keys["a"] *time.dt * 5
	camera.y += held_keys["w"] * time.dt * 5
	camera.y -= held_keys["s"] *time.dt * 5
	
#creating the radius of the exoplanet
def update():
    global t
    t = t + 0.02
    angle = math.pi*40/180

    radius_3 = 4.0 #in terms of solar radii 
    exo.x = math.cos(t+angle*2)*radius_3
    exo.z = math.sin(t+angle*2)*radius_3

    star.rotation_y += time.dt*5
    exo.rotation_y += time.dt
    camera_control()

# parameters of entity 
class Sky(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = "C:/Users/sweth/Desktop/StarsMap.jpg",
            parent = scene,
            scale = 150,
            double_sided = True
        )

app = Ursina()
sku = Sky()
EditorCamera()
# change the textures as jpg files
star = Entity(model= "sphere",  scale=3, texture = "C:/Users/sweth/Desktop/Testtexture2.jpg")
exo = Entity(model='sphere',  scale=1, texture = "C:/Users/sweth/Desktop/Exoplanet.jpg")

t = -math.pi
app.run()