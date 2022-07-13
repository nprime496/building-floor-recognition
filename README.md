# building-floor-recognition

## TODO

* Commencer learning rate plus haut

* Checker [la norme des poids](https://discuss.pytorch.org/t/how-to-check-for-vanishing-exploding-gradients/9019)


* Bayes dépend de la distribution (proportion des classes)

* Essayer plusieurs classifieurs 

* Preprocessing une seule fois, stocker

* Tester plusieurs modèles, noter dans un tableau les caractéristiques, taille embedding, couche cachée.

* Une section par modèle, tester différents classifieurs + random.

* créer une méthodologie de test rigoureuse (augmentation dev set & test set)


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
		* hypersensiblité au training loss
		* **comportement récurrent : loss qui stagne autour de 0.69-0.701**
		* **mêmes valeurs de prédiction**


en cours:
	
	data: RGB
	model:pretrained resnet/inception/etc

A tester:
	
	*  modèle moins large
	* checker les gradients (possible vanishing gradient d'après les recherches)
	* plus de données

questions:
	
	* entrainer un classifieur à partir des images des spectrogrammes ou sonogrammes, pourquoi ça marche ? 
	* comment determiner l'erreur optimale d'un classifieur (quand est-ce que c'est satisfaisant?)
	* données des autres niveaux disponibles?
	* quelles sont les priorités ?
	
possible besoin:
	
	* accès aux GPU du LIG, colab très restreint


no context:
- chunks
- no augmentation
- learning rate : 4e-3 (reduce on plateau ,patience 10, factor 0.5)

![](best_score.jpg)


Remember:
https://towardsdatascience.com/conv1d-and-conv2d-did-you-realize-that-conv1d-is-a-subclass-of-conv2d-8819675bec78

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
