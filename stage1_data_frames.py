# -------------------------------------------------------------------------------------------------------------------------
# ------------IMPORT LIBRARIES -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
import pandas as pd 
import sys







# -------------------------------------------------------------------------------------------------------------------------
# ------------CHECK EACH COLUMN IN DF PERCENTEAGE OF POPULATION -----------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
from functions_data_frames import check_populated_pct







# -------------------------------------------------------------------------------------------------------------------------
# ------------CHECK DATA QUALITY OF THE DF SUCH AS TYPES,HOW MANY ROWS/COLUMNS,DUPLICATION AND ETC' -----------------------
# -------------------------------------------------------------------------------------------------------------------------
from functions_data_frames import table_viewer







# -------------------------------------------------------------------------------------------------------------------------
# ------------A MENU OPEN USER WILL CHOOSE WHICH DF HE WANTS TO SEE DATA SAMPLE  ------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
from functions_data_frames import table_chooser
table_chooser()








# -------------------------------------------------------------------------------------------------------------------------
# ------------USER MENU WILL OPEN AFTER THE USER WILL SEE THE SAMPLE DATA HE CHOOSE ,CAN CONTINUE TO NEXT STEP OR EXIT  ---
# -------------------------------------------------------------------------------------------------------------------------
from functions_data_frames import menu
menu()





