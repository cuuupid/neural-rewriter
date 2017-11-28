"""
Configuration for the generate module
"""

#-----------------------------------------------------------------------------#
# Flags for running on CPU
#-----------------------------------------------------------------------------#
FLAG_CPU_MODE = False

#-----------------------------------------------------------------------------#
# Paths to models and biases
#-----------------------------------------------------------------------------#
paths = dict()

# Skip-thoughts
paths['skmodels'] = '../models/'
paths['sktables'] = '../models/'

# Decoder
paths['decmodel'] = '../romance.npz'
paths['dictionary'] = '../romance_dictionary.pkl'

# Image-sentence embedding
paths['vsemodel'] = '../coco_embedding.npz'

# VGG-19 convnet
paths['vgg'] = '../vgg19.pkl'

# COCO training captions
paths['captions'] = '../coco_train_caps.txt'

# Biases
paths['negbias'] = '../caption_style.npy'
paths['posbias'] = '../romance_style.npy'
