# -*- coding: utf-8 -*-
'''
>>> from pycm import *
>>> import os
>>> import json
>>> import numpy as np
>>> y_test = np.array([600, 200, 200, 200, 200, 200, 200, 200, 500, 500, 500, 200, 200, 200, 200, 200, 200, 200, 200, 200])
>>> y_pred = np.array([100, 200, 200, 100, 100, 200, 200, 200, 100, 200, 500, 100, 100, 100, 100, 100, 100, 100, 500, 200])
>>> cm=ConfusionMatrix(y_test, y_pred)
>>> save_stat=cm.save_stat("test",address=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("test_filtered",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("test_filtered2",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"],class_name=["L1","L2"])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("test_filtered3",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"],class_name=[])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_stat("/asdasd,qweqwe.eo/",address=True)
>>> save_stat=={'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.pycm'"}
True
>>> save_stat=cm.save_html("test",address=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_filtered",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_filtered2",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"],class_name=[100])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_filtered3",address=False,overall_param=["Kappa","Scott PI"],class_param=["TPR","TNR","ACC","AUC"],class_name=[])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_filtered4",address=False,overall_param=["Kappa","Scott PI"],class_param=[],class_name=[100])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_filtered5",address=False,overall_param=[],class_param=["TPR","TNR","ACC","AUC"],class_name=[100])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("test_colored",address=False,color=(130,100,200))
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test",address=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test_filtered",address=False,class_param=["TPR","TNR","ACC","AUC"])
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test_filtered2",address=False,class_param=["TPR","TNR","ACC","AUC"],class_name=[100],matrix_save=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test_filtered3",address=False,class_param=["TPR","TNR","ACC","AUC"],class_name=[],matrix_save=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_csv("test_filtered4",address=False,class_param=[],class_name=[100],matrix_save=False)
>>> save_stat=={'Status': True, 'Message': None}
True
>>> save_stat=cm.save_html("/asdasd,qweqwe.eo/",address=True)
>>> save_stat=={'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.html'"}
True
>>> save_stat=cm.save_csv("/asdasd,qweqwe.eo/",address=True)
>>> save_stat=={'Status': False, 'Message': "[Errno 2] No such file or directory: '/asdasd,qweqwe.eo/.csv'"}
True
>>> save_obj=cm.save_obj("test",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> cm_file=ConfusionMatrix(file=open("test.obj","r"))
>>> print(cm_file)
Predict          100    200    500    600
Actual
100              0      0      0      0
<BLANKLINE>
200              9      6      1      0
<BLANKLINE>
500              1      1      1      0
<BLANKLINE>
600              1      0      0      0
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.14096,0.55904)
AUNP                                                             None
AUNU                                                             None
Bennett S                                                        0.13333
CBA                                                              0.17708
Chi-Squared                                                      None
Chi-Squared DF                                                   9
Conditional Entropy                                              1.23579
Cramer V                                                         None
Cross Entropy                                                    1.70995
Gwet AC1                                                         0.19505
Hamming Loss                                                     0.65
Joint Entropy                                                    2.11997
KL Divergence                                                    None
Kappa                                                            0.07801
Kappa 95% CI                                                     (-0.2185,0.37453)
Kappa No Prevalence                                              -0.3
Kappa Standard Error                                             0.15128
Kappa Unbiased                                                   -0.12554
Lambda A                                                         0.0
Lambda B                                                         0.0
Mutual Information                                               0.10088
NIR                                                              0.8
Overall ACC                                                      0.35
Overall CEN                                                      0.3648
Overall J                                                        (0.60294,0.15074)
Overall MCC                                                      0.12642
Overall MCEN                                                     0.37463
Overall RACC                                                     0.295
Overall RACCU                                                    0.4225
P-Value                                                          1.0
PPV Macro                                                        None
PPV Micro                                                        0.35
Phi-Squared                                                      None
RCI                                                              0.11409
RR                                                               5.0
Reference Entropy                                                0.88418
Response Entropy                                                 1.33667
SOA1(Landis & Koch)                                              Slight
SOA2(Fleiss)                                                     Poor
SOA3(Altman)                                                     Poor
SOA4(Cicchetti)                                                  Poor
Scott PI                                                         -0.12554
Standard Error                                                   0.10665
TPR Macro                                                        None
TPR Micro                                                        0.35
Zero-one Loss                                                    13
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          100                     200                     500                     600
ACC(Accuracy)                                                    0.45                    0.45                    0.85                    0.95
AM(Difference between automatic and manual classification)       11                      -9                      -1                      -1
AUC(Area under the roc curve)                                    None                    0.5625                  0.63725                 0.5
AUCI(AUC value interpretation)                                   None                    Poor                    Fair                    Poor
BCD(Bray-Curtis dissimilarity)                                   0.275                   0.225                   0.025                   0.025
BM(Informedness or bookmaker informedness)                       None                    0.125                   0.27451                 0.0
CEN(Confusion entropy)                                           0.33496                 0.35708                 0.53895                 0.0
DOR(Diagnostic odds ratio)                                       None                    1.8                     8.0                     None
DP(Discriminant power)                                           None                    0.14074                 0.4979                  None
DPI(Discriminant power interpretation)                           None                    Poor                    Poor                    None
ERR(Error rate)                                                  0.55                    0.55                    0.15                    0.05
F0.5(F0.5 score)                                                 0.0                     0.68182                 0.45455                 0.0
F1(F1 score - harmonic mean of precision and sensitivity)        0.0                     0.52174                 0.4                     0.0
F2(F2 score)                                                     0.0                     0.42254                 0.35714                 0.0
FDR(False discovery rate)                                        1.0                     0.14286                 0.5                     None
FN(False negative/miss/type 2 error)                             0                       10                      2                       1
FNR(Miss rate or false negative rate)                            None                    0.625                   0.66667                 1.0
FOR(False omission rate)                                         0.0                     0.76923                 0.11111                 0.05
FP(False positive/type 1 error/false alarm)                      11                      1                       1                       0
FPR(Fall-out or false positive rate)                             0.55                    0.25                    0.05882                 0.0
G(G-measure geometric mean of precision and sensitivity)         None                    0.56695                 0.40825                 None
GI(Gini index)                                                   None                    0.125                   0.27451                 0.0
IS(Information score)                                            None                    0.09954                 1.73697                 None
J(Jaccard index)                                                 0.0                     0.35294                 0.25                    0.0
LS(Lift score)                                                   None                    1.07143                 3.33333                 None
MCC(Matthews correlation coefficient)                            None                    0.10483                 0.32673                 None
MCEN(Modified confusion entropy)                                 0.33496                 0.37394                 0.58028                 0.0
MK(Markedness)                                                   0.0                     0.08791                 0.38889                 None
N(Condition negative)                                            20                      4                       17                      19
NLR(Negative likelihood ratio)                                   None                    0.83333                 0.70833                 1.0
NPV(Negative predictive value)                                   1.0                     0.23077                 0.88889                 0.95
P(Condition positive or support)                                 0                       16                      3                       1
PLR(Positive likelihood ratio)                                   None                    1.5                     5.66667                 None
PLRI(Positive likelihood ratio interpretation)                   None                    Poor                    Fair                    None
POP(Population)                                                  20                      20                      20                      20
PPV(Precision or positive predictive value)                      0.0                     0.85714                 0.5                     None
PRE(Prevalence)                                                  0.0                     0.8                     0.15                    0.05
RACC(Random accuracy)                                            0.0                     0.28                    0.015                   0.0
RACCU(Random accuracy unbiased)                                  0.07563                 0.33062                 0.01562                 0.00063
TN(True negative/correct rejection)                              9                       3                       16                      19
TNR(Specificity or true negative rate)                           0.45                    0.75                    0.94118                 1.0
TON(Test outcome negative)                                       9                       13                      18                      20
TOP(Test outcome positive)                                       11                      7                       2                       0
TP(True positive/hit)                                            0                       6                       1                       0
TPR(Sensitivity, recall, hit rate, or true positive rate)        None                    0.375                   0.33333                 0.0
Y(Youden index)                                                  None                    0.125                   0.27451                 0.0
dInd(Distance index)                                             None                    0.67315                 0.66926                 1.0
sInd(Similarity index)                                           None                    0.52401                 0.52676                 0.29289
<BLANKLINE>
>>> def activation(i):
...	    if i<0.7:
...		    return 1
...	    else:
...		    return 0
>>> cm_6 = ConfusionMatrix([0,0,1,0],[0.87,0.34,0.9,0.12],threshold=activation)
>>> save_obj=cm_6.save_obj("test2",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> cm_file_2=ConfusionMatrix(file=open("test2.obj","r"))
>>> cm_file_2.print_matrix()
Predict          0        1
Actual
0                1        2
1                1        0
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred, sample_weight=[2, 2, 2, 2, 3, 1, 1, 2, 2, 1, 1, 2])
>>> save_obj=cm.save_obj("test3",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> cm_file_3=ConfusionMatrix(file=open("test3.obj","r"))
>>> cm_file_3.print_matrix()
Predict          0    1    2
Actual
0                6    0    0
1                0    1    2
2                4    2    6
<BLANKLINE>
>>> cm_file_3.stat()
Overall Statistics :
<BLANKLINE>
95% CI                                                           (0.41134,0.82675)
AUNP                                                             0.7
AUNU                                                             0.70556
Bennett S                                                        0.42857
CBA                                                              0.47778
Chi-Squared                                                      10.44167
Chi-Squared DF                                                   4
Conditional Entropy                                              0.96498
Cramer V                                                         0.49861
Cross Entropy                                                    1.50249
Gwet AC1                                                         0.45277
Hamming Loss                                                     0.38095
Joint Entropy                                                    2.34377
KL Divergence                                                    0.1237
Kappa                                                            0.3913
Kappa 95% CI                                                     (0.05943,0.72318)
Kappa No Prevalence                                              0.2381
Kappa Standard Error                                             0.16932
Kappa Unbiased                                                   0.37313
Lambda A                                                         0.22222
Lambda B                                                         0.36364
Mutual Information                                               0.47618
NIR                                                              0.57143
Overall ACC                                                      0.61905
Overall CEN                                                      0.43947
Overall J                                                        (1.22857,0.40952)
Overall MCC                                                      0.41558
Overall MCEN                                                     0.50059
Overall RACC                                                     0.37415
Overall RACCU                                                    0.39229
P-Value                                                          0.41709
PPV Macro                                                        0.56111
PPV Micro                                                        0.61905
Phi-Squared                                                      0.49722
RCI                                                              0.34536
RR                                                               7.0
Reference Entropy                                                1.37878
Response Entropy                                                 1.44117
SOA1(Landis & Koch)                                              Fair
SOA2(Fleiss)                                                     Poor
SOA3(Altman)                                                     Fair
SOA4(Cicchetti)                                                  Poor
Scott PI                                                         0.37313
Standard Error                                                   0.10597
TPR Macro                                                        0.61111
TPR Micro                                                        0.61905
Zero-one Loss                                                    8
<BLANKLINE>
Class Statistics :
<BLANKLINE>
Classes                                                          0                       1                       2
ACC(Accuracy)                                                    0.80952                 0.80952                 0.61905
AM(Difference between automatic and manual classification)       4                       0                       -4
AUC(Area under the roc curve)                                    0.86667                 0.61111                 0.63889
AUCI(AUC value interpretation)                                   Very Good               Fair                    Fair
BCD(Bray-Curtis dissimilarity)                                   0.09524                 0.0                     0.09524
BM(Informedness or bookmaker informedness)                       0.73333                 0.22222                 0.27778
CEN(Confusion entropy)                                           0.25                    0.52832                 0.56439
DOR(Diagnostic odds ratio)                                       None                    4.0                     3.5
DP(Discriminant power)                                           None                    0.33193                 0.29996
DPI(Discriminant power interpretation)                           None                    Poor                    Poor
ERR(Error rate)                                                  0.19048                 0.19048                 0.38095
F0.5(F0.5 score)                                                 0.65217                 0.33333                 0.68182
F1(F1 score - harmonic mean of precision and sensitivity)        0.75                    0.33333                 0.6
F2(F2 score)                                                     0.88235                 0.33333                 0.53571
FDR(False discovery rate)                                        0.4                     0.66667                 0.25
FN(False negative/miss/type 2 error)                             0                       2                       6
FNR(Miss rate or false negative rate)                            0.0                     0.66667                 0.5
FOR(False omission rate)                                         0.0                     0.11111                 0.46154
FP(False positive/type 1 error/false alarm)                      4                       2                       2
FPR(Fall-out or false positive rate)                             0.26667                 0.11111                 0.22222
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.33333                 0.61237
GI(Gini index)                                                   0.73333                 0.22222                 0.27778
IS(Information score)                                            1.07039                 1.22239                 0.39232
J(Jaccard index)                                                 0.6                     0.2                     0.42857
LS(Lift score)                                                   2.1                     2.33333                 1.3125
MCC(Matthews correlation coefficient)                            0.66332                 0.22222                 0.28307
MCEN(Modified confusion entropy)                                 0.26439                 0.52877                 0.65924
MK(Markedness)                                                   0.6                     0.22222                 0.28846
N(Condition negative)                                            15                      18                      9
NLR(Negative likelihood ratio)                                   0.0                     0.75                    0.64286
NPV(Negative predictive value)                                   1.0                     0.88889                 0.53846
P(Condition positive or support)                                 6                       3                       12
PLR(Positive likelihood ratio)                                   3.75                    3.0                     2.25
PLRI(Positive likelihood ratio interpretation)                   Poor                    Poor                    Poor
POP(Population)                                                  21                      21                      21
PPV(Precision or positive predictive value)                      0.6                     0.33333                 0.75
PRE(Prevalence)                                                  0.28571                 0.14286                 0.57143
RACC(Random accuracy)                                            0.13605                 0.02041                 0.21769
RACCU(Random accuracy unbiased)                                  0.14512                 0.02041                 0.22676
TN(True negative/correct rejection)                              11                      16                      7
TNR(Specificity or true negative rate)                           0.73333                 0.88889                 0.77778
TON(Test outcome negative)                                       11                      18                      13
TOP(Test outcome positive)                                       10                      3                       8
TP(True positive/hit)                                            6                       1                       6
TPR(Sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5
Y(Youden index)                                                  0.73333                 0.22222                 0.27778
dInd(Distance index)                                             0.26667                 0.67586                 0.54716
sInd(Similarity index)                                           0.81144                 0.52209                 0.6131
>>> cm = ConfusionMatrix(matrix={1:{1:13182,2:30516},2:{1:5108,2:295593}},transpose=True) # Verified Case
>>> save_obj = cm.save_obj("test4",address=False)
>>> save_obj=={'Status': True, 'Message': None}
True
>>> cm_file=ConfusionMatrix(file=open("test4.obj","r"))
>>> cm_file.DP[1]
0.770700985610517
>>> cm_file.Y[1]
0.627145631592811
>>> cm_file.BM[1]
0.627145631592811
>>> cm_file.transpose
True
>>> json.dump({"Actual-Vector": None, "Digit": 5, "Predict-Vector": None, "Matrix": {"0": {"0": 3, "1": 0, "2": 2}, "1": {"0": 0, "1": 1, "2": 1}, "2": {"0": 0, "1": 2, "2": 3}}, "Transpose": True,"Sample-Weight": None},open("test5.obj","w"))
>>> cm_file=ConfusionMatrix(file=open("test5.obj","r"))
>>> cm_file.transpose
True
>>> cm_file.matrix == {"0": {"0": 3, "1": 0, "2": 2}, "1": {"0": 0, "1": 1, "2": 1}, "2": {"0": 0, "1": 2, "2": 3}}
True

>>> os.remove("test.csv")
>>> os.remove("test_matrix.csv")
>>> os.remove("test.obj")
>>> os.remove("test.html")
>>> os.remove("test_filtered.html")
>>> os.remove("test_filtered.csv")
>>> os.remove("test_filtered_matrix.csv")
>>> os.remove("test_filtered.pycm")
>>> os.remove("test_filtered2.html")
>>> os.remove("test_filtered3.html")
>>> os.remove("test_filtered4.html")
>>> os.remove("test_filtered5.html")
>>> os.remove("test_colored.html")
>>> os.remove("test_filtered2.csv")
>>> os.remove("test_filtered3.csv")
>>> os.remove("test_filtered4.csv")
>>> os.remove("test_filtered2.pycm")
>>> os.remove("test_filtered3.pycm")
>>> os.remove("test2.obj")
>>> os.remove("test3.obj")
>>> os.remove("test4.obj")
>>> os.remove("test5.obj")
>>> os.remove("test.pycm")
'''
