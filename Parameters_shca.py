    #File to define the direction of the sam runs.
#######################################################


### My own files


##Adress of the computer
from     files_direction  import *


import   sam_python.var_files.var_to_load_sam as sam


#######################################################
#Files of SAM to load.
#######################################################

########SHCA

name        = 'shca'
#note       = shca , 100 m resolution 
file_29     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_shca_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
shca = sam.ncload(name,date,file_29,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 'shca_wq_l'
#note       = shca with q and q of large goamazon, 100 m resolution 
file_13     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_shca_wq_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,15)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,15)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
shca_wq_l = sam.ncload(name,date,file_13,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 'shca_q_l'
#note       = shca with q of large goamazon, 100 m resolution 
file_13     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_shca_q_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,15)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,15)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
shca_q_l = sam.ncload(name,date,file_13,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 'shca_shf_l'
#note       =  shca  with  shf of large  goamazon, 100 m resolution 
file_13     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_shca_shf_l_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
shca_shf_l = sam.ncload(name,date,file_13,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 'shca_w_l'
#note       =  shca  with  w of large  goamazon, 100 m resolution 
file_13     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_shca_w_l_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
shca_w_l = sam.ncload(name,date,file_13,cal,var1d,var2d,vars_diurnal,date_diurnal)

