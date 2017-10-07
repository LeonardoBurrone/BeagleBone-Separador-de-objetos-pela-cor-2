<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width" />
	<title> Robo </title>
	<link rel="stylesheet" type="text/css" href="css/robo.css">
	<!-- <script type="text/javascript" src="js/functions_led.js"></script> -->
</head>
<body>
	<div class="divMain">
		<form class="form1" action="robo.php" method="get">
			<div class="div1">
				<table>
					<tr>
						<td>
							<center>
								<p class="nome_robo">Robô Gambi</p>
							</center>
						</td>
					</tr>
				</table>
			</div>
			<div class="div2">
				<table>
					<tr>
						<td>
							<center>
								<p class="enunciado">Escolha a cor de cada copo para Robô. O Robô separa 10 objetos. Após a escolha dos copos, espere até a separação dos objetos terminar.</p>
							</center>
						</td>
					</tr>
				</table>
			</div>
			<div class="div3">
				<table>
					<tr>
						<td>
							<center>
								<b>Copo 1:</b>
								<input name="radio1" type="radio" value="1">Vermelho
								<input name="radio1" type="radio" value="2">Verde
								<input name="radio1" type="radio" value="3">Azul
								<input name="radio1" type="radio" value="4">Magenta
							</center>
						</td>
						<td>
							<center>
								<b>Copo 2:</b>
								<input name="radio2" type="radio" value="1">Vermelho
								<input name="radio2" type="radio" value="2">Verde
								<input name="radio2" type="radio" value="3">Azul
								<input name="radio2" type="radio" value="4">Magenta
							</center>
						</td>
					</tr>
				</table>
			</div>
			<div class="div4">
				<table>
					<tr>
						<td>
							<center>
								<b>Copo 3:</b>
								<input name="radio3" type="radio" value="1">Vermelho
								<input name="radio3" type="radio" value="2">Verde
								<input name="radio3" type="radio" value="3">Azul
								<input name="radio3" type="radio" value="4">Magenta
							</center>
						</td>
						<td>
							<center>
								<b>Copo 4:</b>
								<input name="radio4" type="radio" value="1">Vermelho
								<input name="radio4" type="radio" value="2">Verde
								<input name="radio4" type="radio" value="3">Azul
								<input name="radio4" type="radio" value="4">Magenta
							</center>
						</td>
					</tr>
				</table>
			</div>
			<div class="div5">
					<table>
					<tr>
						<td>
							<center>
								Quantidade de objetos que serão separados: <input name="objetos" type="text">
							</center>
						</td>
					</tr>
				</table>
			</div>
			<div class="div6">
					<table>
					<tr>
						<td>
							<center>
								<input type="submit" value="Iniciar Robo" name="robo">
							</center>
						</td>
						<td>
							<center>
								<a href="principal.php" target="_blank"> < Voltar à Página Principal > </a>
							</center>
						</td>
					</tr>
				</table>
			</div>
		</form>
	</div>
	
	<?
	if(isset($_GET["robo"])) {
		if(isset($_GET['radio1']) && isset($_GET['radio2']) && isset($_GET['radio3']) && isset($_GET['radio4']) && !empty($_GET['objetos'])) {
			$copo_1 = $_GET['radio1'];
			$copo_2 = $_GET['radio2'];
			$copo_3 = $_GET['radio3'];
			$copo_4 = $_GET['radio4'];
			$qtd = $_GET['objetos'];
			
			echo "Valores selecionados: $copo_1 $copo_2 $copo_3 $copo_4<br>";
			echo "Quantidade de objetos: $qtd<br>";
			
			if(($copo_1 != $copo_2) && ($copo_1 != $copo_3) && ($copo_1 != $copo_4)) {
				if(($copo_2 != $copo_1) && ($copo_2 != $copo_3) && ($copo_2 != $copo_4)) {
					if(($copo_3 != $copo_1) && ($copo_3 != $copo_2) && ($copo_3 != $copo_4)) {
						if(($copo_4 != $copo_1) && ($copo_4 != $copo_2) && ($copo_4 != $copo_3)) {
							echo "Iniciando robo...<br>";
							exec( "sudo python final.py $copo_1 $copo_2 $copo_3 $copo_4 $qtd" );
						}
						else {
							echo "Não pode haver a mesma cor para copos diferentes!<br>";
						}
					}
					else {
						echo "Não pode haver a mesma cor para copos diferentes!<br>";
					}
				}
				else {
					echo "Não pode haver a mesma cor para copos diferentes!<br>";
				}
			}
			else {
				echo "Não pode haver a mesma cor para copos diferentes!<br>";
			}
		}
		else {
			echo "Selecione uma opção para cada copo!<br>";
		}
	}
	?>
</body>
</html>