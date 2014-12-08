import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

#move player close to origin
mc.player.setPos(1,50,6)

black=7
red=14
orange=1
green=5

#setup empty lights
mc.setBlock(0,0,0,35,black)
mc.setBlock(0,51,0,35,black)
mc.setBlock(0,52,0,35,black)
mc.setBlock(0,53,0,35,black)
mc.setBlock(0,54,0,35,black)
mc.setBlock(0,55,0,35,black)

while True:
  mc.setBlock(0,55,0,35,red)
  mc.setBlock(0,54,0,35,black)
  mc.setBlock(0,53,0,35,black)
  time.sleep(10)
  mc.setBlock(0,55,0,35,red)
  mc.setBlock(0,54,0,35,orange)
  mc.setBlock(0,53,0,35,black)
  time.sleep(3)
  mc.setBlock(0,55,0,35,black)
  mc.setBlock(0,54,0,35,black)
  mc.setBlock(0,53,0,35,green)
  time.sleep(10)
  mc.setBlock(0,55,0,35,black)
  mc.setBlock(0,54,0,35,orange)
  mc.setBlock(0,53,0,35,black)
  time.sleep(3)
