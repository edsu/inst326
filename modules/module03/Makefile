all: index.html slides.pptx

index.html: slides.md
	pandoc --to revealjs --standalone --output index.html slides.md

slides.pptx: slides.md
	pandoc --from markdown --to pptx --output slides.pptx slides.md

exercise.html: exercise.md
	pandoc --output exercise.html --standalone exercise.md

