# Anomaly_ML
Anomaly detection based on autoencoders

Directories & Files:
Anomaly_ML
	main.py
	anomaly_detector.py
	denoising_autoencoder.py
	preprocessing_noising.py
	Data
		/Model
		/Train
			/rescaled
		/Test
		/Original_data
			/Background_pattern
			/Objects_pattern
				/similar_to_anomalies
				/random_objects
		/Prediction_output
		
generate_data.py
Generate a dataset of synthetic data.
Input:
	n_samples 
	n_objects
	paths to backgronds_pattern
	paths to objects_pattern
	paths to Train
Output:
	Dataset in path(Train)

## Anomaly detection based on autoencoders


An Anomaly is an event or item that deviates from what is expected. The frequency of an anomaly is low in comparison to the frequency of standard events. The anomalies that can occur in the products are usually random, some examples are changes in color or texture, scratches, misalignment, missing pieces, or errors in the proportions.
Anomaly Detection allows us to fix or eliminate those parts or elements that are in bad condition from the production chain. As a result manufacturing costs are reduced because of the avoidance of producing and marketing defective products. Anomaly detection, in factories, is a useful tool for Quality Control Systems because of its features and is a big challenge for Machine Learning Engineers.

![alt text](https://miro.medium.com/max/700/0*DQvbb_OURR2qNs8Z)

###Directories & Files: 
Anomaly_ML main.py anomaly_detector.py denoising_autoencoder.py preprocessing_noising.py Data /Model /Train /rescaled /Test /Original_data /Background_pattern /Objects_pattern /similar_to_anomalies /random_objects /Prediction_output

###generate_data.py 
Generate a dataset of synthetic data. Input: n_samples n_objects paths to backgronds_pattern paths to objects_pattern paths to Train Output: Dataset in path(Train)
![alt text](https://miro.medium.com/max/700/0*_Le5C1fvUFaDn52e)

###data_load.py 
Rescale and load data splitting in Train & validate dataset. Name format for files is noised_file_name = background_name + '__' + id_noised_image Input: path to background_pattern path to noised images Output: train dataset arrays validation dataset arrays

###denosing_autoencoder.py 
Define autoencoder structure in Keras Train the model Return the model Input: path to train / validation path to model (default) size of inputs (tuple) filters per layer (list) Output: Histogram visualization (similar vs non similar) Metrics (F1, accuracy, precision,recall) threshold_1.txt autoencoder.h5

![alt text](https://miro.medium.com/max/660/0*_OTOWs4ENnYboRgh)
###generate_validation_metrics.py 
Generate metrics based on validation data. Help to tune the threshold. Input: model path to real_not_anomalies path to real_anomalies Output: Histogram visualization (similar vs non similar) Metrics (F1, accuracy, precision,recall) threshold_2.txt

###image_visualization.py 
Visualize images based on parameters. Used to debug. Input: array1 with images array2 with images type (input_data, input vs output, output_data) Output: visualize 1-1 the datasets

###anomaly_detector.py 
Output function in charge to label (Anomaly or Not Anomaly) the images from a directory. Input: autoencoder.h5 threshold.txt path to directory with images Output: Label images & text file visualize image with anomaly

![alt text](https://miro.medium.com/max/633/0*zZ8NIlCkDM-NKnmR)

###Technology
***Weights & Biases***

Weights and Biases is a developer tool that tracks the machine learning model and creates visualizations of the model and the training. It functions as a Python Library and can be imported as import wandb. It works within Tensorflow, Keras, Pytorch, Scikit, Hugging Face, and XGBoost. Use wandb.config to configure the inputs and hyperparameters; to track the metrics and create visualizations for the input, hyperparameters, model, and training; making it easier to see where changes can and need to be made to improve the model


***Flip Library (LinkedAI)***

Flip is a python library that allows you to generate synthetic images in a few steps from a small set of images made up of backgrounds and objects (images that would be in the background). It also allows you to save the results in jpg, json, csv, and pascal voc files.

###Blog Post
https://medium.com/@704/anomaly-detection-production-line-b8340e1eca43

### Authors

#### Heimer Rojas Castellanos
Electronic Engineer, Entrepreneur, Full Stack Software Engineer
Holberton School Bogota, Colombia
Specialization: Machine Learning

https://github.com/HeimerR

https://www.linkedin.com/in/heimerrojas/

#### Mia L Morton
Educator, Software Engineer
Holberton School Connecticut, United States of America
Specialization: Machine Learning

https://github.com/DracoMindz

https://www.linkedin.com/in/mialmorton/

#### Abdel Giovanny Perez
Electronic Engineer, MBA, Full Stack Developer
Holberton School Bogota, Colombia
Specialization: Machine Learning

https://github.com/ledbagholberton

https://www.linkedin.com/in/abdel-perez-url/

#### Ximena Carolina Andrade Vargas
Mechatronic Engineer, Software Engineer
Holberton School Bogota Colombia
Specialization: Machine Learning

https://github.com/xica369

https://www.linkedin.com/in/xicav369/
