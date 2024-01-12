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
from    Parameters_2d         import * 

# Load function to make the diurnal cycle and profiles figures.  
#import  sam_python.diurnal   as dc

# Load function to make the diurnal cycle and profiles figures.  
import  sam_python.two_dimensional   as two


exp= [small_2d,medium_2d,large_2d]

#separate with comak 
exp_label   = [
                 [r'a)Small  Wind 850[hpa]'], 
                 [r'b)Medium Wind 850[hpa]'], 
                 [r'c)Large  Wind 850[hpa]'], 
              ] 
lev=[850,850,850]

#sempre um intevalo a maid do numero de pontos
#c1=( -3.0  , 0.0  ,21,'[ms$^{-1}$]')
c1=( -8.0  , -6.0  ,21,'[ms$^{-1}$]')

contour     =[
              [c1],
              [c1],
              [c1],
             ]


var_to      =  [
                  [1,1],
                  [1,1],
                  [1,1],
               ]

xlim         =  [
                [(0,50,10)], 
                [(0,50,10)], 
                [(0,50,10)], 
               ]

ylim         =  [
                [(0,50,10)], 
                [(0,50,10)], 
                [(0,50,10)], 
               ]

co1         =  'whbuyl'
co2         =  'RdBu_r'
co3         =  'jet_r'

color       =  [
                [co3,co1],
                [co3,co1],
                [co3,co1],
               ]

####bar ,x,y axis, top_lfc_pbl,size,cm a mais do grafico
a1          =  (True,True,True ,True,0.35,1.34)
a2          =  (False,True,True ,True,0.35,0.06)
a3          =  (False,True,False,True,0.35,0.00)
a4          =  (True ,True,False,True,0.35,1.28)
axis_on     =  [
                [a1,a1],
                [a1,a1],
                [a1,a1],
                ]

l1=(True,10,40)
leg_loc    =  [
                [l1],  
                [l1], 
                [l1]  
              ]

show       =  [
                 [True],
                 [True],
                 [True],
              ]

d1          =(2014,1,1,14,00)

days        = [ 
                [d1],
                [d1],
                [d1],
              ]

#Working to plot whaever variable

#two.plot2d_horizontal(exp,var=var,contour=contour,xlim=xlim,ylim=ylim,days=days,color=color,explabel=exp_label,var_to=var_to,axis_on=axis_on,show=show)

#two.plot2d_horizontal(exp,var=var,days=days,color=color,explabel=exp_label,var_to=var_to,axis_on=axis_on,show=show)

two.plot2d_wind(exp,lev,contour=contour,xlim=xlim,ylim=ylim,days=days,color=color,explabel=exp_label,var_to=var_to,axis_on=axis_on,show=show)

