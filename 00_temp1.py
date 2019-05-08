# -*- coding:utf-8 -*-
# from sklearn import neighbors, datasets, preprocessing
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# iris = datasets.load_iris()
# X, y = iris.data[:, :2], iris.target
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33)
# scaler = preprocessing.StandardScaler().fit(X_train)
# X_train = scaler.transform(X_train)
# X_test = scaler.transform(X_test)
# knn = neighbors.KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train, y_train)
# y_pred = knn.predict(X_test)
# accuracy_score(y_test, y_pred)
# a=-100
# print(abs(a))

# import UserDict


# class Zoo:
#     def __getitem__(self, key):
#         if key == 'dog':
#             return 'dog'
#         elif key == 'pig':
#             return 'pig'
#         elif key == 'wolf':
#             return 'wolf'
#         else:
#             return 'unknown'
#
#
# zoo = Zoo()
# print(zoo['dog'])

class Person(object):
    def __init__(self, newPersonName):
        self.name = newPersonName
        '''
        如果此处不写成self.name
        那么此处的name，只是__init__函数中的局部临时变量name而已
        和全局中的name，没有半毛钱关系
        '''
        # name = newPersonName
        '''
        此处只是为了代码演示，而使用了局部变量name，
        不过需要注意的是，此处很明显，由于接下来的代码也没有利用到此处的局部变量name
        则就导致了，此处的name变量，实际上被浪费了，根本没有利用到
        '''

    def sayYourName(self):
        '''
        此处由于找不到实例中的name变量，所以会报错：
        AttributeError: Person instance has no attribute 'name'
        '''
        print('My name is %s' % self.name)


def selfAndInitDemo():
    personInstance = Person('Tim')
    personInstance.sayYourName()


if __name__ == '__main__':
    selfAndInitDemo()

