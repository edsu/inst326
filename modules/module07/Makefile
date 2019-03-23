all: readings.html index.html exercise1.html exercise2.html

index.html: slides.md
	pandoc --to revealjs --standalone --output index.html slides.md
	
readings.html: readings.md
	pandoc --output readings.html --standalone readings.md

exercise1.html: exercise1.md
	pandoc --output exercise1.html --standalone exercise1.md

exercise2.html: exercise2.md
	pandoc --output exercise2.html --standalone exercise2.md