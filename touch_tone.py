from adafruit_circuitplayground.express import cpx

while True:
  if cpx.touch_A1:
    cpx.play_tone(262, 0.5)
  if cpx.touch_A2:
    cpx.play_tone(294, 0.5)
  if cpx.touch_A3:
    cpx.play_tone(330, 0.5)
  if cpx.touch_A4:
    cpx.play_tone(349, 0.5)
  
