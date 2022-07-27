
import time
import tkinter
from tkinter import *
from turtle import bgcolor, width
from time import sleep









OPTIONS = [
"NFSW->NFSC","NFSW->NFSMW","NFSMW->NFSC"
] #etc






def txtduzenleme():

    with open('Material\\NFSC\\matlist.txt','r') as file:
        filedata = file.read()
    # MATERIAL
    filedata = filedata.replace('MATERIAL	W', 'MATERIAL C')
    # DRAG MATERIAL
    filedata = filedata.replace('DRAG', 'METAL_SWATCH')
    filedata = filedata.replace('ALUMINUM_METAL_SWATCH', 'ALUMINUM_DRAG')
    filedata = filedata.replace('DULLPLASTIC_METAL_SWATCH', 'DULLPLASTIC_DRAG')

    # DECALDULL
    filedata = filedata.replace('DECALDULL', 'DECAL')
    filedata = filedata.replace('DECAL_BADGING', 'DECALDULL_BADGING')

    # HLCHROME
    filedata = filedata.replace('HLCHROME', 'CHROME')
    filedata = filedata.replace('CHROME_HEADLIGHT_LEFT', 'HLCHROME_HEADLIGHT_LEFT')
    filedata = filedata.replace('CHROME_HEADLIGHT_RIGHT', 'HLCHROME_HEADLIGHT_RIGHT')
    filedata = filedata.replace('CHROME_KIT00_HEADLIGHT_ON', 'HLCHROME_KIT00_HEADLIGHT_ON')

    #BLACK
    filedata = filedata.replace('BLACK', 'WINDOW_MASK')
    filedata = filedata.replace('PLAINNOTHING_WINDOW_MASK', 'PLAINNOTHING_BLACK')

    #MARKERS
    filedata = filedata.replace('MARKER	W', 'MARKER C')

    #DRIVER_FEMALE
    filedata = filedata.replace("MATERIAL C	DRIVER_DRIVER_FEMALE	DRIVER	DRIVER_FEMALE", "MATERIAL C	DRIVER_DRIVER_FEMALE	DRIVER	WINDOW_MASK")
    
    time.sleep(1)
    end = Tk()
    end.geometry('250x250')
    end.title('İşlem Tamamlandı!')
    enda = Button(end, text='Tamam',command=end.destroy,width=5,height='3')
    enda.place(x='100',y='250') 
    enda.pack()

    # Write the file out again
    with open('MatlistCikis\matlist.txt', 'w') as file:
        file.write(filedata)
    pass

def txtduzenleme2():


    with open('Material\\NFSMW\\matlist.txt','r') as file:
        filedata = file.read()

    # MATERIAL
    filedata = filedata.replace('MATERIAL	W', 'MATERIAL MW')
    # DRAG MATERIAL
    filedata = filedata.replace('DRAG', 'METAL_SWATCH')
    filedata = filedata.replace('ALUMINUM_METAL_SWATCH', 'ALUMINUM_DRAG')
    filedata = filedata.replace('DULLPLASTIC_METAL_SWATCH', 'DULLPLASTIC_DRAG')

    # DECALDULL
    filedata = filedata.replace('DECALDULL', 'DECAL')
    filedata = filedata.replace('DECAL_BADGING', 'DECALDULL_BADGING')

    # HLCHROME
    filedata = filedata.replace('HLCHROME', 'CHROME')
    filedata = filedata.replace('CHROME_HEADLIGHT_LEFT', 'HLCHROME_HEADLIGHT_LEFT')
    filedata = filedata.replace('CHROME_HEADLIGHT_RIGHT', 'HLCHROME_HEADLIGHT_RIGHT')
    filedata = filedata.replace('CHROME_KIT00_HEADLIGHT_ON', 'HLCHROME_KIT00_HEADLIGHT_ON')

    #BLACK
    filedata = filedata.replace('BLACK', 'WINDOW_MASK')
    filedata = filedata.replace('PLAINNOTHING_WINDOW_MASK', 'PLAINNOTHING_BLACK')

    #MARKERS
    filedata = filedata.replace('MARKER	W', 'MARKER MW')
    #DOORLINE
    filedata = filedata.replace('MATERIAL MW	DOORLINE_DOORLINE	DOORLINE	DOORLINE	DOORLINE_N','MATERIAL MW	DOORLINE_DOORLINE	DIABLOHP	DOORLINE	DOORLINE_N')
    #TIRE
    filedata = filedata.replace('MATERIAL MW	RUBBER_TIRE_STYLE01	RUBBER	TIRE_STYLE01	TIRE_STYLE01_N','MATERIAL MW	RUBBER_TIRE_STYLE01	RUBBER	%_TREAD')

    #EXHAUST_FX
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_1	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_1	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_2	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_2	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_3	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_3	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_4	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_4	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_5	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_5	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_6	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_6	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_7	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_7	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_8	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_8	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_9	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_9	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_10	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_10	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_11	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_11	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_12	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_12	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_13	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_13	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_14	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_14	LEFT_EXHAUST')
    filedata = filedata.replace('MARKER MW	_EXHAUST_FX_15	EXHAUST_FX', 'MARKER MW	_EXHAUST_FX_15	LEFT_EXHAUST')
    filedata = filedata.replace('MATERIAL MW	DAMAGE_DAMAGE0	DAMAGE	DAMAGE0	DAMAGE0_N', 'MATERIAL MW	DAMAGE_DAMAGE0	HOSES	DAMAGE0')

    filedata = filedata.replace("MATERIAL MW	DRIVER_DRIVER_FEMALE	DRIVER	DRIVER_FEMALE", "MATERIAL MW	DRIVER_DRIVER_FEMALE	DRIVER	WINDOW_MASK")
    time.sleep(1)
    end = Tk()
    end.geometry('250x250')
    end.title('İşlem Tamamlandı!')
    enda = Button(end, text='Tamam',command=end.destroy,width=5,height='3')
    enda.place(x='100',y='250') 
    enda.pack()

   
    with open('MatlistCikis\matlist.txt', 'w') as file:
        file.write(filedata)
    pass

def txtduzenleme3():

     with open('Material\\NFSMW\\matlist.txt','r') as file:
        filedata = file.read()  
 
        #MATERIAL
        filedata = filedata.replace('MATERIAL	MW', 'MATERIAL	C')

        #MARKERS
        filedata = filedata.replace('MARKER	MW','MARKER	C')
    

        #DECAL
        filedata = filedata.replace('DECAL_DUMMY_DECAL2	DECAL	DUMMY_DECAL2','DECAL_DUMMY_DECAL2	DECAL	WINDOW_MASK')
        filedata = filedata.replace('DECAL_DUMMY_DECAL3	DECAL	DUMMY_DECAL3','DECAL_DUMMY_DECAL3	DECAL	WINDOW_MASK')
        filedata = filedata.replace('DECAL_DUMMY_DECAL4	DECAL	DUMMY_DECAL4','DECAL_DUMMY_DECAL4	DECAL	WINDOW_MASK')
        filedata = filedata.replace('DECAL_DUMMY_DECAL5	DECAL	DUMMY_DECAL5','DECAL_DUMMY_DECAL5	DECAL	WINDOW_MASK')
        filedata = filedata.replace('DECAL_DUMMY_DECAL6	DECAL	DUMMY_DECAL6','DECAL_DUMMY_DECAL6	DECAL	WINDOW_MASK')

        #EXHAUST_FX
        
        #LEFT
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_1	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_1	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_2	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_2	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_3	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_3	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_4	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_4	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_5	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_5	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_6	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_6	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_7	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_7	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_8	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_8	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_9	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_9	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_10	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_10	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_11	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_11	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_12	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_12	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_13	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_13	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_14	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_14	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _LEFT_EXHAUST_15	LEFT_EXHAUST', 'MARKER C _LEFT_EXHAUST_15	EXHAUST_FX')
        #RIGHT
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_1	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_1	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_2	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_2	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_3	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_3	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_4	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_4	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_5	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_5	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_6	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_6	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_7	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_7	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_8	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_8	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_9	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_9	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_10	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_10	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_11	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_11	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_12	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_12	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_13	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_13	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_1	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_14	EXHAUST_FX')
        filedata = filedata.replace('MARKER C _RIGHT_EXHAUST_1	RIGHT_EXHAUST', 'MARKER C _RIGHT_EXHAUST_15	EXHAUST_FX')

        #ROOF_SCOOP
        filedata = filedata.replace('MARKER C	_ROOF_SCOOP_1	ROOF_SCOOP	BASE_A','MARKER C 	_ROOF_SCOOP_1	ROOF_SCOOP	KIT00_ROOF_A')
        
        #DOORLINE
        filedata = filedata.replace('DIABLOHP_DOORLINE	DIABLOHP	DOORLINE	DOORLINE_N','DIABLOHP_DOORLINE	DOORLINE	DOORLINE	DOORLINE_N')
         
        #DECAL_NUMBER
        filedata = filedata.replace('DECAL_DUMMY_NUMBER_RIGHT	DECAL	DUMMY_NUMBER_RIGHT','DECAL_DUMMY_NUMBER_RIGHT	DECAL	WINDOW_MASK') 
        filedata = filedata.replace('DECAL_DUMMY_NUMBER_LEFT	DECAL	DUMMY_NUMBER_LEFT','DECAL_DUMMY_NUMBER_LEFT	DECAL	WINDOW_MASK')
    
        #DAMAGE
        filedata = filedata.replace('HOSES_DAMAGE0	HOSES	DAMAGE0','HOSES_DAMAGE0	DAMAGE	DAMAGE0 DAMAGE0_N')
        
        

   
     time.sleep(1)
     end = Tk()
     end.geometry('250x250')
     end.title('İşlem Tamamlandı!')
     enda = Button(end, text='Tamam',command=end.destroy,width=5,height='3')
     enda.place(x='100',y='250') 
     enda.pack()

     with open('MatlistCikis\matlist.txt', 'w') as file:
        file.write(filedata)
     pass


def picker():
    if variable.get() == "NFSW->NFSC":
        txtduzenleme()
    if variable.get() == "NFSW->NFSMW":
        txtduzenleme2()
    if variable.get() == "NFSMW->NFSC":
        txtduzenleme3()   


root = Tk()
root.geometry("512x256")
root.title("NFS-Matlist by rybetasz")
root.configure(bg='Black')

variable = StringVar(root)
variable.set(OPTIONS[0])  # default value

om = OptionMenu(root, variable, *OPTIONS)
om.pack()

photo =PhotoImage(file ="Data\\button.png")
caller_button = Button(text="Çalıştır", image=photo, command=lambda: picker())










caller_button.pack(pady=1 , ipady=1 , ipadx=1)




mainloop()