import numpy as np

from coen_models import MostLikelyClassPerRegion, MostLikelyClassPerWeekPerDistrict
from predictionmachine.PredictionMachine import PredictionMachine

# features_path = '/home/peter/Documents/kaggle_SFCrime/data/train.npy'
# labels_path   = '/home/peter/Documents/kaggle_SFCrime/data/labels.npy'
features_path = '/Users/coenjonker/Google Drive/kaggle/SFCrime/data/train.npy'
labels_path = '/Users/coenjonker/Google Drive/kaggle/SFCrime/data/labels.npy'
names_path = '/Users/coenjonker/Google Drive/kaggle/SFCrime/data/names.npy'
classes_path = '/Users/coenjonker/Google Drive/kaggle/SFCrime/data/classes.npy'

names = np.load(names_path)
classes = np.load(classes_path)

# classifier = sklearn.dummy.DummyClassifier(strategy='most_frequent')
classifier = MostLikelyClassPerWeekPerDistrict(classes, names)
PM = PredictionMachine(classifier,
                       features_path=features_path, labels_path=labels_path)
PM.run()

classifier = MostLikelyClassPerRegion(classes, names)
PM = PredictionMachine(classifier,
                       features_path=features_path, labels_path=labels_path)
PM.run()
