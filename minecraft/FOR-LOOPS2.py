import mcpi.minecraft as minecraft, time, random
mc = minecraft.Minecraft.create()

mc.setBlocks(-30,-5,-30,30,30,30,0)

#loops through 0 to 14 using these for the y co ordinate and the wool color.
for b in range(15):
    mc.postToChat(b)
    mc.setBlock(0,b,0,35,b)
    time.sleep(2)
