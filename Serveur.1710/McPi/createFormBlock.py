import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time

#connect to minecraft
mc = minecraft.Minecraft.create()

#get players position
playerPos = mc.player.getTilePos()

#create minecraft drawing object
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

# Draw some lines
mc.postToChat("Draw lines")
time.sleep(5)
# pass 2 sets of co-ordinates and a block
#  - the start of the line and the end of the line
mcdrawing.drawLine(playerPos.x, playerPos.y + 2, playerPos.z,
                   playerPos.x + 10, playerPos.y + 2, playerPos.z,
                   block.STONE)
time.sleep(1)
mcdrawing.drawLine(playerPos.x, playerPos.y + 2, playerPos.z,
                   playerPos.x, playerPos.y + 2, playerPos.z + 10,
                   block.STONE)
time.sleep(1)
mcdrawing.drawLine(playerPos.x, playerPos.y + 2, playerPos.z,
                   playerPos.x - 10, playerPos.y + 2, playerPos.z,
                   block.STONE)
time.sleep(1)
mcdrawing.drawLine(playerPos.x, playerPos.y + 2, playerPos.z,
                   playerPos.x, playerPos.y + 2, playerPos.z - 10,
                   block.STONE)
time.sleep(1)
mcdrawing.drawLine(playerPos.x, playerPos.y + 2, playerPos.z,
                   playerPos.x, playerPos.y + 10, playerPos.z,
                   block.STONE)
time.sleep(1)
mcdrawing.drawLine(playerPos.x, playerPos.y + 2, playerPos.z,
                   playerPos.x + 10, playerPos.y + 10, playerPos.z - 10,
                   block.STONE)
time.sleep(1)
mcdrawing.drawLine(playerPos.x, playerPos.y + 2, playerPos.z,
                   playerPos.x - 10, playerPos.y + 10, playerPos.z - 10,
                   block.STONE)
time.sleep(5)

# Draw a sphere
mc.postToChat("Draw a sphere")
time.sleep(2)
#pass the middle coordinate and a radius
mcdrawing.drawSphere(playerPos.x, playerPos.y + 25, playerPos.z, 5, block.DIAMOND_BLOCK.id)
time.sleep(5)

# Draw some circles
mc.postToChat("Draw some circles")
time.sleep(2)
#pass the middle coordinate and a radius
mcdrawing.drawCircle(playerPos.x, playerPos.y + 25, playerPos.z, 8,block.WOOD.id)
time.sleep(1)
mcdrawing.drawCircle(playerPos.x, playerPos.y + 25, playerPos.z, 11,block.WOOD.id)
time.sleep(5)

# Draw some shapes
#  - by passing a list of points, which then get joined together
mc.postToChat("Draw some shapes")
time.sleep(2)
# some points
shapePoints = []
shapePoints.append(minecraft.Vec3(playerPos.x + 1, playerPos.y + 27, playerPos.z + 10))
shapePoints.append(minecraft.Vec3(playerPos.x + 5, playerPos.y + 36 , playerPos.z + 10))
shapePoints.append(minecraft.Vec3(playerPos.x + 10, playerPos.y + 26, playerPos.z + 10))
# draw the points together and True fills it in
mcdrawing.drawFace(shapePoints, True, block.GOLD_BLOCK.id)

time.sleep(2)
#some points
shapePoints = []
shapePoints.append(minecraft.Vec3(playerPos.x, playerPos.y + 26, playerPos.z + 10))
shapePoints.append(minecraft.Vec3(playerPos.x + 11, playerPos.y + 26 , playerPos.z + 10))
shapePoints.append(minecraft.Vec3(playerPos.x + 11, playerPos.y + 37, playerPos.z + 10))
shapePoints.append(minecraft.Vec3(playerPos.x + 0, playerPos.y + 37, playerPos.z + 10))
# draw the points together and False, DONT fill it in
mcdrawing.drawFace(shapePoints, False, block.IRON_BLOCK.id)

# www.stuffaboutcode.com
