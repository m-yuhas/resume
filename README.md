# Résumé
Over time I've noticed that keeping track of all the versions of my résumé for
various positions has become quite a chore.  The idea behind this repository
is to take advantage of Git to keep track of edits to my résumé over time and
always have access to older versions.

# Usage
The file ```resume.tex``` contains the body of the resume, while contact info
should be stored locally in a file named ```.contact_info.tex```.  This file is
listed in the ```.gitignore``` to prevent contact details from accidently being
uploaded to Github.

To generate a pdf copy of the résumé install pdfTeX and run:
```
$ pdflatex resume.tex
```
