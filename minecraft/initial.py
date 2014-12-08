import mcpi.minecraft as minecraft, time, random
mc = minecraft.Minecraft.create()

def t (x,y,z):
    mc.setBlocks(x+1,y,z,x+1,y+6,z,35)
    mc.setBlocks(x-1,y+6,z,x+3,y+6,z,35)

def j (x,y,z):
    mc.setBlocks(x+1,y+1,z,x+1,y+6,z,35)
    mc.setBlocks(x,y+6,z,x+2,y+6,z,35)
    mc.setBlocks(x,y,z,x-1,y,z,35)
    mc.setBlock(x-2,y+1,z,35)



j (0,0,0)
