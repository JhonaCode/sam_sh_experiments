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
###RESUMEN
#figures name
#####################

exp         =  [ 
               small,
               s_w_m,
               s_t_m,
               s_qt_m,
               s_qshft_m,
               medium,
                ]


ar=r'$+$'
ls='$\mathrm{_{ls}}$'
exp_label   =  [
                'Small(S)',
                '+W(M)',
                r'+$\theta$%s(M)'%(ls) ,  
                r'+[$\theta$%s,q%s](M)'%(ls,ls) ,  
                r'+[$\theta$%s,q%s,SH](M)'%(ls,ls),  
                 'Medium(M)' ,  
               ]


fig_name='s2m_final'

xlabel='uMF [kgm$^{2}$s$^{-1}]$'


color_exp=[
            [[1,0]    ,'blue'],
            #[[2,2,1,2],'darkcyan'],
            [[2,2,1,2],'navy'],
            [[3,1]    ,'cyan'],
            #[[1,2,1,2],'tab:purple'],
            [[1,0]    ,'purple'],
            [[1,1]    ,'green'],
            [[1,0]    ,'orange'],
          ]


########################################################
########################################################

lim         =  [
                (0,0.085)
               ]
alt         =  [
                 (0,3.2), 
               ]

var_to      =  [
                    1 ,
               ]

#text(x,y),loc,z,x,legend
#l1           =  ( 0.007 ,0.9,'lower right',True,True,True)
l1           =  ( [0.002,0.15],[0.02,3.0],'center right',True,True,True)

leg_loc      =  [ 
                  l1,
                ]

show       =  [
                True,
               ]

diurnal     =  [
                True,
              ]

ar=r'$\rightarrow$'
exp_label_2  =  [
                 r'a)Small%sMedium'%ar ,  
                ]

exp_label_3  =  [
                 r'11 Hours LT',  
                ]

dc.diurnal_exp_var_hour_sam(exp,var,11,fig_name,explabel=exp_label,explabel2=exp_label_2,explabel3=exp_label_3,xlabel=xlabel,alt=alt,leg_loc=leg_loc,lim=lim,color=color_exp,show=show,diurnal=diurnal)

lim         =  [
                (0,0.085),
               ]
alt         =  [
                 (0,3.2), 
               ]

#text(x,y),loc,z,x,legend
l1           =  ( [0.002,0.15],[0.02,3.0],'center right',False,True,False)

leg_loc      =  [ 
                  l1,
                ]

exp_label_2  =  [
                 r'b)Small%sMedium'%ar ,  
                ]

exp_label_3  =  [
                 r'14 Hours LT',  
                ]

dc.diurnal_exp_var_hour_sam(exp,var,14,fig_name,explabel=exp_label,explabel2=exp_label_2,explabel3=exp_label_3,xlabel=xlabel,alt=alt,leg_loc=leg_loc,lim=lim,color=color_exp,show=show,diurnal=diurnal)


lim         =  [
                #(0,0.23)
                (0,0.085)
               ]
alt         =  [
                 (0,3.2), 
               ]

l1           =  ( [0.002,0.15],[0.02,3.0],'center right',False,True,False)

leg_loc      =  [ 
                  l1
                ]

exp_label_2  =  [
                 r'c)Small%sMedium'%ar ,  
                ]

exp_label_3  =  [
                 r'17 Hours LT',  
                ]

dc.diurnal_exp_var_hour_sam(exp,var,17,fig_name,explabel=exp_label,explabel2=exp_label_2,explabel3=exp_label_3,xlabel=xlabel,alt=alt,leg_loc=leg_loc,lim=lim,color=color_exp,show=show,diurnal=diurnal)

