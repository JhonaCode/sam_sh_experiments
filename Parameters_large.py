
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


#######################Large

#eSTA COMPLETO, esta funcionando no swan 
name        = 'large'
#note       = large goamazon teste, 100 m resolution 
file_4     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_large_1024x150_100_50m_1s_12stat.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
large = sam.ncload(name,date,file_4,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 'l_shf_s'
#note       =  large with  shf of small goamazon, 100 m resolution 
file_2     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_large_shf_small_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
l_shf_s = sam.ncload(name,date,file_2,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 'l_t_m'
#note       =  large  with  t of medium  goamazon, 100 m resolution 
file_3     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_large_t_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
l_t_m = sam.ncload(name,date,file_3,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 'l_shft_m'
#note       = large with shf and t of medium,  100 m resolution 
file_4     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_large_shft_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
l_shft_m = sam.ncload(name,date,file_4,cal,var1d,var2d,vars_diurnal,date_diurnal)

