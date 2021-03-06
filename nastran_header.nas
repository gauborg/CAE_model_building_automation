$
$
$
$ output from :
$
$
$
$
$
SOL 101
CEND
$-------------------------------------------------------------$
ECHO=NONE
$TITLE =T1XX SUV K706 Frame Static, JUN'17
SUBTITLE = DURABILITY
$------------------------------------------------------------------------------$
$                      Case Control Cards                                      $
$------------------------------------------------------------------------------$
$
$Anonymous Header SET                                                           
$SET 1= 8000001 THRU 8530192                                                
$
STRESS(PLOT,center)=ALL
DISP(PLOT,center)=ALL
$HMNAME LOADSTEP                 1" 0g Vertical"
SUBCASE 500
    LOAD  = 500
    LABEL = Bending
$$$$$
$HMNAME LOADSTEP                 2" 1.0g Vertical"
SUBCASE 600
    LOAD  = 600
    LABEL = Torsion
$------------------------------------------------------------------------------$
$                      Bulk Data Cards                                         $
$------------------------------------------------------------------------------$
BEGIN BULK
PARAM,AUTOSPC,YES
PARAM,GRDPNT,0
PARAM,MAXRATIO,1.00E+09
PARAM,PRGPST,NO        $ TURN OFF GRID POINT SINGULARITY TABLE PRINT (DEF = YES)
PARAM,POST,-2
PARAM   INREL   -2
$$------------------------------------------------------------------------------$
$$                           Force_Data                                         $
$$------------------------------------------------------------------------------$	
FORCE , 500 , 54 , 0 , 1.0 , 0.0 , 0.0 , -1000.0 
FORCE , 500 , 50 , 0 , 1.0 , 0.0 , 0.0 , -1000.0
FORCE , 500 , 55 , 0 , 1.0 , 0.0 , 0.0 , -1000.0 
FORCE , 500 , 56 , 0 , 1.0 , 0.0 , 0.0 , -1000.0 
FORCE , 600 , 54 , 0 , 1.0 , 0.0 , 0.0 , 1000.0 
FORCE , 600 , 50 , 0 , 1.0 , 0.0 , 0.0 , -1000.0
FORCE , 600 , 55 , 0 , 1.0 , 0.0 , 0.0 , 1000.0 
FORCE , 600 , 56 , 0 , 1.0 , 0.0 , 0.0 , -1000.0
$$----------------------------------------------------------------------------------
INCLUDE 'chassis_demo2.bdf'
ENDDATA
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
