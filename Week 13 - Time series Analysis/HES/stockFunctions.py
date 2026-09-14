def conversion(y_train,stk_data):
    import pandas as pd
    Actual_y_train=pd.DataFrame(index=range(len(y_train)),columns=stkdata.columns)
    for i in range(len(y_train)):
        Actual_y_train.iloc[i]=y_train[i]
    return Actual_y_train

def graph(Actual, predicted, Actlabel, predlabel,title,Xlabel,ylabel):
    from matplotlib import pyplot as plt
    plt.figure(figsize=(10,5))
    plt.plot(Actual,color='blue',label=Actlabel)
    plt.plot(predicted,color='green',label=predlabel)
    plt.title(title)
    plt.xlabel(Xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

def rmsemape(y_Test,predicted_stock_price_test_ori):
    from sklearn.metrics import mean_squared_error
    print("RMSE-Testset:",mean_squared_error(y_Test,predicted_stock_price_test_ori,squared=False))
    from sklearn.metrics import mean_absolute_percentage_error
    print("maPe-Testset:",mean_absolute_percentage_error(y_Test,predicted_stock_price_test_ori))

def conversionSingle(y_train,stk_data):
    import pandas as pd
    Actual_y_train=pd.DataFrame(index=range(len(y_train)),columns=stk_data)
    for i in range(len(y_train)):
        Actual_y_train.iloc[i]=y_train[i]
    return Actual_y_train

def conversionOriginal(y_pred,stk_data,Ms):
    from stockFunctions import conversionSingle
    pTestNormTable=conversionSingle(y_pred,stk_data)
    stock_price_test =Ms.inverse_transform(pTestNormTable)
    stock_price_test_ori=conversionSingle(stock_price_test,stk_data)
    return stock_price_test_ori