PDFLATEX=pdflatex # -interaction=batchmode
PDFLATEX_EXTRA="-halt-on-error"

book: common
	@$(PDFLATEX) $(PDFLATEX_EXTRA) book
	@bibtex book
	@makeindex book
	@$(PDFLATEX) $(PDFLATEX_EXTRA) book
	@$(PDFLATEX) $(PDFLATEX_EXTRA) book

common:
	cp settingsbase.tex settings.tex
	echo '\\newcommand{\\basepath}{'$(PWD)'}' >> settings.tex

clean:
	/bin/rm -f *.aux *.idx *.lof *.log *.ilg *.lot  *.fdb_latexmk book.fls
	/bin/rm -f *.out *.pdf *.toc *.ind settings.tex
	/bin/rm -f book.bbl book.blg book.bib.bak

view:
	./view.sh book.pdf





