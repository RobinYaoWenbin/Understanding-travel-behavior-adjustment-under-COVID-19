# Understanding-travel-behavior-adjustment-under-COVID-19

Code for "Understanding travel behavior adjustment under COVID-19"

# Code description
"01Analysis of behavior adjustment pattern under COVID-19 based on LPR data" is the main part of the analysis, which extracts the frequent travel patterns of travelers at all stages of the COVID-19 development based on the license plate recognition data. Then the change of frequent travel pattern is calculated based on frequent travel pattern of each traveler, and the behavior adjustment pattern is obtained on this basis. In addition, this part of the code deeply analyzes the characteristics of each behavior adjustment pattern. Finally, the spatiotemporal travel behavior of travelers before the COVID-19 is extracted to provide support for subsequent analysis.

"02partial dependence analysis of RF model" analyzes the influencing factors of travel behavior adjustment.

"03generate figure" gives the code that plot the figures.

# Structure
```
--01Analysis of behavior adjustment pattern under COVID-19 based on LPR data
----01Analysis of behavior adjustment pattern under COVID-19 based on LPR data(Chinese).ipynb
----01Analysis of behavior adjustment pattern under COVID-19 based on LPR data(English).ipynb
----LPR_data_sample.csv
----YIWU_POI_data.txt
--02partial dependence analysis of RF model
----02partial_dependence RFmodel.py
----data sample.csv
--03generate figure
----Fig. 4 Clustering performance change with the number of clusters
------Fig. 4 Clustering performance change with the number of clusters..ipynb
----Fig. 6 Travel behavior adjustment of each cluster at each stage
------Fig. 6 Travel behavior adjustment of each cluster at each stage..ipynb
------first_last_dec_cluster0.csv
------first_last_dec_cluster1.csv
------first_last_dec_cluster2.csv
------freqdistribution_cluster0.xlsx
------freqdistribution_cluster1.xlsx
------freqdistribution_cluster2.xlsx
------NVT_ATI_cluster0.xlsx
------NVT_ATI_cluster1.xlsx
------NVT_ATI_cluster2.xlsx
```
