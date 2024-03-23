# Main Panoramic camera code

import time
import adafruit_pycamera  # pylint: disable=import-error
import state_machine
import states

pycam = adafruit_pycamera.PyCamera()
pycam.mode = 0  # only mode 0 (JPEG) will work in this example

# User settings - try changing these:
pycam.resolution = 8 # 0-12 preset resolutions:
#                      0: 240x240, 1: 320x240, 2: 640x480, 3: 800x600, 4: 1024x768,
#                      5: 1280x720, 6: 1280x1024, 7: 1600x1200, 8: 1920x1080, 9: 2048x1536,
#                      10: 2560x1440, 11: 2560x1600, 12: 2560x1920
pycam.led_level = 0  # 0-4 preset brightness levels
pycam.led_color = 0  # 0-7  preset colors: 0: white, 1: green, 2: yellow, 3: red,
#                                          4: pink, 5: blue, 6: teal, 7: rainbow
pycam.effect = 0  # 0-7 preset FX: 0: normal, 1: invert, 2: b&w, 3: red,
#                                  4: green, 5: blue, 6: sepia, 7: solarize

print("Panoramic camera ready.")
pycam.tone(800, 0.1)
pycam.tone(1200, 0.05)

machine = state_machine.StateMachine()
machine.register('run', states.RunState)
machine.register('menu', states.MenuState)
machine.register('steps', states.StepsState)
machine.register('start-delay', states.StartDelayState)
machine.register('brightness', states.BrightnessState)


while True:
    pycam.keys_debounce()

    if pycam.card_detect.fell:
        print("SD card removed")
        pycam.unmount_sd_card()
        pycam.display.refresh()
    if pycam.card_detect.rose:
        print("SD card inserted")
        pycam.display_message("Mounting\nSD Card", color=0xFFFFFF)
        for _ in range(3):
            try:
                print("Mounting card")
                pycam.mount_sd_card()
                print("Success!")
                break
            except OSError as e:
                print("Retrying!", e)
                time.sleep(0.5)
        else:
            pycam.display_message("SD Card\nFailed!", color=0xFF0000)
            time.sleep(0.5)
        pycam.display.refresh()


    if pycam.shutter.short_count:
        machine.shutter()
    elif pycam.up.fell:
        machine.up()
    elif pycam.down.fell:
        machine.down()
    elif pycam.left.fell:
        machine.left()
    elif pycam.right.fell:
        machine.right()
    elif pycam.select.fell:
        machine.select()
    elif pycam.ok.fell:
        machine.ok()

    # settings:
    #   number of pics in 360 degrees
    #   delay before starting
    #   pixel ring brightness
    # left/right navigate menu
    # select chooses option
    # up/down change value
    # ok goes back to menu or run mode if in menu

    # if shutter button is short-pressed
    #   play delay start sound
    #   wait for delay
    #   play start sound
    #   for the number of pictures
    #     play shutter sound
    #     take a picture
    #     rotate (360/number of pictures) degrees
    #   rotate back to 0 degrees
    #   play end sound
