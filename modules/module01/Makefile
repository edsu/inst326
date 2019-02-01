all: index.html slides.pptx 105.html

index.html: slides.md
	pandoc --to revealjs --standalone --output index.html slides.md

slides.pptx: slides.md
	pandoc --from markdown --to pptx --output slides.pptx slides.md

105.html: 105.md
	pandoc --to revealjs --standalone --output 105.html 105.md


