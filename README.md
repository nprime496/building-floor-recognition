# building-floor-recognition


# TODO & NOTES

----
## Recap:


Le code est disponible dans le dossier `code/*.ipynb`

Ci-dessous, un résumé sommaire de ce qui a été fait et les résultats obtenus.

### Recuperation des  données:
	
* recuperation des données à l'addresse [APTIKAL](https://aptikal.imag.fr/~amini/Data.zip)
* Les données disponibles sont :
    * des échantillons sonores
    * des enregistements de 3min pour les étages 1 et 5
    * des échantillons sonores de 25s selectionnés par un expert pour les étage 1,3 et 5.
    
<center>

| etages     | R+1 | R+3 | R+5 | 
|--------------|-----|-----|----|
| nb. samples  | 11  | 12  | 15|

</center>

### Traitement des  données:
* Nous avons créé de nouveaux samples à partir des batiments ayant deux enregistrements
* découpage des samples de 25s en 5 samples de 5s chacun, on obtient ainsi 186 enregistrements, on obtient:

<center>

| etages     | R+1 | R+3 | R+5 | 
|--------------|-----|-----|----|
| nb. samples  | 68  | 61  | 57|

</center>

* Le découpage des samples de 30ss en 2 samples de 10s chacun a été envisagé mais le gain en données est trop faible pour que ce soit utilisé.

* Les données prétraîtées disponibles [ici](https://huggingface.co/datasets/nprime496/building_floor_classification/tree/main)
-----

## Tests effectués:

### Setup 
La configuration utilisée pour obtenir les Spectrogrammes est la suivante :
* n_fft : 1024
* win_length : 1024

Celle utilisée pour les MFCC est la suivante:
* n_fft:512
* n_mfcc: 100
* n_mels: 512
* sample_rate:8820



### Données Expert (échantillons de 25s) :

Pour rappel, les resultats obtenus avec les chunks de 5s sur les 03 étages avec la modalité spectrogramme:

|                 | accuracy | f1-score avg | f1 weighted |
|-----------------|----------|--------------|-------------|
| simplesimplenet | 0.44     | 0.39         | 0.37        |
| simplenet       | 0.64     | 0.63         | 0.64        |
| notsimplenet    | 0.67     | 0.67         | 0.68        |
| resnet (fine-tuning)         |    0.70    |      -       |     -        |
| bigone          | 0.54     | 0.48         | 0.48        |

Les resultats obtenus sont les suivants avec les chunks de 5s sur les 03 étages avec la modalité MFCC:

|                 | accuracy | f1-score avg | f1 weighted |
|-----------------|----------|--------------|-------------|
| simplesimplenet | 0.33     | 0.24         | 0.26        |
| simplenet       | 0.36     | 0.31         | 0.33        |
| notsimplenet    | 046      | 0.42         | 0.46        |
| resnet (fine-tuning)       |   0.63       |     -         |     -        |
| bigone          | 0.49     | 0.37         | 0.42        |

Les résultats obtenus en faisant un late fusion avec les modalités précédentes sont :

**A COMPLETER (pas encore fait car il faut faire une selection des meilleurs modèles pour chaque modalité)**

En utlisant le dataset des chunks de 5s et 10s, nous avons également testé la classification en utilisant les méthodes suivantes : RandomForest, SVM, KNN (avec correlation comme métrique), MLP, Random sans résultat de performance notable. 

Les résultats et le code sont disponibles [ici](https://github.com/nprime496/building-floor-recognition/blob/main/code/audio_classification_alternatives.ipynb)



**résumé**:

**Bien qu'on constate une performance qui semble se démarquer d'une classification aléatoire, le manque de données rend ces résulats très incertains. En effet, la performance des modèles peut varier entre les differents essais. Les résultats obtenus avec finetuning sur Resnet (avec la modalité Spectrogramme) n'ont pas été mentionné car trop variants, aucune sorte de correlation entre les essais ne semblait émerger.**

### Augmentation des données


Face à cette difficulté posée par le manque de donnnées, nous avons décidé de faire une augmentation. En effet, les enregistrements originaux étant disponibles, il serait interessant de les utliser. C'est ainsi que nous avons produit un nouveau dataset contenant des chunks de 10s provenant des enregistrements originaux. Cependant, les enregistrements de l'étage 3 ne sont pas disponibles. Nous avons donc fait des tests dans un cas de **classification binaire** sur les différentes modalités.

Nous avons ajouté un nouveaau modèle pré-entrainé dans notre ensemble de modèles à tester : [Resnet34](https://huggingface.co/docs/transformers/model_doc/resnet).

Les resultats obtenus avec la modalité spectrogramme avec les chunks de 5s originaux sont:

|                 | accuracy | f1-score avg | f1 weighted |
|-----------------|----------|--------------|-------------|
| simplesimplenet | 0.71     | 0.70         | 0.70        |
| simplenet       | 0.79     | 0.79         | 0.79        |
| notsimplenet    | 0.79     | 0.79         | 0.79        |
| resnet          | 0.73         |              |             |
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

**On constate une baisse nette de performance avec l'utilisation des données augmentées. Ce qui est assez surprenant. Il semble qu'ajouter des données semble ajouter plus de confusion dans le modèle. Après étude approfondie, il s'avère que de nombreux samples contiennent des patterns trop caractéristiques qui nuisent sévèrement à la capacité de généralisation du modèle.** 

### Spectrogramme

|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|bigone|spec|2\.06|53\.78|1\.39|51\.28|
|notsimplenet|spec|0\.89|59\.09|2\.53|25\.64|
|simplenet|spec|0\.74|71\.97|1\.18|38\.46|
|simplesimplenet|spec|1\.26|42\.42|1\.33|41\.02|

|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|bigone|spec|1\.40|55\.30|1\.07|43\.59|
|notsimplenet|spec|0\.96|57\.57|0\.91|38\.46|
|simplenet|spec|0\.88|58\.33|0\.90|38\.46|
|simplesimplenet|spec|0\.65|77\.27|1\.53|48\.71|



|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|bigone|mfcc|0\.87|61\.36|0\.95|64\.10|
|notsimplenetmfcc|mfcc|1\.03|46\.97|1\.13|33\.33|
|simplenetmfcc|mfcc|0\.72|72\.72|1\.08|46\.15|
|simplesimplenetmfcc|mfcc|0\.94|55\.30|1\.19|33\.33|

### MFCC

|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|bigone|mfcc|0\.87|59\.09|0\.66|71\.79|mfcc|0\.84|58\.33|1\.02|53\.84|
|notsimplenetmfcc|mfcc|0\.84|58\.33|1\.03|53\.84|
|simplenetmfcc|mfcc|0\.733|71\.97|0\.99|51\.28|
|simplesimplenetmfcc|mfcc|1\.00|46\.21|1\.19|35\.89|

|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|bigone|mfcc|0\.86|64\.39|1\.06|64\.10|
|notsimplenetmfcc|mfcc|0\.73|68\.18|0\.89|58\.97|
|simplenetmfcc|mfcc|1\.18|37\.12|1\.32|25\.64|
|simplesimplenetmfcc|mfcc|1\.26|37\.12|1\.68|38\.46|


|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|bigone|mfcc|0\.88|65\.91|0\.83|64\.10|
|notsimplenetmfcc|mfcc|0\.91|58\.33|1\.28|35\.89|
|simplenetmfcc|mfcc|0\.65|75\.75|1\.05|43\.59|
|simplesimplenetmfcc|mfcc|1\.15|43\.18|1\.36|20\.51|

## Late fusion
En utilisant les meilleurs classifieurs pour les différentes modalités.
**[CETTE SECTION EST À COMPLETER]**

## Early fusion

Un auto-encodeur a été utilisé pour apprendre des vecteurs de representation des échantillons audio. Plusieurs classifieurs ont ensuite été utilisés sur ces representations. Les données utilisées pour entrainer l'autoencodeur sont tous les chunks de 5s disponibles.

Les données utilisées pour entrainer les classifieurs proviennent des chunks de 5s disponibles pour les 03 étages.

### Resultats obtenus avec la modalité spec

|index|Model|Accuracy|AUC|Recall|Prec\.|F1|
|---|---|---|---|---|---|---|
|et|Extra Trees Classifier|0\.7317|0\.8734|0\.7429|0\.7969|0\.7191|
|rf|Random Forest Classifier|0\.7073|0\.8038|0\.7151|0\.7354|0\.6961|
|lightgbm|Light Gradient Boosting Machine|0\.6341|0\.8107|0\.6429|0\.6433|0\.6093|
|nb|Naive Bayes|0\.6098|0\.6743|0\.6151|0\.5945|0\.5854|
|gbc|Gradient Boosting Classifier|0\.5854|0\.8023|0\.5857|0\.5702|0\.5714|
|dt|Decision Tree Classifier|0\.5366|0\.6464|0\.5381|0\.565|0\.5333|
|ada|Ada Boost Classifier|0\.5122|0\.6968|0\.5111|0\.5221|0\.5141|
|lda|Linear Discriminant Analysis|0\.5122|0\.6069|0\.5048|0\.519|0\.5057|
|knn|K Neighbors Classifier|0\.439|0\.642|0\.4238|0\.4366|0\.4184|
|ridge|Ridge Classifier|0\.4146|0\.0|0\.4119|0\.4242|0\.4086|
|svm|SVM - Linear Kernel|0\.3902|0\.0|0\.3905|0\.3838|0\.3825|
|lr|Logistic Regression|0\.3659|0\.5614|0\.3635|0\.369|0\.3661|
|dummy|Dummy Classifier|0\.2927|0\.0|0\.3333|0\.0857|0\.1325|
|qda|Quadratic Discriminant Analysis|0\.2439|0\.447|0\.2667|0\.1539|0\.1728|

