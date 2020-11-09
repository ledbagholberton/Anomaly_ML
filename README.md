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

data_load.py
Rescale and load data splitting in Train & validate dataset.
Name format for files is
	noised_file_name = background_name + '__' + id_noised_image
Input: 
	path to background_pattern
	path to noised images
Output:
	train dataset arrays
	validation dataset arrays

denosing_autoencoder.py
Define autoencoder structure in Keras
Train the model
Return the model
Input:
	path to train / validation
	path to model (default)
	size of inputs (tuple)
	filters per layer (list)
Output:
	Histogram visualization (similar vs non similar)
	Metrics (F1, accuracy, precision,recall)
	threshold_1.txt
	autoencoder.h5

generate_validation_metrics.py
Generate metrics based on validation data. Help to tune the threshold.
Input:
	model
	path to real_not_anomalies
	path to real_anomalies
Output:
	Histogram visualization (similar vs non similar)
	Metrics (F1, accuracy, precision,recall)
	threshold_2.txt

image_visualization.py
Visualize images based on parameters. Used to debug.
Input:
	array1 with images
	array2 with images
	type (input_data, input vs output, output_data)
Output:
	visualize 1-1 the datasets

anomaly_detector.py
Output function in charge to label (Anomaly or Not Anomaly) the images from a directory. 
Input: 
	autoencoder.h5
	threshold.txt
	path to directory with images
Output: 
	Label images & text file
	visualize image with anomaly
	


	
