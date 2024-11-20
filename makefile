# Define the PDF engine
PDF_ENGINE = xelatex

# Use `find` to dynamically get lists of markdown files
LETTER_MD := $(shell find job_postings -type f -name "letter_*.md")
RESUME_MD := $(shell find job_postings -type f -name "resume_*.md")

# Define the corresponding PDF files
LETTER_PDF := $(LETTER_MD:.md=.pdf)
RESUME_PDF := $(RESUME_MD:.md=.pdf)

# Default target: build all PDFs
all: $(LETTER_PDF) $(RESUME_PDF)

# Rule to build cover letters
job_postings/%/letter_%.pdf: job_postings/%/letter_%.md src/cover_letter_template.tex
	@echo "Building cover letter PDF: $@"
	pandoc $< -o $@ --pdf-engine=$(PDF_ENGINE) --template=src/cover_letter_template.tex

# Rule to build resumes
job_postings/%/resume_%.pdf: job_postings/%/resume_%.md src/template.tex
	@echo "Building resume PDF: $@"
	pandoc $< -o $@ --pdf-engine=$(PDF_ENGINE) --template=src/template.tex

# Clean target
clean:
	@echo "Cleaning all generated PDFs..."
	find job_postings -type f -name "*.pdf" -delete
	@echo "All PDFs have been removed."

.PHONY: all clean
# Define the PDF engine
PDF_ENGINE = xelatex

# Use `find` to dynamically get lists of markdown files
LETTER_MD := $(shell find job_postings -type f -name "letter_*.md")
RESUME_MD := $(shell find job_postings -type f -name "resume_*.md")

# Define the corresponding PDF files by replacing .md with .pdf
LETTER_PDF := $(LETTER_MD:.md=.pdf)
RESUME_PDF := $(RESUME_MD:.md=.pdf)

# Default target: build all PDFs
all: $(LETTER_PDF) $(RESUME_PDF)

# Rule to build cover letters
$(LETTER_PDF): %.pdf: %.md src/cover_letter_template.tex
	@echo "Building cover letter PDF: $@"
	pandoc $< -o $@ --pdf-engine=$(PDF_ENGINE) --template=src/cover_letter_template.tex

# Rule to build resumes
$(RESUME_PDF): %.pdf: %.md src/template.tex
	@echo "Building resume PDF: $@"
	pandoc $< -o $@ --pdf-engine=$(PDF_ENGINE) --template=src/template.tex

# Clean target
clean:
	@echo "Cleaning all generated PDFs..."
	find job_postings -type f -name "*.pdf" -delete
	@echo "All PDFs have been removed."

.PHONY: all clean
