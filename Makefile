#
# replacing the anti-matter scripts with Makefile
# usage is simple:

# Usage
# 
# make generate -> generates .tex from .yaml and .md
# make mds -> from .md only
# make yamls -> from .yaml only
# make book -> build LaTeX book
# make view_linux -> view pdf on Linux
# make view_mac -> view pdf on mac os x
# make clean_gen -> remove generated files
# make clean_book -> remove book files
# Note: This is hard-wired for zettels and kernel, which is ok, now that incremental .yaml can be handled FAST.
#

GEN_DIR := .gen
YAML_SOURCES := $(shell find zettels kernel -type f -name "*.yaml")
YAML_OBJECTS := $(addprefix $(GEN_DIR)/,$(YAML_SOURCES:.yaml=.tex))

MD_SOURCES := $(shell find zettels kernel -type f -name "*.md")
MD_OBJECTS := $(addprefix $(GEN_DIR)/,$(MD_SOURCES:.md=.tex))

BOOK=cultural-hoc
BOOK_SOURCES := $(wildcard *.tex frontmatter/*.tex chapters/*.tex)

SHELL=/bin/bash

all: book

book : $(BOOK).pdf

generate : mds yamls

yamls: $(YAML_OBJECTS)

mds: $(MD_OBJECTS)

$(BOOK).pdf : $(MD_OBJECTS) $(YAML_OBJECTS) $(BOOK_SOURCES)
	latexmk -pdf $(BOOK).tex

# YAML -> TEX transformation (wildcard rule)

$(YAML_OBJECTS): $(GEN_DIR)/%.tex: %.yaml
	@echo "$< -> $@"
	@mkdir -p $(@D)
	TMPDIR=`mktemp -d`; \
	       echo $${TMPDIR}; \
	       zettel --file $< --save $${TMPDIR}/t1.md; \
	       echo "# zettelgeist" >> $${TMPDIR}/t1.md; \
	       pandoc -f markdown-auto_identifiers $${TMPDIR}/t1.md -o $${TMPDIR}/t1.tex; \
	       sed -f sed-scripts/sed-map-to-zsection.sed $${TMPDIR}/t1.tex > $${TMPDIR}/t2.tex; \
	       sed -f sed-scripts/sed-add-endzsection.sed  $${TMPDIR}/t2.tex > $${TMPDIR}/t3.tex; \
	       sed -f sed-scripts/sed-newcommand-begin.sed $${TMPDIR}/t3.tex > $${TMPDIR}/t4.tex; \
	       sed -f sed-scripts/sed-newcommand-end.sed  $${TMPDIR}/t4.tex > $${TMPDIR}/t5.tex; \
	       sed -f sed-scripts/sed-handle-citation.sed $${TMPDIR}/t5.tex > $${TMPDIR}/t6.tex; \
	       sed -f sed-scripts/sed-remove-esc-underscore.sed $${TMPDIR}/t6.tex > $${TMPDIR}/t7.tex; \
	       cat include/zzrenewcommands.tex $${TMPDIR}/t7.tex > $@; \
	       echo "}" >> $@

#	       rm -rf $${TMPDIR}

# Markdown -> LaTeX transformation (wildcard rule)
#
$(MD_OBJECTS): $(GEN_DIR)/%.tex: %.md
	@echo "$< -> $@"
	@mkdir -p $(@D)
	@pandoc -f markdown-auto_identifiers $< -o $@

clean: clean_book clean_gen

clean_gen:
	rm -rf .gen

clean_book:
	latexmk -pdf -C $(BOOK)
	rm -f *.aux *.log *.bbl *.blg *.out *.gz tmp.inputs *.fdb_latexmk *.dvi *.fls *.idx *.ilg *.ind *.toc *.thm *.tdo


view_linux view_mac view: book
	./view.sh cultural-hoc.pdf

