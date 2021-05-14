# Ingradient Descent

The Jupyter notebook containing the variations of our Recipe1M+ dataset can be found 
[here](https://github.com/sudonotdisturb/ingradient-descent/blob/model-training-files/model_recipe1m.ipynb).

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
- [Recipes5k]()


References:

Marc Bolaños, Aina Ferrà and Petia Radeva. “Food Ingredients Recognition through Multi-label Learning” In Proceedings of the 3rd International Workshop on Multimedia Assisted Dietary Management (ICIAP Workshops), 2017.

@article{marin2019learning,
  title = {Recipe1M+: A Dataset for Learning Cross-Modal Embeddings for Cooking Recipes and Food Images},
  author = {Marin, Javier and Biswas, Aritro and Ofli, Ferda and Hynes, Nicholas and 
  Salvador, Amaia and Aytar, Yusuf and Weber, Ingmar and Torralba, Antonio},
  journal = {{IEEE} Trans. Pattern Anal. Mach. Intell.},
  year = {2019}
}

@inproceedings{salvador2017learning,
  title={Learning Cross-modal Embeddings for Cooking Recipes and Food Images},
  author={Salvador, Amaia and Hynes, Nicholas and Aytar, Yusuf and Marin, Javier and 
          Ofli, Ferda and Weber, Ingmar and Torralba, Antonio},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2017}
}

@book{howard2020deep,
title={Deep Learning for Coders with Fastai and Pytorch: AI Applications Without a PhD},
author={Howard, J. and Gugger, S.},
isbn={9781492045526},
url={https://books.google.no/books?id=xd6LxgEACAAJ},
year={2020},
publisher={O'Reilly Media, Incorporated}
}
