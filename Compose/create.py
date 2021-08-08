import string,random
from vertex import Graph,vertex

def words_and_text(text_p):
    with open(text_p, 'r') as f:
        text = f.read()

        text = ' '.join(text.split())
        text = text.lower()
        text  =text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = words[:1000]
    return words



def compose(g,words,length=50):
    c =[]
    w = g.get_vertex(random.choice(words))

    for _ in range(length):
        c.append(w.value)
        w = g.get_next(w)
    
    return c


def create_graph(words):
    gr = Graph()

    previous = None

    for w in words:
        w_ver = gr.get_vertex(w)

        if previous:
            previous.increment(w_ver)
        
        previous = w_ver

    gr.prob_map()

    return gr


def main():

    words  =words_and_text('Chain-Composer/graph-composer/texts/hp_sorcerer_stone.txt')

    g = create_graph(words)

    c = compose(g,words,100)

    return(' '.join(c))


if __name__ == '__main__' :
    print(main())