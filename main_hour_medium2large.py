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
                [
               medium,
               m_q_l,
               m_t_l,
               m_w_l,
               m_shf_l,
               large, 
               ]
                ]



exp_label   =  [
                [
                'M' ,  
                'M q L',
                'M t L',
                'M w L',
                'M shf L',
                'L' ,  
                ]
               ]



"""
###############################################
#figures name
#####################

exp         =  [ 
               medium,
               m_w_l,
               m_wq_l,
               m_wshf_l,
               m_shft_l,
               large, 
                ]


exp_label   =  [
                'M' ,  
                'M w L',
                'M wq L',
                'M wshf L',
                'M shft L',
                'L',  
               ]

fig_name='m2l_2var'
###############################################
#figures name
#####################

exp         =  [ 
               medium,
               m_w_l,
               m_wqhf_l,
               m_wshf_l,
               m_wshft_l,
               large, 
                ]


exp_label   =  [
                'M',  
                'M w L',
                'M wqhf  L',
                'M wshf  L',
                'M wshft L',
                'L',  
               ]

fig_name='m2l_3var'
"""
###############################################
#figures name
#####################

exp         =  [ 
                [
                    medium,
                    m_wq_l,
                    m_wshft_l,
                    m_w_l,
                    m_wshf_l,
                    large, 
                    ]
                ]


exp_label   =  [
                [
                'M',  
                'M w q L',
                'M w shf t L',
                'M w L',
                'M wshf  L',
                'L',  
                ]
               ]

fig_name='m2l_final'


########################################################
########################################################

lim         =  [
                [(0,0.05)]
               ]

var_to      =  [
                  [1],  
               ]

l1           =  ( 0.001,0.8,'lower right',True,True,True)

leg_loc      =  [ 
                  [l1]
                ]

exp_label_2  =  [
                 ['a) uMF 11 H LT'] ,  
                ]

color        = [['black']]


mf='[kgm$^{2}$s$^{-1}]$'
xlabel       =[[mf]]

color_exp=[
            [[1,0]    ,'blue'],
            #[[2,2,1,2],'darkcyan'],
            [[2,2,1,2],'navy'],
            [[3,1]    ,'cyan'],
            #[[1,2,1,2],'tab:purple'],
            [[1,0]    ,'purple'],
            [[1,1]    ,'green'],
            [[1,0]    ,'red'],
          ]


show       =  [
                [True]
               ]

diurnal     =  [
                [True]
              ]
alt         =  [
                 [1.0]
               ]

dc.diurnal_exp_var_hour_sam(exp,var,11,fig_name,explabel=exp_label,explabel2=exp_label_2,xlabel=xlabel,alt=alt,leg_loc=leg_loc,lim=lim,color=color_exp,show=show,diurnal=diurnal)


exit()

lim         =  [
                (0,0.1),(0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),
               ]
alt         =  [
                 3.0, 3.0, 3.0, 3.0, 
                 3.0, 3.0, 3.0, 3.0, 
                 3.0, 3.0, 3.0, 3.0, 
                 3.0, 3.0, 3.0, 3.0, 
                 3.0, 3.0, 3.0, 3.0, 
               ]

l1           =  ( 0.001,2.8,'upper right',True,True)
l2           =  ( 0.001,2.8,'upper right',True,True)
l3           =  ( 0.001,2.8,'upper right',True,True)

leg_loc      =  [ 
                  l1,l1,l1,l1,
                  l1,l1,l1,l1,
                  l1,l1,l1,l1,
                  l1,l1,l1,l1,
                  l1,l1,l1,l1,
                ]


dc.diurnal_exp_var_hour_sam(exp,var,14,fig_name,explabel=exp_label,alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)

lim         =  [
                (0,0.03),(0,0.03),(0,0.03),(0,0.03),
                (0,0.03),(0,0.03),(0,0.03),(0,0.03),
                (0,0.03),(0,0.03),(0,0.03),(0,0.03),
                (0,0.03),(0,0.03),(0,0.03),(0,0.03),
               ]
alt         =  [
                 3.5, 3.5, 3.5, 3.5, 
                 3.5, 3.5, 3.5, 3.5, 
                 3.5, 3.5, 3.5, 3.5, 
                 3.5, 3.5, 3.5, 3.5, 
               ]

dc.diurnal_exp_var_hour_sam(exp,var,17,fig_name,explabel=exp_label,alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)

