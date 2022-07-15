# building-floor-recognition


## TODO

* Essayer de sampler en prenant en compte le batiment d'origine du son

* sample rate may be important for spectrogram calculation, check it! ✅

* stop mini batching .... 

* add dropout ✅

* automate hyperparameter search (optuna,etc)


* Commencer learning rate plus haut ✅ 
	
	* no improvement, l'entrainement est plus difficile 

* Checker [la norme des poids](https://discuss.pytorch.org/t/how-to-check-for-vanishing-exploding-gradients/9019) ✅


* Erreur de Bayes dépend de la distribution (proportion des classes)

* Essayer plusieurs classifieurs 

* Preprocessing une seule fois, stocker

* Tester plusieurs modèles, noter dans un tableau les caractéristiques, taille embedding, couche cachée.

* Une section par modèle, tester différents classifieurs + random.

* créer une méthodologie de test rigoureuse (augmentation dev set & test set)

----
## Recap:


Le code est disponible dans le fichier `code/audio_classification.ipynb`

Ci-dessous, un résumé sommaire de ce qui a été fait et les résultats obtenus.

### Traitement des  données:
	
* recuperation des données à l'addresse [APTIKAL](https://aptikal.imag.fr/~amini/Data.zip)

* creation de nouveaux samples à partir des batiments ayant deux enregistrements
* découpage des samples de 25s en 5 samples de 5s chacun, on obtient ainsi 130 enregistrements.

| etages     | R+1 | R+5 | 
|--------------|-----|-----|
| nb. samples  | 70  | 60  | 



* nouvelles données disponibles à l'adresse : https://huggingface.co/datasets/nprime496/building_floor_classification/tree/main


### Tests effectués:

data : 
	
* modalité raw (données sous forme de .wav):
	*  quelques essais non fructueux en début de projet, mais reconversion vers le spectrogramme parce que la méthode semblait être plus commune et mieux documentée .
	
* spectrogramme 25 s (données originales)
	* prétraitement:
		* n_fft : 1024
		* win_length : 1024
		* normalisation
		* standartisation
		* min-max 
	* augmentation des données:
		* changement de vitesse (acceleration/ralentissement) 
		* ajout de bruits
	* modeles testés: 
		* random CNN based architecture
	* **résumé**:
	**La plupart des tests évoqués ci-dessus ont été faits avec les échantillons de 25 secondes et n'ont pas produits de résultats vraiment satisfaisants. Une cause probable étant le  nombre d'enregistrements restreint du jeu de données et un problème non résolu de vanishing gradient. Aussi, la faible taille du jeu de données ne permet pas de donner une mesure fiable de la performance des modèles entrainés.**

	* difficultés:
		* hypersensiblité au learning rate
		* comportement récurrent : loss qui stagne autour de 0.69-0.701 et **mêmes valeurs de prédiction** (vanishing gradient)

* spectrogramme 5 s (entrainement avec des spectrogrammes d'enregistrements de 5s)
	* prétraitement:
		* n_fft : 1024
		* win_length : 1024
		* aucun
	* augmentation des données:
		* aucune
	* modeles testés: 
		* random CNN based architectures
		* ajout batchnorm pour réduire l'effet du vanishing gradient
		* ajout dropout pour regularisation
	* **résumé**:
	**Bien que les modèles n'aient fondamentalement pas changé (mis à part l'ajout de batchnorm et dropout), on observe une nette amélioration des performances. En effet le meilleur score obtenu jusqu'à présent est 73.07% d'accuracy.**

	* difficultés:
		* malgré l'augmentation de la performance, le modèle semble toujours avoir un grand bias, il serait interessant de tester d'autres architectures pour voir s'il diminue.
		* Meilleure selection du jeu de test ?


### En cours:

* mise en place du pipeline et test pour les données raw (données sous forme de .wav)
* mise en place du pipeline et test pour les données MFCC 

### questions:

* Vu que j'ai découpé les enregistrements de 25s en enregistrements de 5s, faut-il découper le train et le test set de façon à ne pas avoir des enregistrements venant du même bâtiment dans les deux ensembles ? 

* Pour le traitement des enregistrements audio bruts, l'idée est d'utiliser la séquence des amplitudes (.wav) ou l'image de la sequence ? Je pose la question parce que dans le premier cas, il serait peut-être plus interessant d'utiliser un RNN plutôt qu'un CNN d'après mes recherches.


### Observations:
	
* Augmenter le learning rate, même avec un ReduceOnPlateau pertube fortement l'entraînement, le modèle se retrouve presque toujours sur un optimum local

## Results

The best results obtained so far are summarized in the table below :

| modality     | model       | accuracy | f1 | recall | precision |
|--------------|-------------|----------|----|--------|-----------|
| spectrogram  | SimpleNetv1* | 73.07    |    |        |           |
| raw audio    |             |          |    |        |           |
| MFCC         |             |          |    |        |           |
| Late Fusion  |             |          |    |        |           |
| Early Fusion |             |          |    |        |           |


(*) le code simplenetv1 est disponible dans `report/SimpleNetv1.py`




-----
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


✅ ❌