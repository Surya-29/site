from feedgen.feed import FeedGenerator


def feed_gen(pages):
    fg = FeedGenerator()

    fg.id('http://127.0.0.1:5000/')
    fg.title('Itnaava')
    fg.author({'name': 'Surya', 'email': 'abc@gmail.com'})
    fg.link(href='http://127.0.0.1:5000/', rel='alternate')

    for i in range(len(list(pages))-1):
        fe = fg.add_entry()
        fe.id(list(pages)[i].meta['slug'])
        fe.title(list(pages)[i].meta['title'])
        fe.link(href='http://127.0.0.1:8000/blog/'+list(pages)[i].meta['slug'])
        fe.summary(list(pages)[i].html,type='html')

    fg.atom_str(pretty=True)
    fg.atom_file('feed.xml', )
    with open('feed.xml','r',encoding="utf8",) as f:
        feed_cont = f.read()
        return feed_cont
