import easygopigo3 as easy
import time
time.sleep(10)

my_gopigo = easy.EasyGoPiGo3()


print("freaky turn")
my_gopigo.orbit(360,50)
my_gopigo.turn_degrees(180)


print("freaky square")
lenght=30
for i in range(4):
    my_gopigo.drive_cm(25)
    my_gopigo.turn_degrees(90)
    
print("faire un 8")

my_gopigo.orbit(-270,30)
my_gopigo.drive_cm(60)
my_gopigo.orbit(-270,30)
my_gopigo.drive_cm(60)


print("tu vas te calmer")
my_gopigo.stop()


     



