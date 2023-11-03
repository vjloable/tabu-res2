import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
import time
import threading as thd
import Main as tabu

class ThreadedTask(thd.Thread):
	def __init__(self, prog_bar, iters, subj, teach, btn, status):
		super(ThreadedTask, self).__init__()
		self.prog_bar = prog_bar
		self.iters = iters
		self.subj = subj
		self.teach = teach
		self.btn = btn
		self.status = status

	def run(self):
		#tabu.eval_gui(100000, inputs_subjects, inputs_teachers)
		if tabu.eval_gui(self.iters, self.subj, self.teach):
			self.prog_bar.stop()
			self.status["text"] = "Finished! An Excel file was created in this directory."
			time.sleep(2)
			self.status["text"] = "Idle"
			self.btn["state"] = "normal"

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack(padx=2, pady=5)
		self.create_widgets()

	def create_widgets(self):
		#self.frame_subject()
		iters = ["10k","25k","50k","75k","100k","200k","300k","400k","500k"]

		self.create_choose()
		
		self.FRM_Eval = tk.Frame(self)
		self.FRM_Eval.grid(row=6,column=0,pady=15)
		
		self.LBL_Iter = tk.Label(self.FRM_Eval)
		self.LBL_Iter["text"] = "Iterations:"
		self.LBL_Iter.grid(row=0,column=0,pady=2,padx=2)
		self.OPM_Iter_var = tk.StringVar()
		self.OPM_Iter_var.set(iters[4])
		self.OPM_Iter = tk.OptionMenu(self.FRM_Eval, self.OPM_Iter_var, *iters)
		self.OPM_Iter.config(width=6)
		self.OPM_Iter.grid(row=1,column=0)

		self.BTN_Eval = tk.Button(self.FRM_Eval)
		self.BTN_Eval["text"] = "Evaluate"
		self.BTN_Eval["command"] = self.evaluate
		self.BTN_Eval.config(width=20)
		self.BTN_Eval.grid(row=0, column=1, pady=2)
		
		self.PRG_Eval = Progressbar(self.FRM_Eval, length=300, style='grey.Horizontal.TProgressbar', mode='determinate')
		self.PRG_Eval.grid(row=0,column=2,padx=3)

		self.BTN_Quit = tk.Button(self.FRM_Eval)
		self.BTN_Quit["text"] = "QUIT"
		self.BTN_Quit["fg"] = "red"
		self.BTN_Quit["command"] = self.master.destroy
		self.BTN_Quit.config(width=20)
		self.BTN_Quit.grid(row=1, column=1, pady=2)

		self.LBL_Status = tk.Label(self.FRM_Eval)
		self.LBL_Status["text"] = "Idle"
		self.LBL_Status.grid(row=1,column=2,pady=2,padx=2,sticky=tk.W)

	def pbar_eval(self, etime):
		#val = 0
		t = etime + 3
		for value in range(t+1):
			self.PRG_Eval['value'] = (100/t) * value
			self.update_idletasks() 
			time.sleep(1) 
		time.sleep(2)
		self.PRG_Eval['value'] = 0

	def process_queue(self):
		try:
			msg = self.queue.get(0)
			# Show result of the task if needed
			self.prog_bar.stop()
		except Queue.Empty:
			self.master.after(100, self.process_queue)
	
	def evaluate(self):
		self.BTN_Eval["state"] = "disabled"
		self.PRG_Eval.start()
		self.LBL_Status["text"] = "Generating the schedules..."
	###
		days_a = [
			self.OPM_FFa_var.get(), self.OPM_EEa_var.get(), self.OPM_SSSa_var.get(),
			self.OPM_RRa_var.get(), self.OPM_MMa_var.get(), self.OPM_PPa_var.get(),
			self.OPM_CCa_var.get(), self.OPM_BBa_var.get(), self.OPM_CSSa_var.get(),
			self.OPM_TTa_var.get(), self.OPM_AAa_var.get(), self.OPM_ENNa_var.get()
		]
		tslots_a = [
			self.OPM_Fa_var.get(), self.OPM_Ea_var.get(), self.OPM_SSa_var.get(),
			self.OPM_Ra_var.get(), self.OPM_Ma_var.get(), self.OPM_Pa_var.get(),
			self.OPM_Ca_var.get(), self.OPM_Ba_var.get(), self.OPM_CSa_var.get(),
			self.OPM_Ta_var.get(), self.OPM_Aa_var.get(), self.OPM_ENa_var.get()
		]

		days_b = [
			self.OPM_FFb_var.get(), self.OPM_EEb_var.get(), self.OPM_SSSb_var.get(),
			self.OPM_RRb_var.get(), self.OPM_MMb_var.get(), self.OPM_PPb_var.get(),
			self.OPM_CCb_var.get(), self.OPM_BBb_var.get(), self.OPM_CSSb_var.get(),
			self.OPM_TTb_var.get(), self.OPM_AAb_var.get(), self.OPM_ENNb_var.get()
		]
		tslots_b = [
			self.OPM_Fb_var.get(), self.OPM_Eb_var.get(), self.OPM_SSb_var.get(),
			self.OPM_Rb_var.get(), self.OPM_Mb_var.get(), self.OPM_Pb_var.get(),
			self.OPM_Cb_var.get(), self.OPM_Bb_var.get(), self.OPM_CSb_var.get(),
			self.OPM_Tb_var.get(), self.OPM_Ab_var.get(), self.OPM_ENb_var.get()
		]

		fpb_a = [
			self.CBN_Fa_var.get(), self.CBN_Ea_var.get(),
			self.CBN_SSa_var.get(), self.CBN_Ra_var.get(),
			self.CBN_Ma_var.get(), self.CBN_Pa_var.get(),
			self.CBN_Ca_var.get(), self.CBN_Ba_var.get(),
			self.CBN_CSa_var.get(), self.CBN_Ta_var.get(),
			self.CBN_Aa_var.get(), self.CBN_ENa_var.get()
		]
		fpb_b = [
			self.CBN_Fb_var.get(), self.CBN_Eb_var.get(),
			self.CBN_SSb_var.get(), self.CBN_Rb_var.get(),
			self.CBN_Mb_var.get(), self.CBN_Pb_var.get(),
			self.CBN_Cb_var.get(), self.CBN_Bb_var.get(),
			self.CBN_CSb_var.get(), self.CBN_Tb_var.get(),
			self.CBN_Ab_var.get(), self.CBN_ENb_var.get()
		]

		timeslots = {
			"Period 1":"0","Period 2":"1","Period 3":"2","Period 4":"3",
			"Period 5":"4","Period 6":"5","Period 7":"6","Period 8":"7"
		}

		day = {"MON":"0","TUE":"1","WED":"2","THU":"3"}
		iters = {
			"10k":10000,  "25k":25000,   "50k":50000,
			"75k":75000,  "100k":100000, "200k":200000,
			"300k":300000,"400k":400000, "500k":500000
			}
	###
		inputs_subjects = []
		inputs_teachers = []
		x, y, z = "", "", ""
		for i in range(12):
			x = str(timeslots[tslots_a[i]])
			y = str(day[days_a[i]])
			if fpb_a[i] == 1:
				z = "True"
			elif fpb_a[i] == 0:
				z = "False"
			inputs_subjects.append(x+"-"+y+"-"+z)

		for i in range(12):
			x = str(timeslots[tslots_b[i]])
			y = str(day[days_b[i]])
			if fpb_b[i] == 1:
				z = "True"
			elif fpb_b[i] == 0:
				z = "False"
			inputs_teachers.append(x+"-"+y+"-"+z)

		tabu_thread = ThreadedTask(self.PRG_Eval, iters[self.OPM_Iter_var.get()], inputs_subjects, inputs_teachers, self.BTN_Eval, self.LBL_Status)
		tabu_thread.start()

	def create_choose(self):
		timeslots = [
			"Period 1","Period 2","Period 3","Period 4","Period 5","Period 6","Period 7","Period 8"
		]

		day = [
			"MON","TUE","WED","THU"
		]

#FRM_A
	#FORM A HEAD
		self.LBL_F = tk.Label(self)
		self.LBL_F["text"] = "SUBJECTS' INITIAL PLACEMENT:"
		self.LBL_F.config(width=30)
		self.LBL_F.grid(row=0,column=0,pady=(14,5))
		self.FRM_A = tk.Frame(self, highlightthickness=1, highlightbackground="black")
		self.FRM_A.grid(row=1,column=0,pady=(2,2))
	#FILIPINO
		self.LBL_Fa = tk.Label(self.FRM_A)
		self.LBL_Fa["text"] = "FIL:"
		self.LBL_Fa.config(width=5)
		self.LBL_Fa.grid(row=0,column=0)
		self.OPM_FFa_var = tk.StringVar()
		self.OPM_FFa_var.set(day[0])
		self.OPM_FFa = tk.OptionMenu(self.FRM_A, self.OPM_FFa_var, *day)
		self.OPM_FFa.config(width=5)
		self.OPM_FFa.grid(row=0,column=1)
		self.OPM_Fa_var = tk.StringVar()
		self.OPM_Fa_var.set(timeslots[0])
		self.OPM_Fa = tk.OptionMenu(self.FRM_A, self.OPM_Fa_var, *timeslots)
		self.OPM_Fa.config(width=6)
		self.OPM_Fa.grid(row=0,column=2)
		self.CBN_Fa_var = tk.IntVar()
		self.CBN_Fa = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_Fa_var, onvalue=1, offvalue=0)
		self.CBN_Fa.grid(row=0,column=3,padx=(0,10))
	#ENGLISH
		self.LBL_Ea = tk.Label(self.FRM_A)
		self.LBL_Ea["text"] = "ENG:"
		self.LBL_Ea.config(width=5)
		self.LBL_Ea.grid(row=0,column=4)
		self.OPM_EEa_var = tk.StringVar()
		self.OPM_EEa_var.set(day[0])
		self.OPM_EEa = tk.OptionMenu(self.FRM_A, self.OPM_EEa_var, *day)
		self.OPM_EEa.config(width=5)
		self.OPM_EEa.grid(row=0,column=5)
		self.OPM_Ea_var = tk.StringVar()
		self.OPM_Ea_var.set(timeslots[0])
		self.OPM_Ea = tk.OptionMenu(self.FRM_A, self.OPM_Ea_var, *timeslots)
		self.OPM_Ea.config(width=6)
		self.OPM_Ea.grid(row=0,column=6)
		self.CBN_Ea_var = tk.IntVar()
		self.CBN_Ea = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_Ea_var, onvalue=1, offvalue=0)
		self.CBN_Ea.grid(row=0,column=7,padx=(0,10))
	#SOCSCI
		self.LBL_SSa = tk.Label(self.FRM_A)
		self.LBL_SSa["text"] = "SOC:"
		self.LBL_SSa.config(width=5)
		self.LBL_SSa.grid(row=0,column=8)
		self.OPM_SSSa_var = tk.StringVar()
		self.OPM_SSSa_var.set(day[0])
		self.OPM_SSSa = tk.OptionMenu(self.FRM_A, self.OPM_SSSa_var, *day)
		self.OPM_SSSa.config(width=5)
		self.OPM_SSSa.grid(row=0,column=9)
		self.OPM_SSa_var = tk.StringVar()
		self.OPM_SSa_var.set(timeslots[0])
		self.OPM_SSa = tk.OptionMenu(self.FRM_A, self.OPM_SSa_var, *timeslots)
		self.OPM_SSa.config(width=6)
		self.OPM_SSa.grid(row=0,column=10)
		self.CBN_SSa_var = tk.IntVar()
		self.CBN_SSa = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_SSa_var, onvalue=1, offvalue=0)
		self.CBN_SSa.grid(row=0,column=11,padx=(0,10))
	#RESEARCH
		self.LBL_Ra = tk.Label(self.FRM_A)
		self.LBL_Ra["text"] = " RES:  "
		self.LBL_Ra.config(width=5)
		self.LBL_Ra.grid(row=1,column=0)
		self.OPM_RRa_var = tk.StringVar()
		self.OPM_RRa_var.set(day[0])
		self.OPM_RRa = tk.OptionMenu(self.FRM_A, self.OPM_RRa_var, *day)
		self.OPM_RRa.config(width=5)
		self.OPM_RRa.grid(row=1,column=1)
		self.OPM_Ra_var = tk.StringVar()
		self.OPM_Ra_var.set(timeslots[0])
		self.OPM_Ra = tk.OptionMenu(self.FRM_A, self.OPM_Ra_var, *timeslots)
		self.OPM_Ra.config(width=6)
		self.OPM_Ra.grid(row=1,column=2)
		self.CBN_Ra_var = tk.IntVar()
		self.CBN_Ra = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_Ra_var, onvalue=1, offvalue=0)
		self.CBN_Ra.grid(row=1,column=3,padx=(0,10))
	#MATH
		self.LBL_Ma = tk.Label(self.FRM_A)
		self.LBL_Ma["text"] = "MATH:"
		self.LBL_Ma.config(width=5)
		self.LBL_Ma.grid(row=1,column=4)
		self.OPM_MMa_var = tk.StringVar()
		self.OPM_MMa_var.set(day[0])
		self.OPM_MMa = tk.OptionMenu(self.FRM_A, self.OPM_MMa_var, *day)
		self.OPM_MMa.config(width=5)
		self.OPM_MMa.grid(row=1,column=5)
		self.OPM_Ma_var = tk.StringVar()
		self.OPM_Ma_var.set(timeslots[0])
		self.OPM_Ma = tk.OptionMenu(self.FRM_A, self.OPM_Ma_var, *timeslots)
		self.OPM_Ma.config(width=6)
		self.OPM_Ma.grid(row=1,column=6)
		self.CBN_Ma_var = tk.IntVar()
		self.CBN_Ma = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_Ma_var, onvalue=1, offvalue=0)
		self.CBN_Ma.grid(row=1,column=7,padx=(0,10))
	#PHYSICS
		self.LBL_Pa = tk.Label(self.FRM_A)
		self.LBL_Pa["text"] = "PHYS: "
		self.LBL_Pa.config(width=5)
		self.LBL_Pa.grid(row=1,column=8)
		self.OPM_PPa_var = tk.StringVar()
		self.OPM_PPa_var.set(day[0])
		self.OPM_PPa = tk.OptionMenu(self.FRM_A, self.OPM_PPa_var, *day)
		self.OPM_PPa.config(width=5)
		self.OPM_PPa.grid(row=1,column=9)
		self.OPM_Pa_var = tk.StringVar()
		self.OPM_Pa_var.set(timeslots[0])
		self.OPM_Pa = tk.OptionMenu(self.FRM_A, self.OPM_Pa_var, *timeslots)
		self.OPM_Pa.config(width=6)
		self.OPM_Pa.grid(row=1,column=10)
		self.CBN_Pa_var = tk.IntVar()
		self.CBN_Pa = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_Pa_var, onvalue=1, offvalue=0)
		self.CBN_Pa.grid(row=1,column=11,padx=(0,10))
	#CHEMISTRY
		self.LBL_Ca = tk.Label(self.FRM_A)
		self.LBL_Ca["text"] = "CHEM:"
		self.LBL_Ca.config(width=5)
		self.LBL_Ca.grid(row=2,column=0)
		self.OPM_CCa_var = tk.StringVar()
		self.OPM_CCa_var.set(day[0])
		self.OPM_CCa = tk.OptionMenu(self.FRM_A, self.OPM_CCa_var, *day)
		self.OPM_CCa.config(width=5)
		self.OPM_CCa.grid(row=2,column=1)
		self.OPM_Ca_var = tk.StringVar()
		self.OPM_Ca_var.set(timeslots[0])
		self.OPM_Ca = tk.OptionMenu(self.FRM_A, self.OPM_Ca_var, *timeslots)
		self.OPM_Ca.config(width=6)
		self.OPM_Ca.grid(row=2,column=2)
		self.CBN_Ca_var = tk.IntVar()
		self.CBN_Ca = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_Ca_var, onvalue=1, offvalue=0)
		self.CBN_Ca.grid(row=2,column=3,padx=(0,10))
	#BIOLOGY
		self.LBL_Ba = tk.Label(self.FRM_A)
		self.LBL_Ba["text"] = " BIO: "
		self.LBL_Ba.config(width=5)
		self.LBL_Ba.grid(row=2,column=4)
		self.OPM_BBa_var = tk.StringVar()
		self.OPM_BBa_var.set(day[0])
		self.OPM_BBa = tk.OptionMenu(self.FRM_A, self.OPM_BBa_var, *day)
		self.OPM_BBa.config(width=5)
		self.OPM_BBa.grid(row=2,column=5)
		self.OPM_Ba_var = tk.StringVar()
		self.OPM_Ba_var.set(timeslots[0])
		self.OPM_Ba = tk.OptionMenu(self.FRM_A, self.OPM_Ba_var, *timeslots)
		self.OPM_Ba.config(width=6)
		self.OPM_Ba.grid(row=2,column=6)
		self.CBN_Ba_var = tk.IntVar()
		self.CBN_Ba = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_Ba_var, onvalue=1, offvalue=0)
		self.CBN_Ba.grid(row=2,column=7,padx=(0,10))
	#COMPSCI
		self.LBL_CSa = tk.Label(self.FRM_A)
		self.LBL_CSa["text"] = "COMP:"
		self.LBL_CSa.config(width=5)
		self.LBL_CSa.grid(row=2,column=8)
		self.OPM_CSSa_var = tk.StringVar()
		self.OPM_CSSa_var.set(day[0])
		self.OPM_CSSa = tk.OptionMenu(self.FRM_A, self.OPM_CSSa_var, *day)
		self.OPM_CSSa.config(width=5)
		self.OPM_CSSa.grid(row=2,column=9)
		self.OPM_CSa_var = tk.StringVar()
		self.OPM_CSa_var.set(timeslots[0])
		self.OPM_CSa = tk.OptionMenu(self.FRM_A, self.OPM_CSa_var, *timeslots)
		self.OPM_CSa.config(width=6)
		self.OPM_CSa.grid(row=2,column=10)
		self.CBN_CSa_var = tk.IntVar()
		self.CBN_CSa = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_CSa_var, onvalue=1, offvalue=0)
		self.CBN_CSa.grid(row=2,column=11,padx=(0,10))
	#TECH
		self.LBL_Ta = tk.Label(self.FRM_A)
		self.LBL_Ta["text"] = "  TECH: "
		self.LBL_Ta.config(width=5)
		self.LBL_Ta.grid(row=3,column=0)
		self.OPM_TTa_var = tk.StringVar()
		self.OPM_TTa_var.set(day[0])
		self.OPM_TTa = tk.OptionMenu(self.FRM_A, self.OPM_TTa_var, *day)
		self.OPM_TTa.config(width=5)
		self.OPM_TTa.grid(row=3,column=1)
		self.OPM_Ta_var = tk.StringVar()
		self.OPM_Ta_var.set(timeslots[0])
		self.OPM_Ta = tk.OptionMenu(self.FRM_A, self.OPM_Ta_var, *timeslots)
		self.OPM_Ta.config(width=6)
		self.OPM_Ta.grid(row=3,column=2)
		self.CBN_Ta_var = tk.IntVar()
		self.CBN_Ta = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_Ta_var, onvalue=1, offvalue=0)
		self.CBN_Ta.grid(row=3,column=3,padx=(0,10))
	#AGRI
		self.LBL_Aa = tk.Label(self.FRM_A)
		self.LBL_Aa["text"] = "AGRI: "
		self.LBL_Aa.config(width=5)
		self.LBL_Aa.grid(row=3,column=4)
		self.OPM_AAa_var = tk.StringVar()
		self.OPM_AAa_var.set(day[0])
		self.OPM_AAa = tk.OptionMenu(self.FRM_A, self.OPM_AAa_var, *day)
		self.OPM_AAa.config(width=5)
		self.OPM_AAa.grid(row=3,column=5)
		self.OPM_Aa_var = tk.StringVar()
		self.OPM_Aa_var.set(timeslots[0])
		self.OPM_Aa = tk.OptionMenu(self.FRM_A, self.OPM_Aa_var, *timeslots)
		self.OPM_Aa.config(width=6)
		self.OPM_Aa.grid(row=3,column=6)
		self.CBN_Aa_var = tk.IntVar()
		self.CBN_Aa = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_Aa_var, onvalue=1, offvalue=0)
		self.CBN_Aa.grid(row=3,column=7,padx=(0,10))
	#ENGINEERTNG
		self.LBL_ENa = tk.Label(self.FRM_A)
		self.LBL_ENa["text"] = " ENGI: "
		self.LBL_ENa.config(width=5)
		self.LBL_ENa.grid(row=3,column=8)
		self.OPM_ENNa_var = tk.StringVar()
		self.OPM_ENNa_var.set(day[0])
		self.OPM_ENNa = tk.OptionMenu(self.FRM_A, self.OPM_ENNa_var, *day)
		self.OPM_ENNa.config(width=5)
		self.OPM_ENNa.grid(row=3,column=9)
		self.OPM_ENa_var = tk.StringVar()
		self.OPM_ENa_var.set(timeslots[0])
		self.OPM_ENa = tk.OptionMenu(self.FRM_A, self.OPM_ENa_var, *timeslots)
		self.OPM_ENa.config(width=6)
		self.OPM_ENa.grid(row=3,column=10)
		self.CBN_ENa_var = tk.IntVar()
		self.CBN_ENa = tk.Checkbutton(self.FRM_A, text="F.P.B", variable=self.CBN_ENa_var, onvalue=1, offvalue=0)
		self.CBN_ENa.grid(row=3,column=11,padx=(0,10))

	#First Period BIAS
		def BTN_Checkall_A_select():
			self.CBN_Fa_var.set(1)
			self.CBN_Ea_var.set(1)
			self.CBN_SSa_var.set(1)
			self.CBN_Ra_var.set(1)
			self.CBN_Ma_var.set(1)
			self.CBN_Pa_var.set(1)
			self.CBN_Ca_var.set(1)
			self.CBN_Ba_var.set(1)
			self.CBN_CSa_var.set(1)
			self.CBN_Ta_var.set(1)
			self.CBN_Aa_var.set(1)
			self.CBN_ENa_var.set(1)
			pass
		def BTN_Resetall_A_select():
			self.CBN_Fa_var.set(0)
			self.CBN_Ea_var.set(0)
			self.CBN_SSa_var.set(0)
			self.CBN_Ra_var.set(0)
			self.CBN_Ma_var.set(0)
			self.CBN_Pa_var.set(0)
			self.CBN_Ca_var.set(0)
			self.CBN_Ba_var.set(0)
			self.CBN_CSa_var.set(0)
			self.CBN_Ta_var.set(0)
			self.CBN_Aa_var.set(0)
			self.CBN_ENa_var.set(0)
			
		self.FRM_FPBa = tk.Frame(self)
		self.FRM_FPBa.grid(row=2,column=0)
		self.LBL_FPB_A = tk.Label(self.FRM_FPBa)
		self.LBL_FPB_A["text"] = "F.P.B = First Period Bias"
		self.LBL_FPB_A.grid(row=0,column=0,padx=(0,10))
		self.BTN_Checkall_A = tk.Button(self.FRM_FPBa)
		self.BTN_Checkall_A["text"] = "CHECK ALL"
		self.BTN_Checkall_A["command"] = BTN_Checkall_A_select
		self.BTN_Checkall_A.config(width=12)
		self.BTN_Checkall_A.grid(row=0,column=1,padx=(0,5))
		self.BTN_Resetall_A = tk.Button(self.FRM_FPBa)
		self.BTN_Resetall_A["text"] = "RESET ALL CHECKS"
		self.BTN_Resetall_A["fg"] = "red"
		self.BTN_Resetall_A["command"] = BTN_Resetall_A_select
		self.BTN_Resetall_A.config(width=18)
		self.BTN_Resetall_A.grid(row=0,column=2)

#FRM_B
	#FORM B HEAD
		self.LBL_F = tk.Label(self)
		self.LBL_F["text"] = "TEACHERS' PREFERENCE:"
		self.LBL_F.config(width=20)
		self.LBL_F.grid(row=3,column=0,pady=(14,5))
		self.FRM_B = tk.Frame(self, highlightthickness=1, highlightbackground="black")
		self.FRM_B.grid(row=4,column=0,pady=(2,2))
	#FILIPINO
		self.LBL_Fb = tk.Label(self.FRM_B)
		self.LBL_Fb["text"] = "FIL:"
		self.LBL_Fb.config(width=5)
		self.LBL_Fb.grid(row=0,column=0)
		self.OPM_FFb_var = tk.StringVar()
		self.OPM_FFb_var.set(day[0])
		self.OPM_FFb = tk.OptionMenu(self.FRM_B, self.OPM_FFb_var, *day)
		self.OPM_FFb.config(width=5)
		self.OPM_FFb.grid(row=0,column=1)
		self.OPM_Fb_var = tk.StringVar()
		self.OPM_Fb_var.set(timeslots[0])
		self.OPM_Fb = tk.OptionMenu(self.FRM_B, self.OPM_Fb_var, *timeslots)
		self.OPM_Fb.config(width=6)
		self.OPM_Fb.grid(row=0,column=2)
		self.CBN_Fb_var = tk.IntVar()
		self.CBN_Fb = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_Fb_var, onvalue=1, offvalue=0)
		self.CBN_Fb.grid(row=0,column=3,padx=(0,10))
	#ENGLISH
		self.LBL_Eb = tk.Label(self.FRM_B)
		self.LBL_Eb["text"] = "ENG:"
		self.LBL_Eb.config(width=5)
		self.LBL_Eb.grid(row=0,column=4)
		self.OPM_EEb_var = tk.StringVar()
		self.OPM_EEb_var.set(day[0])
		self.OPM_EEb = tk.OptionMenu(self.FRM_B, self.OPM_EEb_var, *day)
		self.OPM_EEb.config(width=5)
		self.OPM_EEb.grid(row=0,column=5)
		self.OPM_Eb_var = tk.StringVar()
		self.OPM_Eb_var.set(timeslots[0])
		self.OPM_Eb = tk.OptionMenu(self.FRM_B, self.OPM_Eb_var, *timeslots)
		self.OPM_Eb.config(width=6)
		self.OPM_Eb.grid(row=0,column=6)
		self.CBN_Eb_var = tk.IntVar()
		self.CBN_Eb = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_Eb_var, onvalue=1, offvalue=0)
		self.CBN_Eb.grid(row=0,column=7,padx=(0,10))
	#SOCSCI
		self.LBL_SSb = tk.Label(self.FRM_B)
		self.LBL_SSb["text"] = "SOC:"
		self.LBL_SSb.config(width=5)
		self.LBL_SSb.grid(row=0,column=8)
		self.OPM_SSSb_var = tk.StringVar()
		self.OPM_SSSb_var.set(day[0])
		self.OPM_SSSb = tk.OptionMenu(self.FRM_B, self.OPM_SSSb_var, *day)
		self.OPM_SSSb.config(width=5)
		self.OPM_SSSb.grid(row=0,column=9)
		self.OPM_SSb_var = tk.StringVar()
		self.OPM_SSb_var.set(timeslots[0])
		self.OPM_SSb = tk.OptionMenu(self.FRM_B, self.OPM_SSb_var, *timeslots)
		self.OPM_SSb.config(width=6)
		self.OPM_SSb.grid(row=0,column=10)
		self.CBN_SSb_var = tk.IntVar()
		self.CBN_SSb = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_SSb_var, onvalue=1, offvalue=0)
		self.CBN_SSb.grid(row=0,column=11,padx=(0,10))
	#RESEARCH
		self.LBL_Rb = tk.Label(self.FRM_B)
		self.LBL_Rb["text"] = " RES:  "
		self.LBL_Rb.config(width=5)
		self.LBL_Rb.grid(row=1,column=0)
		self.OPM_RRb_var = tk.StringVar()
		self.OPM_RRb_var.set(day[0])
		self.OPM_RRb = tk.OptionMenu(self.FRM_B, self.OPM_RRb_var, *day)
		self.OPM_RRb.config(width=5)
		self.OPM_RRb.grid(row=1,column=1)
		self.OPM_Rb_var = tk.StringVar()
		self.OPM_Rb_var.set(timeslots[0])
		self.OPM_Rb = tk.OptionMenu(self.FRM_B, self.OPM_Rb_var, *timeslots)
		self.OPM_Rb.config(width=6)
		self.OPM_Rb.grid(row=1,column=2)
		self.CBN_Rb_var = tk.IntVar()
		self.CBN_Rb = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_Rb_var, onvalue=1, offvalue=0)
		self.CBN_Rb.grid(row=1,column=3,padx=(0,10))
	#MATH
		self.LBL_Mb = tk.Label(self.FRM_B)
		self.LBL_Mb["text"] = "MATH:"
		self.LBL_Mb.config(width=5)
		self.LBL_Mb.grid(row=1,column=4)
		self.OPM_MMb_var = tk.StringVar()
		self.OPM_MMb_var.set(day[0])
		self.OPM_MMb = tk.OptionMenu(self.FRM_B, self.OPM_MMb_var, *day)
		self.OPM_MMb.config(width=5)
		self.OPM_MMb.grid(row=1,column=5)
		self.OPM_Mb_var = tk.StringVar()
		self.OPM_Mb_var.set(timeslots[0])
		self.OPM_Mb = tk.OptionMenu(self.FRM_B, self.OPM_Mb_var, *timeslots)
		self.OPM_Mb.config(width=6)
		self.OPM_Mb.grid(row=1,column=6)
		self.CBN_Mb_var = tk.IntVar()
		self.CBN_Mb = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_Mb_var, onvalue=1, offvalue=0)
		self.CBN_Mb.grid(row=1,column=7,padx=(0,10))
	#PHYSICS
		self.LBL_Pb = tk.Label(self.FRM_B)
		self.LBL_Pb["text"] = "PHYS: "
		self.LBL_Pb.config(width=5)
		self.LBL_Pb.grid(row=1,column=8)
		self.OPM_PPb_var = tk.StringVar()
		self.OPM_PPb_var.set(day[0])
		self.OPM_PPb = tk.OptionMenu(self.FRM_B, self.OPM_PPb_var, *day)
		self.OPM_PPb.config(width=5)
		self.OPM_PPb.grid(row=1,column=9)
		self.OPM_Pb_var = tk.StringVar()
		self.OPM_Pb_var.set(timeslots[0])
		self.OPM_Pb = tk.OptionMenu(self.FRM_B, self.OPM_Pb_var, *timeslots)
		self.OPM_Pb.config(width=6)
		self.OPM_Pb.grid(row=1,column=10)
		self.CBN_Pb_var = tk.IntVar()
		self.CBN_Pb = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_Pb_var, onvalue=1, offvalue=0)
		self.CBN_Pb.grid(row=1,column=11,padx=(0,10))
	#CHEMISTRY
		self.LBL_Cb = tk.Label(self.FRM_B)
		self.LBL_Cb["text"] = "CHEM:"
		self.LBL_Cb.config(width=5)
		self.LBL_Cb.grid(row=2,column=0)
		self.OPM_CCb_var = tk.StringVar()
		self.OPM_CCb_var.set(day[0])
		self.OPM_CCb = tk.OptionMenu(self.FRM_B, self.OPM_CCb_var, *day)
		self.OPM_CCb.config(width=5)
		self.OPM_CCb.grid(row=2,column=1)
		self.OPM_Cb_var = tk.StringVar()
		self.OPM_Cb_var.set(timeslots[0])
		self.OPM_Cb = tk.OptionMenu(self.FRM_B, self.OPM_Cb_var, *timeslots)
		self.OPM_Cb.config(width=6)
		self.OPM_Cb.grid(row=2,column=2)
		self.CBN_Cb_var = tk.IntVar()
		self.CBN_Cb = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_Cb_var, onvalue=1, offvalue=0)
		self.CBN_Cb.grid(row=2,column=3,padx=(0,10))
	#BIOLOGY
		self.LBL_Bb = tk.Label(self.FRM_B)
		self.LBL_Bb["text"] = " BIO: "
		self.LBL_Bb.config(width=5)
		self.LBL_Bb.grid(row=2,column=4)
		self.OPM_BBb_var = tk.StringVar()
		self.OPM_BBb_var.set(day[0])
		self.OPM_BBb = tk.OptionMenu(self.FRM_B, self.OPM_BBb_var, *day)
		self.OPM_BBb.config(width=5)
		self.OPM_BBb.grid(row=2,column=5)
		self.OPM_Bb_var = tk.StringVar()
		self.OPM_Bb_var.set(timeslots[0])
		self.OPM_Bb = tk.OptionMenu(self.FRM_B, self.OPM_Bb_var, *timeslots)
		self.OPM_Bb.config(width=6)
		self.OPM_Bb.grid(row=2,column=6)
		self.CBN_Bb_var = tk.IntVar()
		self.CBN_Bb = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_Bb_var, onvalue=1, offvalue=0)
		self.CBN_Bb.grid(row=2,column=7,padx=(0,10))
	#COMPSCI
		self.LBL_CSb = tk.Label(self.FRM_B)
		self.LBL_CSb["text"] = "COMP:"
		self.LBL_CSb.config(width=5)
		self.LBL_CSb.grid(row=2,column=8)
		self.OPM_CSSb_var = tk.StringVar()
		self.OPM_CSSb_var.set(day[0])
		self.OPM_CSSb = tk.OptionMenu(self.FRM_B, self.OPM_CSSb_var, *day)
		self.OPM_CSSb.config(width=5)
		self.OPM_CSSb.grid(row=2,column=9)
		self.OPM_CSb_var = tk.StringVar()
		self.OPM_CSb_var.set(timeslots[0])
		self.OPM_CSb = tk.OptionMenu(self.FRM_B, self.OPM_CSb_var, *timeslots)
		self.OPM_CSb.config(width=6)
		self.OPM_CSb.grid(row=2,column=10)
		self.CBN_CSb_var = tk.IntVar()
		self.CBN_CSb = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_CSb_var, onvalue=1, offvalue=0)
		self.CBN_CSb.grid(row=2,column=11,padx=(0,10))
	#TECH
		self.LBL_Tb = tk.Label(self.FRM_B)
		self.LBL_Tb["text"] = "  TECH: "
		self.LBL_Tb.config(width=5)
		self.LBL_Tb.grid(row=3,column=0)
		self.OPM_TTb_var = tk.StringVar()
		self.OPM_TTb_var.set(day[0])
		self.OPM_TTb = tk.OptionMenu(self.FRM_B, self.OPM_TTb_var, *day)
		self.OPM_TTb.config(width=5)
		self.OPM_TTb.grid(row=3,column=1)
		self.OPM_Tb_var = tk.StringVar()
		self.OPM_Tb_var.set(timeslots[0])
		self.OPM_Tb = tk.OptionMenu(self.FRM_B, self.OPM_Tb_var, *timeslots)
		self.OPM_Tb.config(width=6)
		self.OPM_Tb.grid(row=3,column=2)
		self.CBN_Tb_var = tk.IntVar()
		self.CBN_Tb = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_Tb_var, onvalue=1, offvalue=0)
		self.CBN_Tb.grid(row=3,column=3,padx=(0,10))
	#AGRI
		self.LBL_Ab = tk.Label(self.FRM_B)
		self.LBL_Ab["text"] = "AGRI: "
		self.LBL_Ab.config(width=5)
		self.LBL_Ab.grid(row=3,column=4)
		self.OPM_AAb_var = tk.StringVar()
		self.OPM_AAb_var.set(day[0])
		self.OPM_AAb = tk.OptionMenu(self.FRM_B, self.OPM_AAb_var, *day)
		self.OPM_AAb.config(width=5)
		self.OPM_AAb.grid(row=3,column=5)
		self.OPM_Ab_var = tk.StringVar()
		self.OPM_Ab_var.set(timeslots[0])
		self.OPM_Ab = tk.OptionMenu(self.FRM_B, self.OPM_Ab_var, *timeslots)
		self.OPM_Ab.config(width=6)
		self.OPM_Ab.grid(row=3,column=6)
		self.CBN_Ab_var = tk.IntVar()
		self.CBN_Ab = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_Ab_var, onvalue=1, offvalue=0)
		self.CBN_Ab.grid(row=3,column=7,padx=(0,10))
	#ENGINEERTNG
		self.LBL_ENb = tk.Label(self.FRM_B)
		self.LBL_ENb["text"] = " ENGI: "
		self.LBL_ENb.config(width=5)
		self.LBL_ENb.grid(row=3,column=8)
		self.OPM_ENNb_var = tk.StringVar()
		self.OPM_ENNb_var.set(day[0])
		self.OPM_ENNb = tk.OptionMenu(self.FRM_B, self.OPM_ENNb_var, *day)
		self.OPM_ENNb.config(width=5)
		self.OPM_ENNb.grid(row=3,column=9)
		self.OPM_ENb_var = tk.StringVar()
		self.OPM_ENb_var.set(timeslots[0])
		self.OPM_ENb = tk.OptionMenu(self.FRM_B, self.OPM_ENb_var, *timeslots)
		self.OPM_ENb.config(width=6)
		self.OPM_ENb.grid(row=3,column=10)
		self.CBN_ENb_var = tk.IntVar()
		self.CBN_ENb = tk.Checkbutton(self.FRM_B, text="F.P.B", variable=self.CBN_ENb_var, onvalue=1, offvalue=0)
		self.CBN_ENb.grid(row=3,column=11,padx=(0,10))
	
	#First Period BIAS
		def BTN_Checkall_B_select():
			self.CBN_Fb_var.set(1)
			self.CBN_Eb_var.set(1)
			self.CBN_SSb_var.set(1)
			self.CBN_Rb_var.set(1)
			self.CBN_Mb_var.set(1)
			self.CBN_Pb_var.set(1)
			self.CBN_Cb_var.set(1)
			self.CBN_Bb_var.set(1)
			self.CBN_CSb_var.set(1)
			self.CBN_Tb_var.set(1)
			self.CBN_Ab_var.set(1)
			self.CBN_ENb_var.set(1)

		def BTN_Resetall_B_select():
			self.CBN_Fb_var.set(0)
			self.CBN_Eb_var.set(0)
			self.CBN_SSb_var.set(0)
			self.CBN_Rb_var.set(0)
			self.CBN_Mb_var.set(0)
			self.CBN_Pb_var.set(0)
			self.CBN_Cb_var.set(0)
			self.CBN_Bb_var.set(0)
			self.CBN_CSb_var.set(0)
			self.CBN_Tb_var.set(0)
			self.CBN_Ab_var.set(0)
			self.CBN_ENb_var.set(0)
			
		self.FRM_FPBb = tk.Frame(self)
		self.FRM_FPBb.grid(row=5,column=0)
		self.LBL_FPB_B = tk.Label(self.FRM_FPBb)
		self.LBL_FPB_B["text"] = "F.P.B = First Period Bias"
		self.LBL_FPB_B.grid(row=0,column=0,padx=(0,10))
		self.BTN_Checkall_B = tk.Button(self.FRM_FPBb)
		self.BTN_Checkall_B["text"] = "CHECK ALL"
		self.BTN_Checkall_B["command"] = BTN_Checkall_B_select
		self.BTN_Checkall_B.config(width=12)
		self.BTN_Checkall_B.grid(row=0,column=1,padx=(0,5))
		self.BTN_Resetall_B = tk.Button(self.FRM_FPBb)
		self.BTN_Resetall_B["text"] = "RESET ALL CHECKS"
		self.BTN_Resetall_B["fg"] = "red"
		self.BTN_Resetall_B["command"] = BTN_Resetall_B_select
		self.BTN_Resetall_B.config(width=18)
		self.BTN_Resetall_B.grid(row=0,column=2)

def center(window):
	window.update_idletasks()
	screen_width = window.winfo_screenwidth()
	screen_height = window.winfo_screenheight()

	size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
	x = screen_width/2 - size[0]/2 + (screen_width * 0.08)
	y = screen_height/2 - size[0]/2 + (screen_height * 0.01)

	window.geometry("+%d+%d" % (x,y))

root = tk.Tk()
root.title("PISAY Senior High Time-table Scheduling Tool")
root.resizable(width=False, height=False)
center(root)
app = Application(master=root)
app.mainloop()
