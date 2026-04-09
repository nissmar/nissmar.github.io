webpage = "https://diego1401.github.io/BlobsToSpokesWebsite/"
img = "img/blobs_spokes.jpg"
paper_name = "From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians"
authors = "Diego Gomez<sup>*</sup>, Antoine Guédon<sup>*</sup>, Nissim Maruani, Bingchen Gong, Maks Ovsjanikov"

conference = "ArXiv, 2026"

abstract = "3D Gaussian Splatting (3DGS) has revolutionized fast novel view synthesis, yet its opacity-based formulation makes surface extraction fundamentally difficult. Unlike implicit methods built on Signed Distance Fields or occupancy, 3DGS lacks a global geometric field, forcing existing approaches to resort to heuristics such as TSDF fusion of blended depth maps. Inspired by the Objects as Volumes framework, we derive a principled occupancy field for Gaussian Splatting and show how it can be used to extract highly accurate watertight meshes of complex scenes. Our key contribution is to introduce a learnable oriented normal at each Gaussian element and to define an adapted attenuation formulation, which leads to closed-form expressions for both the normal and occupancy fields at arbitrary locations in space. We further introduce a novel consistency loss and a dedicated densification strategy to enforce Gaussians to wrap the entire surface by closing geometric holes, ensuring a complete shell of oriented primitives. We modify the differentiable rasterizer to output depth as an isosurface of our continuous model, and introduce Primal Adaptive Meshing for Region-of-Interest meshing at arbitrary resolution. We additionally expose fundamental biases in standard surface evaluation protocols and propose two more rigorous alternatives. Overall, our method Gaussian Wrapping sets a new state-of-the-art on DTU and Tanks and Temples, producing complete, watertight meshes at a fraction of the size of concurrent work-recovering thin structures such as the notoriously elusive bicycle spokes."

# DO NOT TOUCH
authors = authors.replace("Nissim Maruani", "<b>Nissim Maruani</b>")
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
