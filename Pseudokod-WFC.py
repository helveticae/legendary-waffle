

# rows är illustrationer av en vektor, kan användas för tile generation och(?) stats
# vi tar fram o, x och l genom att börja på en (eller flera) slumpade koordinat(er)
# jag har valt o, x och l endast för att enklare kunna särskilja tecken åt i illustrationen

o = 0
x = 0
l = 0


row1 = ([ ],[ ],[ ])
row2 = ([ ],[ ],[ ])
row3 = ([ ],[ ],[ ])


# rule 1: l cannot be bredvid a
    # bredvid = radie 1, (8st)
    # def nudda(): = radie 1

# enligt regler nu:
row1 = ([l],[l],[l])
row2 = ([x],[x],[l])
row3 = ([o],[x],[l])

# men också okej:
row1 = ([o],[o],[o])
row2 = ([o],[o],[o])
row3 = ([o],[o],[o])

# rule 2: o får nudda < 2 o
# rule 3: l får nudda < 2 l
# rule 4: x får nudda allt

# enligt regler nu:
row1 = ([l],[l],[x])
row2 = ([x],[x],[x])
row3 = ([o],[x],[l])

# men också okej:
row1 = ([x],[x],[x])
row2 = ([x],[x],[x])
row3 = ([x],[x],[x])

# rule 5: x får inte nudda > 8 x

# enligt regler nu:

row1 = ([x],[x],[x])
row2 = ([x],[l],[x])
row3 = ([x],[l],[x])

# min förutsägelse är att a och l sällan kommer att genereras på samma vektor
# eftersom x används som "avskiljare" och det finns få scenarion på 3*3 grid

# Med nuvarande regler, hur många utfall finns?