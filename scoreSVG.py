import drawsvg as dw
wx = 450
wy = 100
d = dw.Drawing(wx, wy)

def staff(x=10,number=5):
    linedex = 0
    while linedex < number:
        lineshow = dw.Line(40,x,400,x,stroke="black", stroke_width=.5)
        d.append(lineshow)
        x = x+10
        linedex += 1
def gClef(x=10,y=10,linspace=12,color='black',sw=2):
    p1 = x+linspace,y+linspace*3
    c1a = x+linspace*1.5,y+linspace*2
    c1b = x+linspace*3.2,y+linspace*2.7
    p2 = x+linspace*1.5,y+linspace*3.5
    c2a = x+linspace*0.01,y+linspace*4
    c2b = x+linspace/5,y+linspace*2
    p3 = x+linspace*1.5,y+linspace
    c3a = x+linspace*2,y+linspace/2
    c3b = x+linspace*2,y+linspace*0.01
    p4 = x+linspace*1.5,y+linspace*0.01
    c4a = x+linspace*0.5,y+linspace*0.1
    c4b = x+linspace*2,y+linspace*2
    p5 = x+linspace*1.1,y+linspace*4.5


    p = dw.Path(stroke=color,stroke_width=sw,fill='none')
    p.M(*p1)
    p.C(*c1a, *c1b, *p2)
    p.C(*c2a, *c2b, *p3)
    p.C(*c3a, *c3b, *p4)
    p.C(*c4a, *c4b, *p5)
    d.append(p)
def fClef(x=50,y=20,linspace=15,color='black',sw=2.4,r=1):
    """draws a bass clef.  x,y are top left of the stave
    sw = stroke width, r = radius for two points"""
    p1 = x+linspace*.7,y+linspace*.8
    c1a = x+linspace*.9,y+linspace*1.1
    c1b = x+linspace*.5, y+linspace*1.3
    p2 = x+linspace*.4,y+linspace
    c2a = x+linspace*.2,y+linspace/2
    c2b = x+linspace*.6,y
    p3 = x+linspace*1,y+linspace/7
    c3a = x+linspace*2,y+linspace/2
    c3b = x+linspace, y+linspace*3
    p4 = x+linspace/3,y+linspace*2.7-linspace/2
    p = dw.Path(stroke=color,stroke_width=sw,fill='none')
    p.M(*p1)
    p.C(*c1a, *c1b, *p2)
    p.C(*c2a, *c2b, *p3)
    p.C(*c3a, *c3b, *p4)
    d.append(p)
    d.append(dw.Circle(x+linspace*2,y+linspace-r*3,r,stroke=color))
    d.append(dw.Circle(x+linspace*2,y+linspace+r*3,r,stroke=color))
def arrow(x=10,y=10,l=30,w=8,rot=0,c='black',sw=1,**args):
    """simple arrow. rot=0 means downwards"""
    y2 = y+l
    p1 = x-w,y2-w
    p2 = x+w,y2-w
    p = dw.Path(stroke_width=sw,stroke=c,fill='none',transform='rotate(%f %f %f)' % (rot,x,y),**args)
    p.M(x,y)
    p.V(y2)
    p.M(*p1)
    p.L(x,y2)
    p.L(*p2)
    d.append(p)
def note(x=100,y=65,y_space=10,swfac=1,dotted=0,c='black',dotspace=1,dotsiz=1,**args):
    sw = y_space * swfac * 0.1 
    r = y_space/2
    p = dw.Path(stroke_width=sw,stroke=c,**args)
    p1 = x-r*1.2,y+r*.6
    p2 = x+r*1.2,y-r*.6
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
def bflat(x_note=10,y_note=10,y_space=10,color='black',sw=1,x_offset_mult=1):
    """b flat sign before a note
    x_note and y_note are the middle of the note
    x_offset_mult: x offset between sharp and note as ratio of y_space"""
    width = y_space*1/2
    x_offset = y_space*x_offset_mult
    x_left = x_note-x_offset-width
    y_top = y_note-y_space*1.5
    y_bot = y_note+y_space*0.5
    y_end = y_note-y_space*1/4
    p = dw.Path(fill='none',stroke=color,stroke_width=sw)
    p.M(x_left,y_top)
    p.V(y_bot)
    p.Q(x_note-x_offset*1/4,y_note-y_space*3/4 ,x_left,y_end)
    d.append(p) 
def Qflat(x_note=10,y_note=10,y_space=10,color='black',sw=1,x_offset_mult=1):
    """b flat sign before a note
    x_note and y_note are the middle of the note
    x_offset_mult: x offset between sharp and note as ratio of y_space"""
    width = y_space*0.5
    x_offset = y_space*x_offset_mult
    x_left = x_note+5-x_offset-width
    y_top = y_note-y_space*1.5
    y_bot = y_note+y_space*0.5
    y_end = y_note-y_space*0.25
    p = dw.Path(fill='none',stroke=color,stroke_width=sw)
    p.M(x_left,y_top)
    p.V(y_bot)
    p.Q(x_note-x_offset*2.15,y_note-y_space*0.6 ,x_left,y_end)
    d.append(p)
def koron(x=10,y=100,color='black',sw=1):
    xstart = x-20
    ystart = y+25
    p = dw.Path(fill='none',stroke=color,stroke_width=sw)
    p.M(xstart,ystart)
    p.L(xstart,ystart-30)
    p.L(xstart+7,ystart-25)
    p.L(xstart,ystart-20)
    d.append(p)
def sharp(x_note=10,y_note=10,y_space=10,color='black',sw=1,x_offset_mult=2/3):
    width = y_space*1/2
    x_offset = y_space*x_offset_mult
    ybot = y_note+y_space
    ybot1 = y_note+y_space*1/2 #left
    ybot2 = y_note+y_space*1/9 #right
    ytop = y_note-y_space
    ytop2 = y_note-y_space*1/2 #left
    ytop1 = y_note-y_space*1/9 #right
    x1 = x_note-x_offset-width-y_space/2
    x2 = x_note-x_offset-y_space/2
    xmin = x1-y_space*1/5
    xmax = x2+y_space*1/5
    g = dw.Group(stroke=color,stroke_width=sw)
    g.append(dw.Line(x1,ybot,x1,ytop))
    g.append(dw.Line(x2,ybot,x2,ytop))
    g.append(dw.Line(xmin,ybot1,xmax,ybot2))
    g.append(dw.Line(xmin,ytop1,xmax,ytop2))
    d.append(g)
def Qsharp(x_note=10,y_note=10,y_space=10,color='black',sw=1,x_offset_mult=0.8):
    width = y_space*0.5
    x_offset = y_space*x_offset_mult
    ybot = y_note+y_space
    ybot1 = y_note+y_space*1/2 #left
    ybot2 = y_note+y_space*1/9 #right
    ytop = y_note-y_space
    ytop2 = y_note-y_space*1/2 #left
    ytop1 = y_note-y_space*1/9 #right
    x1 = x_note-x_offset-y_space*0.5
    x2 = x_note-x_offset-y_space/2
    xmin = x1-y_space*1/5
    xmax = x2+y_space*1/5
    g = dw.Group(stroke=color,stroke_width=sw)
    g.append(dw.Line(x1,ybot,x1,ytop))
    # g.append(dw.Line(x2,ybot,x2,ytop))
    g.append(dw.Line(xmin-1,ybot1,xmax+1,ybot2))
    g.append(dw.Line(xmin-1,ytop1,xmax+1,ytop2))
    d.append(g)    
def sori(x_note=10,y_note=10,y_space=10,color='black',sw=1,x_offset_mult=2/3):
    width = y_space*1/2
    x_offset = y_space*x_offset_mult+5
    ybot = y_note+y_space
    ybot1 = y_note+y_space*1/2 #left
    ybot2 = y_note+y_space*1/9 #right
    ytop = y_note-y_space
    ytop2 = y_note-y_space*1/2 #left
    ytop1 = y_note-y_space*1/9 #right
    x1 = x_note-x_offset-width-y_space*0.5
    x2 = x_note-x_offset-y_space*0.5
    xmin = x1-y_space*0.5
    xmax = x2+y_space*0.7
    g = dw.Group(stroke=color,stroke_width=sw)
    g.append(dw.Line(x1,ybot+2,x1,ytop+2))
    g.append(dw.Line(x2,ybot,x2,ytop))
    g.append(dw.Line(xmin,ybot1,xmax,ytop+10))
    g.append(dw.Line(xmin,ytop1-1,xmax,ytop+10))
    d.append(g)
def WriteNote(midiNote=48,time=150):
    yStart = 80
    Qshrp = 0
    Qflt = 0
    shrp = 0
    flt = 0
    octave = int(midiNote/12)-3
    indxMidiIn = (midiNote % 12)
    indxMidi = int(midiNote % 12)
    iSCent = indxMidiIn-indxMidi
    altre =  [1, 3, 6, 8, 10]
    if iSCent == 0.5:
        shrp = 0
        Qflt = 0
        Qshrp = 1
        for i in altre:
            if indxMidi == i:
                indxMidi = indxMidi+1
                Qflt = 1
                Qshrp = 0
    elif iSCent == 0:
        Qflt = 0
        Qshrp = 0
        shrp = 0
        for i in altre:
            if indxMidi == i:
                indxMidi = indxMidi
                flt = 0
                shrp = 1
    if indxMidi == 10:
        flt = 1
        Qflt = 0
        Qshrp = 0
        shrp = 0
        indxMidi = indxMidi+1
    plusArr = [0,0,5,5,10,15,15,20,20,25,25,30]
    ySpace = plusArr[indxMidi]
    y = yStart-(ySpace)-(octave*35)
    note(time,y)
    if Qflt == 1:
        Qflat(time,y)
    if Qshrp == 1:
        Qsharp(time,y)
    if shrp == 1:
        sharp(time,y)
    if flt == 1:
        bflat(time,y)
def timeline(starttime=0,endtime=30):
    d.append(dw.Text('%.2f sec'%starttime,12,50,80,text_anchor='middle',valign='middle'))
    d.append(dw.Text('%.2f sec'%endtime,12,770,80,text_anchor='middle',valign='middle'))
def kadr(wx=820,wy=600):
    clr = 'black'
    kadr = dw.Path(stroke=clr,fill='none')
    kadr.M(0,0)
    kadr.L(wx,0)
    kadr.L(wx,wy)
    kadr.L(0,wy)
    kadr.L(0,0)
    d.append(kadr)

kadr(wx,wy)
filename = 'WriteMidi.txt'
with open(filename, 'r') as f:
    data = f.read()
    dataSplit = data.split()
    len = len(dataSplit)
    time = 150
    noteIndx = 0
    while noteIndx < len:
        x = float(dataSplit[noteIndx])
        midi = x
        WriteNote(midi,time-30)
        time += 50
        noteIndx += 1
        

        






staffIndx = 0
xStaff = 20
while staffIndx < 5:
    
    xStaff += 120
    staffIndx += 1
staff(20,5)
fClef(50,20)






d.save_svg("AllNotes.svg")
d
