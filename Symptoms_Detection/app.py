
import pandas as pd

dataset_1= pd.read_csv("training_data.csv")
#dataset_1

#for i in dataset_1.columns:

    #print(i)


# Create a new column with merged column names where value is 1
dataset_1['symptoms_text'] = dataset_1.apply(lambda row: ','.join([col for col in dataset_1.columns if row[col] == 1]), axis=1)

#print("Original DataFrame:")
#print(dataset_1)



#dataset_1.to_csv("training_data_after_changes.csv")


final_dataset = pd.DataFrame(dataset_1[["prognosis","symptoms_text"]])
final_dataset.columns = ['label', 'text']
#final_dataset.to_csv("final_dataset.csv")
#final_dataset

##############3
import pandas as pd
dataset_2= pd.read_csv("Symptom2Disease.csv")
dataset_2 = dataset_2[["label","text"]]
#dataset_2

#################
df_combined = pd.concat([final_dataset, dataset_2], axis=0, ignore_index=True)
#df_combined

################
import nltk
nltk.download('stopwords')
import pandas as pd
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s\,]', ' ', text)
    # Tokenize text
    tokens = word_tokenize(cleaned_text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    
    # Rejoin tokens into a single string
    cleaned_text = ' '.join(tokens)
    
    return cleaned_text

df_combined["cleaned_text"] = df_combined["text"].apply(preprocess_text)

#print(df_combined)


###########
#df_combined.to_csv("final_dataset_llms.csv")

###########

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
print("scikit-learn imported successfully!")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load your dataset
data = pd.read_csv('final_dataset_llms.csv')  # Replace with your file path

# Example columns: 'symptoms' and 'label'
X = data['cleaned_text']
y = data['label']

# Convert text data to numerical data
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, y_pred))

########################pip
#########################
###############################
###########################################

data['label'].nunique()

#############################################

def precaution(label):
    dataset_precau = pd.read_csv("disease_precaution.csv", encoding='latin1')
    label = str(label)
    label = label.lower() 
    
    dataset_precau["Disease"] = dataset_precau["Disease"].str.lower()
    # Filter the DataFrame for the given label
    filtered_precautions = dataset_precau[dataset_precau["Disease"] == label]
    
    # Extract precaution columns
    precautions = filtered_precautions[["Precaution_1", "Precaution_2", "Precaution_3", "Precaution_4"]]
    return precautions.values.tolist()  # Convert DataFrame to a list of lists
     # Return an empty list if no matching label is found

def occurance(label):
    dataset_occur = pd.read_csv("disease_riskFactors.csv", encoding='latin1')
    label = str(label)
    label = label.lower() 
    
    dataset_occur["DNAME"] = dataset_occur["DNAME"].str.lower()
    # Filter the DataFrame for the given label
    filtered_occurrence = dataset_occur[dataset_occur["DNAME"] == label]

    occurrences = filtered_occurrence["OCCUR"].tolist()  # Convert Series to list
    return occurrences
      # Return an empty list if no matching label is found
################################################################################

import streamlit as st
import numpy as np
import sklearn
from sklearn.feature_extraction.text import CountVectorizer

st.title("SYMPTOMS DETECTION, PRECAUTION n OCCURANCE")

symptoms = st.text_area("Enter your symptoms (comma-separated):")

if symptoms.lower() != "exit":
    # Convert input string to a list of symptoms
    

    # Function to predict new symptoms
    def predict_symptoms(new_symptoms):
        preprocessed_text = preprocess_text(new_symptoms)

        if isinstance(preprocessed_text, str):
            new_symptoms = [preprocessed_text]

        # Vectorize the new symptoms
        new_symptoms_vectorized = vectorizer.transform(new_symptoms)
        # Make predictions
        prediction = model.predict(new_symptoms_vectorized)

        return prediction
    
    st.write("disease :")
    symptoms_list = [symptom.strip() for symptom in symptoms.split(',')]

    # Predict symptoms
    prediction = predict_symptoms(' '.join(symptoms_list))

    
    st.write(prediction)
    st.write("precautions:")
    precautions_names = precaution(prediction)
    st.write(precautions_names)
    st.write("Occurance:")
    occurance_name = occurance(prediction)
    st.write(occurance_name) 

else:
    st.write("Please enter symptoms to get the disease.")


    

# Get user input

# Make a prediction









    




