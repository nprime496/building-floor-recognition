

Auto encoder full dataset chunked 5 spec (normalized)

|index|Model|Accuracy|AUC|Recall|Prec\.|F1|Kappa|MCC|TT \(Sec\)|
|---|---|---|---|---|---|---|---|---|---|
|et|Extra Trees Classifier|0\.7271|0\.8708|0\.7083|0\.7769|0\.7139|0\.5833|0\.6046|0\.502|
|rf|Random Forest Classifier|0\.7133|0\.8596|0\.6967|0\.7299|0\.7003|0\.5553|0\.5727|0\.606|
|lightgbm|Light Gradient Boosting Machine|0\.6795|0\.8254|0\.6678|0\.6796|0\.6642|0\.5079|0\.5188|3\.523|
|gbc|Gradient Boosting Classifier|0\.6714|0\.8474|0\.6694|0\.6768|0\.6604|0\.4982|0\.5074|21\.518|
|dt|Decision Tree Classifier|0\.6171|0\.7071|0\.6111|0\.648|0\.6155|0\.4194|0\.4274|0\.198|
|knn|K Neighbors Classifier|0\.5857|0\.7759|0\.5733|0\.5858|0\.5627|0\.3708|0\.3903|0\.175|
|ada|Ada Boost Classifier|0\.5833|0\.7083|0\.5694|0\.6037|0\.5696|0\.3587|0\.3692|1\.605|
|lr|Logistic Regression|0\.5095|0\.6187|0\.4844|0\.4402|0\.4422|0\.2517|0\.2953|1\.124|
|nb|Naive Bayes|0\.5024|0\.6359|0\.5006|0\.5589|0\.4652|0\.2579|0\.2924|0\.079|
|ridge|Ridge Classifier|0\.4948|0\.0|0\.4817|0\.4886|0\.431|0\.2407|0\.2763|0\.061|
|lda|Linear Discriminant Analysis|0\.4205|0\.5234|0\.4228|0\.4152|0\.4017|0\.1327|0\.1378|0\.188|
|dummy|Dummy Classifier|0\.3943|0\.5|0\.3333|0\.1559|0\.2233|0\.0|0\.0|0\.023|
|svm|SVM - Linear Kernel|0\.3871|0\.0|0\.3733|0\.2746|0\.2458|0\.0597|0\.106|0\.163|
|qda|Quadratic Discriminant Analysis|0\.3371|0\.5199|0\.3222|0\.3443|0\.3334|-0\.0043|-0\.0065|0\.113|



All dataset
|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|simplesimplenet|spec\_norm|0\.9793321378938444|49\.79310344827586|1\.3709178924560548|34\.177215189873415|
|simplenet|spec\_norm|0\.8772042243035285|58\.06896551724138|1\.0048291206359863|50\.63291139240506|
|notsimplenet|spec\_norm|1\.0631226759690504|37\.93103448275862|1\.132801628112793|25\.31645569620253|


|index|modality|train\_loss|train\_accuracy|test\_loss|test\_accuracy|
|---|---|---|---|---|---|
|simplesimplenetmfcc|mfcc|1\.018844520652687|50\.3448275862069|1\.0505678176879882|40\.50632911392405|
|simplenetmfcc|mfcc|0\.9110180362240299|57\.51724137931035|1\.0555892944335938|51\.89873417721519|
|notsimplenetmfcc|mfcc|0\.6061156555846497|70\.62068965517241|1\.4583629608154296|60\.75949367088608|

0.333  using resnet


|index|Model|Accuracy|AUC|Recall|Prec\.|F1|Kappa|MCC|TT \(Sec\)|
|---|---|---|---|---|---|---|---|---|---|
|lda|Linear Discriminant Analysis|0\.7167|0\.8631|0\.7278|0\.6986|0\.6823|0\.5727|0\.6037|0\.012|
|ridge|Ridge Classifier|0\.7|0\.0|0\.7167|0\.7383|0\.6691|0\.5525|0\.6181|0\.01|
|rf|Random Forest Classifier|0\.7|0\.8908|0\.6944|0\.7297|0\.6729|0\.5566|0\.6167|0\.448|
|qda|Quadratic Discriminant Analysis|0\.7|0\.9153|0\.6944|0\.7097|0\.6851|0\.5471|0\.5698|0\.012|
|et|Extra Trees Classifier|0\.7|0\.8471|0\.7|0\.7228|0\.6656|0\.5558|0\.6194|0\.397|
|nb|Naive Bayes|0\.6833|0\.8922|0\.7|0\.7617|0\.6844|0\.5412|0\.5821|0\.013|
|ada|Ada Boost Classifier|0\.6833|0\.7854|0\.6889|0\.7611|0\.6717|0\.5248|0\.5678|0\.074|
|dt|Decision Tree Classifier|0\.6667|0\.7542|0\.6556|0\.6986|0\.6375|0\.5077|0\.5674|0\.011|
|gbc|Gradient Boosting Classifier|0\.6667|0\.8353|0\.6778|0\.6897|0\.6287|0\.5101|0\.5836|0\.166|
|lightgbm|Light Gradient Boosting Machine|0\.6667|0\.7915|0\.6556|0\.7017|0\.6404|0\.4842|0\.5422|0\.097|
|lr|Logistic Regression|0\.6167|0\.8108|0\.6333|0\.6153|0\.5695|0\.4238|0\.4716|0\.272|
|knn|K Neighbors Classifier|0\.6167|0\.7926|0\.5833|0\.5819|0\.5612|0\.4155|0\.4464|0\.113|
|svm|SVM - Linear Kernel|0\.5333|0\.0|0\.5333|0\.5342|0\.4952|0\.2806|0\.2936|0\.059|
|dummy|Dummy Classifier|0\.4|0\.5|0\.3333|0\.1667|0\.2333|0\.0|0\.0|0\.01|
