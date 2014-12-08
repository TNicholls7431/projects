import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
 pos = mc.player.getPos()
 x = pos.x
 y = pos.y
 z = pos.z

 block = 41

 mc.setBlock(x,y-1,z,block)
 time.sleep(0.2)
