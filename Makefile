PDFLATEX=pdflatex # -interaction=batchmode
PDFLATEX_EXTRA="-halt-on-error"
BOOK=se4ml

BOOK_SOURCES := $(wildcard *.tex frontmatter/*.tex software/*.tex unsupervised/*.tex)


all: $(BOOK).pdf

$(BOOK).pdf: $(BOOK_SOURCES) settings.tex
	@$(PDFLATEX) $(PDFLATEX_EXTRA) $(BOOK)
	@bibtex $(BOOK)
	@makeindex $(BOOK)
	@$(PDFLATEX) $(PDFLATEX_EXTRA) $(BOOK)
	@$(PDFLATEX) $(PDFLATEX_EXTRA) $(BOOK)

settings.tex: settingsbase.tex
	cp settingsbase.tex settings.tex
	echo '\\newcommand{\\basepath}{'$(PWD)'}' >> settings.tex

clean:
	/bin/rm -f *.aux *.idx *.lof *.log *.ilg *.lot  *.fdb_latexmk $(BOOK).fls
	/bin/rm -f *.out *.pdf *.toc *.ind settings.tex
	/bin/rm -f $(BOOK).bbl $(BOOK).blg $(BOOK).bib.bak

view: $(BOOK).pdf # create the latest version
	./view.sh $(BOOK).pdf





