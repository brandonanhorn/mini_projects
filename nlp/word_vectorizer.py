import gensim
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

model = gensim.models.KeyedVectors.load_word2vec_format('lexvec.enwiki+newscrawl.300d.W.pos.vectors.gz')

model.doesnt_match(['man', 'woman', 'king', 'queen', 'dog'])

model.doesnt_match(['toronto', 'calgary', 'ontario', 'alberta', 'popsicle'])

model.most_similar('basketball')
model.most_similar('politician')


model.rank('love','hate')
