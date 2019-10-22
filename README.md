# GANs with spectral normalization and projection discriminator
Modified [Preferred Networks' implementation of SNGAN with projection](https://github.com/pfnet-research/sngan_projection) to work with the original dataset.

## The notable changes are:
* add ./configs/dataset-name.yml to set a configuration.

* add ./datasets/dataset-name.py to load and preprocess an image dataset.

* add ./datasets/image_list.txt that contains image path and label pair.

* modified evalution.py and evaluations/gen_images.py for custom evalutions (ie. save latent vectors z, generate an image from the given z, spherical interpolation, etc...)

# Examples
to be come
