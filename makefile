# sudo apt-get install texlive-fonts-extra texlive-xetex
resume:
	pandoc resume.md -o Gavin_Guinn_resume.pdf --pdf-engine=xelatex --template=template.tex