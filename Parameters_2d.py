
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
file_small_stat  = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_experiments/OUT_STAT/GOAMAZON_LES_small_1024x150_100_50m_1s.nc'
file_small_2d    = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_experiments/OUT_2D/GOAMAZON_LES_small_1024x150_100_50m_1s_512.2Dcom_1.nc'
var1d         = ['MCUP','QC'] 
var2d         = ['MCUP','QC'] 
vars_diurnal  = ['MCUP','QC']
date          = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal  = [(2014,1,1,9),(2014,1,1,19)] 
cal           = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
small    = sam.ncload(name,date,file_small_stat,cal,var1d,var2d,vars_diurnal,date_diurnal)
small_2d = sam_2d.ncload(name,date,file_small_2d,cal,var1d,var2d,vars_diurnal,date_diurnal)



name			= 'large'
#note			= large with 2d OUT each hour, 100 m resolution 
f_large_stat	        = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_experiments/OUT_STAT/GOAMAZON_LES_large_1024x150_100_50m_1s.nc'
large_st		= sam.ncload(name,date,f_large_stat,cal,var1d,var2d,vars_diurnal,date_diurnal)
f_large_2d	        = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_experiments/OUT_2D/GOAMAZON_LES_large_1024x150_100_50m_1s_512.2Dcom_1.nc'
large_2d		= sam_2d.ncload(name,date,f_large_2d,cal,var1d,var2d,vars_diurnal,date_diurnal)
var1d			= ['MCUP','QC'] 
var2d			= ['MCUP','QC'] 
vars_diurnal		= ['MCUP','QC']
date			= [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal		= [(2014,1,1,9),(2014,1,1,19)] 
cal			= ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']


name			= 'medium'
#note			= medium with 2d OUT each hour, 100 m resolution 
f_medium_stat	        = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_experiments/OUT_STAT/GOAMAZON_LES_medium_1024x150_100_50m_1s.nc'
medium_st		= sam.ncload(name,date,f_medium_stat,cal,var1d,var2d,vars_diurnal,date_diurnal)
f_medium_2d	        = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_experiments/OUT_2D/GOAMAZON_LES_medium_1024x150_100_50m_1s_512.2Dcom_1.nc'
medium_2d		= sam_2d.ncload(name,date,f_medium_2d,cal,var1d,var2d,vars_diurnal,date_diurnal)
var1d			= ['MCUP','QC'] 
var2d			= ['MCUP','QC'] 
vars_diurnal		= ['MCUP','QC']
date			= [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal		= [(2014,1,1,9),(2014,1,1,19)] 
cal			= ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
