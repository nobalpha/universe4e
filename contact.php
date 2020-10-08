<!doctype html>
<!-- Website template by freewebsitetemplates.com -->
<html>

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Universal4E</title>
	<link rel="stylesheet" href="css/style.css" type="text/css">
	<link rel="stylesheet" type="text/css" href="css/mobile.css">
	<script src="js/mobile.js" type="text/javascript"></script>
	<script src="./js/lingumania.min.js"></script>
</head>

<body>
	<script type="text/javascript">
		function googleTranslateElementInit() {
			new google.translate.TranslateElement({
				pageLanguage: 'en'
			}, 'google_translate_element');
		}
	</script>

	<script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
	<div id="page">

		<div id="header">
			<div>
				<a href="index.php" class="logo"><img src="images/logo.png" alt=""></a>
				<ul id="navigation">
					<li class="selected">
						<a href="index.php">Home</a>
					</li>
					<li>
						<a href="about.php">About</a>
					</li>
					<li class="menu">
						<a href="team.php">Team</a>
					</li>
					<li>
						<a href="contact.php">Contact</a>
					</li>
				</ul>
			</div>
		</div>
		<div id="body">
			<div class="header">
				<div class="contact">
					<h1>Contact</h1>
					<h2>DO NOT HESITATE TO CONTACT US</h2>
					<form action="index.php">
						<input type="text" name="Name" value="Name" onblur="this.value=!this.value?'Name':this.value;"
							onfocus="this.select()" onclick="this.value='';">
						<input type="text" name="Email Address" value="Email Address"
							onblur="this.value=!this.value?'Email Address':this.value;" onfocus="this.select()"
							onclick="this.value='';">
						<input type="text" name="Subject" value="Subject"
							onblur="this.value=!this.value?'Subject':this.value;" onfocus="this.select()"
							onclick="this.value='';">
						<textarea name="message" cols="50" rows="7">Message</textarea>
						<input type="submit" value="Send" id="submit">
					</form>
				</div>
			</div>
		</div>
		<div id="footer">
			<div id="google_translate_element"></div>
			<div class="footnote">
				<div>
					<p>&copy; 2023 BY Tardigrades | ALL RIGHTS RESERVED</p>
				</div>
			</div>
		</div>
	</div>

</body>

</html>