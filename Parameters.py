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

##########name        = 'bx'
###########note       = bomex teste, 100 m resolution 
##########file_3     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/BOMEX_128x128x100_100m_40m_3s.nc'
##########var1d       = ['MCUP','QC'] 
##########var2d       = ['MCUP','QC'] 
##########vars_diurnal= ['MCUP','QC']
##########date        = [(2014,1,1,9),(2014,1,1,15)] 
##########date_diurnal= [(2014,1,1,9),(2014,1,1,15)] 
##########cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
##########bx = sam.ncload(name,date,file_3,cal,var1d,var2d,vars_diurnal,date_diurnal)


########SMALLLLLLLLLL
#Esta completo ate as 7 da noite
name        = 'small'
#note       =small, 100 m resolution 
file_1      = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_experiments/OUT_STAT/GOAMAZON_LES_small_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        =[(2014,1,1,9),(2014,1,1,19)] 
date_diurnal=[(2014,1,1,9),(2014,1,1,19)] 
cal         =['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
small       = sam.ncload(name,date,file_1,cal,var1d,var2d,vars_diurnal,date_diurnal)

###Esta completo
name        = 's_shf_l'
#note       = small, 100 m resolution 
file_2     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_shf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_shf_l = sam.ncload(name,date,file_2,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_lhf_l'
#note       = small with lhf of large, 100 m resolution 
file_3     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_lhf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_lhf_l = sam.ncload(name,date,file_3,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_q_l'
#note       = small with w and q of large goamazon, 100 m resolution 
file_4     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_q_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_q_l = sam.ncload(name,date,file_4,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_tinit_l'
#note       = small only t init ,  of large, 100 m resolution 
file_5     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_tinit_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_tinit_l = sam.ncload(name,date,file_5,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_t_l'
#note       = small only t ,  of large, 100 m resolution 
file_6     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_t_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_t_l = sam.ncload(name,date,file_6,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_w_l'
#note       =  small  with  w of large  goamazon, 100 m resolution 
file_7     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_w_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_w_l = sam.ncload(name,date,file_7,cal,var1d,var2d,vars_diurnal,date_diurnal)


#################
###Duas variaveis
#################

name        = 's_qt_l'
#note       = small with q and t  of large , 100 m resolution 
file_9     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_qt_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_qt_l = sam.ncload(name,date,file_9,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_hf_l'
#note       = small, 100 m resolution 
file_10     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_hf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_hf_l = sam.ncload(name,date,file_10,cal,var1d,var2d,vars_diurnal,date_diurnal)

#Esta completo
name        = 's_wq_l'
#note       = small with w and q of large goamazon, 100 m resolution 
file_11     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_wq_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_wq_l = sam.ncload(name,date,file_11,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_wshf_l'
#note       = small with w  and shf of large goamazon, 100 m resolution 
file_12     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_wshf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_wshf_l = sam.ncload(name,date,file_12,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_wlhf_l'
#note       = medium with w and lhf  of large, 100 m resolution 
file_13     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_wlhf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_wlhf_l = sam.ncload(name,date,file_13,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 's_shft_l'
#note       =  small with  T  and shf of large goamazon, 100 m resolution 
file_14     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_shft_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_shft_l = sam.ncload(name,date,file_14,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_wt_l'
#note       = small with w and and t of large,  100 m resolution 
file_30     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_wt_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_wt_l = sam.ncload(name,date,file_30,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 's_qshf_l'
#note       = small with q and shf of large,  100 m resolution 
file_31     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_qshf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_qshf_l = sam.ncload(name,date,file_31,cal,var1d,var2d,vars_diurnal,date_diurnal)


###########################
#########Tres Variaveis 
###########################

name        = 's_whf_l'
#note       = small with w  lhf and shf of large goamazon, 100 m resolution 
file_16     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_whf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_whf_l = sam.ncload(name,date,file_16,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_wshft_l'
#note       =  small with w T  and shf of large goamazon, 100 m resolution 
file_17     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_shft_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_wshft_l = sam.ncload(name,date,file_17,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 's_wqshf_l'
#note       = small with w,  q and shf of large goamazon, 100 m resolution 
file_18     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_wqshf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_wqshf_l = sam.ncload(name,date,file_18,cal,var1d,var2d,vars_diurnal,date_diurnal)



name        = 's_wqthf_l'
#note       =  small with w,q, t shf and lhf  of large, 100 m resolution 
file_19     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_wqthf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_wqthf_l = sam.ncload(name,date,file_19,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 's_wqthfuv_l'
#note       =  small with w,q, t shf and lhf uv  of large, 100 m resolution 
file_20    = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_wqthfuv_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_wqthfuv_l = sam.ncload(name,date,file_20,cal,var1d,var2d,vars_diurnal,date_diurnal)

#########################################33
#########################################33
#Tres experimentos
#########################################33
#########################################33

name        = 's_t_m_shf_l'
#note       = small with  t of medium  shf of large , 100 m resolution 
file_21     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_t_medium_shf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_t_m_shf_l = sam.ncload(name,date,file_21,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_t_m_w_l'
#note       = small with t of medium and w of large, 100 m resolution 
file_27     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_t_medium_w_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_t_m_w_l = sam.ncload(name,date,file_27,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 's_t_m_q_l'
#note       = small with t of medium and q of large, 100 m resolution 
file_28     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_t_medium_q_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_t_m_q_l = sam.ncload(name,date,file_28,cal,var1d,var2d,vars_diurnal,date_diurnal)

##### Two variables

name        = 's_qt_m_w_l'
#note       = small  q and tof medium; w of large,  100 m resolution 
file_22     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_qt_medium_w_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_qt_m_w_l = sam.ncload(name,date,file_22,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 's_qt_m_shf_l'
#note       = small with q and t of medium  shf of large , 100 m resolution 
file_23     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_qt_medium_shf_large_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_qt_m_shf_l = sam.ncload(name,date,file_23,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_qt_m_wshf_l'
#note       = small with q and t of medium  w and shf of large , 100 m resolution 
file_24     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_qt_medium_wshf_lar_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_qt_m_wshf_l = sam.ncload(name,date,file_24,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 's_t_m_wshf_l'
#note       = small  with  t of  medium, and  w and shf of large  100 m resolution 
file_36     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_t_medium_wshf_lar_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_t_m_wshf_l = sam.ncload(name,date,file_36,cal,var1d,var2d,vars_diurnal,date_diurnal)



########################3
##Small to medium 
########################3
name        = 's_t_m'
#note       =  small  with  t of medium  goamazon, 100 m resolution 
file_8     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_t_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_t_m = sam.ncload(name,date,file_8,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_shf_m'
#note       = small with shf  of medium, 100 m resolution 
file_25     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_shf_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_shf_m = sam.ncload(name,date,file_25,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 's_tinit_m'
#note       = small with tinit  of medium, 100 m resolution 
file_26     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_tinit_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_tinit_m = sam.ncload(name,date,file_26,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_qt_m'
#note       = small with q and tof medium,  100 m resolution 
file_15     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_qt_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_qt_m = sam.ncload(name,date,file_15,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_wshf_m'
#note       = small with w shf   of medium, 100 m resolution 
file_35     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_wshf_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_wshf_m = sam.ncload(name,date,file_35,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_wshft_m'
#note       = small with w shf and t  of medium, 100 m resolution 
file_36     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_wshft_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_wshft_m = sam.ncload(name,date,file_36,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 's_shft_m'
#note       = small with  shf and t  of medium, 100 m resolution 
file_38     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_shft_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_shft_m = sam.ncload(name,date,file_38,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_qshft_m'
#note       = small with q shf and t  of medium, 100 m resolution 
file_37     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_qshft_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_qshft_m = sam.ncload(name,date,file_37,cal,var1d,var2d,vars_diurnal,date_diurnal)

########################3
########################3
########################3
########################3

name        = 's_q_m'
#note       = small with q of medium , 100 m resolution 
file_31     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_q_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_q_m = sam.ncload(name,date,file_31,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        = 's_w_m'
#note       = small with w of medium , 100 m resolution 
file_32     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_w_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_w_m = sam.ncload(name,date,file_32,cal,var1d,var2d,vars_diurnal,date_diurnal)

name        = 's_qinit_m'
#note       = small  q init of  medium,  100 m resolution 
file_34     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_qinit_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_qinit_m = sam.ncload(name,date,file_34,cal,var1d,var2d,vars_diurnal,date_diurnal)

####################################$$$$$$$$$$$$$$$$$$4
####################################$$$$$$$$$$$$$$$$$$4



name        = 's_tadv_m'
#note       = small with  T advection only no tinit  of medium, 100 m resolution 
file_37     = '/dados/bamc/jhonatan.aguirre/SHALLOW/shca_teste/OUT_STAT/GOAMAZON_LES_small_tadv_medium_1024x150_100_50m_1s.nc'
var1d       = ['MCUP','QC'] 
var2d       = ['MCUP','QC'] 
vars_diurnal= ['MCUP','QC']
date        = [(2014,1,1,9),(2014,1,1,19)] 
date_diurnal= [(2014,1,1,9),(2014,1,1,19)] 
cal         = ['days  since 2014-01-01 00:00:00 +04:00:00','gregorian']
s_tadv_m = sam.ncload(name,date,file_37,cal,var1d,var2d,vars_diurnal,date_diurnal)
