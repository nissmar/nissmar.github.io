webpage = ""
img = "img/supersdf_trailer.png"
paper_name = "Learning-based Sparse Signed Distance Field Super-Resolution"
authors = "Sagar Panwar<sup>*</sup>, Nissim Maruani<sup>*</sup>, Céline Loscos, Mathieu Desbrun, Pierre Alliez"
authors = authors.replace("Nissim Maruani", "<b>Nissim Maruani</b>")

conference = "ACM Trans. Graph. (SIGGRAPH), 2026"

abstract = "Signed Distance Fields (SDFs) are a powerful volumetric representation for 3D geometry. Recent advances in surface generation from SDFs increasingly rely on learnable surface representations and direct supervision on meshes. In this work, we challenge this trend and show that high-quality surface reconstruction can instead be achieved by learning to refine the volumetric signal itself. We present SuperSDF, a learning-based approach for sparse SDF super-resolution that operates directly in SDF space, without introducing any auxiliary surface representation or mesh-level supervision. Using a sparse voxel neural network restricted to a narrow band near the surface, our method predicts high-resolution signed-distance values from coarse inputs in a scalable and resolution-agnostic manner. Standard isosurface extraction algorithms can then process the resulting super-resolved SDFs, yielding accurate and detailed surface meshes. Our results demonstrate that learning-based SDF upsampling alone is sufficient to recover fine geometric details that are missed by classical interpolation and prior reconstruction methods. Compared to state-of-the-art ML approaches, our method produces higher-fidelity surfaces at a fraction of the computational cost and scales to volumetric resolutions previously out of reach."
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
