# PYTHON script
'''
Developed by:Gaurav Borgaonkar
Date:10/25/2019

Name: Automatic Creation of Loads and Subcases for Durability Analysis in Nastran
Description: Accepts user input - the csv file containing Nastran load definitons, names, directions and magnitudes  
Developments: Added complete Nastran header for Magna, included subcase creation along with loads

'''

import os
import ansa
from ansa import utils, base, constants

def main():
	created_forces = list()
	solver = constants.NASTRAN
	print("Please select the FORCE CSV file...")
	filename = utils.SelectOpenFile(0, "csv file (*.csv)")
	if not filename[0]:
		return
	fileopen = open(filename[0], "r")
	for line in fileopen:
		if "Channel" not in line[:7]:
			columns = line.replace("\n","").split(",")
			sid = columns[0]

			name = columns[1]
			
			grid = columns[2]

			axis = columns[3]

			if columns[3]=="FX":
				n1=1
				n2=0
				n3=0
				typ="FORCE"				
			if columns[3]=="FY":
				n1=0
				n2=1
				n3=0	
				typ="FORCE"			
			if columns[3]=="FZ":
				n1=0
				n2=0
				n3=1	
				typ="FORCE"
			if columns[3]=="MX":
				n1=1
				n2=0
				n3=0
				typ="MOMENT"				
			if columns[3]=="MY":
				n1=0
				n2=1
				n3=0	
				typ="MOMENT"			
			if columns[3]=="MZ":
				n1=0
				n2=0
				n3=1	
				typ="MOMENT"
				
			cid=columns[4]
			magn=columns[5]
			
			created_forces.append(base.CreateEntity(solver,"FORCE",{"TYPE":typ,"Name":name,"SID":sid,"by":"node","G":grid,"CID":cid,"F":magn,"N1":n1,"N2":n2,"N3":n3}))
			
			bc = base.GetEntity(solver,"LOAD_SET",int(sid))
			base.SetEntityCardValues(solver,bc,{"Name":name,})
			
				
	total_forces = len(created_forces)
	print(total_forces, "forces and moments created successfully!")
	
	#Creating Nastran Header with Subcases...#
	
	header = base.CreateEntity(solver, "Nastran Header")
	
	text = "SOL 101\n" + "TIME = 3.15E7\n" + "CEND\n" + "$\n" + "$\n"
	text += "DISPLACEMENT(PLOT) = ALL\n" + "STRESS(PLOT) = ALL\n" + "$\n" + "$\n"
	
	#Creating Subcases for the different loads#
	for f in created_forces:
		
		name = base.GetEntityCardValues(solver, f, ("Name",))["Name"]
		force_id = base.GetEntityCardValues(solver, f, ("SID",))["SID"]
		
		text += "Subcase " + str(force_id) + "\n"
		text += "Load = " + str(force_id) + "\n" + "Label = " + name + "\n" + "$\n"
	
	#Setting the rest of the header
	text += "BEGIN BULK\n";
	text += "PARAM, AUTOSPC, YES\n" + "PARAM, GRDPNT,0\n" + "PARAM, INREL,-2\n" + "PARAM, K6ROT, 100.\n" + "PARAM, MAXRATIO,1.E8\n" + "PARAM, POST, -2\n"
	text += "$\n" + "$\n"
	
	base.SetNastranHeaderText(header, text)
	
	fileopen.close()
	print("Done!!!")

if __name__ == '__main__':
	main()
