input.onButtonPressed(Button.A, function on_button_pressed_a() {
    open_the_gate()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    Kitronik_Robotics_Board.allOff()
    basic.showString("TURINING OFF")
})
function close_the_gate() {
    music.play(music.stringPlayable("C5 C5 C5 - - C5 C5 C5 ", 299), music.PlaybackMode.InBackground)
    basic.showString("CLOSING")
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor1, Kitronik_Robotics_Board.MotorDirection.Reverse, 41)
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor2, Kitronik_Robotics_Board.MotorDirection.Reverse, 41)
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor3, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor4, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
    basic.pause(200)
    Kitronik_Robotics_Board.motorOff(Kitronik_Robotics_Board.Motors.Motor1)
    Kitronik_Robotics_Board.motorOff(Kitronik_Robotics_Board.Motors.Motor2)
    Kitronik_Robotics_Board.motorOff(Kitronik_Robotics_Board.Motors.Motor3)
    Kitronik_Robotics_Board.motorOff(Kitronik_Robotics_Board.Motors.Motor4)
    basic.clearScreen()
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    close_the_gate()
})
function open_the_gate() {
    music.play(music.stringPlayable("C5 C5 C5 - - C5 C5 C5 ", 294), music.PlaybackMode.InBackground)
    basic.showString("OPENING ")
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor1, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor2, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor3, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor4, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
    basic.pause(2000)
    Kitronik_Robotics_Board.motorOff(Kitronik_Robotics_Board.Motors.Motor1)
    Kitronik_Robotics_Board.motorOff(Kitronik_Robotics_Board.Motors.Motor2)
    Kitronik_Robotics_Board.motorOff(Kitronik_Robotics_Board.Motors.Motor3)
    Kitronik_Robotics_Board.motorOff(Kitronik_Robotics_Board.Motors.Motor4)
    basic.clearScreen()
}

while (true) {
    basic.showNumber(input.lightLevel())
    if (input.lightLevel() > 160) {
        open_the_gate()
    } else {
        close_the_gate()
    }
    
}
let MOTORS = [Kitronik_Robotics_Board.Motors.Motor1, Kitronik_Robotics_Board.Motors.Motor2, Kitronik_Robotics_Board.Motors.Motor3, Kitronik_Robotics_Board.Motors.Motor4]
let LIGHT_THRESHOLD = 159
let MOTOR_SPEED = 59
let IS_PRESSED = 0
let MOTORS_ARE_ACTIVATED = false
let MUSIC_IS_PLAYING = false
function activate_motors(direction: number) {
    
    if (MOTORS_ARE_ACTIVATED) {
        throw_an_error("motors were already activated!")
    }
    
    for (let motor of MOTORS) {
        Kitronik_Robotics_Board.motorOn(motor, direction, MOTOR_SPEED)
    }
}

function stop_motors() {
    
    if (MOTORS_ARE_ACTIVATED === false) {
        throw_an_error("motors weren't activated yet!")
    }
    
    for (let motor of MOTORS) {
        Kitronik_Robotics_Board.motorOff(motor)
    }
}

function display_info(info: string) {
    basic.showString(info)
}

function play_music() {
    
    if (MUSIC_IS_PLAYING) {
        
    }
    
    music.play(music.stringPlayable("C5 C5 C5 - - C5 C5 C5 ", 294), music.PlaybackMode.InBackground)
}

function open_the_roof(roof_is_opened: any, light_level: any) {
    if (roof_is_opened) {
        if (MOTORS_ARE_ACTIVATED) {
            stop_motors()
        }
        
        display_info("" + light_level)
        
    }
    
    activate_motors(Kitronik_Robotics_Board.MotorDirection.Forward)
}

function close_the_roof(roof_is_closed: any, light_level: any) {
    if (roof_is_closed) {
        if (MOTORS_ARE_ACTIVATED) {
            stop_motors()
            display_info("" + light_level)
        }
        
        
    }
    
    activate_motors(Kitronik_Robotics_Board.MotorDirection.Reverse)
}

function throw_an_error(message: string) {
    basic.showString(message)
}

function complete_shutdown() {
    display_info("shutting down!")
    Kitronik_Robotics_Board.allOff()
}

//  give me a break
//  sleep(59)
basic.forever(function on_forever() {
    //  light level indicator
    let light_level = Math.trunc(input.lightLevel())
    //  two limit switches
    //  for now I don't know how to describe
    //  them in the code.
    let middle_switch = null
    let side_switch = null
    //  supposed to be True or False
    //  depending on whether the roof is opened or not.
    let roof_is_opened = side_switch == 0 && middle_switch != 0
    // logic of the program
    if (light_level > LIGHT_THRESHOLD) {
        open_the_roof(roof_is_opened, light_level)
    } else if (light_level < LIGHT_THRESHOLD) {
        close_the_roof(roof_is_opened, light_level)
    } else {
        throw_an_error("light indicator does not work!")
    }
    
})
