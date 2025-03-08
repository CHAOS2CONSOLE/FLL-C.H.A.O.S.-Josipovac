from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task
# from colors import bcolors

hub = PrimeHub()

# https://www.flltournament.com/Scoresheet.aspx?CID=1070

#region drivebase
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

robot = DriveBase(left_motor, right_motor, 62.4, 119)
robot.use_gyro(False)
robot.settings(600, 500)
#endregion

#region ruke
left_hand = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_hand = Motor(Port.A)

# left_hand.run_target(800, 0, wait=False)
# right_hand.run_target(800, 0)
#endregion

#region misc
def gumb() -> None:
    robot.use_gyro(False)
    while len(hub.buttons.pressed()) < 1: wait(10)
    wait(500)
    robot.use_gyro(True)
#endregion

#region glavne func

def f1_cool() -> None:
    robot.settings(turn_acceleration=300, turn_rate=400)
    robot.straight(390)
    robot.turn(15+2)
    robot.straight(90)
    right_hand.run_target(800, 80)
    robot.straight(-10)
    robot.turn(45-2)
    right_hand.run_target(800, 20, wait=False)
    robot.straight(-80)
    right_hand.run_target(800, 90, wait=False)
    robot.turn(-60+10)
    # robot.settings(turn_acceleration=500, turn_rate=600)
    robot.straight(220)
    robot.turn(30)
    robot.straight(70)
    right_hand.run_target(1000, -10)
    robot.turn(-200)
    robot.straight(350)
    robot.turn(-70)
    right_hand.run_target(800, 90, wait=False)
    wait(100)
    robot.straight(-300)
    robot.straight(500)
    # robot.straight(-200)

    return
    # robot.turn(-180-30)
    robot.straight(300)
    robot.turn(-90)
    robot.straight(-200)
    robot.drive(1000, 0)
    wait(1500)
    robot.stop()

def f2_izguraj() -> None:
    left_hand.run_target(800, 220, wait=False)
    robot.settings(turn_acceleration=300, turn_rate=400)
    robot.straight(100)
    robot.turn(-54)
    robot.straight(650)
    robot.turn(45)
    right_hand.run_target(1000, 200)
    robot.turn(140)
    robot.straight(-400)

def f3_podigni_oba() -> None:
    robot.turn(-100)
    dist = 80
    robot.straight(-dist)
    robot.straight(dist)
    robot.turn(15)
    left_hand.run_target(800, 60, wait=False)
    robot.straight(100)
    # robot.turn(-19)
    left_hand.run_target(1000, 180)
    wait(500)
    robot.straight(-100)
    robot.turn(-50)
    right_hand.run_target(800, 90)
    robot.straight(70)
    right_hand.run_target(1000, 190)
    robot.straight(-30)

def f4_kupi_namjernice() -> None:
    robot.settings(turn_rate=400, turn_acceleration=300)
    robot.turn(-95) # -86 = -90 orijentacija
    right_hand.run_target(800, 0)
    robot.straight(400)
    robot.turn(-65)
    # robot.straight(-100)
    # robot.turn(-20)
    robot.straight(600)

def f5_cvijece() -> None:
    robot.straight(50)
    robot.turn(10)
    robot.straight(690)
    robot.turn(-100) 
    robot.straight(200)
    right_hand.run_target(250, 90)
    robot.turn(10)
    right_hand.run_target(100, 40, wait=False)
    robot.straight(-175)
    robot.turn(80)
    robot.straight(50)
    right_hand.run_target(800, 10)
    robot.straight(-100)
    robot.turn(-60)
    robot.straight(200)
    

    return
    right_hand.run_target(800, 60, wait=False)

    right_hand.run_target(800, 80, wait=False)
    robot.straight(165)
    right_hand.run_target(1000, 120)
    robot.straight(-175)
    robot.turn(90)
    right_hand.run_target(800, 105, wait=False)
    robot.straight(60)
    right_hand.run_target(800, 75, wait=False)
    robot.straight(-100)
    robot.turn(-45)
    robot.straight(170)
    left_hand.run_target(1000, 0, then=Stop.NONE)
    wait(300)
    left_hand.stop()
    right_hand.run_target(800, 120)
    robot.turn(45)
    left_hand.run_target(800, 60, wait=False)
    robot.turn(50)
    robot.straight(10)
    left_hand.run(1000)
    wait(400)
    left_hand.stop()
    robot.turn(-30)
    robot.straight(-800)

def f6_arrr_brod() -> None:
    # left_hand.run_until_stalled(-300, Stop.COAST_SMART, duty_limit=20)
    # left_hand.run_target(800, left_hand.angle()+40)
    # robot.straight(440)
    # robot.turn(90)
    # robot.settings(straight_speed=300)
    # robot.straight(240)
    # robot.straight(-20)
    # robot.turn(145)
    # robot.settings(straight_speed=600)
    # robot.straight(500)
    robot.straight(580)
    robot.turn(90)
    robot.settings(straight_speed=300)
    robot.straight(180)
    robot.straight(-270)
    robot.turn(90)
    robot.settings(straight_speed=600)
    robot.straight(430)

def f7_arrr_brod() -> None:
    right_hand.run_target(500, 180)
    hub.speaker.beep()
    gumb()
    hub.speaker.beep()
    robot.straight(980)
    robot.straight(-400)
    # robot.settings(turn_acceleration=700, turn_rate=800)
    # left_hand.run_target(800, 80)
    # robot.straight(190)
    # left_hand.run_target(800, 25)
    # robot.straight(80)
    # robot.turn(-180)
    # robot.turn(30)
    # left_hand.run_target(800, 110)
    # robot.turn(-30)
    # robot.straight(200)
    # gumb()
    # robot.straight(500)
    # robot.straight(-190)
    # left_hand.run_target(800, 30)
    # robot.straight(190)
    # robot.turn(35)
    # robot.straight(80)
    # robot.turn(-25)
    # robot.curve(radius=1000, angle=-10)
    # robot.straight(110)
    # robot.turn(20)
    # robot.straight(-30)
    # left_hand.run_target(800, 110)
    # robot.turn(-20)
    # robot.straight(-250)
    # robot.turn(35)
    # robot.straight(-150)
    # robot.turn(-45)
    # robot.straight(-550)
    # robot.turn(45)

def f8_morski_pas_posta():
    robot.straight(100)
    robot.turn(-111.5)
    robot.straight(-780)
    robot.straight(790)

def f9_koralji() -> None:
    robot.settings(100, 50)
    robot.straight(-100)
    robot.straight(100)
    robot.settings(600, 500)

def f10_koraljno_drvce() -> None:
    left_hand.run_target(800, 25)
    robot.straight(240)
    left_hand.run(-41)
    robot.drive(130, 0)
    wait(1800)
    left_hand.run_target(800, left_hand.angle()+25)
    robot.straight(-470)
    gumb()
#endregion



def generate(x, n) -> list:
    l = [i for i in range(x, n+1, 1)]
    l.append('X')
    l.extend([i for i in range(1, x, 1)])
    return l

async def __postavi_ruke(speed, duty_limit):
    await multitask(
        left_hand.run_until_stalled(speed, then=Stop.HOLD, duty_limit=duty_limit),
        right_hand.run_until_stalled(speed, then=Stop.HOLD, duty_limit=duty_limit)
    )

def postavi_ruke(speed=500, duty_limit=30):
    run_task(
        __postavi_ruke(-speed, duty_limit)
    )


def main() -> None:
    x = 3
    N = 8

    while True:
        robot.use_gyro(False)
        left_hand.run_target(800, 0, wait=False)
        right_hand.run_target(800, 0)
        num = hub_menu(*generate(x, N))
        start:StopWatch = StopWatch()
        # postavi_ruke()
        if type(num) == int:
            if num == N: x = N
            else: x = num+1
        hub.display.off()
        robot.use_gyro(True)
        try:
            if num == 1:
                left_hand.run_target(800, 100, wait=False)
                f1_cool()
            elif num == 2:
                left_hand.run_target(800, 100, wait=False)
                f2_izguraj()
                f3_podigni_oba()
                f4_kupi_namjernice()
            elif num == 3:
                left_hand.run_target(800, 200, wait=False)
                right_hand.run_target(800, 80, wait=False)
                gumb()
                right_hand.run_target(800, 10, wait=False)
                f5_cvijece()
            elif num == 4:
                f6_arrr_brod()
            elif num == 5:
                f7_arrr_brod()
            elif num == 6:
                f8_morski_pas_posta()
            elif num == 7:
                f9_koralji()
            elif num == 8:
                f10_koraljno_drvce()
            else:
                break
        finally:
            if type(num) != int:
                print(f"The time it took to do mission num. {num} was {start.time()/1000}")
        
        


# region battery
battery = hub.battery.voltage()
if battery <= 7650:
    # print(bcolors.FAIL + bcolors.BOLD, sep="", end="")
    print("----------------------------------------------------")
    print(f" HEY TI, DA TI KOIJ PROGRAMIRA, ROBOT JE PRAZAN!!! (voltage {battery})")
    print("----------------------------------------------------")
    # print(bcolors.HEADER + bcolors.ENDC)
    for _ in range(3):
        hub.speaker.beep(1000, 200)
        wait(100)
else:
    print(f"The voltage is {battery}")
#endregion

#region start up the robot
time = StopWatch()

try:
    main()
finally:
    left_hand.run_target(800, 0, wait=False)
    right_hand.run_target(800, 0)
    while not (left_hand.done() or right_hand.done()): wait(10)
    print(f"The time is {time.time()/1000}", "\n")
#endregion