# sudo apt-get install texlive-fonts-extra texlive-xetex
resume:
	pandoc resume.md -o resume.pdf --pdf-engine=xelatex --template=template.tex