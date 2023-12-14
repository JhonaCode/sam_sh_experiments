
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

name        = 'medium'
#note       = medium , 100 m resolution 
file_1      = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
medium = sam.ncload(name,date,file_1 ,cal,var1d,var2d,vars_diurnal,date_diurnal)


#Esta completo 
name        = 'm_q_l'
#note       = medium with q of large goamazon, 100 m resolution 
file_2      = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_medium_q_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
m_q_l = sam.ncload(name,date,file_2,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 'm_t_l'
#note       =  medium  t of large  goamazon, 100 m resolution 
file_3      = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_medium_t_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
m_t_l = sam.ncload(name,date,file_3,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 'm_shf_l'
#note       =  medium  shf of large  goamazon, 100 m resolution 
file_4     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_medium_shf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
m_shf_l = sam.ncload(name,date,file_4,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 'm_w_l'
#note       =  medium  w of large  goamazon, 100 m resolution 
file_5     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_medium_w_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
m_w_l = sam.ncload(name,date,file_5,cal,var1d,var2d,vars_diurnal,date_diurnal)



#Esta completo 
name        = 'm_wq_l'
#note       = medium with w and q of large goamazon, 100 m resolution 
file_6     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_medium_wq_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
m_wq_l = sam.ncload(name,date,file_6,cal,var1d,var2d,vars_diurnal,date_diurnal)

#######################

name        = 'm_wshf_l'
#note       =  medium  w and shf of large  goamazon, 100 m resolution 
file_7     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_medium_wshf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
m_wshf_l = sam.ncload(name,date,file_7,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 'm_shft_l'
#note       =  medium  sfh and t of large  goamazon, 100 m resolution 
file_8     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_medium_shft_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
m_shft_l = sam.ncload(name,date,file_8,cal,var1d,var2d,vars_diurnal,date_diurnal) 


name        = 'm_wqhf_l'
#note       =  medium  with  w q shf lhf of large  goamazon, 100 m resolution 
file_9     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_medium_wqhf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
m_wqhf_l = sam.ncload(name,date,file_9,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 'm_wshft_l'
#note       = medium with w shf and t of large,  100 m resolution 
file_10     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_medium_wshft_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
m_wshft_l = sam.ncload(name,date,file_10,cal,var1d,var2d,vars_diurnal,date_diurnal)

##############testes com lhf and shf

name        = 'm_halflhf'
#note       =  medium  with  half lhf of nothing  goamazon, 100 m resolution 
file_11     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_medium_halflhf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
m_halflhf = sam.ncload(name,date,file_11,cal,var1d,var2d,vars_diurnal,date_diurnal)


