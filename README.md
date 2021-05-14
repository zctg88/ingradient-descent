# Ingradient Descent

The models:

- [Recipe1M+ model](https://github.com/sudonotdisturb/ingradient-descent/blob/model-training-files/model_recipe1m.ipynb)
- [Recipes5k model](https://github.com/sudonotdisturb/ingradient-descent/blob/model-training-files/model_recipes5k.ipynb)

Our technical report on the project and trained models can be found 
[here](https://github.com/sudonotdisturb/ingradient-descent/blob/model-training-files/report.ipynb).

The notebook `model_recipe1m.ipynb` is set up to download the sample of the data we used automatically. 
In order to speed up the data wrangling process, we have provided the files necessary to get started 
together with the notebook. Ensure you upload the following files to the current directory, or wherever path is pointing to:

- training_images.txt :: list of training set image filenames in the sample
- valid_images.txt :: list of validation set image filenames in the sample
- layer1_sample.json :: json data containing recipe id, instructions, ingredients, and train-val-test partition
- layer2_sample.json :: json data containing recipe id, associated images, and urls for the images
- ingredients_simplified_Recipes5k.txt:: list of common ingredients, curated by the creators of the Recipes5k dataset
- blacklist.txt :: list of words to filter out of ingredients text



Datasets we used:

- [Recipe1M+](http://pic2recipe.csail.mit.edu/)
- [Recipes5k](http://www.ub.edu/cvub/recipes5k/)


References:

Howard, J., and S., Gugger. *Deep Learning for Coders with Fastai and Pytorch: AI Applications Without a PhD*. O'Reilly Media, Incorporated, 2020.

Marc Bolaños, Aina Ferrà and Petia Radeva. “Food Ingredients Recognition through Multi-label Learning” In Proceedings of the 3rd International Workshop on Multimedia Assisted Dietary Management (ICIAP Workshops), 2017.

Marin, Javier, Aritro, Biswas, Ferda, Ofli, Nicholas, Hynes, Amaia, Salvador, Yusuf, Aytar, Ingmar, Weber, and Antonio, Torralba. "Recipe1M+: A Dataset for Learning Cross-Modal Embeddings for Cooking Recipes and Food Images". IEEE Trans. Pattern Anal. Mach. Intell. (2019).

Salvador, Amaia, Nicholas, Hynes, Yusuf, Aytar, Javier, Marin, Ferda, Ofli, Ingmar, Weber, and Antonio, Torralba. "Learning Cross-modal Embeddings for Cooking Recipes and Food Images.". In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2017.



