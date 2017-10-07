import Adafruit_BBIO.PWM as PWM
import sys

red = "P8_13"
green = "P8_19"
blue = "P9_42"

PWM.start(red, 0)
PWM.start(blue, 0)
PWM.start(green, 0)

def acionar_cor_led(nivel_vermelho, nivel_verde, nivel_azul):
	PWM.set_duty_cycle(red, nivel_vermelho)
	PWM.set_duty_cycle(green, nivel_verde)
	PWM.set_duty_cycle(blue, nivel_azul)

if __name__ == "__main__":
	r = int(sys.argv[1])
	g = int(sys.argv[2])
	b = int(sys.argv[3])
	acionar_cor_led(r, g, b)