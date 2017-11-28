import os
import numpy
import skipthoughts
import decoder
import config
from console_logging.console import Console
console=Console()

def load():
    stv = skipthoughts.load_model(config.paths['skmodels'],
                                  config.paths['sktables'])
    console.log("Loaded skipthoughts model")
    bneg = numpy.load(config.paths['negbias'])
    console.log("Loaded negative bias")
    bpos = numpy.load(config.paths['posbias'])
    console.log("Loaded positive bias")
    dec = decoder.load_model(config.paths['decmodel'],
                            config.paths['dictionary'])
    console.log("Loaded decoder")
    return (stv, bpos, bneg, dec)

def generate(sentences, stv, bpos, bneg, dec):
    # Compute skip-thought vectors for sentences
    svecs = skipthoughts.encode(stv, sentences, verbose=False)
    console.log("Encoded skipthought vector")
    # Style shifting
    shift = svecs.mean(0) - bneg + bpos
    console.log("Shifted style")
    # TODO: clean up here
    # Generate story conditioned on shift
    passage = decoder.run_sampler(dec, shift, beam_width=50)
    console.log("Sampled passage")
    return passage

def main():
    stv, bpos, bneg, dec = load()
    sentences = []
    with open('./in.txt') as f:
        sentences = f.readlines()
        sentences = [sentence.strip().lstrip() for sentence in sentences]
    p = generate(sentences, stv, bpos, bneg, dec)
    print(p)

main()