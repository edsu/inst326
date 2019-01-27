all: syllabi

syllabi:
	echo "creating syllabus pdfs"
	pandoc --pdf-engine=xelatex sp2019-105.md -o sp2019-105.pdf
	pdflatex sp2019-101.tex > /dev/null
	rm *.out *.log *.aux
