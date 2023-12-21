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
from    Parameters         import *
from    Parameters_medium  import * 
from    Parameters_large   import *

################################################################ 
# to defined fig out direction, and others important parameters 

# Load function to make the diurnal cycle and profiles figures.  
#import  sam_python.diurnal   as dc

# Load function to make the diurnal cycle and profiles figures.  
import  sam_python.two_dimensional   as two


exp     = [
           small,
           medium,
           large,
           s_w_m,
           s_t_m,
           m_w_l,
           #m_wshf_l,
           #s_t_m_wshf_l,
           #s_qt_m_wshf_l,
          ]

var     =  ['MCUP']###,'RELH','WOBS',]

#separate with comak 
exp_label   = [
                 [r'a) uMF Small'], 
                 [r'b) uMF Medium'], 
                 [r'c) uMF Large'], 
                 [r'd) uMF Small+W(Medium)'], 
                 [r'e) uMF Small+$\mathrm{\theta_{ls}}$(Medium)'], 
                 [r'f) uMF Medium+W(Large)'], 
                 [r'uMF M+[W,SH](L)'], 
                 [r'uMF S+$\mathrm{\theta_{ls}}$(M)+[W,SH](L)'], 
                 [r'uMF S+[$\mathrm{\theta_{ls}}$,q$_{ls}$](M)+[W,SH](L)'], 
              ] 


#print(small.QVOBS.units)
#print(small.WOBS.units)
#print(small.THETAV.units)

#sempre um intevalo a maid do numero de pontos
c1=( 0.001   ,0.12   ,21,'[kgm$^{2}$s$^{-1}$]')

contour     =[
              [c1],
              [c1],
              [c1],
              [c1],
              [c1],
              [c1],
              [c1],
              [c1],
              [c1],
             ]


var_to      =  [
                  [1,1],
                  [1,1],
                  [1,1],
                  [1,1],
                  [1,1],
                  [1,1],
                  [1,1],
                  [1,1],
                  [1,1],
                  [1,1],
               ]

alt         =  [
                [(0,3.5),(0,3.5)], 
                [(0,3.5),(0,3.5)], 
                [(0,3.5),(0,3.5)], 
                [(0,3.5),(0,3.5)], 
                [(0,3.5),(0,3.5)], 
                [(0,3.5),(0,3.5)], 
                [(0,3.5),(0,3.5)], 
                [(0,3.5),(0,3.5)], 
                [(0,3.5),(0,3.5)], 
                [(0,3.5),(0,3.5)], 
                [(0,3.5),(0,3.5)], 
               ]

co1         =  'whbuyl'

color       =  [
                [co1,co1],
                [co1,co1],
                [co1,co1],
                [co1,co1],
                [co1,co1],
                [co1,co1],
                [co1,co1],
                [co1,co1],
                [co1,co1],
                [co1,co1],
                [co1,co1],
               ]

####bar ,x,y axis, top_lfc_pbl,size,cm a mais do grafico
a1          =  (True,True,True ,True,0.35,1.34)
a2          =  (False,True,True ,True,0.35,0.06)
a3          =  (False,True,False,True,0.35,0.00)
a4          =  (True ,True,False,True,0.35,1.28)
axis_on     =  [
                [a2,a2],
                [a3,a3],
                [a4,a4],
                [a2,a2],
                [a3,a3],
                [a4,a4],
                [a1,a1],
                [a1,a1],
                [a1,a1],
                [a1,a1],
                ]


show       =  [
                 [False],
                 [False],
                 [True],
                 [True],
                 [False],
                 [False],
                 [False],
                 [False],
                 [False],
                 [False],
                 [False],
              ]

d1=[(2014,1,1,8,00),(2014,1,1,20,5)]
days        = [ 
                [d1,d1],
                [d1,d1],
                [d1,d1],
                [d1,d1],
                [d1,d1],
                [d1,d1],
                [d1,d1],
                [d1,d1],
                [d1,d1],
                [d1,d1],
              ]


two.plot2d_contour(exp,var=var,contour=contour,alt=alt,days=days,color=color,explabel=exp_label,var_to=var_to,axis_on=axis_on,show=show)


