# -*- coding: utf-8 -*-
"""
Arbeidskrav 1

@author: Terje Jakobsen,      
terjako@gmail.com

GitHub konto: terjako9000

2026 09 20

"""


"""
Forutsetninger:
    km 12000
    registrert 365 dager pr år    
    
"""
#%% felles data

km = 12000 # [kjørte_km]
D = 365 # [dager_pr_år]
t = 8.38 # [sats_trafikkforsikringsavgift]

#%% data_El-bil

E_fors = 5000 # [forsikring]
B_E = 0.1 # [sats_bom_elbil]
P_el = 2 # [kr/kwt]
F_el = 0.2 # [forbruk el]

#%% data_bensinbil

B_fors = 7500 # [forsikring]
B_B = 0.3 # [sats_bom_bensinbil]
P_B = 1 # [forbruk kr/km]

#%% delberegninger El-bil

Bom_E = B_E * km # [bomavgift]
E_fuel_sats = F_el * P_el # [grunnlag_forbrul_el]
E_fuel_forb = E_fuel_sats * km # [totalt_drivstofforbruk_elbil]
t_fors = t * D # [trafikkforsikringsavgift]

#%% delberegninger Bensinbil

Bom_B = B_B * km # [bomavgift]
B_fuel_forb = P_B * km # [totalt_drivstofforbruk_bensinbil]
t_fors = t * D # [trafikkforsikringsavgift]

#%% TOTAL

T_E = Bom_E + E_fuel_forb + t_fors + E_fors # [TOTAL_ELBIL]
T_B = Bom_B + B_fuel_forb + t_fors + B_fors # [TOTAL_BENSINBIL]

#%% DIFFERANSE

DIFF = T_B - T_E

#%% Utskrift

print("TOTAL KOST EL-BIL =" , "kr" , T_E)
print("TOTAL KOST BENSINBIL =" , "kr" , T_B)
print("DIFFERANSEN ÅRLIG = " , "kr" , DIFF)