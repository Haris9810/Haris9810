import numpy as np
import pandas as pd
import seaborn as sns
import random
from matplotlib import pyplot as plt
from collections import Counter
from sklearn.utils import resample
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.models import  Sequential

from keras.callbacks import EarlyStopping
from keras.layers import BatchNormalization, Convolution2D , MaxPooling2D
from sklearn.decomposition import PCA
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore",category=plt.cbook.mplDeprecation)
random.seed(54)

train=pd.read_csv('heart.csv')


train.head()