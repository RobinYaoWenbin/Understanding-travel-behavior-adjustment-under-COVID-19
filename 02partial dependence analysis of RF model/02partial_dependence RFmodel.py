import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from collections import Counter
from imblearn.over_sampling import BorderlineSMOTE
from sklearn.ensemble import RandomForestClassifier
from pdpbox import pdp

def get_data(indepvar_filt):
    indepvar_filt.drop(columns=['Unnamed: 0'],inplace=True)
    y_true=indepvar_filt['label'] #y:label
    indepvar_filt.drop(columns=['label'],inplace=True) #x:feature
    feature_names=[i for i in indepvar_filt.columns]
    x_train,x_test,y_train,y_test=train_test_split(indepvar_filt,y_true,test_size=0.3,random_state=0)
    min_max_scaler=preprocessing.MinMaxScaler()
    x_train_minmax=min_max_scaler.fit_transform(x_train) #normalization

    print(Counter(y_train))
    smo=BorderlineSMOTE(random_state=0)
    x_train_minmax_smo,y_train_smo=smo.fit_resample(x_train_minmax,y_train) #SMOTE
    print(Counter(y_train_smo))
    x_train_smo=min_max_scaler.inverse_transform(x_train_minmax_smo) #inverse

    return x_train_smo,y_train_smo,x_test,y_test,feature_names

def model_train(train_data_x,train_data_y): #train
    clf=RandomForestClassifier(n_estimators=500,max_depth= 6,random_state=1,class_weight = 'balanced')
    model=clf.fit(train_data_x,train_data_y)
    return model

def draw_pic(target_feature_name,n,rf_model,feature_names): #draw
    '''
    target_feature_name:name of the target feature
    n:number of the target feature
    '''
    pdp_dist=pdp.pdp_isolate(model=rf_model,dataset=x_test,model_features=feature_names,feature=target_feature_name)
    if n>=10:
        n={n}
    pdp.pdp_plot(pdp_dist,feature_name='$X_{0}$'.format(n),figsize=(10,10))
    plt.show()
    return None



if __name__ == "__main__":

    indepvar_filt=pd.read_csv('data sample.csv',encoding='gbk')
    x_train_smo,y_train_smo,x_test,y_test,feature_names=get_data(indepvar_filt)
    rf_model=model_train(x_train_smo,y_train_smo)
    #draw X4,'count2'
    draw_pic('count2',4,rf_model,feature_names)
    #draw X18,'freqstd4'
    draw_pic('freqstd4',18,rf_model,feature_names)









