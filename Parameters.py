#######################################################
#File to define the direction of the sam runs.
#######################################################


### My own files


##Adress of the computer
from     files_direction  import *


import   sam_python.var_files.var_to_load_sam as sam


#######################################################
#Files of SAM to load.
#######################################################


name       = 'small'
#note=small, 100 m resolution 
file_1 = '/home/jhona/repositories/sam/SAM6.11.4/GOAMAZON_LES/python/stat/testes_xc50/OUT_STAT/GOAMAZON_LES_small_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date =[(2014,1,1,9),(2014,1,1,18)] 
date_diurnal =[(2014,1,1,9),(2014,1,1,1)] 
cal=['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
small = sam.ncload(name,date,file_1,cal,var1d,var2d,vars_diurnal,date_diurnal)


name       = 'small_shf_l'
#note=small, 100 m resolution 
file_2 = '/home/jhona/repositories/sam/SAM6.11.4/GOAMAZON_LES/python/stat/testes_xc50/OUT_STAT/GOAMAZON_LES_small_shf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date =[(2014,1,1,9),(2014,1,1,15)] 
date_diurnal =[(2014,1,1,9),(2014,1,1,17)] 
cal=['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_shf_l = sam.ncload(name,date,file_2,cal,var1d,var2d,vars_diurnal,date_diurnal)
