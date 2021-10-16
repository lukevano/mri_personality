# Personality Cortex

This project was created during the final weeks of the 25-week part-time Data Science bootcamp run by Le Wagon. Christopher Holmes, Francisco Costa Duarte, and Dr Luke Vano took the project to idea to reality before creating an online app and completing an online presentation. We are indebted to teachers at Le Wagon for their continued support and guidance throughout the bootcamp. We would like to extend a special thank you to Jae Kim and Chris Westerman, who were our project lead teachers, and to Julio Quintana, the lead teacher for our entire bootcamp batch.

Link to the online presentation:
https://www.youtube.com/watch?v=AY5JIDGuu4U

## Identified problems

- The most accurate personality tests currently allow the measurement of discrete personality traits across a scale. NEO-FFI is the most commonly used and for this scale you are given a score for each of the following domains: Neuroticism, Extraversion, Openness, Agreeableness, and Conscientiousness. Whilst it is known that relationships exist between these traits, for example Neuroticism and Conscientiousness are inversely correlated, current personality tests do not look at these relationships. Is it possible that these personality clusters could be identified using a large NEO-FFI dataset?
- Whilst there is evidence that the size and thickness of different brain areas are related to personality, cortical thickness is inversly correlated with neuroticism (Riccelli, 2017), we were unable to find a published model that could take in one's brain thinckness/volume data and give out a prediction of their personality.
- Current methods of generating brain thickness/volume data from MRI images (FreeSurfer: https://surfer.nmr.mgh.harvard.edu/) are reliable but may take 6-24 hours to generate the data for one image. Is there a way that enough of this thickness/volume data could be generate to allow the prediction of personality in seconds from MRI images?

## Methods

- We used The Amsterdam Open MRI Collection (AOMIC) for our NEO-FFI and MRI data, gaining 1370 participants with data we could use for building our models.
- K-means clustering was used to identify 5 personality clusters from the NEO-FFI traits. These clusters were used as targets- we would be predicting which personality cluster each participant fell into using their brain imagin data and comparing this with the cluster generated using their NEO-FFI scores.
- Build a logistic regression model that would predict which cluster a participant would fall into given their MRI data. The features for this model would be the thickness and volume data generated from FreeSurfer (around 120 features).
- Build a convoluntional neural network that would take in MRI data and make predictions on which cluster the participant would fall into.
- Generate an online app where users could input their MRI or thickness/volume data and get predictions on their personality clusters.

## Output

- Please see the slides in the presentations folder for a breakdown of our results.
