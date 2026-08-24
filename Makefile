.DEFAULT_GOAL := pdf

MAIN := main
BUILD_DIR := build
CACHE_DIR := $(BUILD_DIR)/texmf-cache
VAR_DIR := $(BUILD_DIR)/texmf-var
CWD := $(abspath .)
BIBS := $(wildcard *.bib)
BST := jhep.bst

LATEXMK := latexmk
MAKEINDEX_STYLE := $(abspath styles/index.ist)
MAKEINDEX_CMD := upmendex -g -s "$(MAKEINDEX_STYLE)" %O -o %D %S
LATEXMK_MAKEINDEX_FLAG := -e '$$makeindex=q{$(MAKEINDEX_CMD)}'
LATEXMK_FLAGS := -f -lualatex -synctex=1 -interaction=nonstopmode -file-line-error -output-directory=$(BUILD_DIR) $(LATEXMK_MAKEINDEX_FLAG)
LATEXMK_FORCE_FLAGS := -f -gg -lualatex -synctex=1 -interaction=nonstopmode -file-line-error -output-directory=$(BUILD_DIR) $(LATEXMK_MAKEINDEX_FLAG)
OPEN_PDF := sh src/open_pdf.sh
PYTHON := venv/bin/python
MPL_CACHE_DIR := $(BUILD_DIR)/matplotlib
XDG_CACHE_DIR := $(BUILD_DIR)/xdg-cache
MATPLOTLIB_ENV := MPLBACKEND=Agg MPLCONFIGDIR=$(MPL_CACHE_DIR) XDG_CACHE_HOME=$(XDG_CACHE_DIR)
GENERATED_FIGURES := fig/gh.pdf

SOURCES := $(MAIN).tex $(BIBS) $(BST) $(wildcard .latexmkrc) $(wildcard chapters/*.tex) $(wildcard fig/*) $(wildcard assets/figures/*) $(wildcard styles/*)

.PHONY: all pdf figures open clean distclean

open: $(MAIN).pdf
	$(OPEN_PDF) $(MAIN).pdf

all: | $(BUILD_DIR) $(CACHE_DIR) $(VAR_DIR)
	BIBINPUTS=$(CWD):$(BIBINPUTS) BSTINPUTS=$(CWD):$(BSTINPUTS) TEXMFCACHE=$(CACHE_DIR) TEXMFVAR=$(VAR_DIR) $(LATEXMK) $(LATEXMK_FORCE_FLAGS) $(MAIN).tex
	cp $(BUILD_DIR)/$(MAIN).pdf $(MAIN).pdf

pdf: $(MAIN).pdf

figures: $(GENERATED_FIGURES)

$(MAIN).pdf: $(BUILD_DIR)/$(MAIN).pdf
	cp $(BUILD_DIR)/$(MAIN).pdf $@

$(BUILD_DIR)/$(MAIN).pdf: $(SOURCES) $(GENERATED_FIGURES) | $(BUILD_DIR) $(CACHE_DIR) $(VAR_DIR)
	BIBINPUTS=$(CWD):$(BIBINPUTS) BSTINPUTS=$(CWD):$(BSTINPUTS) TEXMFCACHE=$(CACHE_DIR) TEXMFVAR=$(VAR_DIR) $(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex

fig/gh.pdf: src/gh.py | $(MPL_CACHE_DIR) $(XDG_CACHE_DIR)
	$(MATPLOTLIB_ENV) $(PYTHON) $<

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(CACHE_DIR):
	mkdir -p $(CACHE_DIR)

$(VAR_DIR):
	mkdir -p $(VAR_DIR)

$(MPL_CACHE_DIR):
	mkdir -p $(MPL_CACHE_DIR)

$(XDG_CACHE_DIR):
	mkdir -p $(XDG_CACHE_DIR)

clean:
	TEXMFCACHE=$(CACHE_DIR) TEXMFVAR=$(VAR_DIR) $(LATEXMK) -c -output-directory=$(BUILD_DIR) $(MAIN).tex
	rm -f $(MAIN).synctex.gz
	rm -rf $(BUILD_DIR)

distclean: clean
	rm -f $(BUILD_DIR)/$(MAIN).pdf
	rm -f $(MAIN).pdf
	rm -f $(MAIN).synctex.gz
