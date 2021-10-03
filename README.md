# Personality Cortex

This project was created during the final weeks of the 25-week part-time Data Science bootcamp run by Le Wagon. Christopher Holmes, Francisco Costa Duarte, and Dr Luke Vano took the project to idea to reality before creating an online app and completing an online presentation. We are indebted to teachers at Le Wagon for their continued support and guidance throughout the bootcamp. We would like to extend a special thank you to Jae Kim and Chris Westerman, who were our project lead teachers, and to Julio Quintana, the lead teacher for our entire bootcamp batch.

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

# Appendix 

The rest of this file details the steps we took to initialise the project.

# Starting up the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for mri_personality in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/mri_personality`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "mri_personality"
git remote add origin git@github.com:{group}/mri_personality.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
mri_personality-run
```

# Install

Go to `https://github.com/{group}/mri_personality` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/mri_personality.git
cd mri_personality
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
mri_personality-run
```
