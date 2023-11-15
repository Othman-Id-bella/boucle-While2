p_Agadir=500000
p_Marrakech=1000000
nbr_years=0
while p_Marrakech>p_Agadir:
    p_Agadir=p_Agadir*1.08
    p_Marrakech=p_Marrakech+50000
    nbr_years=nbr_years+1
print("Agadir will overtake Marrakech after",nbr_years,"years")