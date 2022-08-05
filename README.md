# building-floor-recognition


# TODO & NOTES

----
## Recap:


Le code est disponible dans le dossier `code/*.ipynb`

Ci-dessous, un résumé sommaire de ce qui a été fait et les résultats obtenus.

### Traitement des  données:
	
* recuperation des données à l'addresse [APTIKAL](https://aptikal.imag.fr/~amini/Data.zip)

* creation de nouveaux samples à partir des batiments ayant deux enregistrements
* découpage des samples de 25s en 5 samples de 5s chacun, on obtient ainsi 186 enregistrements.

| etages     | R+1 | R+3 | R+5 | 
|--------------|-----|-----|----|
| nb. samples  | 68  | 61  | 57|

* découpage des samples de 25s en 2 samples de 10s chacun, on obtient ainsi 18 enregistrements.

| etages     | R+1 | R+3 | R+5 | 
|--------------|-----|-----|----|
| nb. samples  | -  | -  | -|


* Les données prétraîtées disponibles [ici](https://huggingface.co/datasets/nprime496/building_floor_classification/tree/main)


## Tests effectués:

### Données Expert :
La configuration utilisée pour obtenir les Spectrogrammes est la suivante :
* n_fft : 1024
* win_length : 1024

Celle utilisée pour les MFCC est la suivante:
* n_fft:1024
* n_mfcc: 1024
* n_mels: 1024
* sample_rate:8820

Pour rappel, les resultats obtenus avec les chunks de 5s sur les 03 étages avec la modalité spectrogramme:

|                 | accuracy | f1-score avg | f1 weighted |
|-----------------|----------|--------------|-------------|
| simplesimplenet | 0.44     | 0.39         | 0.37        |
| simplenet       | 0.64     | 0.63         | 0.64        |
| notsimplenet    | 0.67     | 0.67         | 0.68        |
| resnet          |    -    |      -       |     -        |
| bigone          | 0.54     | 0.48         | 0.48        |

Les resultats obtenus sont les suivants avec les chunks de 5s sur les 03 étages avec la modalité MFCC:

|                 | accuracy | f1-score avg | f1 weighted |
|-----------------|----------|--------------|-------------|
| simplesimplenet | 0.33     | 0.24         | 0.26        |
| simplenet       | 0.36     | 0.31         | 0.33        |
| notsimplenet    | 046      | 0.42         | 0.46        |
| resnet          |   -       |     -         |     -        |
| bigone          | 0.49     | 0.37         | 0.42        |

Les résultats obtenus en faisant un late fusion avec les modalités précédentes sont :

**A COMPLETER (pas encore fait car il faut faire une selection des meilleurs modèles pour chaque modalité)**

En utlisant le dataset des chunks de 5s et 10s, nous avons également testé la classification en utilisant les méthodes suivantes : RandomForest, SVM, KNN (avec correlation comme métrique), MLP, Random sans résultat de performance notable. 

Les résultats et le code sont disponibles [ici](https://github.com/nprime496/building-floor-recognition/blob/main/code/audio_classification_alternatives.ipynb)



**résumé**:

**Bien qu'on constate une performance qui semble se démarquer d'une classification aléatoire, le manque de données rend ces résulats très incertains. En effet, la performance des modèles peut varier entre les differents essais. Les résultats obtenus avec finetuning sur Resnet (avec la modalité Spectrogramme) n'ont pas été mentionné car trop variants, aucune sorte de correlation entre les essais ne semblait émerger.**

### Augmentation des données

Face à cette difficulté, nous nous sommes tournés vers une approche d'augmentation des données. En effet, les enregistrements originaux étant disponibles, il serait interessant de les utliser. C'est ainsi que nous avons produit un nouveau dataset contenant des chunks de 10s provenant des enregistrements originaux. Cependant, les enregistrements de l'étage 3 ne sont pas disponibles. Nous avons donc fait des tests dans un cas de classification binaire sur les différentes modalités.

Nous avons ajouté un nouveaau modèle pré-entrainé dans notre ensemble de modèles à tester : [Resnet34](https://huggingface.co/docs/transformers/model_doc/resnet).

Les resultats obtenus avec la modalité spectrogramme avec les chunks de 5s originaux sont:

|                 | accuracy | f1-score avg | f1 weighted |
|-----------------|----------|--------------|-------------|
| simplesimplenet | 0.71     | 0.70         | 0.70        |
| simplenet       | 0.79     | 0.79         | 0.79        |
| notsimplenet    | 0.79     | 0.79         | 0.79        |
| resnet          |          |              |             |
| bigone          | 0.79     | 0.79         | 0.79        |

Les resultats obtenus avec la modalité spectrogramme avec les chunks de 5s augmentés sont:

|                 | accuracy | f1-score avg | f1 weighted |
|-----------------|----------|--------------|-------------|
| simplesimplenet | 0.44     | 0.35         | 0.39        |
| simplenet       | 0.53     | 0.38         | 0.43        |
| notsimplenet    | 0.35     | 0.31         | 0.34        |
| resnet          |    0.38      |        0.44      |     0.44        |
| bigone          | 0.50     | 0.35         | 0.41        |

Les resultats obtenus avec la modalité spectrogramme avec les chunks de 10s augmentés sont:



|                 | accuracy | f1-score avg | f1 weighted |
|-----------------|----------|--------------|-------------|
| simplesimplenet | 0.65     | 0.64         | 0.64        |
| simplenet       | 0.50     | 0.44         | 0.40        |
| notsimplenet    | 0.61     | 0.56         | 0.58        |
| resnet          |   0.66       |  0.66            |   0.66          |
| bigone          | 0.52     | 0.48         | 0.46        |

Le code relatif à l'entrainement en utilisant resnet est disponible [ici](https://github.com/nprime496/building-floor-recognition/blob/main/code/audio_classification_fine_tuning.ipynb)

**On constate une baisse nette de performance avec l'utilisation des données augmentées. Ce qui est assez surprenant. Il semble qu'ajouter des données semble ajouter plus de confusion dans le modèle.** 



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
