from tkinter import Entry,Label,Button,END,Tk,mainloop
import pandas as pd
from hmm import *
from config import *

master = Tk()
master.geometry('500x500')

parameters = Hmm_parameters()

def show_transition_matrix():
  p_ss = e_ss.get()
  p_sr = e_sr.get()
  p_rs = e_rs.get()
  p_rr = e_rr.get()

  p_s = e_s.get()
  p_r = e_r.get()

  p_sh = e_sh.get()
  p_sg = e_sg.get()
  p_rh = e_rh.get()
  p_rg = e_rg.get()

  transition_matrix = [p_ss,p_sr,p_rs,p_rr]
  emission_matrix = [p_sh,p_sg,p_rh,p_rg]
  prob_weather = [p_s,p_r]
  parameters.update_values(transition_matrix,prob_weather,emission_matrix)
  parameters.display_parameters()
  
                 

Label(master,text = 'Sunny').grid(row =1,column=0)
Label(master,text = 'Rainy').grid(row = 2,column=0)
Label(master,text = 'Sunny').grid(row =0,column=1)
Label(master,text = 'Rainy').grid(row = 0,column=2)

e_ss = Entry(master)
e_sr = Entry(master)
e_rs = Entry(master)
e_rr = Entry(master)

e_ss.insert(END,0.8)
e_sr.insert(END,0.2)
e_rs.insert(END,0.4)
e_rr.insert(END,0.6)

e_ss.grid(row = 1,column = 1)
e_sr.grid(row = 1,column = 2)
e_rs.grid(row = 2,column = 1)
e_rr.grid(row = 2,column = 2)

Label(master,text = 'p(sunny)').grid(row = 4,column=0)
Label(master,text = 'p(rainy)').grid(row = 5,column=0)
e_s = Entry(master)
e_r = Entry(master)
e_s.insert(END,0.8)
e_r.insert(END,0.2)
e_s.grid(row = 4,column = 1)
e_r.grid(row = 5,column = 1)


Label(master,text = 'Sunny').grid(row =7,column=0)
Label(master,text = 'Rainy').grid(row = 8,column=0)
Label(master,text = 'Happy').grid(row =6,column=1)
Label(master,text = 'Grumpy').grid(row = 6,column=2)

e_sh = Entry(master)
e_sg = Entry(master)
e_rh = Entry(master)
e_rg = Entry(master)

e_sh.insert(END,0.8)
e_sg.insert(END,0.2)
e_rh.insert(END,0.4)
e_rg.insert(END,0.6)

e_sh.grid(row = 7,column = 1)
e_sg.grid(row = 7,column = 2)
e_rh.grid(row = 8,column = 1)
e_rg.grid(row = 8,column = 2)

Button(master,text = 'show',command = show_transition_matrix).grid(row=9,column=0)
Button(master,text = 'Quit',command = master.quit).grid(row=9,column=1)

mainloop()