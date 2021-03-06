from sklearn.metrics import confusion_matrix,classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

data = pd.read_csv("amazon_dataframe.csv")

data = pd.read_csv("amazon_dataframe.csv")

train_data = data.head(40000)
test_data = data.tail(10000)

train_data ['feedback sentiment'] = train_data ['star_rating'].apply(lambda rating : 1 if rating > 3.0 else (-1 if rating < 3.0  else 0))
test_data ['feedback sentiment'] = test_data ['star_rating'].apply(lambda rating : 1 if rating > 3.0 else (-1 if rating < 3.0  else 0) )


print(train_data)
print(test_data)

tokenizer = CountVectorizer(token_pattern=r'\b\w+\b')

train_matrix = tokenizer.fit_transform(train_data['review_body'].values.astype('U'))
test_matrix = tokenizer.transform(test_data['review_body'].values.astype('U'))

neigh = KNeighborsClassifier(n_neighbors=3)

neigh.fit(train_matrix,train_data['feedback sentiment'])

prediction = neigh.predict(test_matrix)

print(confusion_matrix(test_data['feedback sentiment'],prediction))
print(classification_report(test_data['feedback sentiment'],prediction))