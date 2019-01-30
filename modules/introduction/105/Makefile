all: slides install

slides:
	pandoc --to revealjs --standalone --output index.html slides.md
	pandoc --to pptx --output slides.pptx slides.md

install:
	pandoc install.md --output install.html --standalone
	pandoc install.md --output install.docx
