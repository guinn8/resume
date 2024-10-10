# Directories
COVER_LETTERS_DIR = cover_letters
OUTPUT_DIR = output
COVER_LETTERS_OUTPUT_DIR = $(OUTPUT_DIR)/cover_letters

# Templates
RESUME_TEMPLATE = template.tex
COVER_LETTER_TEMPLATE = cover_letter_template.tex

# Files
RESUME_MD = resume.md
RESUME_PDF = $(OUTPUT_DIR)/Gavin_Guinn_resume.pdf

# Cover letters
COVER_LETTER_MD = $(wildcard $(COVER_LETTERS_DIR)/*.md)
COVER_LETTER_PDFS = $(patsubst $(COVER_LETTERS_DIR)/%.md, $(COVER_LETTERS_OUTPUT_DIR)/%_coverletter_gavinguinn.pdf, $(COVER_LETTER_MD))

# Build cover letters
$(COVER_LETTERS_OUTPUT_DIR)/%_coverletter_gavinguinn.pdf: $(COVER_LETTERS_DIR)/%.md $(COVER_LETTER_TEMPLATE) | $(COVER_LETTERS_OUTPUT_DIR)
	pandoc $< -o $@ --pdf-engine=$(PDF_ENGINE) --template=$(COVER_LETTER_TEMPLATE)

# PDF Engine
PDF_ENGINE = xelatex

# Pandoc options
PANDOC_OPTIONS = --pdf-engine=$(PDF_ENGINE)

# Default target
all: $(RESUME_PDF) $(COVER_LETTER_PDFS)

# Create output directories
$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

$(COVER_LETTERS_OUTPUT_DIR):
	mkdir -p $(COVER_LETTERS_OUTPUT_DIR)

# Build resume
$(RESUME_PDF): $(RESUME_MD) $(RESUME_TEMPLATE) | $(OUTPUT_DIR)
	pandoc $(RESUME_MD) -o $(RESUME_PDF) --pdf-engine=$(PDF_ENGINE) --template=$(RESUME_TEMPLATE)

# Clean generated PDFs
clean:
	rm -rf $(OUTPUT_DIR)

.PHONY: all clean
