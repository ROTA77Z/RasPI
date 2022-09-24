# RasPI
Raspberry Pi Audio/Video Application

Use Raspberry Pi zero for video player with DAC(Pirate Audio).
This section video control trial by python.

On other project use ST7789 for display movie on it.
(Pi4 can it, I trinig it on PiZero)

Pimoroni Audio Dac Shim (PIM542)
If you don't push the board all the way into the pins on the Raspberry Pi, the contact may not work. If you use extension pins, they may not be thick enough to cause contact problems. (I had a hard time with that)
I'm stacking Audio Dac Shim(line) on Raspberry Pi Zero W with Pirate Audio Amp. So, it makes 4 speaker system.

RaspBerryPi Zero W --- Pirate Aucio 3W Amp     --- 2x 8 ohm speaker

                    +- Audio Dac Shim Line out --- USB speaker

Pimoroni Audio AMP Shim (PIM541)
This board is more severe, and thin GPIO pins don't make good contact. It seems that if it is not a thick pin like Pimoroni's hammered GPIO pin, it will not make contact even if it is pushed all the way to the root.　Therefore, I was able to purchase it, but I have not tried it.
