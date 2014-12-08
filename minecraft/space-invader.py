import mcpi.minecraft as minecraft, time, random
mc = minecraft.Minecraft.create()

#mc.setBlocks(-50,-1,-50,50,65,50,0)

for block in (3,9):
    mc.setBlock(block,8,0,22)

##for block in (4,8):
##    mc.setBlock(block,7,0,35,random.randint(1,16))
##
##for block in (3,4,5,6,7,8,9):
##    mc.setBlock(block,6,0,35,random.randint(1,16))
##
##for block in (2,3,5,6,7,9,10):
##    mc.setBlock(block,5,0,35,random.randint(1,16))
##
##for block in (1,2,3,4,5,6,7,8,9,10,11):
##    mc.setBlock(block,4,0,35,random.randint(1,16))
##
##for block in (1,3,4,5,6,7,8,10):
##    mc.setBlock(block,3,0,35,random.randint(1,16))
##
##for block in (1,3,8,10):
##    mc.setBlock(block,2,0,35,random.randint(1,16))
##
##for block in (4,5,7,8):
##    mc.setBlock(block,1,0,35,random.randint(1,16))
