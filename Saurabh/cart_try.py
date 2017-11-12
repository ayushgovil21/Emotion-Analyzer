import csv
import pickle
import numpy as np 
from sklearn import tree

def function(userName):
    clf=tree.DecisionTreeClassifier(max_leaf_nodes=20)
    x11 = []
    i=0
    x1 = [0, 1, 1, 2, 9, 2]
    x2 = [0, 0, 1, 1, 5, 1]
    x3 = [9, 4, 11, 3,3,8]
    X1 = np.array([x1,x2,x3]).T
    last_emt=None
    counter=0
    decision_vector=[]
    f= open("ans_exp","rb")
    f1 = open("vector1","rb")
    f=pickle.load(f)
    f1 = pickle.load(f1)
    tmp=[]
    for i in set(f):
        tmp.append(f.count(i))
    decision_vector = np.append(decision_vector,counter)
    x11 = np.array(x11)
    #X=np.array(trainingData[0])
    y=np.array(decision_vector)
    clf=clf.fit(f1,f)
    features=["anger","anticipation","disgust","fear","joy","sad","surprise","trust"]
    with open("dst.dot","w") as f:
        f = tree.export_graphviz(clf,
                                feature_names=features,
                                class_names=["anger","anticipation","disgust","fear","joy","sad","surprise","trust"],
                                filled=True, rounded=True,special_characters=True,out_file=f)

    #Reading test tweet and test vector files below


    file1 = open('%s_latest_tweets' % userName,'wb')
    file2 = open('%s_test_vectors' % userName,'wb')

    tweets = pickle.load(file1)
    vectors = pickle.load(file2)

    for i in range(0,len(tweets)):
            print('Tweet: ', tweets[i])
            print('Vectors: ', vectors[i])
            print('Emotion: ', clf.predict([vectors[i]]))
            print('\n')
