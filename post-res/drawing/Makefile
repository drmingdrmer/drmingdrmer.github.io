BIGs = $(wildcard *-big.jpg)
SMALLs = $(BIGs:-big.jpg=-small.jpg)

all: $(SMALLs)

%-small.jpg:%-big.jpg
	convert -resize '25%%' $< $@

clean:
	rm $(SMALLs)
