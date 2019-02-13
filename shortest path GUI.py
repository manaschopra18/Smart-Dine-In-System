#SMART DINE-IN USING DFS
#exec(open("C:\\Users\\manas\\Desktop\\ada2.py").read())  

from collections import defaultdict

class Graph:

	def __init__(self):	#Default constructor

		self.graph = defaultdict(list)
		self.path=[]
		self.found= False

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self,v,visited,d):

		# Mark the current node as visited
		if(self.found!=True):
                        visited[v]= True
                        for i in self.graph[v]:
                                if visited[i] == False and i!=d and self.found!=True:
                                        self.DFSUtil(i, visited,d)
                                        if self.found==True:
                                                self.path.append(v)
                                elif visited[i] == False and i==d and self.found!=True:
                                        self.path.append(v)
                                        self.found=True
                                        break;

	def DFS(self,v,d):  #v= source vertex , d= destination
                self.path=[]
                self.found= False
		# Mark all the vertices as not visited
                visited = [False]*(len(self.graph))
                self.DFSUtil(v,visited,d)

	def printPath(self):
                for i in range(len(self.path)-1,-1,-1):
                        if self.path[i] not in path:
                                path.append(self.path[i])
                        #print(self.path[i],end=" ")
                                
g = Graph()
g.addEdge(0, 1) #adding all the directed paths
g.addEdge(0, 4)
g.addEdge(1, 2)
g.addEdge(1, 5)
g.addEdge(2, 3)
g.addEdge(2, 6)
g.addEdge(3, 19)
g.addEdge(3, 7)


g.addEdge(4, 5)
g.addEdge(4, 8)
g.addEdge(5, 6)
g.addEdge(5, 9)
g.addEdge(6, 7)
g.addEdge(6, 10)
g.addEdge(7, 18)
g.addEdge(7, 11)

g.addEdge(8, 9)
g.addEdge(8, 12)
g.addEdge(9, 10)
g.addEdge(9, 13)
g.addEdge(10, 11)
g.addEdge(10, 14)
g.addEdge(11, 17)
g.addEdge(11, 15)


g.addEdge(12, 13)
g.addEdge(13, 14)
g.addEdge(14, 15)
g.addEdge(15, 16)

g.addEdge(16, 17)
g.addEdge(17, 18)
g.addEdge(18, 19)
g.addEdge(19, 20)
g.addEdge(20, 0)

path=[]
#d=int(input("Enter the destination :"))


# --------------------------------------------------------GUI PART STARTS HERE--------------------

from tkinter import *
M = 4 # No. of rows of tables
N = 4 # No. of columns of tables
window=Tk()
window.title(" SMART DINE-IN SYSTEM ")
window.geometry("700x650")
canvas=Canvas(window,width=700,height=650)
canvas.grid(row=5,column=0)

l=Label(canvas,text=" SMART DINE_IN SYSTEM ",font='Helvetica 12 bold underline')

l.grid(row=0,column=1,columnspan=3)
l1=Label(canvas,text="( NOTE: Click on the numbered box to select table number )",font='Helvetica 10 bold')
l1.grid(row=1,column=0,columnspan=5)

#l.place(x=580,y=15)
table_name="btn"

def reset_color():            # TO RESET ALL THE COLORS OF TABLES TO INITIAL
    print("COLORS RESET")
    btn20.config(bg='#355C7D')
    for i in range(16):
        btn_name[i].config(bg='#355C7D')
    for i in line_name.keys():
        canvas.itemconfigure(line_name[i],fill='#355C7D')

def table_number(num):       #THIS FUNCTION IS CALLED IF A TABLE IS CLICKED
    reset_color()
    print("table ",num)
    table_name="btn"+str(num)
    print(table_name)
    if num in range(0,16):
        btn_name[num].config(bg='brown')
        btn20.config(bg='brown')   #kitchen
        del path[:]
        path.append(20)    #Food starts from kitchen i.e. node 20
        g.DFS(0,num)
        g.printPath()
        g.DFS(num,20)
        g.printPath()
        path.append(21)     #after node 19 path followed if 19 - > 21 -> `20 (KITCHEN)
        path.append(20)
        print(path)
        for i in range(len(path)-1):
            s="L"+str(path[i])+str(path[i+1])
            #line_name[2].config(bg='brown')
            canvas.itemconfigure(line_name[s],fill='green')

##btn=[]
##for i in range(16):
##  btn.append(Button(canvas,text=i,bg='#355C7D',command=lambda : table_number(i),width=7, height=3).grid(row=((i//M)+3), column=(i%M), sticky=W , padx =35,pady=35))

# CREATING TABLES USING BUTTONS
btn0=Button(canvas,text=0, font='Helvetica 9 bold',bg='#355C7D',fg="white",command=lambda : table_number(0),width=7, height=3)
btn0.grid(row=3, column=0, sticky=W , padx =35,pady=35)
btn1=Button(canvas,text=1,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(1),width=7, height=3)
btn1.grid(row=3, column=1, sticky=W , padx =35,pady=35)
btn2=Button(canvas,text=2,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(2),width=7, height=3)
btn2.grid(row=3, column=2, sticky=W , padx =35,pady=35)
btn3=Button(canvas,text=3,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(3),width=7, height=3)
btn3.grid(row=3, column=3, sticky=W , padx =35,pady=35)
btn4=Button(canvas,text=4,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(4),width=7, height=3)
btn4.grid(row=4, column=0, sticky=W , padx =35,pady=35)
btn5=Button(canvas,text=5,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(5),width=7, height=3)
btn5.grid(row=4, column=1, sticky=W , padx =35,pady=35)
btn6=Button(canvas,text=6,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(6),width=7, height=3)
btn6.grid(row=4, column=2, sticky=W , padx =35,pady=35)
btn7=Button(canvas,text=7,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(7),width=7, height=3)
btn7.grid(row=4, column=3, sticky=W , padx =35,pady=35)
btn8=Button(canvas,text=8,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(8),width=7, height=3)
btn8.grid(row=5, column=0, sticky=W , padx =35,pady=35)
btn9=Button(canvas,text=9,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(9),width=7, height=3)
btn9.grid(row=5, column=1, sticky=W , padx =35,pady=35)
btn10=Button(canvas,text=10,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(10),width=7, height=3)
btn10.grid(row=5, column=2, sticky=W , padx =35,pady=35)
btn11=Button(canvas,text=11,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(11),width=7, height=3)
btn11.grid(row=5, column=3, sticky=W , padx =35,pady=35)

btn12=Button(canvas,text=12,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(12),width=7, height=3)
btn12.grid(row=6, column=0, sticky=W , padx =35,pady=35)
btn13=Button(canvas,text=13,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(13),width=7, height=3)
btn13.grid(row=6, column=1, sticky=W , padx =35,pady=35)
btn14=Button(canvas,text=14,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(14),width=7, height=3)
btn14.grid(row=6, column=2, sticky=W , padx =35,pady=35)
btn15=Button(canvas,text=15,bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda : table_number(15),width=7, height=3)
btn15.grid(row=6, column=3, sticky=W , padx =35,pady=35)

btn19=Button(canvas,text="",bg='#355C7D',font='Helvetica 9 bold',fg="white",state=DISABLED,command=lambda :table_number(19),width=2, height=1).grid(row=3, column=4, sticky=W , padx =35,pady=35)
btn18=Button(canvas,text="",bg='#355C7D',font='Helvetica 9 bold',fg="white",state=DISABLED,command=lambda :table_number(18),width=2, height=1).grid(row=4, column=4, sticky=W , padx =35,pady=35)
btn17=Button(canvas,text="",bg='#355C7D',font='Helvetica 9 bold',fg="white",state=DISABLED,command=lambda :table_number(17),width=2, height=1).grid(row=5, column=4, sticky=W , padx =35,pady=35)
btn16=Button(canvas,text="",bg='#355C7D',font='Helvetica 9 bold',fg="white",state=DISABLED,command=lambda :table_number(16),width=2, height=1).grid(row=6, column=4, sticky=W , padx =35,pady=35)
#btn.append(Button(canvas,text="KITCHEN",bg='#355C7D',command=table_number,width=7, height=3).grid(row=2, column=0, sticky=W , padx =35,pady=35))

btn20=Button(canvas,text="KITCHEN",bg='#355C7D',font='Helvetica 9 bold',fg="white",command=lambda :table_number(20),width=7, height=3)
btn20.grid(row=2, column=0, sticky=W , padx =35,pady=35)
btn_reset=Button(canvas,text="RESET",bg="white",command=reset_color,width=5, height=1).grid(row=3, column=5, sticky=W , padx =30,pady=30)

# dictionary to fetch button names
btn_name={0:btn0,1:btn1,2:btn2,3:btn3,4:btn4,5:btn5,6:btn6,7:btn7,8:btn8,9:btn9,10:btn10,11:btn11,12:btn12,13:btn13,14:btn14,15:btn15,20:btn20}

# CREATING ALL THE CONNECTING LINES 
line2120=canvas.create_line(50,112,567,112,fill='#355C7D', width=10)
#canvas.itemconfigure(line2120,fill='brown')
line200=canvas.create_line(60,112,60,235,fill='#355C7D', width=10)
#line01=canvas.create_line(50,87,200,87,fill='green', width=10)  ## C06C84 pink
line01=canvas.create_line(50,235,200,235,fill='#355C7D', width=10)
line45=canvas.create_line(50,360,200,360,fill='#355C7D', width=10)
line89=canvas.create_line(50,485,200,485,fill='#355C7D', width=10)
line1213=canvas.create_line(50,610,200,610,fill='#355C7D', width=10)

line12=canvas.create_line(200,235,350,235,fill='#355C7D', width=10)
line56=canvas.create_line(200,360,350,360,fill='#355C7D', width=10)
line910=canvas.create_line(200,485,350,485,fill='#355C7D', width=10)
line1314=canvas.create_line(200,610,350,610,fill='#355C7D', width=10)

line23=canvas.create_line(350,235,450,235,fill='#355C7D', width=10)
line67=canvas.create_line(350,360,450,360,fill='#355C7D', width=10)
line1011=canvas.create_line(350,485,450,485,fill='#355C7D', width=10)
line1415=canvas.create_line(350,610,450,610,fill='#355C7D', width=10)

line319=canvas.create_line(450,235,550,235,fill='#355C7D', width=10)
line718=canvas.create_line(450,360,550,360,fill='#355C7D', width=10)
line1117=canvas.create_line(450,485,550,485,fill='#355C7D', width=10)
line1516=canvas.create_line(450,610,550,610,fill='#355C7D', width=10)

line04=canvas.create_line(60,235,60,360,fill='#355C7D', width=10)
line48=canvas.create_line(60,360,60,485,fill='#355C7D', width=10)
line812=canvas.create_line(60,485,60,610,fill='#355C7D', width=10)

line15=canvas.create_line(195,235,195,360,fill='#355C7D', width=10)
line59=canvas.create_line(195,360,195,485,fill='#355C7D', width=10)
line913=canvas.create_line(195,485,195,610,fill='#355C7D', width=10)

line26=canvas.create_line(320,235,320,360,fill='#355C7D', width=10)
line610=canvas.create_line(320,360,320,485,fill='#355C7D', width=10)
line1014=canvas.create_line(320,485,320,610,fill='#355C7D', width=10)

line37=canvas.create_line(450,235,450,360,fill='#355C7D', width=10)
line711=canvas.create_line(450,360,450,485,fill='#355C7D', width=10)
line1115=canvas.create_line(450,485,450,610,fill='#355C7D', width=10)

line1921=canvas.create_line(562,107,562,235,fill='#355C7D', width=10)
line1819=canvas.create_line(562,235,562,360,fill='#355C7D', width=10)
line1718=canvas.create_line(562,360,562,485,fill='#355C7D', width=10)
line1617=canvas.create_line(562,485,562,610,fill='#355C7D', width=10)

# USING THIS DICTIONARY TO MAP THE LINES AND CHANGE THEIR COLOR TO SHOW PATH
line_name={"L200":line200,"L01":line01,"L12":line12,"L23":line23,"L319":line319,"L45":line45,"L56":line56,"L67":line67,"L718":line718,"L89":line89,"L910":line910,"L1011":line1011,"L1117":line1117,"L1213":line1213,"L1314":line1314,"L1415":line1415,"L1516":line1516,"L04":line04,"L48":line48,"L812":line812,"L15":line15,"L59":line59,"L913":line913,"L26":line26,"L610":line610,"L1014":line1014,"L37":line37,"L711":line711,"L1115":line1115,"L1617":line1617,"L1718":line1718,"L1819":line1819,"L1921":line1921,"L2120":line2120}

window.mainloop()
