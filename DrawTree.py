# -*- coding: UTF-8 -*-
import Tkinter as tk
import time
import thread
import math

L=20
xita=25
begi=150
begj=50
begxita=90
CvW=300
CvH=400
step=50
class Stack:
     def __init__(self):
         self.items = []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def clear(self):
         del self.items[:]

     def isempty(self):
         return self.size() == 0

     def size(self):
         return len(self.items)

     def top(self):
         return self.items[self.size()-1]
        
def draw(cv,starti,startj,endi,endj):
    x_step=(endi-starti)/step
    y_step=(endj-startj)/step
    i=0
    dstarti=starti
    dstartj=startj
    dendi=dstarti+x_step
    dendj=dstartj+y_step
    while i<step:
        cv.create_line((dstarti,dstartj,dendi,dendj),
                       arrow='none',
                       arrowshape='40 40 10'
                       )
        dstarti=dendi
        dstartj=dendj
        dendi=dstarti+x_step
        dendj=dstartj+y_step
        time.sleep(0.01)
        cv.update()
        i=i+1


def transition(stat):
    line=[]
    line.append(stat[0])
    line.append(CvH-stat[1])
    a=CvH-(stat[1]+L*math.sin(math.pi*stat[2]/180))
    #print 'a=',a
    #print 'CVH=',CvH
    #print stat[0],CvH-stat[1],stat[0]+L*math.cos(math.pi*stat[2]/180),CvH-(stat[1]+L*math.sin(math.pi*stat[2]/180))
    #print CvH-stat[1]+L*math.sin(math.pi*stat[2]/180)
    line.append(stat[0]+L*math.cos(math.pi*stat[2]/180))
    line.append(CvH-(stat[1]+L*math.sin(math.pi*stat[2]/180)))
    return line



def interp_flag(s,stat,flag):
    new_stat=[]
    if(flag=='F'):
        new_stat.append(stat[0]+L*math.cos(math.pi*stat[2]/180))
        new_stat.append(stat[1]+L*math.sin(math.pi*stat[2]/180))
        new_stat.append(stat[2])
        return new_stat
    if(flag=='+'):
        new_stat.append(stat[0])
        new_stat.append(stat[1])
        new_stat.append(stat[2]-xita)
        return new_stat
    if(flag=='-'):
        new_stat.append(stat[0])
        new_stat.append(stat[1])
        new_stat.append(stat[2]+xita)
        return new_stat
    if(flag=='['):
        s.push(stat)
        return stat
    if(flag==']'):
        new_stat=s.pop()
        return new_stat

def DrawTree_first():
     S='FF[+FF[+F[+F[+F][-F]][-F]][-F[+F][-F]]][-F[+F[+F][-F]][-F[+F][-F[+F][-F]]]]FF[+F][-F]'   
     s=Stack()
     stat=[begi,begj,begxita]
     #thread.start_new(draw,(cv,line[0],line[1],line[2],line[3]))
     for flag in S:
          if flag=='F':
               line=transition(stat)
               draw(cv,line[0],line[1],line[2],line[3])
          stat=interp_flag(s,stat,flag)

    
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('388x400')

    frame1=tk.Frame(root,height=CvH,width=CvW)
    frame1.pack(side = tk.LEFT)

    frame2=tk.Frame(root,height=CvH,width=200)
    frame2.pack(side = tk.RIGHT)
    
    cv=tk.Canvas(frame1,bg='blue',height=CvH,width=CvW)
    cv.pack(side = tk.LEFT)
    
    button=tk.Button(frame2,width=9,text='生成树',command=DrawTree_first)
    button.pack(side=tk.LEFT)


    root.mainloop()    
