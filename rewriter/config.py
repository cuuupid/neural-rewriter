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
paths['decmodel'] = '../storyteller/romance.npz'
paths['dictionary'] = '../storyteller/romance_dictionary.pkl'

# Image-sentence embedding
paths['vsemodel'] = '../storyteller/coco_embedding.npz'

# VGG-19 convnet
paths['vgg'] = '../storyteller/vgg19.pkl'

# COCO training captions
paths['captions'] = '../storyteller/coco_train_caps.txt'

# Biases
paths['negbias'] = '../storyteller/caption_style.npy'
paths['posbias'] = '../storyteller/romance_style.npy'
