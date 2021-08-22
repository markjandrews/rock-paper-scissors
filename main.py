hand = 0

def on_gesture_shake():
    global hand
    for index in range(3):
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        basic.show_number(3 - index)
    music.play_tone(392, music.beat(BeatFraction.WHOLE))

    hand = randint(1, 3)
    if hand == 1:
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
    elif hand == 2:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
    else:
        basic.show_leds("""
            # # . . #
                        # # . # .
                        . . # . .
                        # # . # .
                        # # . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
