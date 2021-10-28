from ramp.core.core import User, np
User_list = []

'''
Input file for C scenario of thesis project with GommyrPower (Village X)
CASE B: IGAs + 100 households, based on socioeconomic scenario 80 low income (LI) + 20 high income (HI) households are assumed
The appliances of HI and LI are based on DOI: 10.5281/zenodo.3980355
referring to target 1 for LI and target 4 for HI
CASE C: IGAs + 100 households + air conditioning (AC) units of nominal powers: 800W for fancoils (centralized units), 
        1700W as standard power (residential and commercial units), 4000W for industrial units
'''

#Create new user classes

#Create new user classes
WH = User("Warehouse",1)
User_list.append(WH)

sf = User("storage facility",1)
User_list.append(sf)

PH = User("Powerhouse",1)
User_list.append(PH)

cs = User("Cold storage",1)
User_list.append(cs)

fishp = User("Fish procsfing",1)
User_list.append(fishp)

supmar = User("Supermarket",1)
User_list.append(supmar)

cnt = User("Canteen",1)
User_list.append(cnt)

lndr = User("Laundry",1)
User_list.append(lndr)

printst = User("Printing store",1)
User_list.append(printst)

pharm = User("Pharmacy")
User_list.append(pharm)

rtA = User("Retail shop A",1)
User_list.append(rtA)

rtB = User("Retail shop B",1)
User_list.append(rtB)

tpr = User("Technology provider",1)
User_list.append(tpr)

bar = User("Bar",1)
User_list.append(bar)

hot = User("Hotel",1)
User_list.append(hot)

bak = User("Bakery",1)
User_list.append(bak)

icef = User("Ice factory",1)
User_list.append(icef)

watsup = User("Water supply",1)
User_list.append(watsup)

off = User("Office",1)
User_list.append(off)

bnk = User("Bank",1)
User_list.append(bnk)

stud = User("Studio",1)
User_list.append(stud)

#Additionals with respect to CASE A (as for CASE B)

LI = User("Low income households",80)
User_list.append(LI)

HI = User("High income households",20)
User_list.append(HI)

#Create new appliances

#Warehouse

WH_indoor_bulb = WH.Appliance(WH,20,12,2,360,0.2,120,flat='yes',wd_we_type=0)
WH_indoor_bulb.windows([420,600],[840,1020],0.2)

WH_outdoor_bulb = WH.Appliance(WH,10,40,2,720,0,720, fixed='yes',flat='yes')
WH_outdoor_bulb.windows([0,360],[1080,1440],0.05)

WH_indoor_tube = WH.Appliance(WH,130,30,2,720,0,720,flat='no', fixed='yes',wd_we_type=0)
WH_indoor_tube.windows([420,600],[840,1020],0.2)

WH_phone_charger = WH.Appliance(WH,8,5,2,300,0.2,10,flat='yes', fixed='no',wd_we_type=0)
WH_phone_charger.windows([480,720],[840,1020],0.35)

WH_pc = WH.Appliance(WH,2,100,1,540,0.2,360,wd_we_type=0)
WH_pc.windows([480,1020],[0,0],0.2)

WH_laptop = WH.Appliance(WH,3,65,1,240,0.2,120,wd_we_type=0)
WH_laptop.windows([480,990],[0,0],0.2)

WH_printer = WH.Appliance(WH,1,40,2,30,0.2,1,wd_we_type=0)
WH_printer.windows([600,720],[840,1020],0.35)

WH_photocopy = WH.Appliance(WH,1,400,2,30,0.2,1,wd_we_type=0)
WH_photocopy.windows([600,720],[840,1020],0.35)

WH_radio = WH.Appliance(WH,1,5,1,90,0.2,60,flat='yes', fixed='no',wd_we_type=0)
WH_radio.windows([720,840],[0,0],0.1)

WH_router = WH.Appliance(WH,2,6,1,1440,0,1440, flat='yes', fixed='yes')
WH_router.windows([0,1440],[0,0],0)

WH_pump = WH.Appliance(WH,1,750,1,120,0.1,30,wd_we_type=0)
WH_pump.windows([360,1020],[0,0],0.1)

WH_electricforklift = WH.Appliance(WH,3,750,2,180,0.2,20,wd_we_type=0)
WH_electricforklift.windows([360,480],[840,960],0.2)

WH_fan = WH.Appliance(WH,3,63,1,400,0.1,30,flat='yes', occasional_use = 0.7,fixed='yes',wd_we_type=0)
WH_fan.windows([600,900],[0,0],0.4)

#storage facility

sf_indoor_tube = sf.Appliance(sf,50,30,1,300,0.2,240, flat='yes', fixed='yes')
sf_indoor_tube.windows([480,1020],[0,0],0.2)

sf_outdoor_bulb = sf.Appliance(sf,10,40,2,720,0,720, flat='yes', fixed='no')
sf_outdoor_bulb.windows([0,360],[1080,1440],0.05)

sf_it_services = sf.Appliance(sf,1,270,1,1440,0.2,720)
sf_it_services.windows([0,1440],[0,0],0)

sf_router = sf.Appliance(sf,1,6,1,1440,0,1440, flat='yes', fixed='yes')
sf_router.windows([0,1440],[0,0],0)

sf_industrial_fan = sf.Appliance(sf,5,120,1,480,0.1,60,flat='yes',occasional_use =0.9,fixed='yes')
sf_industrial_fan.windows([540,1080],[0,0],0.1)

sf_phone = sf.Appliance(sf,3,7,1,300,0.2,60)
sf_phone.windows([480,1020],[0,0],0.2)

#Powerhouse

PH_indoor_tube = PH.Appliance(PH,100,30,1,300,0.2,120, flat='yes', fixed='yes')
PH_indoor_tube.windows([480,1020],[0,0],0.2)

PH_outdoor_bulb = PH.Appliance(PH,25,40,2,720,0,720, flat='yes', fixed='no')
PH_outdoor_bulb.windows([0,360],[1080,1440],0.05)

PH_it_services = PH.Appliance(PH,2,270,1,1440,0.2,420)
PH_it_services.windows([0,1440],[0,0],0)

PH_router = PH.Appliance(PH,1,6,1,1440,0,1440, flat='yes', fixed='yes')
PH_router.windows([0,1440],[0,0],0)

PH_industrial_fan = PH.Appliance(PH,5,120,1,480,0.1,60,fixed='yes',occasional_use =0.9,flat='yes')
PH_industrial_fan.windows([540,1080],[0,0],0.1)

PH_phone = PH.Appliance(PH,3,7,1,60,0.2,10)
PH_phone.windows([480,1020],[0,0],0.2)

#Cold storage

cs_indoor_bulb = cs.Appliance(cs,15,12,1,540,0.2,400, fixed='yes',flat='no',wd_we_type=0)
cs_indoor_bulb.windows([240,1320],[0,0],0.35)

cs_indoor_tube = cs.Appliance(cs,45,30,1,540,0.2,400, fixed='yes',flat='no',wd_we_type=0)
cs_indoor_tube.windows([240,1320],[0,0],0.35)

cs_outdoor_bulb = cs.Appliance(cs,10,40,2,720,0,720, flat='yes', fixed='no')
cs_outdoor_bulb.windows([0,360],[1080,1440],0.05)

cs_phone = cs.Appliance(cs,5,7,1,150,0.2,30,wd_we_type=0)
cs_phone.windows([420,1020],[0,0],0)

cs_cold_room = cs.Appliance(cs,5,750,1,1440,0,30,fixed='no',fixed_cycle=2,occasional_use=1,flat='no')
cs_cold_room.windows([0,1440],[0,0])
cs_cold_room.specific_cycle_1(750,30,80,20) 
cs_cold_room.specific_cycle_2(750,15,80,35)
cs_cold_room.cycle_behaviour([600,1020],[0,0],[1,599],[1021,1440])

#Fish procsfing

fishp_indoor_bulb = fishp.Appliance(fishp,25,12,1,540,0.2,400,fixed='yes',flat='no',wd_we_type=0)
fishp_indoor_bulb.windows([360,1050],[0,0],0.35)

fishp_indoor_tube = fishp.Appliance(fishp,80,30,1,540,0.2,400,fixed='yes',flat='no',wd_we_type=0)
fishp_indoor_tube.windows([360,1050],[0,0],0.35)

fishp_outdoor_bulb = fishp.Appliance(fishp,25,40,2,720,0,720, flat='yes', fixed='yes')
fishp_outdoor_bulb.windows([0,360],[1080,1440],0.05)

fishp_phone = fishp.Appliance(fishp,7,7,1,150,0.2,30,wd_we_type=0)
fishp_phone.windows([360,1020],[0,0],0)

fishp_conveyor_belt = fishp.Appliance(fishp,30,60,1,400,0.1,240,fixed='yes',occasional_use=0.9,flat='no',wd_we_type=0)
fishp_conveyor_belt.windows([360,780],[0,0],0.1)

fishp_packaging_machinery = fishp.Appliance(fishp,2,500,1,240,0.1,30,fixed='yes',occasional_use=0.9,flat='no',wd_we_type=0)
fishp_packaging_machinery.windows([390,810],[0,0],0.1)

fishp_electric_forklift = fishp.Appliance(fishp,2,750,2,180,0.2,45,fixed='no',occasional_use=0.9,flat='no',wd_we_type=0)
fishp_electric_forklift.windows([360,780],[900,1050],0.1)

fishp_phone_charger = fishp.Appliance(fishp,10,5,2,240,0.2,10,wd_we_type=0)
fishp_phone_charger.windows([480,720],[840,1020],0.35)

fishp_industrial_fan = fishp.Appliance(fishp,3,120,1,380,0.1,60,fixed='yes',occasional_use=0.8,flat='no',wd_we_type=0)
fishp_industrial_fan.windows([540,930],[0,0],0.1)

fishp_cold_room = fishp.Appliance(fishp,2,750,1,1440,0,30,fixed='no',fixed_cycle=2,flat='no')
fishp_cold_room.windows([0,1440],[0,0])
fishp_cold_room.specific_cycle_1(750,30,80,20) 
fishp_cold_room.specific_cycle_2(750,15,80,35)
fishp_cold_room.cycle_behaviour([600,1020],[0,0],[1,599],[1021,1440])

fishp_cold_room = fishp.Appliance(fishp,2,750,1,1440,0,30,fixed='no',fixed_cycle=2,flat='no')
fishp_cold_room.windows([0,1440],[0,0])
fishp_cold_room.specific_cycle_1(750,30,80,20) 
fishp_cold_room.specific_cycle_2(750,15,80,35)
fishp_cold_room.cycle_behaviour([600,1020],[0,0],[1,599],[1021,1440])

fishp_blast_chiller = fishp.Appliance(fishp,1,2000,1,1440,0,30,fixed='no',fixed_cycle=2,flat='no',wd_we_type=0)
fishp_blast_chiller.windows([0,1440],[0,0])
fishp_blast_chiller.specific_cycle_1(2000,240,280,120) 
fishp_blast_chiller.specific_cycle_2(2000,210,280,150)
fishp_blast_chiller.cycle_behaviour([600,1020],[0,0],[1,599],[1021,1440])

#Supermarket

supmar_indoor_bulb = supmar.Appliance(supmar,25,12,1,420,0.2,120, flat='yes', fixed='yes',wd_we_type=0)
supmar_indoor_bulb.windows([450,1020],[0,0],0.2)

supmar_indoor_tube = supmar.Appliance(supmar,200,30,1,420,0.2,120, flat='yes', fixed='yes',wd_we_type=0)
supmar_indoor_tube.windows([450,1020],[0,0],0.2)

supmar_outdoor_bulb = supmar.Appliance(supmar,23,40,2,720,0,720, flat='yes', fixed='yes')
supmar_outdoor_bulb.windows([0,360],[1080,1440],0.05)

supmar_phone_charger = supmar.Appliance(supmar,3,5,1,240,0.2,10,wd_we_type=0)
supmar_phone_charger.windows([480,840],[0,0],0.35)

supmar_phone = supmar.Appliance(supmar,2,7,1,60,0.2,10,wd_we_type=0)
supmar_phone.windows([450,930],[0,0],0.1)

supmar_PC = supmar.Appliance(supmar,1,100,1,480,0.2,360,wd_we_type=0)
supmar_PC.windows([480,1020],[0,0],0)

supmar_vending_machine = supmar.Appliance(supmar,2,350,1,1440,0,30,fixed='no',fixed_cycle=2,flat='no')
supmar_vending_machine.windows([0,1440],[0,0])
supmar_vending_machine.specific_cycle_1(350,40,50,20) 
supmar_vending_machine.specific_cycle_2(350,20,50,40)
supmar_vending_machine.cycle_behaviour([600,1020],[0,0],[1,599],[1021,1440])

supmar_radio = supmar.Appliance(supmar,1,5,1,90,0.2,60,flat='yes', fixed='no',wd_we_type=0)
supmar_radio.windows([540,840],[0,0],0.1)

supmar_printer = supmar.Appliance(supmar,1,40,1,30,0.2,1,wd_we_type=0)
supmar_printer.windows([480,840],[0,0],0.35)

supmar_photocopy = supmar.Appliance(supmar,1,400,1,30,0.2,1,wd_we_type=0)
supmar_photocopy.windows([480,840],[0,0],0.35)

supmar_speaker_system = supmar.Appliance(supmar,1,300,1,60,0.2,10,wd_we_type=0)
supmar_speaker_system.windows([480,960],[0,0],0.1)

supmar_router = supmar.Appliance(supmar,1,6,1,1440,0,1440, flat='yes', fixed='no')
supmar_router.windows([0,1440],[0,0],0)

supmar_fan = supmar.Appliance(supmar,7,63,1,240,0.1,30,fixed='yes',occasional_use=0.7,flat='no',wd_we_type=0)
supmar_fan.windows([600,900],[0,0],0.4)

supmar_cash_desk = supmar.Appliance(supmar,2,300,1,180,0.35,45,fixed='yes',flat='no',wd_we_type=0)
supmar_cash_desk.windows([480,930],[0,0],0.1)

supmar_refrigerated_cabinet = supmar.Appliance(supmar,5,230,1,1440,0,60,fixed='yes',fixed_cycle=3)
supmar_refrigerated_cabinet.windows([0,1440],[0,0])
supmar_refrigerated_cabinet.specific_cycle_1(230,20,15,10)
supmar_refrigerated_cabinet.specific_cycle_2(230,15,15,15)
supmar_refrigerated_cabinet.specific_cycle_3(230,10,15,20)
supmar_refrigerated_cabinet.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

supmar_freezer = supmar.Appliance(supmar,2,280,1,1440,0,30,fixed='yes',fixed_cycle=3)
supmar_freezer.windows([0,1440],[0,0])
supmar_freezer.specific_cycle_1(280,20,30,10)
supmar_freezer.specific_cycle_2(280,15,30,15)
supmar_freezer.specific_cycle_3(280,10,30,20)
supmar_freezer.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

supmar_product_scanner = supmar.Appliance(supmar,4,10,1,240,0.1,10,wd_we_type=0)
supmar_product_scanner.windows([480,840],[0,0],0.3)

#Canteen

cnt_indoor_bulb = cnt.Appliance(cnt,8,12,2,560,0.2,120, flat='yes', fixed='yes',wd_we_type=0)
cnt_indoor_bulb.windows([510,930],[1110,1290],0.1)

cnt_indoor_tube = cnt.Appliance(cnt,70,30,2,560,0.2,120, flat='yes', fixed='yes',wd_we_type=0)
cnt_indoor_tube.windows([510,930],[1110,1290],0.1)

cnt_outdoor_bulb = cnt.Appliance(cnt,10,40,2,720,0,720, flat='yes', fixed='yes')
cnt_outdoor_bulb.windows([0,360],[1080,1440],0.05)

cnt_phone_charger = cnt.Appliance(cnt,8,5,2,240,0.2,10,wd_we_type=0)
cnt_phone_charger.windows([540,840],[1140,1260],0.35)

cnt_vending_machine = cnt.Appliance(cnt,1,350,1,1440,0,30,fixed_cycle=2)
cnt_vending_machine.windows([0,1440],[0,0])
cnt_vending_machine.specific_cycle_1(350,40,50,20) 
cnt_vending_machine.specific_cycle_2(350,20,50,40)
cnt_vending_machine.cycle_behaviour([600,1020],[0,0],[1,599],[1021,1440])

cnt_radio = cnt.Appliance(cnt,1,5,2,180,0.1,120,occasional_use=0.9,flat='yes',wd_we_type=0)
cnt_radio.windows([660,870],[1110,1290],0.2)

cnt_speaker_system = cnt.Appliance(cnt,1,230,2,180,0.1,120,occasional_use=0.9,flat='yes',wd_we_type=0)
cnt_speaker_system.windows([660,870],[1110,1290],0.1)

cnt_fan = cnt.Appliance(cnt,5,80,1,240,0.35,30,fixed='yes',occasional_use=0.7,wd_we_type=0)
cnt_fan.windows([600,900],[0,0],0.2)

cnt_cash_desk = cnt.Appliance(cnt,1,300,2,180,0.2,45,fixed='yes',flat='no',wd_we_type=0)
cnt_cash_desk.windows([750,930],[1140,1290],0.1)

cnt_fridge = cnt.Appliance(cnt,2,230,1,1440,0,60,fixed='yes',fixed_cycle=3)
cnt_fridge.windows([0,1440],[0,0])
cnt_fridge.specific_cycle_1(230,20,15,10)
cnt_fridge.specific_cycle_2(230,15,15,15)
cnt_fridge.specific_cycle_3(230,10,15,20)
cnt_fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

cnt_freezer = cnt.Appliance(cnt,1,280,1,1440,0,30,fixed='yes',fixed_cycle=3)
cnt_freezer.windows([0,1440],[0,0])
cnt_freezer.specific_cycle_1(280,20,20,10) 
cnt_freezer.specific_cycle_2(280,15,20,25)
cnt_freezer.specific_cycle_3(280,10,20,20)
cnt_freezer.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

cnt_oven = cnt.Appliance(cnt,2,3000,2,240,0.1,60,occasional_use=0.8,wd_we_type=0)
cnt_oven.windows([510,690],[1080,1230],0.1)

cnt_kettle = cnt.Appliance(cnt,3,2500,2,180,0.3,15,wd_we_type=0)
cnt_kettle.windows([510,720],[1080,1230],0.1)

cnt_fryer = cnt.Appliance(cnt,1,3000,2,120,0.3,60,occasional_use=0.7,wd_we_type=0)
cnt_fryer.windows([720,810],[1140,1230],0.2)

cnt_toaster = cnt.Appliance(cnt,2,1200,2,90,0.35,10,wd_we_type=0)
cnt_toaster.windows([690,810],[1140,1230],0.3)

#Laundry

lndr_indoor_bulb = lndr.Appliance(lndr,3,12,1,300,0.1,120, flat='yes', fixed='yes',wd_we_type=0)
lndr_indoor_bulb.windows([450,900],[0,0],0.1)

lndr_indoor_tube = lndr.Appliance(lndr,15,30,1,300,0.1,120, flat='yes', fixed='yes',wd_we_type=0)
lndr_indoor_tube.windows([450,900],[0,0],0.1)

lndr_outdoor_bulb = lndr.Appliance(lndr,2,40,2,720,0,720, flat='yes', fixed='yes')
lndr_outdoor_bulb.windows([0,360],[1080,1440],0.05)

lndr_phone_charger = lndr.Appliance(lndr,3,5,1,240,0.2,10,wd_we_type=0)
lndr_phone_charger.windows([480,780],[0,0],0.35)

lndr_iron = lndr.Appliance(lndr,3,2000,1,180,0.35,30,wd_we_type=0)
lndr_iron.windows([450,750],[0,0],0.15)

lndr_steamer = lndr.Appliance(lndr,2,1000,1,200,0.2,30,wd_we_type=0)
lndr_steamer.windows([450,750],[0,0],0.15)

lndr_washing_machine = lndr.Appliance(lndr,4,2000,1,330,0.15,60,wd_we_type=0)
lndr_washing_machine.windows([480,870],[0,0],0.2)

lndr_stereo = lndr.Appliance(lndr,1,25,1,240,0.2,10,wd_we_type=0)
lndr_stereo.windows([480,840],[0,0],0.25)

lndr_phone = lndr.Appliance(lndr,1,7,1,60,0.2,10,wd_we_type=0)
lndr_phone.windows([510,810],[0,0],0.2)

lndr_laptop = lndr.Appliance(lndr,1,100,1,120,0.2,45,wd_we_type=0)
lndr_laptop.windows([480,870],[0,0],0.35)

lndr_fan = lndr.Appliance(lndr,1,80,1,180,0.35,30,occasional_use=0.7,wd_we_type=0)
lndr_fan.windows([600,840],[0,0],0.2)

#Printing store

printst_indoor_bulb = printst.Appliance(printst,5,10,2,360,0.2,120, flat='yes', fixed='yes',wd_we_type=0)
printst_indoor_bulb.windows([480,720],[840,990],0.1)

printst_indoor_tube = printst.Appliance(printst,25,30,2,360,0.2,120, flat='yes', fixed='yes',wd_we_type=0)
printst_indoor_tube.windows([480,720],[840,990],0.1)

printst_outdoor_bulb = printst.Appliance(printst,2,40,2,720,0,720, flat='yes', fixed='yes')
printst_outdoor_bulb.windows([0,360],[1080,1440],0.05)

printst_PC = printst.Appliance(printst,2,100,2,210,0.1,60,flat='yes',wd_we_type=0)
printst_PC.windows([510,720],[840,960],0.2)

printst_printer = printst.Appliance(printst,3,40,2,60,0.2,1,wd_we_type=0)
printst_printer.windows([510,720],[840,960],0.35)

printst_photocopy = printst.Appliance(printst,2,400,2,60,0.2,1,wd_we_type=0)
printst_photocopy.windows([510,720],[840,960],0.35)

printst_scanner = printst.Appliance(printst,1,380,2,45,0.2,1,wd_we_type=0)
printst_scanner.windows([510,720],[840,960],0.35)

printst_router = printst.Appliance(printst,1,6,1,1440,0,1440,flat='yes', fixed='no')
printst_router.windows([0,1440],[0,0],0)

printst_phone = printst.Appliance(printst,2,7,1,60,0.2,10,wd_we_type=0)
printst_phone.windows([510,990],[0,0],0.1)

printst_phone_charger = printst.Appliance(printst,3,5,1,180,0.2,10,wd_we_type=0)
printst_phone_charger.windows([540,960],[0,0],0.2)

#Pharmacy

pharm_indoor_bulb = pharm.Appliance(pharm,15,12,2,300,0.1,240,fixed='yes',flat='no',wd_we_type=0)
pharm_indoor_bulb.windows([540,750],[810,990],0.1)

pharm_indoor_tube = pharm.Appliance(pharm,60,30,2,300,0.1,240,fixed='yes',flat='no',wd_we_type=0)
pharm_indoor_tube.windows([540,750],[810,990],0.1)

pharm_outdoor_bulb = pharm.Appliance(pharm,20,40,2,720,0,720, flat='yes', fixed='yes')
pharm_outdoor_bulb.windows([0,360],[1080,1440],0.05)

pharm_sterilizer = pharm.Appliance(pharm,1,120,1,240,0.2,60,wd_we_type=0)
pharm_sterilizer.windows([480,1020],[0,0],0.35)

pharm_shaker = pharm.Appliance(pharm,2,10,1,240,0.2,120,wd_we_type=0)
pharm_shaker.windows([480,1020],[0,0],0.35)

pharm_medical_refrigerator = pharm.Appliance(pharm,1,380,1,1440,0,60,fixed='yes',fixed_cycle=2)
pharm_medical_refrigerator.windows([0,1440],[0,0])
pharm_medical_refrigerator.specific_cycle_1(380,35,20,15)
pharm_medical_refrigerator.specific_cycle_2(380,25,20,25)
pharm_medical_refrigerator.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

pharm_PC = pharm.Appliance(pharm,2,100,1,540,0.1,360,wd_we_type=0)
pharm_PC.windows([480,1020],[0,0],0.35)

pharm_telescopic_lamp = pharm.Appliance(pharm,2,18,2,120,0.2,10,wd_we_type=0)
pharm_telescopic_lamp.windows([480,720],[840,990],0.1)

pharm_phone = pharm.Appliance(pharm,2,7,2,60,0.2,10,wd_we_type=0)
pharm_phone.windows([480,720],[840,990],0.15)

pharm_phone_charger = pharm.Appliance(pharm,3,5,1,180,0.2,10,wd_we_type=0)
pharm_phone_charger.windows([540,960],[0,0],0.2)

pharm_security_system = pharm.Appliance(pharm,1,8,1,1440,0,1440,flat='yes', fixed='no')
pharm_security_system.windows([0,1440],[0,0],0)

pharm_router = pharm.Appliance(pharm,1,6,1,1440,0,1440,flat='yes', fixed='no')
pharm_router.windows([0,1440],[0,0],0)

pharm_vending_machine = pharm.Appliance(pharm,1,350,1,1440,0,30,fixed_cycle=2)
pharm_vending_machine.windows([0,1440],[0,0])
pharm_vending_machine.specific_cycle_1(350,40,50,20) 
pharm_vending_machine.specific_cycle_2(350,20,50,40)
pharm_vending_machine.cycle_behaviour([600,1020],[0,0],[1,599],[1021,1440])

pharm_fan = pharm.Appliance(pharm,2,80,1,180,0.35,30,flat='yes',occasional_use=0.7,wd_we_type=0)
pharm_fan.windows([600,840],[0,0],0.15)

#Retail shop A

rtA_indoor_bulb = rtA.Appliance(rtA,5,12,2,300,0.3,240, flat='yes', fixed='yes',wd_we_type=0)
rtA_indoor_bulb.windows([540,750],[840,990],0.1)

rtA_indoor_tube = rtA.Appliance(rtA,15,30,2,300,0.2,240, flat='yes', fixed='yes',wd_we_type=0)
rtA_indoor_tube.windows([540,750],[840,990],0.1)

rtA_outdoor_bulb = rtA.Appliance(rtA,3,40,2,720,0,720, flat='yes', fixed='yes')
rtA_outdoor_bulb.windows([0,360],[1080,1440],0.05)

rtA_phone = rtA.Appliance(rtA,1,7,2,60,0.2,10,wd_we_type=0)
rtA_phone.windows([540,750],[870,990],0.1)

rtA_phone_charger = rtA.Appliance(rtA,2,5,1,120,0.2,10,wd_we_type=0)
rtA_phone_charger.windows([540,960],[0,0],0.2)

rtA_fan = rtA.Appliance(rtA,1,80,1,180,0.35,30,occasional_use=0.7,wd_we_type=0)
rtA_fan.windows([600,840],[0,0],0.15)

#Retail shop B

rtB_indoor_bulb = rtB.Appliance(rtB,10,12,2,300,0.3,240, flat='yes', fixed='yes',wd_we_type=0)
rtB_indoor_bulb.windows([540,750],[840,990],0.1)

rtB_indoor_tube = rtB.Appliance(rtB,25,30,2,300,0.2,240, flat='yes', fixed='yes',wd_we_type=0)
rtB_indoor_tube.windows([540,750],[840,990],0.1)

rtB_outdoor_bulb = rtB.Appliance(rtB,5,40,2,720,0,720, flat='yes', fixed='yes')
rtB_outdoor_bulb.windows([0,360],[1080,1440],0.05)

rtB_phone = rtB.Appliance(rtB,2,7,2,60,0.2,10,wd_we_type=0)
rtB_phone.windows([540,750],[870,990],0.1)

rtB_phone_charger = rtB.Appliance(rtB,5,5,1,180,0.2,10,wd_we_type=0)
rtB_phone_charger.windows([540,960],[0,0],0.2)

rtB_fan = rtB.Appliance(rtB,3,80,1,180,0.35,30,occasional_use=0.7,wd_we_type=0)
rtB_fan.windows([600,840],[0,0],0.15)

rtB_heater = rtB.Appliance(rtB,1,1000,1,45,0.3,10,occasional_use=0.5,wd_we_type=0)
rtB_heater.windows([540,690],[0,0],0.35)

rtB_kettle = rtB.Appliance(rtB,1,2500,1,60,0.3,15,wd_we_type=0)
rtB_kettle.windows([660,810],[0,0],0.1)

rtB_router = rtB.Appliance(rtB,1,6,1,1440,0,1440, flat='yes', fixed='no')
rtB_router.windows([0,1440],[0,0],0)

rtB_laptop = rtB.Appliance(rtB,2,100,2,150,0.2,45,wd_we_type=0)
rtB_laptop.windows([540,720],[840,960],0.35)

#Technology provider ("tech as a service" store)

tpr_indoor_bulb = tpr.Appliance(tpr,8,12,2,300,0.3,240, flat='yes', fixed='yes',wd_we_type=0)
tpr_indoor_bulb.windows([540,750],[810,990],0.1)

tpr_indoor_tube = tpr.Appliance(tpr,50,30,2,300,0.2,240, flat='yes', fixed='yes',wd_we_type=0)
tpr_indoor_tube.windows([540,750],[810,990],0.1)

tpr_outdoor_bulb = tpr.Appliance(tpr,10,30,2,720,0,720, flat='yes', fixed='yes')
tpr_outdoor_bulb.windows([0,360],[1080,1440],0.05)

tpr_phone = tpr.Appliance(tpr,3,7,2,60,0.2,10,wd_we_type=0)
tpr_phone.windows([540,750],[810,990],0.2)

tpr_phone_charger = tpr.Appliance(tpr,5,5,1,180,0.2,10,wd_we_type=0)
tpr_phone_charger.windows([540,960],[0,0],0.2)

tpr_PC = tpr.Appliance(tpr,2,100,1,300,0.1,120,wd_we_type=0)
tpr_PC.windows([540,960],[0,0],0.1)

tpr_router = tpr.Appliance(tpr,1,6,1,1440,0,1440, flat='yes', fixed='no')
tpr_router.windows([0,1440],[0,0],0)

tpr_laptop = tpr.Appliance(tpr,2,100,2,150,0.2,45,wd_we_type=0)
tpr_laptop.windows([540,750],[840,990],0.35)

tpr_fan = tpr.Appliance(tpr,3,80,1,180,0.35,30,fixed='yes',occasional_use=0.7,wd_we_type=0)
tpr_fan.windows([600,840],[0,0],0.15)

tpr_test_bench = tpr.Appliance(tpr,1,6000,2,150,0.4,15,occasional_use=0.95,wd_we_type=0)
tpr_test_bench.windows([555,750],[840,990],0.1)

tpr_test_desk = tpr.Appliance(tpr,3,250,1,360,0.1,360, flat='yes', fixed='yes',wd_we_type=0)
tpr_test_desk.windows([540,990],[0,0],0.1)

#Bar 

bar_indoor_bulb = bar.Appliance(bar,10,12,2,560,0.2,480, flat='yes', fixed='yes',wd_we_type=0)
bar_indoor_bulb.windows([390,750],[870,1080],0.1)

bar_indoor_tube = bar.Appliance(bar,35,30,2,560,0.2,480, flat='yes', fixed='yes',wd_we_type=0)
bar_indoor_tube.windows([390,750],[870,1080],0.1)

bar_outdoor_bulb = bar.Appliance(bar,5,40,2,720,0,720, flat='yes', fixed='yes')
bar_outdoor_bulb.windows([0,360],[1080,1440],0.05)

bar_phone_charger = bar.Appliance(bar,10,5,2,270,0.2,10,wd_we_type=0)
bar_phone_charger.windows([420,720],[900,1050],0.2)

bar_router = bar.Appliance(bar,2,6,1,1440,0,1440, flat='yes', fixed='no')
bar_router.windows([0,1440],[0,0],0)

bar_radio = bar.Appliance(bar,1,5,2,240,0.25,120, flat='yes', fixed='no',wd_we_type=0)
bar_radio.windows([450,750],[870,1080],0.1)

bar_speaker_system = bar.Appliance(bar,1,230,2,180,0.25,120, flat='yes', fixed='no',wd_we_type=0)
bar_speaker_system.windows([450,750],[870,1080],0.1)

bar_fan = bar.Appliance(bar,3,80,1,210,0.35,30,flat='yes',occasional_use=0.8,wd_we_type=0)
bar_fan.windows([600,810],[870,930],0.2)

bar_fridge = bar.Appliance(bar,1,230,1,1440,0,60,fixed='yes',fixed_cycle=3)
bar_fridge.windows([0,1440],[0,0])
bar_fridge.specific_cycle_1(230,20,15,10)
bar_fridge.specific_cycle_2(230,15,15,15)
bar_fridge.specific_cycle_3(230,10,15,20)
bar_fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

bar_freezer = bar.Appliance(bar,1,280,1,1440,0,30,fixed='yes',fixed_cycle=3)
bar_freezer.windows([0,1440],[0,0])
bar_freezer.specific_cycle_1(280,20,20,10) 
bar_freezer.specific_cycle_2(280,15,20,25)
bar_freezer.specific_cycle_3(280,10,20,20)
bar_freezer.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

bar_oven = bar.Appliance(bar,3,3000,1,240,0.1,60,occasional_use=0.8,wd_we_type=0)
bar_oven.windows([405,690],[0,0],0.1)

bar_kettle = bar.Appliance(bar,2,2500,2,240,0.3,15,wd_we_type=0)
bar_kettle.windows([450,750],[870,1080],0.1)

bar_toaster = bar.Appliance(bar,1,1200,2,120,0.35,10,wd_we_type=0)
bar_toaster.windows([450,750],[870,1080],0.3)

bar_mixer = bar.Appliance(bar,2,250,1,60,0.4,30,wd_we_type=0)
bar_mixer.windows([405,630],[0,0],0.35)

bar_kneading_machine = bar.Appliance(bar,2,2400,2,180,0.1,90, flat='yes', fixed='yes',wd_we_type=0)
bar_kneading_machine.windows([405,690],[930,1080],0.2)

bar_coffee_machine = bar.Appliance(bar,1,3600,2,240,0.4,60,wd_we_type=0)
bar_coffee_machine.windows([420,750],[870,1080],0.2)

#Hotel

hot_indoor_bulb = hot.Appliance(hot,150,12,1,630,0.3,540, flat='yes', fixed='yes')
hot_indoor_bulb.windows([390,1410],[0,0],0.1)

hot_indoor_tube = hot.Appliance(hot,300,30,1,660,0.2,540, flat='yes', fixed='yes')
hot_indoor_tube.windows([390,1410],[0,0],0.1)

hot_outdoor_bulb = hot.Appliance(hot,45,40,2,720,0,720, flat='yes', fixed='yes')
hot_outdoor_bulb.windows([390,1410],[0,0],0.1)

hot_phone_charger = hot.Appliance(hot,30,5,3,280,0.2,10)
hot_phone_charger.windows([0,390],[690,1050],0.15,[1230,1440])

hot_phone = hot.Appliance(hot,5,7,2,150,0.2,45)
hot_phone.windows([540,750],[810,1170],0.2)

hot_router = hot.Appliance(hot,3,6,1,1440,0,1440, flat='yes', fixed='no')
hot_router.windows([0,1440],[0,0],0)

hot_PC = hot.Appliance(hot,2,100,1,540,0.1,360, flat='yes', fixed='yes')
hot_PC.windows([480,1020],[0,0],0.35)

hot_laptop = hot.Appliance(hot,7,100,2,150,0.2,45, flat='yes', fixed='yes')
hot_laptop.windows([480,1020],[1170,1439],0.25)

hot_radio = hot.Appliance(hot,5,5,3,300,0.25,120, flat='yes', fixed='no')
hot_radio.windows([570,630],[870,1080],0.1,[1170,1350])

hot_speaker_system = hot.Appliance(hot,1,230,3,180,0.25,120)
hot_speaker_system.windows([570,630],[870,1080],0.1,[1170,1350])

hot_fan = hot.Appliance(hot,12,80,2,180,0.35,20,occasional_use=0.8)
hot_fan.windows([600,930],[1110,1230],0.15)

hot_fridge = hot.Appliance(hot,2,230,1,1440,0,60,fixed='yes',fixed_cycle=3)
hot_fridge.windows([0,1440],[0,0])
hot_fridge.specific_cycle_1(230,20,15,10)
hot_fridge.specific_cycle_2(230,15,15,15)
hot_fridge.specific_cycle_3(230,10,15,20)
hot_fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

hot_kettle = hot.Appliance(hot,3,2500,2,240,0.3,15)
hot_kettle.windows([450,750],[870,1080],0.1)

hot_toaster = hot.Appliance(hot,1,1200,2,120,0.35,10)
hot_toaster.windows([450,750],[870,1080],0.3)

hot_coffee_machine = hot.Appliance(hot,1,3600,2,240,0.3,60)
hot_coffee_machine.windows([420,750],[870,1080],0.2)

hot_vacuum_cleaner = hot.Appliance(hot,3,250,1,90,0.2,20,fixed='yes',flat='no')
hot_vacuum_cleaner.windows([600,840],[0,0],0.1)

hot_heater = hot.Appliance(hot,1,3000,2,210,0.3,60,occasional_use=0.9)
hot_heater.windows([0,690],[1170,1440],0.2)

hot_stereo = hot.Appliance(hot,3,25,2,300,0.2,10, flat='yes', fixed='no')
hot_stereo.windows([480,840],[1110,1350],0.1)

hot_decoder = hot.Appliance(hot,5,8,1,1440,0,1440, flat='yes', fixed='no')
hot_decoder.windows([0,1440],[0,0],0)

hot_TV = hot.Appliance(hot,5,150,3,210,0.5,30)
hot_TV.windows([510,630],[870,1080],0.1,[1170,1410])

hot_antenna = hot.Appliance(hot,1,8,3,120,0.1,5)
hot_antenna.windows([510,630],[870,1080],0.35,[1170,1410])

hot_security_system = hot.Appliance(hot,2,8,1,1440,0,1440, flat='yes', fixed='yes')
hot_security_system.windows([0,1440],[0,0],0)

hot_pump = hot.Appliance(hot,1,1000,1,240,0.25,90, flat='yes', fixed='no')
hot_pump.windows([360,1440],[0,0],0.1)

#Bakery

bak_indoor_bulb = bak.Appliance(bak,10,12,2,500,0.2,480, flat='yes', fixed='yes',wd_we_type=0)
bak_indoor_bulb.windows([330,750],[870,990],0.1)

bak_indoor_tube = bak.Appliance(bak,25,30,2,500,0.2,480, flat='yes', fixed='yes',wd_we_type=0)
bak_indoor_tube.windows([330,750],[870,990],0.1)

bak_outdoor_bulb = bak.Appliance(bak,3,40,2,720,0,720, flat='yes', fixed='yes')
bak_outdoor_bulb.windows([0,360],[1080,1440],0.05)

bak_phone_charger = bak.Appliance(bak,10,5,2,270,0.2,10,wd_we_type=0)
bak_phone_charger.windows([420,720],[930,990],0.2)

bak_radio = bak.Appliance(bak,1,5,2,240,0.25,120, flat='yes', fixed='no',wd_we_type=0)
bak_radio.windows([420,750],[870,960],0.1)

bak_fan = bak.Appliance(bak,3,80,2,200,0.35,30,fixed='yes',occasional_use=0.8)
bak_fan.windows([600,750],[870,930],0.2)

bak_ventilation_fan = bak.Appliance(bak,2,50,1,960,0,900, flat='yes', fixed='no')
bak_ventilation_fan.windows([330,1350],[0,0],0.05)

bak_cold_room = bak.Appliance(bak,1,230,1,1440,0,30,fixed_cycle=2)
bak_cold_room.windows([0,1440],[0,0])
bak_cold_room.specific_cycle_1(750,30,80,20) 
bak_cold_room.specific_cycle_2(750,15,80,35)
bak_cold_room.cycle_behaviour([600,1020],[0,0],[1,599],[1021,1440])

bak_freezer = bak.Appliance(bak,1,280,1,1440,0,30,fixed='yes',fixed_cycle=3)
bak_freezer.windows([0,1440],[0,0])
bak_freezer.specific_cycle_1(280,20,20,10) 
bak_freezer.specific_cycle_2(280,15,20,25)
bak_freezer.specific_cycle_3(280,10,20,20)
bak_freezer.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

bak_oven = bak.Appliance(bak,5,3000,1,240,0.1,60,fixed='yes',occasional_use=0.95,flat='yes',wd_we_type=0)
bak_oven.windows([405,690],[0,0],0.1)

bak_mixer = bak.Appliance(bak,2,250,1,60,0.4,30,wd_we_type=0)
bak_mixer.windows([405,630],[0,0],0.35)

bak_leavening_room = bak.Appliance(bak,2,1500,1,1440,0,120,fixed_cycle=2)
bak_leavening_room.windows([0,1440],[0,0])
bak_leavening_room.specific_cycle_1(1500,60,80,120) 
bak_leavening_room.specific_cycle_2(1500,120,80,60)
bak_leavening_room.cycle_behaviour([600,1020],[0,0],[1,599],[1021,1440])

bak_kneading_machine = bak.Appliance(bak,4,2400,2,180,0.1,90, flat='yes', fixed='yes',wd_we_type=0)
bak_kneading_machine.windows([405,690],[930,1080],0.2)

#Ice factory

icef_indoor_bulb = icef.Appliance(icef,15,12,2,400,0.2,400, flat='yes', fixed='yes',wd_we_type=0)
icef_indoor_bulb.windows([330,750],[870,1050],0.2)

icef_indoor_tube = icef.Appliance(icef,45,30,2,400,0.2,400, flat='yes', fixed='yes',wd_we_type=0)
icef_indoor_tube.windows([330,750],[870,1050],0.2)

icef_outdoor_bulb = icef.Appliance(icef,10,40,2,720,0,720, flat='yes', fixed='yes')
icef_outdoor_bulb.windows([0,360],[1080,1440],0.05)

icef_phone = icef.Appliance(icef,1,7,1,150,0.2,30,wd_we_type=0)
icef_phone.windows([510,1020],[0,0],0)

icef_phone_charger = icef.Appliance(icef,5,5,2,120,0.3,10,wd_we_type=0)
icef_phone_charger.windows([540,720],[930,990],0.2)

icef_freezer = icef.Appliance(icef,2,800,1,1440,0,30,fixed='yes',fixed_cycle=3)
icef_freezer.windows([0,1440],[0,0])
icef_freezer.specific_cycle_1(280,20,20,10) 
icef_freezer.specific_cycle_2(280,15,20,25)
icef_freezer.specific_cycle_3(280,10,20,20)
icef_freezer.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

icef_ice_maker = icef.Appliance(icef,3,1500,2,210,0.1,90,wd_we_type=0)
icef_ice_maker.windows([510,690],[930,1440],0.1)

icef_industrial_fan = icef.Appliance(icef,2,120,1,360,0.1,60,fixed='yes',occasional_use=0.8,flat='yes',wd_we_type=0)
icef_industrial_fan.windows([540,930],[0,0],0.25)

#Water supply

watsup_indoor_bulb = watsup.Appliance(watsup,5,12,2,300,0.2,90,fixed='yes',occasional_use=0.8,flat='yes')
watsup_indoor_bulb.windows([570,750],[870,1050],0.35)

watsup_indoor_tube = watsup.Appliance(watsup,40,30,300,0.2,90,fixed='yes',occasional_use=0.8,flat='yes')
watsup_indoor_tube.windows([570,750],[870,1050],0.35)

watsup_outdoor_bulb = watsup.Appliance(watsup,5,40,2,720,0,720, flat='yes', fixed='yes')
watsup_outdoor_bulb.windows([0,360],[1080,1440],0.05)

watsup_phone = watsup.Appliance(watsup,1,7,1,150,0.2,30,occasional_use=0.7)
watsup_phone.windows([510,1020],[0,0],0.2)

watsup_ventilation_fan = watsup.Appliance(watsup,2,50,1,960,0,900,occasional_use=0.7)
watsup_ventilation_fan.windows([330,1350],[0,0],0)

watsup_pump = watsup.Appliance(watsup,2,2000,1,360,0.25,180, flat='yes', fixed='no')
watsup_pump.windows([360,1439],[0,0],0.1)

watsup_backup_pump = watsup.Appliance(watsup,1,1500,1,120,0.1,120,occasional_use=0.3,flat='yes')
watsup_backup_pump.windows([360,1439],[0,0],0.1)

#Office

off_indoor_bulb = off.Appliance(off,5,12,2,300,0.3,240, flat='yes', fixed='yes',wd_we_type=0)
off_indoor_bulb.windows([510,750],[840,990],0.1)

off_indoor_tube = off.Appliance(off,5,30,2,300,0.2,240, flat='yes', fixed='yes',wd_we_type=0)
off_indoor_tube.windows([510,750],[840,990],0.1)

off_outdoor_bulb = off.Appliance(off,5,30,2,720,0,720, flat='yes', fixed='yes')
off_outdoor_bulb.windows([0,360],[1080,1440],0.05)

off_phone = off.Appliance(off,5,7,2,60,0.35,10, flat='yes', fixed='yes',wd_we_type=0)
off_phone.windows([510,750],[840,990],0.2)

off_phone_charger = off.Appliance(off,15,5,1,180,0.2,10,wd_we_type=0)
off_phone_charger.windows([540,960],[0,0],0.2)

off_kettle = off.Appliance(off,1,2500,1,60,0.3,15,wd_we_type=0)
off_kettle.windows([660,810],[0,0],0.1)

off_router = off.Appliance(off,3,6,1,1440,0,1440, flat='yes', fixed='yes')
off_router.windows([0,1440],[0,0],0)

off_laptop = off.Appliance(off,4,100,2,150,0.15,45,fixed='yes',flat='no',wd_we_type=0)
off_laptop.windows([510,750],[840,960],0.35)

off_fan = off.Appliance(off,3,80,1,180,0.35,30,occasional_use=0.7,wd_we_type=0)
off_fan.windows([600,840],[0,0],0.15)

off_PC = off.Appliance(off,7,100,2,150,0.1,45, flat='yes', fixed='yes',wd_we_type=0)
off_PC.windows([510,750],[840,960],0.3)

off_coffee_machine = off.Appliance(off,1,1200,2,90,0.3,15,fixed='yes',flat='no',wd_we_type=0)
off_coffee_machine.windows([540,750],[870,960],0.2)

off_security_system = off.Appliance(off,1,8,1,1440,0,1440, flat='yes', fixed='no')
off_security_system.windows([0,1440],[0,0],0)

off_vending_machine = off.Appliance(off,1,350,1,1440,0,30,fixed_cycle=2)
off_vending_machine.windows([0,1440],[0,0])
off_vending_machine.specific_cycle_1(350,40,50,20) 
off_vending_machine.specific_cycle_2(350,20,50,40)
off_vending_machine.cycle_behaviour([600,1020],[0,0],[1,599],[1021,1440])

off_water_dispenser = off.Appliance(off,1,500,1,1440,0.6,1440)
off_water_dispenser.windows([0,1440],[0,0],0)

#Bank

bnk_indoor_bulb = bnk.Appliance(bnk,25,12,2,300,0.3,240, flat='yes', fixed='yes',wd_we_type=0)
bnk_indoor_bulb.windows([510,750],[870,990],0.1)

bnk_indoor_tube = bnk.Appliance(bnk,80,30,2,300,0.2,240, flat='yes', fixed='yes',wd_we_type=0)
bnk_indoor_tube.windows([510,750],[870,990],0.1)

bnk_outdoor_bulb = bnk.Appliance(bnk,15,30,2,720,0,720, flat='yes', fixed='yes')
bnk_outdoor_bulb.windows([0,360],[1080,1440],0.05)

bnk_phone = bnk.Appliance(bnk,3,7,2,60,0.35,10,wd_we_type=0)
bnk_phone.windows([510,750],[870,990],0.2)

bnk_phone_charger = bnk.Appliance(bnk,8,5,1,180,0.2,10,wd_we_type=0)
bnk_phone_charger.windows([540,960],[0,0],0.2)

bnk_router = bnk.Appliance(bnk,2,6,1,1440,0,1440, flat='yes', fixed='yes')
bnk_router.windows([0,1440],[0,0],0)

bnk_laptop = bnk.Appliance(bnk,3,100,2,150,0.15,45, flat='yes', fixed='no',wd_we_type=0)
bnk_laptop.windows([510,720],[870,960],0.35)

bnk_fan = bnk.Appliance(bnk,4,80,1,180,0.35,30,fixed='yes',occasional_use=0.7,wd_we_type=0)
bnk_fan.windows([600,840],[0,0],0.15)

bnk_PC = bnk.Appliance(bnk,5,100,2,150,0.1,45, flat='yes', fixed='yes',wd_we_type=0)
bnk_PC.windows([510,750],[840,960],0.3)

bnk_coffee_machine = bnk.Appliance(bnk,1,1200,2,90,0.3,15,wd_we_type=0)
bnk_coffee_machine.windows([525,750],[870,960],0.2)

bnk_security_system = bnk.Appliance(bnk,3,8,1,1440,0,1440, flat='yes', fixed='yes')
bnk_security_system.windows([0,1440],[0,0],0)

bnk_ATM = bnk.Appliance(bnk,3,3200,1,1440,0.45,1440, flat='yes', fixed='yes')
bnk_ATM.windows([0,1440],[0,0],0)

bnk_printer = bnk.Appliance(bnk,4,40,2,30,0.25,1,wd_we_type=0)
bnk_printer.windows([540,720],[840,960],0.35)

bnk_photocopy = bnk.Appliance(bnk,2,400,2,30,0.15,1,wd_we_type=0)
bnk_photocopy.windows([540,720],[840,960],0.35)

bnk_money_counter = bnk.Appliance(bnk,3,12,2,180,0.35,60,wd_we_type=0)
bnk_money_counter.windows([540,750],[900,960],0.35)

bnk_speaker_system = bnk.Appliance(bnk,1,230,2,180,0.25,150, flat='yes', fixed='yes',wd_we_type=0)
bnk_speaker_system.windows([540,720],[870,960],0.1)

bnk_water_dispenser = bnk.Appliance(bnk,1,500,1,1440,0.6,1440)
bnk_water_dispenser.windows([0,1440],[0,0],0)

#Studio

stud_indoor_bulb = stud.Appliance(stud,10,12,2,300,0.3,240, flat='yes', fixed='yes',wd_we_type=0)
stud_indoor_bulb.windows([510,750],[840,990],0.1)

stud_indoor_tube = stud.Appliance(stud,35,30,2,300,0.2,240, flat='yes', fixed='yes',wd_we_type=0)
stud_indoor_tube.windows([510,750],[840,990],0.1)

stud_outdoor_bulb = stud.Appliance(stud,4,30,2,720,0,720, flat='yes', fixed='yes')
stud_outdoor_bulb.windows([0,360],[1080,1440],0.05)

stud_phone = stud.Appliance(stud,3,7,2,60,0.35,10,wd_we_type=0)
stud_phone.windows([510,750],[840,990],0.2)

stud_phone_charger = stud.Appliance(stud,12,5,1,180,0.2,10,wd_we_type=0)
stud_phone_charger.windows([540,960],[0,0],0.2)

stud_kettle = stud.Appliance(stud,1,2500,1,60,0.3,15,wd_we_type=0)
stud_kettle.windows([660,810],[0,0],0.1)

stud_router = stud.Appliance(stud,1,6,1,1440,0,1440, flat='yes', fixed='yes')
stud_router.windows([0,1440],[0,0],0)

stud_laptop = stud.Appliance(stud,4,100,2,150,0.15,45,wd_we_type=0)
stud_laptop.windows([510,750],[840,960],0.35)

stud_fan = stud.Appliance(stud,2,80,1,180,0.35,30,fixed='yes',occasional_use=0.7,wd_we_type=0)
stud_fan.windows([600,840],[0,0],0.15)

stud_PC = stud.Appliance(stud,4,100,2,150,0.1,45, flat='yes', fixed='no',wd_we_type=0)
stud_PC.windows([510,750],[840,960],0.3)

stud_coffee_machine = stud.Appliance(stud,1,1200,2,90,0.3,15,wd_we_type=0)
stud_coffee_machine.windows([540,750],[870,960],0.2)

stud_vending_machine = stud.Appliance(stud,1,350,1,1440,0,30,fixed_cycle=2)
stud_vending_machine.windows([0,1440],[0,0])
stud_vending_machine.specific_cycle_1(350,40,50,20) 
stud_vending_machine.specific_cycle_2(350,20,50,40)
stud_vending_machine.cycle_behaviour([600,1020],[0,0],[1,599],[1021,1440])

#Low income households

LI_indoor_bulb = LI.Appliance(LI,3,12,2,120,0.2,10)
LI_indoor_bulb.windows([360,510],[1110,1440],0.35)

LI_phone_charger = LI.Appliance(LI,2,5,1,240,0.2,10)
LI_phone_charger.windows([0,1440],[0,0],0)

LI_radio = LI.Appliance(LI,1,10,2,60,0.1,5)
LI_radio.windows([360,510],[1110,1320],0.35)

#High income households

HI_indoor_bulb = HI.Appliance(HI,6,12,2,120,0.2,10)
HI_indoor_bulb.windows([360,510],[1110,1440],0.35)

HI_phone_charger = HI.Appliance(HI,3,5,1,240,0.2,10)
HI_phone_charger.windows([0,1440],[0,0],0)

HI_radio = HI.Appliance(HI,1,10,2,60,0.1,5)
HI_radio.windows([360,510],[1110,1320],0.35)

HI_router = HI.Appliance(HI,1,6,1,1440,0,1440)
HI_router.windows([0,1440],[0,0],0)

HI_fan = HI.Appliance(HI,2,80,1,180,0.35,30,occasional_use=0.8)
HI_fan.windows([600,960],[0,0],0.15)

HI_stereo = HI.Appliance(HI,1,25,2,60,0.2,10)
HI_stereo.windows([480,840],[1110,1350],0.1)

HI_decoder = HI.Appliance(HI,1,8,1,1440,0,1440)
HI_decoder.windows([0,1440],[0,0],0)

HI_TV = HI.Appliance(HI,1,150,3,90,0.4,15)
HI_TV.windows([510,630],[870,1080],0.1,[1170,1410])

HI_AC = HI.Appliance(HI,1,1700,2,270,0.15,60,flat='yes', occasional_use = 0.8,fixed='yes',wd_we_type=0)
HI_AC.windows([570,990],[1110,1230],0.2)





