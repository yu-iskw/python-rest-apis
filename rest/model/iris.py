import argparse
from time import time

from mlxtend.classifier import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.ensemble import VotingClassifier
from sklearn.externals import joblib
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier


class IrisModel(object):

    model = None

    def __init__(self, model_path):
        if self.__class__.model is None:
            self.__class__.model = joblib.load(model_path)

    def predict(self, X):
        start_time = time()
        predictions = self.__class__.model.predict(X)
        result = {
            'prediction': int(predictions[0]),
            'inference_time': time() - start_time
        }
        return result

    @staticmethod
    def train(output_path):
        # Prepare for the data.
        data = load_iris()
        X = data.data
        y = data.target
        target_names = data.target_names
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

        # Train the model.
        dt = DecisionTreeClassifier(random_state=42)
        bnb = BernoulliNB()
        gnb = GaussianNB()
        clf = VotingClassifier(estimators=[
            ('dt', dt),
            ('gnb', gnb),
            ('bnb', bnb),
        ], voting='soft')
        params = {
            'dt__max_depth': list(range(2, 5)),
            'dt__criterion': ['gini', 'entropy'],
            'gnb__var_smoothing': [1e-09, 1e-08, 1e-07],
            'bnb__alpha': [1.0, 0.1, 0.01],
        }
        grid_search = GridSearchCV(clf, param_grid=params, cv=5, scoring='accuracy',
                                   n_jobs=-1, verbose=2)
        grid_search.fit(X_train, y_train)

        # Show best score and parameters.
        print("Best Score: ", grid_search.best_score_)
        print("Best Params: ", grid_search.best_params_)

        # Show metrics on testing data.
        predictions = grid_search.best_estimator_.predict(X_test)
        print(classification_report(y_test, predictions, target_names=target_names))

        # Save the best model.
        best_model = grid_search.best_estimator_
        joblib.dump(best_model, output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--output', type=str, help='host name', required=False, default='iris.joblib')
    args = parser.parse_args()

    IrisModel.train(output_path=args.output)
