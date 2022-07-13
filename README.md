# building-floor-recognition

## TODO

* first classifier evaluation raw audio R+1, R+5
* reporter setup
* meeting M. Amini
* xai setup
* first classifier amelioration

## Meeting:

données:
	* recuperation des données à l'addresse https://aptikal.imag.fr/~amini/Data.zip
	* creation de nouveaux samples à partir des batiments ayant deux enregistrements
	
Tests effectués:	
	data : 
		* 1 channel raw : un ou deux essais, mais reconversion vers le spectrogramme parce que SOTA.
		* 1 channel spectrogramme 
			prétraitement:
				* normalisation
				* standartisation
				* min-max
			augmentation des données:
				* ralentissement
				* acceleration
				* chunks 
	model: 
		* CNN based

	difficultés:
		* **comportement récurrent : loss qui stagne autour de 0.69-0.701**
		* **mêmes valeurs de prédiction**

en cours:
	data: RGB
	model:pretrained

A tester:
	*  modèle moins large
	* checker les gradients (possible vanishing gradient d'après les recherches)
	* plus de données


possible besoin:
	* accès aux GPU du LIG, colab très restreint

https://towardsdatascience.com/conv1d-and-conv2d-did-you-realize-that-conv1d-is-a-subclass-of-conv2d-8819675bec78

Remember:

* Train with more data
* Data Augmentation
* adding noise to the input and ouput data
* feature selection
* cross-validation
* simplify data
* regularization
* emsembling
* early stopping
* adding dropout layers
