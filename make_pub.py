webpage = "https://anttwo.github.io/milo/"
img = "img/milo.gif"
paper_name = "MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient Surface Reconstruction"
authors = "Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov"
authors = authors.replace("Nissim Maruani", "<b>Nissim Maruani</b>")

conference = "SIGGRAPH Asia - Journal Track (TOG), 2025"

abstract = "Our method introduces a novel differentiable mesh extraction framework that operates during the optimization of 3D Gaussian Splatting representations. At every training iteration, we differentiably extract a mesh—including both vertex locations and connectivity—only from Gaussian parameters. This enables gradient flow from the mesh to Gaussians, allowing us to promote bidirectional consistency between volumetric (Gaussians) and surface (extracted mesh) representations. This approach guides Gaussians toward configurations better suited for surface reconstruction, resulting in higher quality meshes with significantly fewer vertices. Our framework can be plugged into any Gaussian splatting representation, increasing performance while generating an order of magnitude fewer mesh vertices. MILo makes the reconstructions more practical for downstream applications like physics simulations and animation."

text = f"""
<ul class="pub">
		<div class="container">
			<div class="zoomhover">
				<a href="{webpage}">
					<img class="pub-img" src="{img}" alt="Publication 1 Image">
				</a>
			</div>
			<div>
				<a class="pub-title" href="{webpage}"> {paper_name}
					Diffusion</a>
				<div class="pub-authors"> {authors} </div>

				<div class="pub-abstract">
					{abstract}
				</div>
				<div class="pub-conf">{conference}</div>
			</div>
		</div>
	</ul>"""

print(text)
