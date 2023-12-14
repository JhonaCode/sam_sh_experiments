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

exp         =  [] 

exp_label   =  [ 
                'S'        , 
                'S shf L' ,
                'S lhf L'  , 
                'S q L'    ,
                'M',
                'S Tint L',
                'S T L'    , 
                'S w L'    ,
                'S T M'    ,
                'L'
               ]


###############################################
#figures name
#####################

exp         =  [ 
               small,
               s_t_m_shf_l,
               s_qt_m_w_l,
               medium,
               s_qt_m_shf_l,
               s_qt_m_wshf_l,
               large,
                ]


exp_label   =  [
                'S',
                'S T M shf L',
                'S q T M w L',
                'M' ,  
                'S q T M shf L',
                'S q T M w shf L',
                'L'
               ]

fig_name='s2l_s_m_l'
"""
"""
"""
#figures name
#####################

exp         =  [ 
               small,
               s_t_l,
               s_qt_l,
               s_wshft_l,
               medium,
               s_qt_m_w_l,
               s_wqthf_l,
               s_wqthfuv_l,
               large,
                ]


exp_label   =  [
                'S',
                'S t L'          ,
                'S qt L'         ,
                'S w shf T L'    ,
                'M',
                'S q T M w L'    ,
                'S w q shf T L'  ,  
                'S w q shf T u v L ',
                'L'
               ]

fig_name='s2l_final'
"""

lim         =  [
                (0,0.05),(0,0.05),
                (0,0.05),(0,0.05),
                (0,0.05),(0,0.05),
                (0,0.05),(0,0.05),
                (0,0.05),(0,0.05),
               ]

var_to      =  [
                    1 ,1,1,  
                    1 ,1,1,  
                    1 ,1,1,  
                    1 ,1,1,  
                    1 ,1,1,  
               ]


l1           =  ( 0.001,2.8,'lower right',True,True)
l2           =  ( 0.001,2.8,'lower right',True,True)
l3           =  ( 0.001,2.8,'lower right',True,True)

leg_loc      =  [ 
                  l1,l1,
                  l1,l1,
                  l1,l1,
                  l1,l1,
                  l1,l1,
                ]


color       =  [
                'black','black',
                'black','black',
                'black','black',
                'black','black',
                'black','black',
               ]

show       =  [
                True,True,
                True,True,
                True,True,
                True,True,
                True,True,
               ]

diurnal     =  [
                True,True,
                True,True,
                True,True,
                True,True,
                True,True,
              ]
alt         =  [
                 1.0, 1.0, 
                 1.0, 1.0, 
                 1.0, 1.0, 
                 1.0, 1.0, 
                 1.0, 1.0, 
               ]

dc.diurnal_exp_var_hour_sam(exp,var,11,fig_name,explabel=exp_label,alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)

lim         =  [
                (0,0.1),(0,0.1),
                (0,0.1),(0,0.1),
                (0,0.1),(0,0.1),
                (0,0.1),(0,0.1),
                (0,0.1),(0,0.1),
               ]
alt         =  [
                 3.0, 3.0, 
                 3.0, 3.0, 
                 3.0, 3.0, 
                 3.0, 3.0, 
                 3.0, 3.0, 
               ]

l1           =  ( 0.001,2.8,'upper right',True,True)
l2           =  ( 0.001,2.8,'upper right',True,True)
l3           =  ( 0.001,2.8,'upper right',True,True)

leg_loc      =  [ 
                  l1,l1,
                  l1,l1,
                  l1,l1,
                  l1,l1,
                  l1,l1,
                ]


dc.diurnal_exp_var_hour_sam(exp,var,14,fig_name,explabel=exp_label,alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)

lim         =  [
                (0,0.03),(0,0.03),
                (0,0.03),(0,0.03),
                (0,0.03),(0,0.03),
                (0,0.03),(0,0.03),
                (0,0.03),(0,0.03),
               ]
alt         =  [
                 3.5, 3.5, 
                 3.5, 3.5, 
                 3.5, 3.5, 
                 3.5, 3.5, 
                 3.5, 3.5, 
               ]

dc.diurnal_exp_var_hour_sam(exp,var,17,fig_name,explabel=exp_label,alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)

