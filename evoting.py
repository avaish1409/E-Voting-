# Evoting

from tkinter import*
import os
fl=open("evoting.txt","r+")
vf1=open("president.txt","r+")
vf2=open("vice_president.txt","r+")
vf3=open("prime_minister.txt","r+")
vf4=open("deputy_pm.txt","r+")
vf5=open("speaker.txt","r+")
r=Tk()
r.title("E-Voting System")
r.geometry("900x600")
pic1=PhotoImage(file="login.png")
p2=vp2=dp2=sp=pm=0
def check():
	rolls=list()
	l=fl.readlines()
	for i in l:
		l2=i.split(";")
		rolls.append(l2[0])
	if rolls.count(str(rno.get()))==0:
		print("Allowed!")
		fl.write(str(rno.get())+";"+str(name.get())+";"+str(dob.get())+"\n")
		r.destroy()
	else :
		print("Invalid Entry!!")
		fl.seek(0)


def vote():
	#r.destroy()
	r=Tk()
	r.title("E-Voting System")
	r.geometry("800x700")
	Tops=Frame(r, width=1600,relief=SUNKEN)
	Tops.pack(side=TOP)

	f1=Frame(r,width=800,height=700,relief=SUNKEN)
	f1.pack(side=LEFT)
	
	
	lb02=Label(Tops,font=('arial',50,'bold'),text="E-Voting System",fg="Black")
	lb02.grid(row=0,column=0)

	pic2=PhotoImage(file="vote.png",height=500)
	lbi2=Label(f1,image=pic2)
	lbi2.image=pic2
	lbi2.grid(row=0,column=3,rowspan=40,padx=100)
	
	p=IntVar()
	vp=IntVar()
	pm=IntVar()
	dp=IntVar()
	sp=IntVar()
		
	def submit():
		r.quit()
		p2=p.get()
		vp2=vp.get()
		pm2=pm.get()
		dp2=dp.get()
		sp2=sp.get()
		print(p2)
		def fun(a,v,n):
			l=a.readlines()
			temp=open("temp.txt","w")
			print(int(v))
			for i in range(len(l)):
				if int(v)!=i+1 :
					temp.write(l[i])
					print("NA")
				else :
					print("working")
					t=l[i].split(";")
					t[1]=str(int(t[1])+1)
					t=t[0]+";"+t[1]+"\n"
					temp.write(t)
			a.close()
			temp.close()
			os.remove(n)
			os.rename("temp.txt",n)
			a=open(n,"r+")
		pl=[[vf1,p2,"president.txt"],[vf2,vp2,"vice_president.txt"],[vf3,pm2,"prime_minister.txt"],[vf4,dp2,"deputy_pm.txt"],[vf5,sp2,"speaker.txt"]]
		for i in pl:
			fun(i[0],i[1],i[2])


	lbl1=Label(f1,text="President :")
	lbl1.grid(row=0,column=0)
	r11=Radiobutton(f1,text="Pranab Mukharji",variable=p,value=1)
	r11.grid(row=1,column=1)
	r12=Radiobutton(f1,text="Ramnath Govind",variable=p,value=2)
	r12.grid(row=2,column=1)
	r13=Radiobutton(f1,text="Pratibha Patil",variable=p,value=3)
	r13.grid(row=3,column=1)
	lbl2=Label(f1,text="Vice-President :")
	lbl2.grid(row=4,column=0)
	r21=Radiobutton(f1,text="Venkaya Naidu",variable=vp,value=1)
	r21.grid(row=5,column=1)
	r22=Radiobutton(f1,text="Hamid Ansari",variable=vp,value=2)
	r22.grid(row=6,column=1)
	r23=Radiobutton(f1,text="Amit Shah",variable=vp,value=3)
	r23.grid(row=7,column=1)
	lbl3=Label(f1,text="Prime Minister :")
	lbl3.grid(row=8,column=0)
	r31=Radiobutton(f1,text="Narendra Modi",variable=pm,value=1)
	r31.grid(row=9,column=1)
	r32=Radiobutton(f1,text="Rahul Gandhi",variable=pm,value=2)
	r32.grid(row=10,column=1)
	r33=Radiobutton(f1,text="Mamta Banerji",variable=pm,value=3)
	r33.grid(row=11,column=1)
	lbl4=Label(f1,text="Deputy Prime Minister :")
	lbl4.grid(row=12,column=0)
	r41=Radiobutton(f1,text="Pranab Mukharji1",variable=dp,value=1)
	r41.grid(row=13,column=1)
	r42=Radiobutton(f1,text="Pranab Mukharji2",variable=dp,value=2)
	r42.grid(row=14,column=1)
	r43=Radiobutton(f1,text="Pranab Mukharji3",variable=dp,value=3)
	r43.grid(row=15,column=1)
	lbl5=Label(f1,text="Speaker :")
	lbl5.grid(row=16,column=0)
	r51=Radiobutton(f1,text="Pranab Mukharji4",variable=sp,value=1)
	r51.grid(row=17,column=1)
	r52=Radiobutton(f1,text="Pranab Mukharji5",variable=sp,value=2)
	r52.grid(row=18,column=1)
	r53=Radiobutton(f1,text="Pranab Mukharji6",variable=sp,value=3)
	r53.grid(row=19,column=1)
	b2=Button(f1,text="Submit\nResponse",command=submit,fg="white",height=3,width=20,bg="blue")
	b2.grid(row=18,column=3,rowspan=2)
	mainloop()
	print(p2)
	


rno=StringVar()
name=StringVar()
dob=StringVar()
r.title("E-Voting System")
Tops=Frame(r, width=600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(r,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

lb0=Label(Tops,font=('arial',50,'bold'),text="E-Voting System",fg="Black")
lb0.grid(row=0,column=0)
lbi=Label(f1,image=pic1)
lbi.image=pic1
lbi.grid(row=0,column=3,rowspan=6,padx=100)
lb1=Label(f1,text="Roll No. :")
lb1.grid(row=0,column=1)
e1=Entry(f1,textvariable=rno,justify="right")
e1.grid(row=1,column=2)
lb2=Label(f1,text="Name :")
lb2.grid(row=2,column=1)
e2=Entry(f1,textvariable=name,justify="right")
e2.grid(row=3,column=2)
lb3=Label(f1,text="Date of Birth :")
lb3.grid(row=4,column=1)
e3=Entry(f1,textvariable=dob,justify="right")
e3.grid(row=5,column=2)
b1=Button(f1,text="Submit",command=check)
b1.grid(row=6,column=2)
r.mainloop()
vote()






