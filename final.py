import cv2
import sys
import numpy as np
import time
import thread
import Adafruit_BBIO.PWM as PWM

#configuracao foto
CV_CAP_PROP_FRAME_WIDTH = 3
CV_CAP_PROP_FRAME_HEIGHT = 4
LARGURA_FOTO = 320
ALTURA_FOTO = 240

#pixels analisados pela foto
T_FOTO_INICIAL = 55
T_FOTO_FINAL = 85
L_FOTO_INICIAL = 120
L_FOTO_FINAL = 150

#pinos de sinal dos motores
#valores: 6, 4.5, 3
servo_pin_objetos="P9_14"
#valores: 4.6, 6, 7.5, 9
servo_pin_copos="P9_21"

#pinos para o LED
led_vermelho = "P8_13"
led_verde = "P8_19"
led_azul = "P9_42"

#nivel para LED
NIVEL_MINIMO = 0
NIVEL_MAXIMO = 100

#posicoes para os motores
POSICAO_INICIAL_SERVO_OBJETOS = 6
POSICAO_TIRAR_FOTO = 4.5
POSICAO_ESCORREGADOR = 3
POSICAO_INICIAL_SERVO_COPOS = 4.6

#posicoes para os copos
POSICAO_COPO_1 = 4.6
POSICAO_COPO_2 = 6
POSICAO_COPO_3 = 7.5
POSICAO_COPO_4 = 9

#numero das cores
VERMELHO = 1
VERDE = 2
AZUL = 3
MAGENTA = 4

#numero dos copos (de acordo com a cor recebida como parametro)
COPO_1 = VERMELHO
COPO_2 = VERDE
COPO_3 = AZUL
COPO_4 = MAGENTA

#numero de objetos separados
NUMERO_OBJETOS = 0

def analisa_parametros(p1, p2, p3, p4, p5):
	global COPO_1
	global COPO_2
	global COPO_3
	global COPO_4
	global NUMERO_OBJETOS
	COPO_1 = p1
	COPO_2 = p2
	COPO_3 = p3
	COPO_4 = p4
	NUMERO_OBJETOS = p5
	
def posicionar_motor(servo, ciclo):
    PWM.set_duty_cycle(servo, ciclo)
	
def tirar_foto():
    capture = cv2.VideoCapture(0)

    capture.set(CV_CAP_PROP_FRAME_WIDTH, LARGURA_FOTO)
    capture.set(CV_CAP_PROP_FRAME_HEIGHT, ALTURA_FOTO)

    ret, frame = capture.read()

    cv2.imwrite('foto.jpg', frame)

    capture.release()
    cv2.destroyAllWindows()
	
def analisar_cor_objeto():
	imagem = cv2.imread('foto.jpg')
	
	#[T,L]
	pixel_azul = imagem[T_FOTO_INICIAL:T_FOTO_FINAL,L_FOTO_INICIAL:L_FOTO_FINAL,0]
	pixel_verde = imagem[T_FOTO_INICIAL:T_FOTO_FINAL,L_FOTO_INICIAL:L_FOTO_FINAL,1]
	pixel_vermelho = imagem[T_FOTO_INICIAL:T_FOTO_FINAL,L_FOTO_INICIAL:L_FOTO_FINAL,2]
	
	qtd_linhas = len(pixel_azul)
	qtd_colunas = len(pixel_azul[0])
	
	media_azul = 0
	media_verde = 0
	media_vermelho = 0
	
	for i in range(qtd_linhas):
		for j in range(qtd_colunas):
			media_azul += pixel_azul[i,j]
			media_verde += pixel_verde[i,j]
			media_vermelho += pixel_vermelho[i,j]
			
	if media_azul > media_verde and media_azul > media_vermelho:
		if media_vermelho > media_verde:
			acionar_led(NIVEL_MAXIMO, NIVEL_MINIMO, NIVEL_MAXIMO)
			if COPO_1 == MAGENTA:
				return POSICAO_COPO_1
			elif COPO_2 == MAGENTA:
				return POSICAO_COPO_2
			elif COPO_3 == MAGENTA:
				return POSICAO_COPO_3
			else:
				return POSICAO_COPO_4
		else:
			acionar_led(NIVEL_MINIMO, NIVEL_MINIMO, NIVEL_MAXIMO)
			if COPO_1 == AZUL:
				return POSICAO_COPO_1
			elif COPO_2 == AZUL:
				return POSICAO_COPO_2
			elif COPO_3 == AZUL:
				return POSICAO_COPO_3
			else:
				return POSICAO_COPO_4
	elif media_verde > media_azul and media_verde > media_vermelho:
		acionar_led(NIVEL_MINIMO, NIVEL_MAXIMO, NIVEL_MINIMO)
		if COPO_1 == VERDE:
			return POSICAO_COPO_1
		elif COPO_2 == VERDE:
			return POSICAO_COPO_2
		elif COPO_3 == VERDE:
			return POSICAO_COPO_3
		else:
			return POSICAO_COPO_4
	elif media_vermelho > media_azul and media_vermelho > media_verde:
		acionar_led(NIVEL_MAXIMO, NIVEL_MINIMO, NIVEL_MINIMO)
		if COPO_1 == VERMELHO:
			return POSICAO_COPO_1
		elif COPO_2 == VERMELHO:
			return POSICAO_COPO_2
		elif COPO_3 == VERMELHO:
			return POSICAO_COPO_3
		else:
			return POSICAO_COPO_4
			
def acionar_led(nivel_vermelho, nivel_verde, nivel_azul):
	PWM.set_duty_cycle(led_vermelho, nivel_vermelho)
	PWM.set_duty_cycle(led_verde, nivel_verde)
	PWM.set_duty_cycle(led_azul, nivel_azul)

def main():
	PWM.start(servo_pin_objetos, POSICAO_INICIAL_SERVO_OBJETOS, 50)
	PWM.start(servo_pin_copos, POSICAO_INICIAL_SERVO_COPOS, 50)
	PWM.start(led_vermelho, 0)
	PWM.start(led_verde, 0)
	PWM.start(led_azul, 0)
	
	analisa_parametros(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))

	print ("Copo 1: %d." % (COPO_1))
	print ("Copo 2: %d." % (COPO_2))
	print ("Copo 3: %d." % (COPO_3))
	print ("Copo 4: %d." % (COPO_4))
	print ("Numero de objetos que serao separados: %d." % (NUMERO_OBJETOS))
	
	i = NUMERO_OBJETOS
	
	while(i > 0):
		posicionar_motor(servo_pin_objetos, POSICAO_TIRAR_FOTO)
		tirar_foto()
		posicao_copo = analisar_cor_objeto()
		thread.start_new_thread(posicionar_motor, (servo_pin_copos, posicao_copo, ))
		posicionar_motor(servo_pin_objetos, POSICAO_ESCORREGADOR)
		time.sleep(3)
		posicionar_motor(servo_pin_objetos, POSICAO_INICIAL_SERVO_OBJETOS)
		time.sleep(1)
		i -= 1

if __name__ == '__main__':
    main()