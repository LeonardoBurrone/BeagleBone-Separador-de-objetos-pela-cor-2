<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width" />
	<title> LED </title>
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<!-- <script type="text/javascript" src="js/functions_led.js"></script> -->
</head>
<body>
	<div class="divMain">
		<form class="form1" action="led.php" method="get">
			<div class="div1">
				<table>
					<tr>
						<td>
							<center>
								<p>Escolha uma cor para o LED</p>
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
								<input type="submit" value="Desligar" name="desligado">
							</center>
						</td>
						<td>
							<center>
								<input type="submit" value="Branco" name="botao_branco">
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
									<input type="submit" value="Vermelho" name="botao_vermelho">
								</center>
							</td>
							<td>
								<center>
									<input type="submit" value="Verde" name="botao_verde">
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
									<input type="submit" value="Azul" name="botao_azul">
								</center>
							</td>
							
							<td>
								<center>
									<input type="submit" value="Amarelo" name="botao_amarelo">
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
									<input type="submit" value="Ciano" name="botao_ciano">
								</center>
							</td>
							
							<td>
								<center>
									<input type="submit" value="Magenta" name="botao_magenta">
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
								<a href="principal.php" target="_blank"> < Voltar à Página Principal > </a>
							</center>
						</td>
					</tr>
				</table>
			</div>
		</form>
	</div>
	
	<?
	if(isset($_GET["desligado"])){
		exec( "sudo python led.py 0 0 0" );
	}
	else if(isset($_GET["botao_vermelho"])){
		exec( "sudo python led.py 100 0 0" );
	}
	else if(isset($_GET["botao_verde"])){
		exec( "sudo python led.py 0 100 0" );
	}
	else if(isset($_GET["botao_azul"])){
		exec( "sudo python led.py 0 0 100" );
	}
	else if(isset($_GET["botao_amarelo"])){
		exec( "sudo python led.py 100 100 0" );
	}
	else if(isset($_GET["botao_ciano"])){
		exec( "sudo python led.py 0 100 100" );
	}
	else if(isset($_GET["botao_magenta"])){
		exec( "sudo python led.py 100 0 100" );
	}
	else if(isset($_GET["botao_branco"])){
		exec( "sudo python led.py 100 100 100" );
	}
	?>
</body>
</html>