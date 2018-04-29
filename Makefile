PDFLATEX = pdflatex # -interaction=batchmode

book: common
	@$(PDFLATEX) book
	@bibtex book
	@makeindex book
	@$(PDFLATEX) book
	@$(PDFLATEX) book
	@evince book.pdf &

common:
	cp settingsbase.tex settings.tex
	echo '\\newcommand{\\basepath}{'$(PWD)'}' >> settings.tex

clean:
	/bin/rm -f *.aux *.idx *.lof *.log *.ilg *.lot 
	/bin/rm -f *.out *.pdf *.toc *.ind settings.tex



