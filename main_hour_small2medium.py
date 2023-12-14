################################################################
#Program to plot meteorological date
#of the OUT_STAT files of SAM with
#python and  Netcdf library.

###########################
#Modified:23/01/23
# To run using the same files
# python_src files

###########################
#Create by: Jhonatan Aguirre
#Date:07/04/2022
#working
#python 3.9

################################################################
# To activate this environment, use
#
# $ conda activate py37
# Went panda is use
# To deactivate an active environment, use
#
# $ conda deactivate
#
# path of the ncfile or data to plot
from    Parameters import *
from    Parameters_large  import *
from    Parameters_medium import *

################################################################ 
# to defined fig out direction, and others important parameters 
from    files_direction import *

# Load function to make the diurnal cycle and profiles figures.  
#import  sam_python.diurnal   as dc

# Load function to make the diurnal cycle and profiles figures.  
import  sam_python.diurnal   as dc

import  datetime as dt 


#separate with coma

var         =   ['MCUP']        

###############################################
#figures name
#####################
exp         =  [ 
               small,
               s_tinit_m,
               s_tadv_m,
               s_t_m,
               s_shf_m,
               s_w_m,
               s_q_m,
               s_qinit_m,
               medium,
               large, 
                ]


xlabel='[kgm$^{2}$s$^{-1}]$'

exp_label   =  [
                'S',
                'S Tinit  M',
                'S Tadv   M',
                'S T M ',
                'S shf M' ,  
                'S w M',
               'S q M',
                'S qint M',
                'M' ,  
                'L' ,  
               ]
fig_name='s2m_1var'
"""
###############################################
#figures name
#####################

exp         =  [ 
               small,
               s_qt_m,
               s_wshf_m,
               s_shft_m,
               medium,
               s_qshft_m,
               s_wshft_m,
               large, 
                ]


exp_label   =  [
                'S',
                'S q T M' ,  
                'S W shf  M' ,  
                'S shf T M' ,  
                'M' ,  
                'S q shf T M' ,  
                'S W shf T M' ,  
                'L' ,  
               ]

fig_name='s2m_2var'

###The roll of T
#figures name
#####################

exp         =  [ 
               small,
               s_t_m,
               s_shft_m,
               s_qt_m,
               medium,
               s_qshft_m,
               large, 
                ]


exp_label   =  [
                'S',
                'S T M' ,  
                'S shf T M' ,  
                'S q T M' ,  
                'M' ,  
                'S q shf T M' ,  
                'L' ,  
               ]

fig_name='s2m_Troll'

###RESUMEN
#figures name
#####################

exp         =  [ 
               s_w_m,
               small,
               s_t_m,
               s_qt_m,
               medium,
               s_qshft_m,
               large, 
                ]


exp_label   =  [
                'S W M' ,  
                'S',
                'S T M' ,  
                'S q T M' ,  
                'M' ,  
                'S q shf T M' ,  
                'L' ,  
               ]

fig_name='s2m_final'

"""

########################################################
########################################################

hour=11

lim         =  [
                (0,0.05)
                ,
                (0,0.05)
               ]

var_to      =  [
                    1,
                    1,
               ]


l1           =  ( 0.02,0.9,'lower right',True,True,True)

leg_loc      =  [ 
                  l1,
                  l1
                ]


color       =  [
                'black',
                'black'
               ]

show       =  [
                True,
                True
               ]

diurnal     =  [
                True,True
              ]
alt         =  [
                 [0,1.0],
                 [0,1.0]
               ]
exp_label_2  =  [
                
                 'uMF %s H LT'%hour ,  
                 ]

dc.diurnal_exp_var_hour_sam(exp,var,hour,fig_name,alt=alt,explabel=exp_label,explabel2=exp_label_2,xlabel=xlabel,leg_loc=leg_loc,lim=lim,show=show,diurnal=diurnal)

######################################################
######################################################
######################################################
hour=14

lim         =  [
                (0,0.1)
               ]

alt         =  [
                 (0,3.5)
               ]

l1           =  ( 0.01,0.1,'upper right',True,True,True)

leg_loc      =  [ 
                  l1,
                ]


exp_label_2  =  [
                
                 'uMF %s H LT'%hour ,  
                 ]

dc.diurnal_exp_var_hour_sam(exp,var,hour,fig_name,alt=alt,explabel=exp_label,explabel2=exp_label_2,xlabel=xlabel,leg_loc=leg_loc,lim=lim,show=show,diurnal=diurnal)

######################################################
######################################################
######################################################

hour=17

lim         =  [
                (0,0.025)
               ]

alt         =  [
                 (0,3.5)
               ]

exp_label_2  =  [
                
                 'uMF %s H LT'%hour ,  
                 ]

dc.diurnal_exp_var_hour_sam(exp,var,hour,fig_name,alt=alt,explabel=exp_label,explabel2=exp_label_2,xlabel=xlabel,leg_loc=leg_loc,lim=lim,show=show,diurnal=diurnal)


