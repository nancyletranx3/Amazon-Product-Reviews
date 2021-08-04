## Why Natural Language Processing?
The purpose of this project is to classify the reviews into one or more defined categories (positive, negative, or neutral) using the best model with the best accuracy score and classification report.

![image](https://user-images.githubusercontent.com/62524529/126676540-acfeaefc-61d9-439c-a61a-85356e3961c0.png)

## How will this help us?
- If we sell products from many different parties, we need to figure out how our products are doing to see if we could make our products better
- Could scrape and compile the reviews from the 3rd party resellers 
- With this model, we could see which reviews are positive, negative, or neutral 
- Use natural language processing to tell which product lines are doing well or bad 
- With the products that are doing well, we could market those products more and we can spend more time refining them and developing them
- With the products that are not doing so well, we could spend some time to see what common words customers said about the products and use that to improve our products 

## Things to Consider
- Natural Language Preprocessing doesn't read sarcasm
- Some customers may confuse 1 star reviews with 5 star reviews and vice versa

## Connecting Mongo DB to Python
Here I have data in Mongo DB and I want to connect the data to Python.

![image](https://user-images.githubusercontent.com/62524529/126516357-ae719392-cc52-4ef4-a9fb-7c4182335305.png)

- Connected MongoDB to Python using pymongo library 
- Created a connection to the database using MongoClient
- Passed the collection name to the database and turn it into a dataframe

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

**Using TFIDF Vectorizer**
- Cleaning the reviews text by eliminating stop words 
- Removing punctuations 
- Transform our text into numerical information for the computer to understand
- Helps downscale weights for the words that occur in many documents (reviews)

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

### Word Cloud

![image](https://user-images.githubusercontent.com/62524529/126502765-e7214de1-7511-4530-b26b-b4d36f597b20.png)

Notice that "bought" and "mom" is the most frequent words. Out of all these words in the word cloud, I assumed the most frequent words are more on the positive side.

## Partition the Data

![image](https://user-images.githubusercontent.com/62524529/126503007-302cd6c8-661c-48a8-addf-16af9a7f6125.png)

I am creating a sample of 90% for training data and 10% for the test data. Since I already know there’s an imbalanced data between the classes, it is best to use a small test sample size. 

## Model Building
### The classifier that works best with TFIDF vectorizer was LinearSVC.

![image](https://user-images.githubusercontent.com/62524529/128206352-d77c54b1-198b-4456-bf17-4b008e0d1737.png)

- Although it has a high accuracy, the data between the classes are imbalanced
- The recall score of positive is really high compared to neutral and negative. Want recall scores to be higher because it correctly identifies the true positives (classes)

### Using a combination of TFIDF vectorizer, Linear SVC, and SMOTE

![image](https://user-images.githubusercontent.com/62524529/126504961-bb7ba9f8-2e5c-4422-b6da-39f35842ed3e.png)

- Using SMOTE will help with oversampling by duplicating examples in the minority class (neutral)
- Our recall scores improved, but low accuracy

### Using a combination of TFIDF vectorizer, Linear SVC, and RandomUnderSampler

![image](https://user-images.githubusercontent.com/62524529/128206593-321cf6c6-aa29-4167-87fa-fc934f46ce95.png)

- Using RandomUnderSampler will help with imbalanced classes by deleting examples from the majority class (positive)
- Set the sampling strategy to **not minority** meaning it will resample all classes except for the minority class (neutral)
- The recall scores in the classification report improved and is more balanced between the classes

### Adding ngram_range

![image](https://user-images.githubusercontent.com/62524529/128206929-f7e687a7-6d2c-407d-919c-c527ac5cc154.png)

- Set the ngram_range to (1,3), which means combination of 2 words (ex: cheesy jalapeno potatoes)
- Accuracy score improved and the recall scores improved
- **This is the model we want to use for deployment**

## Build the chosen model using the whole dataset
I made predictions on the entire dataset using the model I have chosen.

![image](https://user-images.githubusercontent.com/62524529/127019551-ac7cf0c1-115f-4b3f-8169-980bf9905fd0.png)


## Next Steps:
To improve the accuracy score even more, I could look deeper into some reviews to manually add any additional stop words that could help improve my model. Also, remove any sarcastic reviews, good reviews that show up as 1 star, and bad reviews that show up as 5 star.






















