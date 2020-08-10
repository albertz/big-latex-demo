default:
	pdflatex thesis
	makeglossaries thesis
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis
	pdflatex thesis

clean:
	# rm -f thesis.log thesis.aux thesis.bbl thesis.blg */*.aux
	rm -f *.bbl *.blg *.glo *.ist *.loa *.lof *.log *.lot *.out thesis.pdf *.toc */*.aux

