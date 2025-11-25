webpage = "https://arxiv.org/abs/2511.17454"
img = "img/illustrators_depth_square.pdf"
paper_name = "Illustrator’s Depth: Monocular Layer Index Prediction for Image Decomposition"
authors = "Nissim Maruani, Peiying Zhang, Siddhartha Chaudhuri, Matthew Fisher, Nanxuan Zhao, Vladimir G. Kim, Pierre Alliez, Mathieu Desbrun, Wang Yifan"
authors = authors.replace("Nissim Maruani", "<b>Nissim Maruani</b>")

conference = "Arxiv, 2025"

abstract = "We introduce Illustrator’s Depth, a novel definition of depth that addresses a key challenge in digital content creation: decomposing flat images into editable, ordered layers. Inspired by an artist’s compositional process, illustrator’s depth infers a layer index for each pixel, forming an interpretable image decomposition through a discrete, globally consistent ordering of elements optimized for editability. We also propose and train a neural network using a curated dataset of layered vector graphics to predict layering directly from raster inputs. Our layer index inference unlocks a range of powerful downstream applications. In particular, it significantly outperforms state-of-the-art baselines for image vectorization while also enabling high-fidelity text-to-vector-graphics generation, automatic 3D relief generation from 2D images, and intuitive depth-aware editing. By reframing depth from a physical quantity to a creative abstraction, illustrator's depth prediction offers a new foundation for editable image decomposition."

# DO NOT TOUCH
text = f"""
        <ul class="pub">
                <div class="container">
                        <div class="zoomhover">
                                <a href="{webpage}">
                                        <img class="pub-img" src="{img}" alt="Publication 1 Image">
                                </a>
                        </div>
                        <div>
                                <a class="pub-title" href="{webpage}"> {paper_name}</a>
                                <div class="pub-authors"> {authors} </div>

                                <div class="pub-abstract">
                                        {abstract}
                                </div>
                                <div class="pub-conf">{conference}</div>
                        </div>
                </div>
        </ul>
        <ul class="pub-line"></ul>
        """

with open('index.html', 'r') as f:
    html_text = f.read()
    f.close()

with open('index_backup.html', 'w') as f:
    f.write(html_text)
    f.close()
html_text = html_text.replace(
    "<h2>Publications</h2>", "<h2>Publications</h2> \n"+text)
print(html_text)
with open('index.html', 'w') as f:
    f.write(html_text)
    f.close()
# print(text)
