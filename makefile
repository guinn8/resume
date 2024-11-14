PDF_ENGINE = xelatex

# Define directories
SRC_DIR = src
COVER_LETTERS_DIR = $(SRC_DIR)/cover_letters
RESUMES_DIR = $(SRC_DIR)/resumes

# Collect markdown files in the new src structure
RESUME_MD := $(wildcard $(RESUMES_DIR)/*.md)
COVER_LETTER_MD := $(wildcard $(COVER_LETTERS_DIR)/*.md)

# Define output paths for PDFs
RESUME_PDF := $(patsubst $(RESUMES_DIR)/%.md, output/resumes/%_Gavin_Guinn_Resume.pdf, $(RESUME_MD))
COVER_LETTER_PDF := $(patsubst $(COVER_LETTERS_DIR)/%.md, output/cover_letters/%_coverletter_gavinguinn.pdf, $(COVER_LETTER_MD))

# Default target
all: $(RESUME_PDF) $(COVER_LETTER_PDF)

# Build resumes
output/resumes/%_Gavin_Guinn_Resume.pdf: $(RESUMES_DIR)/%.md $(SRC_DIR)/template.tex
	mkdir -p $(dir $@)
	pandoc $< -o $@ --pdf-engine=$(PDF_ENGINE) --template=$(SRC_DIR)/template.tex

# Build cover letters
output/cover_letters/%_coverletter_gavinguinn.pdf: $(COVER_LETTERS_DIR)/%.md $(SRC_DIR)/cover_letter_template.tex
	mkdir -p $(dir $@)
	pandoc $< -o $@ --pdf-engine=$(PDF_ENGINE) --template=$(SRC_DIR)/cover_letter_template.tex

# Clean generated files
clean:
	rm -rf output

.PHONY: all clean
