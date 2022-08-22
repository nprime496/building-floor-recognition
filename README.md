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
* n_fft:512
* n_mfcc: 100
* n_mels: 512
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

Face à cette difficulté, nous nous sommes tournés vers une approche d'augmentation des données. En effet, les enregistrements originaux étant disponibles, il serait interessant de les utliser. C'est ainsi que nous avons produit un nouveau dataset contenant des chunks de 10s provenant des enregistrements originaux. Cependant, les enregistrements de l'étage 3 ne sont pas disponibles. Nous avons donc fait des tests dans un cas de **classification binaire** sur les différentes modalités.

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

**On constate une baisse nette de performance avec l'utilisation des données augmentées. Ce qui est assez surprenant. Il semble qu'ajouter des données semble ajouter plus de confusion dans le modèle. Après étude approfondie, il s'avère que de nombreux samples contiennent des patterns trop caractéristiques qui nuisent sévèrement à la capacité de généralisation du modèle.** 

### Spectrogramme

|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|bigone|spec|2\.067902508903952|53\.78787878787878|1\.3941661834716796|51\.28205128205128|
|simplenet|spec|0\.7475207272697898|71\.96969696969697|1\.1897236824035644|38\.46153846153847|
|notsimplenet|spec|0\.8936526354621438|59\.09090909090909|2\.5394668579101562|25\.64102564102564|
|simplesimplenet|spec|1\.2620386235854204|42\.42424242424242|1\.3371530532836915|41\.02564102564102|

|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|bigone|spec|1\.4041337405934053|55\.3030303030303|1\.0686330795288086|43\.58974358974359|
|simplenet|spec|0\.8865025464226218|58\.333333333333336|0\.9042177200317383|38\.46153846153847|
|notsimplenet|spec|0\.9641312991871553|57\.57575757575758|0\.914417839050293|38\.46153846153847|
|simplesimplenet|spec|0\.6542682086720186|77\.27272727272727|1\.5335296630859374|48\.717948717948715|



|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|bigone|mfcc|0\.8718697604011086|61\.36363636363637|0\.9470756530761719|64\.1025641025641|
|notsimplenetmfcc|mfcc|1\.0375050937428194|46\.96969696969697|1\.132332992553711|33\.33333333333333|
|simplenetmfcc|mfcc|0\.726630266974954|72\.72727272727273|1\.0803455352783202|46\.15384615384615|
|simplesimplenetmfcc|mfcc|0\.9430997511919808|55\.3030303030303|1\.19197998046875|33\.33333333333333|

### MFCC

|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|simplenetmfcc|mfcc|0\.7375007517197553|71\.96969696969697|0\.9980084419250488|51\.28205128205128|
|simplesimplenetmfcc|mfcc|1\.0094036775476791|46\.21212121212121|1\.1970024108886719|35\.8974358974359|
|bigone|mfcc|0\.869238068075741|59\.09090909090909|0\.6679233551025391|71\.7948717948718|
|notsimplenetmfcc|mfcc|0\.8487607170553768|58\.333333333333336|1\.029397201538086|53\.84615384615385|

|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|bigone|mfcc|0\.8621444702148438|64\.39393939393939|1\.0662317276000977|64\.1025641025641|
|notsimplenetmfcc|mfcc|0\.7360283346737132|68\.18181818181817|0\.8918451309204102|58\.97435897435898|
|simplenetmfcc|mfcc|1\.1899316451128792|37\.121212121212125|1\.3227727890014649|25\.64102564102564|
|simplesimplenetmfcc|mfcc|1\.261759926291073|37\.121212121212125|1\.6856094360351563|38\.46153846153847|


|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|simplenetmfcc|mfcc|0\.6527907988604378|75\.75757575757575|1\.0517154693603517|43\.58974358974359|
|notsimplenetmfcc|mfcc|0\.9132613013772404|58\.333333333333336|1\.2837324142456055|35\.8974358974359|
|bigone|mfcc|0\.8887166976928711|65\.9090909090909|0\.8309106826782227|64\.1025641025641|
|simplesimplenetmfcc|mfcc|1\.155884911032284|43\.18181818181818|1\.3596012115478515|20\.51282051282051|

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

