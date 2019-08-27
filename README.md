![title](https://github.com/TaraRosen/Cannabis_Rec_Engine/blob/master/1_title.png)

Imagine that all forms of marijuana are now legal across the U.S. and imagine that you just finished up a huge and stressful project. It’s time to relax, you go into your child proof lock box and, oh my goodness, you are low on your favorite strain. 

You head to your favorite website and your day just got worse, your favorite strain is out of stock -

![out of stock](https://github.com/TaraRosen/Cannabis_Rec_Engine/blob/master/2_out_of_stock.png)

Within the next few years, this scenario could become a reality.

## Public Sentiment

![status by state](https://github.com/TaraRosen/Cannabis_Rec_Engine/blob/master/3_status_by_state.png)

Currently, there are 33 states that allow medical marijuana.

There are 11 states where marijuana is fully legal and decriminalized, and 15 states where there is reduced criminalization. 

There are just 12 states where marijuana is fully illegal. 

And public sentiment is shifting...

![public sentiment](https://github.com/TaraRosen/Cannabis_Rec_Engine/blob/master/4_sentiment_changing_1.png)



*Over the last 10 or 15 years, the American people’s attitudes have changed dramatically,” Boehner told Bloomberg. “I find myself in that same position.”*                                                        -John Boehner, Former House Speaker 


And in April of this year, the largest cannabis company in the world, Canadian-based Canopy Growth, entered into a multi-billion deal to acquire American medical marijuana firm, Acreage Holdings. This is a deal that can only take effect once the federal government legalizes marijuana. If we were to read the tea leaves, it would appear that federal legalization could be happening soon.

So what does all this mean? It means that this hypothetical situation of your favorite website being out of your favorite strain could become a reality and you will need a recommendation for a strain that will make you feel similar to the way
your favorite strain makes you feel.

## Data

Using the world’s largest cannabis information resource, leafly.com, I scraped the urls of over 3000 strains and ended up creating a database of over 2600 strains. 

Included in this database were the strain name, positive attributes, medicinal purposes, negative side effects, category (indica, sativa, or hybrid) and flavors.

![blue dream attributes](https://github.com/TaraRosen/Cannabis_Rec_Engine/blob/master/5_features.png)

## Analysis Using NLP, CountVectorizer and Cosine Similarity

I used Natural Language Processing (NLP) to process the text data with scikit-learn’s CountVectorizer. 

I used CountVectorizer to represent my text attributes as vectors. I combined all of the features for each strain into a single corpus in a newly created ‘combined’ column and count vectorized that column. Because I needed a simple frequency counter for each word in my combined column, I went with count vectorization rather than TF-IDF. TF-IDF would give less importance to words that are more present in the entire dataframe’s combined column, whereas, count vectorization makes every word important. Scikit-learn’s cosine_similarity was then used to build a recommendation engine that takes in a strain and returned the top 5 recommended strains.

## Recommendation Engine Results Using Blue Dream Strain:

### Blue Dreams 5 Most Similar Strains:

['cherry skunk', 'elvis', 'blueberry headband', 'white berry', 'bruce banner 3']

### How Blue Dream Matches Up to Cherry Skunk, its most similar recommendation:

It looks like Blue Dream’s top match is Cherry Skunk. As you can see, Cherry Skunk matches up exactly with Blue Dream on the top 3 effects and matches up on all 5 effects.   

For medicinal purposes, Cherry Skunk doesn’t have any exact matches with Blue Dream, however the same 5 medical purposes that people use Blue Dream for are the same 5 medical purposes that people use Cherry Skunk for. 

![blue dream cherry skunk comp1](https://github.com/TaraRosen/Cannabis_Rec_Engine/blob/master/6_results_1.png)

For negative attributes, Blue Dream and Cherry Skunk match up perfectly on 3 attributes and share the other two.

And finally, both strains match up on 2 out of the 3 of their flavors and their type.

![blue dream cherry skunk comp2](https://github.com/TaraRosen/Cannabis_Rec_Engine/blob/master/7_results_2.png)

Overall, Blue Dream and Cherry Skunk match up exactly on 9 out of 19 of their attributes and share 18 out of 19 of the same attributes.

Looks like NLP with CountVectorizer and cosine similarity works pretty well and I think that someone would be very pleased with using Cherry Skunk as a Blue Dream substitute!




[Code File](https://github.com/TaraRosen/Cannabis_Rec_Engine/blob/master/Cannabis%20Recommender%20-%20DS042219%20-%20Final.ipynb)
[Quick Recommendation](https://github.com/TaraRosen/Cannabis_Rec_Engine/blob/master/Recommend_Closest_5_Strains.ipynb)