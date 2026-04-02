from microbit import sleep


def on_button_pressed_a():
    open_the_gate()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    Kitronik_Robotics_Board.all_off()
    basic.show_string("TURINING OFF")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def close_the_gate():
    music.play(music.string_playable("C5 C5 C5 - - C5 C5 C5 ", 299),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_string("CLOSING")
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.REVERSE,
        41)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR2,
        Kitronik_Robotics_Board.MotorDirection.REVERSE,
        41)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR3,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        50)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        50)
    basic.pause(200)
    Kitronik_Robotics_Board.motor_off(Kitronik_Robotics_Board.Motors.MOTOR1)
    Kitronik_Robotics_Board.motor_off(Kitronik_Robotics_Board.Motors.MOTOR2)
    Kitronik_Robotics_Board.motor_off(Kitronik_Robotics_Board.Motors.MOTOR3)
    Kitronik_Robotics_Board.motor_off(Kitronik_Robotics_Board.Motors.MOTOR4)
    basic.clear_screen()

def on_button_pressed_b():
    close_the_gate()
input.on_button_pressed(Button.B, on_button_pressed_b)

def open_the_gate():
    music.play(music.string_playable("C5 C5 C5 - - C5 C5 C5 ", 294),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_string("OPENING ")
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        50)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR2,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        50)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR3,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        50)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        50)
    basic.pause(2000)
    Kitronik_Robotics_Board.motor_off(Kitronik_Robotics_Board.Motors.MOTOR1)
    Kitronik_Robotics_Board.motor_off(Kitronik_Robotics_Board.Motors.MOTOR2)
    Kitronik_Robotics_Board.motor_off(Kitronik_Robotics_Board.Motors.MOTOR3)
    Kitronik_Robotics_Board.motor_off(Kitronik_Robotics_Board.Motors.MOTOR4)
    basic.clear_screen()
while True:
    basic.show_number(input.light_level())
    if input.light_level() > 160:
        open_the_gate()
    else:
        close_the_gate()






MOTORS = [
    Kitronik_Robotics_Board.Motors.MOTOR1,
    Kitronik_Robotics_Board.Motors.MOTOR2,
    Kitronik_Robotics_Board.Motors.MOTOR3,
    Kitronik_Robotics_Board.Motors.MOTOR4
]
LIGHT_THRESHOLD = 159
MOTOR_SPEED = 59
MOTORS_ARE_ACTIVATED = False


def activate_motors(direction):
    """Activate motors according to direction."""
    global MOTORS_ARE_ACTIVATED
    if MOTORS_ARE_ACTIVATED:
        throw_an_error(
            message="motors were already activated!"
        )
    for motor in MOTORS:
        Kitronik_Robotics_Board.motor_on(
            motor,
            direction,
            MOTOR_SPEED
        )
    MOTORS_ARE_ACTIVATED = True


def stop_motors():
    """Stop motors according to direction."""
    global MOTORS_ARE_ACTIVATED
    if not MOTORS_ARE_ACTIVATED:
        throw_an_error(
            message="motors weren't activated yet!"
        )
    for motor in MOTORS:
        Kitronik_Robotics_Board.motor_off(motor)
    MOTORS_ARE_ACTIVATED = False


def display_info(info):
    """Displaying any desired message on the microbit.

    :param info: light level indicator on the microbit.
    """
    basic.show_string(info)


def play_music():
    """Using buzzer to create a sound.

    Usually only during opening or closing the gates.
    """
    music.play(
        music.string_playable("C5 C5 C5 - - C5 C5 C5 ", 294),
        music.PlaybackMode.IN_BACKGROUND
    )


def throw_an_error(message):
    """idk"""
    basic.show_string(message)


def complete_shutdown():
    """wefdf"""
    display_info(info="shutting down!")
    Kitronik_Robotics_Board.all_off()


def on_button_pressed_a():
    """roof opening? idk"""
    # I don't think it's a proper way of doing it.
    side_switch = None
    is_opened = (side_switch == 0)
    open_the_roof(light_level=None, roof_is_opened=is_opened)
input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_b():
    """roof closing?"""
    middle_switch = None
    is_closed = (middle_switch == 0)
    # I don't think it's a proper way of doing it.
    close_the_roof(light_level=None, roof_is_closed=is_closed)
input.on_button_pressed(Button.B, on_button_pressed_b)


def on_button_pressed_ab():
    complete_shutdown()
input.on_button_pressed(Button.AB, on_button_pressed_ab)


def open_the_roof(roof_is_opened, light_level):
    """Calling this method when the light
    level hits a certain threshold.

    Opening the roof till it'll reach the side switch.
    """
    # define our global variable so we could
    # access its value and change it from within
    # this method
    global MOTORS_ARE_ACTIVATED

    # if the roof is already opened or closed
    # we need to deactivate our motors and
    # display current level of light.
    global MOTORS_ARE_ACTIVATED
    if roof_is_opened:
        if MOTORS_ARE_ACTIVATED:
            stop_motors()
        display_info(info=str(light_level))
        pass

    # if the roof is still somewhere in the middle
    # then we have to make sure our motors are active.
    activate_motors(
        direction=Kitronik_Robotics_Board.MotorDirection.FORWARD
    )

    # make a sound.
    play_music()

def close_the_roof(roof_is_closed, light_level):
    """Calling this method when the light
    level hits a certain threshold.

    Closing the roof till it will reach a limit switch.
    """
    # define our global variable so we could
    # access its value and change it from within
    # this method
    global MOTORS_ARE_ACTIVATED

    # if the roof is already opened or closed
    # we need to deactivate our motors and
    # display current level of light.
    if roof_is_closed:
        if MOTORS_ARE_ACTIVATED:
            stop_motors()
        display_info(info=str(light_level))
        pass

    # if the roof is still somewhere in the middle
    # then we have to make sure our motors are active.
    activate_motors(direction=Kitronik_Robotics_Board.MotorDirection.REVERSE)

    # make a sound.
    play_music()


def on_forever():
    # light level indicator
    light_level = int(input.light_level())

    # two limit switches.
    # for now, I don't know how to describe
    # them in the code.
    middle_switch = None
    side_switch = None

    # bla bla bla
    if light_level > LIGHT_THRESHOLD:
        # checking whether side switch is pressed.
        roof_is_opened = (side_switch == 0 and middle_switch != 0)
        open_the_roof(
            roof_is_opened=roof_is_opened,
            light_level=light_level,
        )
    elif light_level < LIGHT_THRESHOLD:
        # checking whether middle switch is pressed.
        roof_is_closed = (side_switch != 0 and middle_switch == 0)
        close_the_roof(
            roof_is_closed=roof_is_closed,
            light_level=light_level,
        )
    else:
        throw_an_error(
            message="light indicator does not work!"
        )

    # give me a break
    # sleep(59)

basic.forever(on_forever)