import drawsvg as dw
wx = 1000
wy = 500 # wx*1.4145
d = dw.Drawing(wx, wy)

# import 'def.py'
exec(open('def.py').read())




kadr(wx,wy)
staffs(100,150,5)
staffs(100,230,5)
staffs(100,310,3)
# fClef(50,20)
gClef(105,145)
gClef(105,225)


d.append(dw.Text('Clarinet Bb', font_size=15, x=10, y=175, font_weight='bold'))
d.append(dw.Text('Kamancheh', font_size=15, x=10, y=255, font_weight='bold'))
d.append(dw.Text('Gloom Guardian', font_size=30, x=320, y=60, font_weight='bold'))
d.append(dw.Text(': Dance of Sorrow', font_size=25, x=550, y=60, font_weight='bold'))
d.append(dw.Text('Parham Izadyar', font_size=15, x=850, y=120, font_weight='light'))


def note(x=100,y=65,y_space=10,swfac=1,dotted=0,c='black',dotspace=1,dotsiz=1,**args):
    sw = y_space * swfac * 0.1 
    r = y_space/2
    p = dw.Path(stroke_width=sw,stroke=c,**args)
    p1 = x-r*1.2,y+r*.7
    p2 = x+r*1.2,y-r*.7
    p.M(*p1)
    p.C(x-r*1.7,y-r*.3, x+r*.3,y-r*1.4, *p2)
    p.C(x+r*1.7,y+r*.3, x-r*.3,y+r*1.4, *p1)
    d.append(p)
    if dotted > 0:
        x = p2[0]+dotspace*y_space/2
        y = p2[1]-y_space/10
        for i in range(dotted):
            d.append(dw.Circle(x,y,dotsiz*y_space/6,fill=c))
            x += dotspace*y_space/2


# note(150, 15
note(170, 160)
note(x=150,y=150,y_space=10,swfac=1,dotted=0,c='black',dotspace=1,dotsiz=1)
linenote(156, 120, 29, 1)
linenote(176, 125, 34, 1)
# linecu(156, 120, 176, 125,2)
# linecu(156, 124, 176, 129, 2)
d.save_svg("score.svg")
# d.save_pdf("score.pdf")