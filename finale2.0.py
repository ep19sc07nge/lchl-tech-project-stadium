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
    global MOTORS_ARE_ACTIVATED, MOTORS
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
    global MOTORS_ARE_ACTIVATED, MOTORS
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
    side_switch = get_current_switch_value(DigitalPin.P1)
    # 0 means pressed.
    is_opened = (side_switch == 0)
    open_the_roof(
        light_level=get_current_light_level(),
        roof_is_opened=is_opened
    )
input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_b():
    """roof closing?"""
    middle_switch = get_current_switch_value(DigitalPin.P0)
    is_closed = (middle_switch == 0)
    close_the_roof(
        light_level=get_current_light_level(),
        roof_is_closed=is_closed
    )
input.on_button_pressed(Button.B, on_button_pressed_b)


def on_button_pressed_ab():
    complete_shutdown()
input.on_button_pressed(Button.AB, on_button_pressed_ab)


def open_the_roof(roof_is_opened, light_level):
    """Calling this method when the light
    level hits a certain threshold.

    Opening the roof till it'll reach the side switch.
    """
    global MOTORS_ARE_ACTIVATED

    # if roof is opened we need to deactivate
    # the motors and display current level of light.
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

    # additional stuff.
    display_info(info="OPENING")
    play_music()


def close_the_roof(roof_is_closed, light_level):
    """Calling this method when the light
    level hits a certain threshold.

    Closing the roof till it will reach a limit switch.
    """
    global MOTORS_ARE_ACTIVATED

    # if roof is closed we need to deactivate
    # the motors and display current level of light.
    if roof_is_closed:
        if MOTORS_ARE_ACTIVATED:
            stop_motors()
        display_info(info=str(light_level))
        pass

    # if the roof is still somewhere in the middle
    # then we have to make sure our motors are active.
    activate_motors(
        direction=Kitronik_Robotics_Board.MotorDirection.REVERSE
    )

    # additional stuff.
    display_info(info="CLOSING")
    play_music()


def get_current_switch_value(switch_pin):
    return int(pins.digital_read_pin(switch_pin))


def get_current_light_level():
    return int(input.light_level())


def on_forever():
    # light level indicator
    light_level = get_current_light_level()

    # two limit switches.
    # for now, I don't know how to describe
    # them in the code.
    middle_switch = get_current_switch_value(DigitalPin.P0)
    side_switch = get_current_switch_value(DigitalPin.P1)

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
    basic.pause(59)

basic.forever(on_forever)
