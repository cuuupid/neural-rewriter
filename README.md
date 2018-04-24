# Neural Rewriter

Based off of [neural-storyteller](https://github.com/ryankiros/neural-storyteller), for text style shifting.

![1](https://i.imgur.com/hreoKKF.png)

```
$ git clone git://github.com/pshah123/neural-rewriter.git
```

## neural-rewriter

```sh
$ mkdir models && cd models
$ curl -O http://www.cs.toronto.edu/~rkiros/models/dictionary.txt
$ curl -O http://www.cs.toronto.edu/~rkiros/models/utable.npy
$ curl -O http://www.cs.toronto.edu/~rkiros/models/btable.npy
$ curl -O http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz
$ curl -O http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz.pkl
$ curl -O http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz
$ curl -O http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz.pkl
$ cd ..
$ mkdir storyteller && cd storyteller
$ wget -ci https://s3.amazonaws.com/lasagne/recipes/pretrained/imagenet/vgg19.pkl
$ wget http://www.cs.toronto.edu/\~rkiros/neural_storyteller.zip
$ unzip neural_storyteller.zip && rm neural_storyteller.zip
```

Add input text to rewriter/in.txt and

```sh
$ pip install -r requirements.txt --user
# emerge dev-python/nltk
$ python
  >>> import nltk
  >>> nltk.download('punkt')
$ cd rewriter
$ python generate.py

```

If you get error like sequence bla bla...
```sh
$  grep '[^[:blank:]]' < in.txt > file.out && rm in.txt && mv file.out in.txt
```


## Credits

[ryankiros](https://github.com/ryankiros) for the original repo.

[RomaniukVadim](https://github.com/RomaniukVadim) for great documentation!
