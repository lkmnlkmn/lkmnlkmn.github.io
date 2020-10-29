import tkinter
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
import pandas as pd

def hanshu1():
    fig = plt.figure(figsize=(4,3),dpi=80)
    ax1 = axisartist.Subplot(fig, 111)
    fig.add_axes(ax1)
    ax1.axis[:].set_visible(False)
    ax1.axis["x"] = ax1.new_floating_axis(0,0)
    ax1.axis["x"].set_axisline_style("->", size = 1.0)
    ax1.axis["y"] = ax1.new_floating_axis(1,0)
    ax1.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax1.axis["x"].set_axis_direction("top")
    ax1.axis["y"].set_axis_direction("right")
    plt.xlim(-5, 5)
    plt.ylim(-0, 2.0)
    for i1 in np.arange(-5,5):
        if i1 != 0:
             t1 = [i1]
             t2 = [0]
             plt.plot(t1, t2, 'b*')
        else:
            t1 = [i1, i1]
            t2 = [0, 1]
            plt.plot(t1, t2, 'b*-')
    plt.title('1.δ[n]')
    plt.xlabel('n')
    plt.show()

def hanshu2():
    fig = plt.figure(figsize=(4, 3),dpi=80)
    ax2 = axisartist.Subplot(fig, 111)
    fig.add_axes(ax2)
    ax2.axis[:].set_visible(False)
    ax2.axis["x"] = ax2.new_floating_axis(0,0)
    ax2.axis["x"].set_axisline_style("->", size = 1.0)
    ax2.axis["y"] = ax2.new_floating_axis(1,0)
    ax2.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax2.axis["x"].set_axis_direction("top")
    ax2.axis["y"].set_axis_direction("right")
    plt.xlim(-5, 5)
    plt.ylim(-0, 1.5)
    for i2 in np.arange(-5, 5):
           if i2 < 0:
                 t5 = [i2]
                 t6 = [0]
                 plt.plot(t5, t6, 'b*')
           else:
                 t5 = [i2, i2]
                 t6 = [0, 1]
                 plt.plot(t5, t6, 'b*-')
    plt.title('2.u[n]')
    plt.xlabel('n')
    plt.show()

def hanshu3():
    fig = plt.figure(figsize=(4, 3),dpi=80)
    ax3 = axisartist.Subplot(fig, 111)
    fig.add_axes(ax3)
    ax3.axis[:].set_visible(False)
    ax3.axis["x"] = ax3.new_floating_axis(0,0)
    ax3.axis["x"].set_axisline_style("->", size = 1.0)
    ax3.axis["y"] = ax3.new_floating_axis(1,0)
    ax3.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax3.axis["x"].set_axis_direction("top")
    ax3.axis["y"].set_axis_direction("right")
    plt.xlim(-1,8)
    plt.ylim(0, 1.5)
    for i3 in np.arange(-1,8,1):
        if 0<=i3<=6-1:
             t7=[i3,i3]
             t8=[0,1]
             plt.plot(t7,t8,'r*-')
        else:
             t7=[i3]
             t8=[0]
             plt.plot(t7,t8,'r*')
    plt.title('$3.G_N[n]=1,0<=n<=6-1;0,n>=6$')
    plt.xlabel('n')
    plt.show()


def hanshu4():
    fig = plt.figure(figsize=(10,8),dpi=80)
    ax4= axisartist.Subplot(fig, 111)
    fig.add_axes(ax4)
    ax4.axis[:].set_visible(False)
    ax4.axis["x"] = ax4.new_floating_axis(0,0)
    ax4.axis["x"].set_axisline_style("->", size = 1.0)
    ax4.axis["y"] = ax4.new_floating_axis(1,0)
    ax4.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax4.axis["x"].set_axis_direction("top")
    ax4.axis["y"].set_axis_direction("right")
    plt.xlim(-3.2,8)
    plt.ylim(-20, 15)
    a=-1.5
    for i4 in np.arange(-3,8):
        t11=a**i4
        t9=[i4,i4]
        t10=[0,t11]
        plt.plot(t9,t10,'r*-')
    plt.title('$4.x[n]=ca^n$')
    plt.show()
    
def hanshu5():
    fig = plt.figure(figsize=(10,8),dpi=80)
    ax5= axisartist.Subplot(fig, 111)
    fig.add_axes(ax5)
    ax5.axis[:].set_visible(False)
    ax5.axis["x"] = ax5.new_floating_axis(0,0)
    ax5.axis["x"].set_axisline_style("->", size = 1.0)
    ax5.axis["y"] = ax5.new_floating_axis(1,0)
    ax5.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax5.axis["x"].set_axis_direction("top")
    ax5.axis["y"].set_axis_direction("right")
    plt.xlim(-5,3.2)
    plt.ylim(-15, 40)
    a=0.5
    for i5 in np.arange(-5,3.2):
        t11=a**i5
        t9=[i5,i5]
        t10=[0,t11]
        plt.plot(t9,t10,'r*-')
    plt.title('$5.x[n]=ca^n$')
    plt.show()

def hanshu6():
    fig = plt.figure(figsize=(10,8),dpi=80)
    ax6= axisartist.Subplot(fig, 111)
    fig.add_axes(ax6)
    ax6.axis[:].set_visible(False)
    ax6.axis["x"] = ax6.new_floating_axis(0,0)
    ax6.axis["x"].set_axisline_style("->", size = 1.0)
    ax6.axis["y"] = ax6.new_floating_axis(1,0)
    ax6.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax6.axis["x"].set_axis_direction("top")
    ax6.axis["y"].set_axis_direction("right")
    plt.xlim(-10,10)
    plt.ylim(-1, 1)
    for i6 in np.arange(-20,21):
        t12=np.sin(3*i6/4)
        t13=[i6,i6]
        t14=[0,t12]
        plt.plot(t13,t14,'r*-')
    plt.title('$6.x[n]=sin(3n/4)$')
    plt.show()

def hanshu7():
    fig = plt.figure(figsize=(10,8),dpi=80)
    ax7= axisartist.Subplot(fig, 111)
    fig.add_axes(ax7)
    ax7.axis[:].set_visible(False)
    ax7.axis["x"] = ax7.new_floating_axis(0,0)
    ax7.axis["x"].set_axisline_style("->", size = 1.0)
    ax7.axis["y"] = ax7.new_floating_axis(1,0)
    ax7.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax7.axis["x"].set_axis_direction("top")
    ax7.axis["y"].set_axis_direction("right")
    plt.xlim(-10,10)
    plt.ylim(-1, 1)
    for i7 in np.arange(-10,11):
        t15=np.cos(3*i7/4)
        t16=[i7,i7]
        t17=[0,t15]
        plt.plot(t16,t17,'r*-')
    plt.title('$7.x[n]=cos(8n/31)$')
    plt.show()

def hanshu8():
    fig = plt.figure(figsize=(10,8),dpi=80)
    ax8= axisartist.Subplot(fig, 111)
    fig.add_axes(ax8)
    ax8.axis[:].set_visible(False)
    ax8.axis["x"] = ax8.new_floating_axis(0,0)
    ax8.axis["x"].set_axisline_style("->", size = 1.0)
    ax8.axis["y"] = ax8.new_floating_axis(1,0)
    ax8.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax8.axis["x"].set_axis_direction("top")
    ax8.axis["y"].set_axis_direction("right")
    plt.xlim(-5,8)
    plt.ylim(-60,60)
    d=1j
    c=1*np.exp(d*1)
    for i8 in np.arange(-5,8):
        a=2.0**(i8)*np.exp(d*1*(i8))
        t18=a*c
        t19=[i8,i8]
        t20=[0,t18]
        plt.plot(t19,t20,'r*-')
    plt.title('$8.x[n]=e^{1j}*2^ne^{j1n}$')
    plt.show()

def hanshu9():
    fig = plt.figure(figsize=(10,8),dpi=80)
    ax9= axisartist.Subplot(fig, 111)
    fig.add_axes(ax9)
    ax9.axis[:].set_visible(False)
    ax9.axis["x"] = ax9.new_floating_axis(0,0)
    ax9.axis["x"].set_axisline_style("->", size = 1.0)
    ax9.axis["y"] = ax9.new_floating_axis(1,0)
    ax9.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax9.axis["x"].set_axis_direction("top")
    ax9.axis["y"].set_axis_direction("right")
    plt.xlim(-8,5)
    plt.ylim(-60,60)
    d=1j
    c=1*np.exp(d*1)
    for i9 in np.arange(-8,5):
        a=0.5**(i9)*np.exp(d*1*(i9))
        t21=a*c
        t22=[i9,i9]
        t23=[0,t21]
        plt.plot(t22,t23,'r*-')
    plt.title('$9.x[n]=e^{1j}*0.5^ne^{j1n}$')
    plt.show()

top=tkinter.Tk(className='离散') 
top.geometry('200x300')

button = tkinter.Button(top)
button['text'] = '1.单位脉冲信号'
button['command'] = hanshu1
button.pack()

button = tkinter.Button(top)
button['text'] = '2.阶跃信号'
button['command'] = hanshu2
button.pack()

button = tkinter.Button(top)
button['text'] = '3.矩阵信号'
button['command'] = hanshu3
button.pack()

button = tkinter.Button(top)
button['text'] = '4.ce^-1.5n'
button['command'] = hanshu4
button.pack()

button = tkinter.Button(top)
button['text'] = '5.ce^0.5n'
button['command'] = hanshu5
button.pack()

button = tkinter.Button(top)
button['text'] = '6.sin(3n/4)'
button['command'] = hanshu6
button.pack()

button = tkinter.Button(top)
button['text'] = '7.cos(3n/4)'
button['command'] = hanshu7
button.pack()

button = tkinter.Button(top)
button['text'] = '8.增长信号'
button['command'] = hanshu8
button.pack()

button = tkinter.Button(top)
button['text'] = '9.衰退信号'
button['command'] = hanshu9
button.pack()

top.mainloop()