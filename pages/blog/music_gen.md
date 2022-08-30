---

slug: music_gen

title: Music Generation

subtitle: Using LSTM and language models

date: 21 Aug, 2022

---
#### Project Title

Composition of music by training a model on sheet music.

#### Project Members

- Surya Narayan AI&DS B
- Vishal Kalathil AI&DS B

#### Abstract

Our goal is to compose music (more like short piece of music) by training various deep learning models on a specific instrument's MIDI dataset.We will be looking into both RNN(principally LSTM networks) based and NLP based model as a music generation system,but our primary focus will be more on the latter.

#### Introduction

The art of ordering tones or sound in succession, in combination is music. It is a temporal relationship to produce a composition of notes having continuity and unity.Predicting the likely next few notes can be thought of as a time series problem due to the presence of long-term structural patterns in the music sequence.Also due to its sequential nature ,we can also consider this as an NLP problem.

Techniques like Recurrent Neural Networks (RNN's) can be used ,which incorporates dependencies across time. Long Short Term Memory is one such variant of RNN, that is capable of capturing long-term temporal dependencies in the given music dataset and it might be a great fit for generating music.

Transformer archietecture looks really promising not only for NLP problems but also for music generation since it is faster and have really good memory so extracting long-term structural patterns wouldn't be a problem.

**Preprocessing of musical instrument digital interface (MIDI) Files**

Using the <a href='https://magenta.tensorflow.org/datasets/'>instrument dataset</a> (i.e.,represented as an MIDI files) we have to extract the features required. Python libraries like music21,python-midi,etc,. can be used to perform the necessary operations.MIDI files plays an important role in extracting information about note sequence, note velocity and the time component.

For training a model with this data we might need to encode the MIDI file into a music notation format i.e we can use the _music21_ library to read the MIDI file, using that returns objects that specifies the notes and chords of the music file.

Now that we have extracted all the notes and chords we can create the sequences that will serve as the input of our model.(i.e Sequencing)

We will approach this problem by framing music generation as a language modeling problem. The idea is to encode midi files into a vocabulary of tokens(i.e Tokenization) and have the neural network predict the next token in a sequence from thousands of midi-files.

**Model Training**

- <u>RNN based approach</u>:

	Long Term Short Memory (LSTM),special type of RNN variant will be used.Since traditional RNN based models will not be able to retain information for long periods of time.
	
	Image from <a href='https://towardsdatascience.com/neural-networks-for-music-generation-97c983b50204?gi=57ecd2161d78'>article</a> 
		
	<a href="https://arxiv.org/pdf/1909.09586.pdf">Link</a>:Brief on LSTM architecture and function. 

-  <u>Language models based approach</u>

   >	GPT is an architecture based on Transformers decoders stacked together.The Transformer is a sequence model that leverage self-attention and that already had impressive results for generation tasks involving long-range dependencies. It is essentially the vanilla Transformer model with its encoder block and cross-attention mechanism stripped away — so that it can perform more efficiently on unsupervised tasks. This makes it well suited for music representation.
	
	Source from <a href='https://towardsdatascience.com/neural-networks-for-music-generation-97c983b50204?gi=57ecd2161d78'>article</a> 
		
	Image form <a href='https://towardsdatascience.com/creating-a-pop-music-generator-with-the-transformer-5867511b382a?gi=d1154441bcd7'>article</a>
	
	Apart from GPT language `model` we will also try to implement this approach on various other language models like BERT,GPT-2,etc,. 
``` CSS
code {
	font-family:'Fira Code';
	font-size: 12px;
	overflow-x: auto;
	overflow-y: hidden;
	padding: 1px;
	min-width: 0;
	background-color: var(--light-gray)!important;
	margin-bottom: 10px;
}
```

#### References
- **Dataset** :
  - <https://magenta.tensorflow.org/datasets/groove>
  - <https://magenta.tensorflow.org/datasets/maestro>
  - <https://magenta.tensorflow.org/datasets/nsynth>
  
- **Articles and Research Papers :**
	- <https://towardsdatascience.com/creating-a-pop-music-generator-with-the-transformer-5867511b382a?gi=d1154441bcd7>
	- RNN Architecture : <https://karpathy.github.io/2015/05/21/rnn-effectiveness/>
	- <https://arxiv.org/ftp/arxiv/papers/1908/1908.01080.pdf>
	- <https://medium.com/artists-and-machine-intelligence/neural-nets-for-generating-music-f46dffac21c0>
	- Detailed working on LSTM networks : <http://www.bioinf.jku.at/publications/older/2604.pdf>
	- Transformer Architecture : <https://jalammar.github.io/illustrated-transformer/>
	- Research articles by magenta : <https://magenta.tensorflow.org/research/>
