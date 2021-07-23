## Why Natural Language Processing?
The purpose of this project is to classify the reviews into one or more defined categories (positive, negative, or neutral) using the best model with the best accuracy score and classification report.

![image](https://user-images.githubusercontent.com/62524529/126676540-acfeaefc-61d9-439c-a61a-85356e3961c0.png)

## How will this help us?
If we sell products from many different parties, we need to figure out how our products are doing to see if we could make our products better. We could scrape and compile the reviews from the 3rd party resellers. With this model, we could see which reviews are positive, negative, or neutral. We can use natural language processing to tell which product lines are doing well or bad. With the products that are doing well, we could market those products more and we can spend more time refining them and developing them. With the products that are not doing so well, we could spend some time to see what common words customers said about the products and use that to improve our products. 

## Connecting Mongo DB to Python
Here we have data in Mongo DB and we want to connect the data to Python.

![image](https://user-images.githubusercontent.com/62524529/126516357-ae719392-cc52-4ef4-a9fb-7c4182335305.png)

We connect python to MongoDB using pymongo library. Then we create a connection to the database using MongoClient. Finally, we pass the collection name to the database and turn it into a dataframe.

![image](https://user-images.githubusercontent.com/62524529/126516498-60bb4521-a3c1-40b8-bfc6-09d3fd031076.png)

## Data Preprocessing
**Data**
 - Removing items that have less than 100 reviews because items that have at least 100 reviews are more impactful
 - Removing reviews that have FALSE in the verified column because reviews were not verified
 - Removing all rows with NA values in reviewText column (our most important column for analysis)
 - Replacing 4 and 5 in overall column with "Positive", replacing 3 with "Neutral", and replacing 1 and 2 with "Negative"
 - Removing all the columns except for overall column (target) and reviewText (analysis)
 - Add two calculated columns: Number of words (length) and number of punctuations (punct) to see if it's useful for predictions

**Reviews**
- Removing HTML code artifacts
- Removing any blank reviews 
- Removing non-word reviews (symbols or numbers)
- Cleaning the reviews text by eliminating stop words 
- Removing punctuations 
- Transform our text into numerical information for the computer to understand

![image](https://user-images.githubusercontent.com/62524529/126501110-cedd20ac-661c-45b0-b9a5-f5c45fa8a491.png)

## Data Visualizations
### Bar Chart of Overall Rating

![image](https://user-images.githubusercontent.com/62524529/126501869-b7c2b0be-efc4-48bd-8407-0e23ef0e64bf.png)

This bar graph shows that there are more positive reviews than neutral and negative. It also shows that there's definitely an imbalanced classes with the overall rating variable.

### Histogram of Number of Words by Rating

![image](https://user-images.githubusercontent.com/62524529/126502022-1d0e14c6-ac75-47c9-8014-2fd5160cd661.png)

This histogram shows that there is not that much difference in number of words (length) between the ratings.

### Histogram of Number of Punctuations by Rating

![image](https://user-images.githubusercontent.com/62524529/126502129-ca74b5e6-1f2d-4014-97b0-f1ef25f243c2.png)

This histogram shows the positive reviews will have less number of punctuations compared to the neutral and negative reviews. 

### Scatterplot of Number of Words vs Number of Punctuations

![image](https://user-images.githubusercontent.com/62524529/126502238-97b1e141-b206-4b58-80ce-66d91ad32723.png)

There is a positive correlation between the number of words and number of punctuations. If we are writing a long review with lots of sentences, there will be lots of punctuations.

### Word Cloud

![image](https://user-images.githubusercontent.com/62524529/126502765-e7214de1-7511-4530-b26b-b4d36f597b20.png)

Notice that "bought" and "mom" is the most frequent words. Out of all these words in the word cloud, we could assume the most frequent words are more on the positive side.

## Partition the Data

![image](https://user-images.githubusercontent.com/62524529/126503007-302cd6c8-661c-48a8-addf-16af9a7f6125.png)

We are creating a sample of 90% for training data and 10% for the test data. Since we already know there’s an imbalanced data between the classes, it is best to use a small test sample size. 

## Model Building
### The classifier that works best with TFIDF vectorizer was LinearSVC.

![image](https://user-images.githubusercontent.com/62524529/126504209-525f8706-ba3f-4fe7-8122-d7f112f53639.png)

- TFIDF vectorizer helps downscale weights for the words that occur in many documents
- Although it has a high accuracy, the data between the classes are imbalanced
- The recall score of positive is really high compared to neutral and negative. Want recall scores to be higher because it correctly identifies the true positives (classes)

### Using a combination of TFIDF vectorizer, Linear SVC, and SMOTE

![image](https://user-images.githubusercontent.com/62524529/126504961-bb7ba9f8-2e5c-4422-b6da-39f35842ed3e.png)

- SMOTE is used for oversampling where we oversample the minority class (neutral) which involves duplicating examples in the minority class
- Our recall scores improved, but low accuracy

### Using a combination of TFIDF vectorizer, Linear SVC, and RandomUnderSampler

![image](https://user-images.githubusercontent.com/62524529/126509216-c504ed7c-1b68-402d-b2ec-44cbf8d2c3c2.png)

- Set the sampling strategy to **not minority** meaning it will resample all classes except for the minority class (neutral)
- The recall scores in the classification report improved and is more balanced between the classes

### Adding ngram_range

![image](https://user-images.githubusercontent.com/62524529/126509430-794f54b5-a6d5-418d-a02f-aa559abe175a.png)

- Set the ngram_range to (1,5), which means combination of 5 words (ex: cheese spicy jalapeno flavored snack)
- Accuracy score improved and the recall scores improved
- **This is the model we want to use for deployment**

## Build the chosen model using the whole dataset
We will make predictions on the entire dataset based on the model we have chosen.

![image](https://user-images.githubusercontent.com/62524529/126666531-380a99f8-aa8a-49b5-af8c-d9f9366ab23b.png)


## Next Steps:
To improve the accuracy score even more, we could look deeper into some reviews to manually add any additional stop words that could help improve our model. 





















