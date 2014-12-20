images = local-vars-plot.png parse-tree-1.neg.png parse-tree-2.neg.png vts.png
code = sample.py samplex.py myrename.py

slides.html: slides.txt $(images) $(code)
	asciidoc -b dzslides slides.txt

%.png: %.dia
	dia -t cairo-alpha-png -e $@ $<

%.neg.png: %.png
	convert -negate $< $@

clean:
	rm -f $(images)
	rm -f slides.html