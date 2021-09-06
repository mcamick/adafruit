from adafruit_circuitplayground.express import cpx

while True:  
  if cpx.button_a:
     #add file to circuit drive and then list file name here
     cpx.play_file("game_over.wav")
  if cpx.button_b:
     cpx.play_file("oops.wav")
  if cpx.switch:
    cpx.pixels.fill( (0, 0, 255) )
