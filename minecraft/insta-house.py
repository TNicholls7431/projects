import mcpi.minecraft as minecraft, time, random
mc = minecraft.Minecraft.create()

def house(x,y,z):
    mc.setBlocks(x+1,y,z+1,x+5,y+3,z+5,45)
    mc.setBlocks(x+2,y,z+2,x+4,y+2,z+4,0)

house(30,16,20)
house(40,16,20)
house(50,16,20)
