all: clean Modelo-PPgSC.tex
	pdflatex Modelo-PPgSC
	bibtex Modelo-PPgSC
	pdflatex Modelo-PPgSC
	pdflatex Modelo-PPgSC
	evince Modelo-PPgSC.pdf&

clean:
	@rm -f *.pdf *.aux *.toc *.l* *.snm *.out *.nav *.bb* *.bl*
