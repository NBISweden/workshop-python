CSS_HIGHLIGHTER=.codehilite

define CSS_HIGHLIGHT_INDENT
${CSS_HIGHLIGHTER} .indent {
border-left:1px solid #ccc;
box-sizing:border-box;
margin-left:-1px;
line-height:1.75em;
display:inline-block;
/* background:pink; */
}
endef
export CSS_HIGHLIGHT_INDENT

all: cleanall install style.css clean

install: ep/__init__.py ep/ep.py
	python setup.py install -f

clean:
	rm -rf build dist ep.egg-info
	rm -rf ep/__pycache__

cleanall:
	rm -f style.css

style.css:
	pygmentize -f html -S EmacsPython -a ${CSS_HIGHLIGHTER} > $@
	echo "$$CSS_HIGHLIGHT_INDENT" >> $@ 

