
#######################################################
#File to define the direction of the sam runs.
#######################################################


### My own files


##Adress of the computer
from     files_direction  import *

import   sam_python.var_files.var_to_load_sam as sam
import   sam_python.var_files.var_to_load_sam_2d as sam_2d


#######################################################
#Files of SAM to load.
#######################################################


#######################Large

#eSTA COMPLETO, esta funcionando no swan 

name        = 'small'
#note       = small with 2d OUT each hour, 100 m resolution 
file_small_stat  = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_1024x150_100_50m_1s.nc'
file_small_2d    = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_2D/GOAMAZON_LES_small_1024x150_100_50m_1s_512.2Dcom_1.nc'
var1d         = ['MCUP','QC'] 
var2d         = ['MCUP','QC'] 
vars_diurnal  = ['MCUP','QC']
date          = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal  = [(2014,1,1,9),(2014,1,1,19)] 
cal           = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
small    = sam.ncload(name,date,file_small_stat,cal,var1d,var2d,vars_diurnal,date_diurnal)
small_2d = sam_2d.ncload(name,date,file_small_2d,cal,var1d,var2d,vars_diurnal,date_diurnal)

#name        = 'medium'
##note       = medium with 2d OUT each hour, 100 m resolution 
#file_2     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_2D/GOAMAZON_LES_medium_1024x150_100_50m_1s.nc'
#var1d       = ['MCUP','QC'] 
#var2d       = ['MCUP','QC'] 
#vars_diurnal= ['MCUP','QC']
#date        = [(2014,1,1,9),(2014,1,1,19)] 
#date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
#cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
#medium = sam.ncload(name,date,file_2,cal,var1d,var2d,vars_diurnal,date_diurnal)
