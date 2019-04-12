Reproducibility
====================


Reproducibility Packages
----------------------------

Reproducible computation requires more than being open source and providing open data sets.
While open access and liberal licensing are essential prerequisites, on top of this minimum we require structured organization of the materials and detailed documentation of the processes.

A "reproducibility package" [Barba-Praxis]_ includes descriptions about files uploaded to a data repository, including but not limited to code, parameters, input arguments, plotting scripts, and figures corresponding to a particular result. In software engineering, we often use the term "configuraiton management" to manage software artifacts; however, a reproducibility package is focused not only the software artifact but all artifacts in support of reproducibility to ensure that an experiment can be carried out fully by others trying to use the methods.

IEEE Computing in Science and Engineering, a publication focused on scientific and engineering computing, has a Reproducible Research Department [Barba-Thiruvathukal-RR]_, which is the first magazine department in the IEEE Computer Society to have a peer-reviewed track that requires authors to submit reproducibility packages and undergo peer review (which is also done openly). For an article to be accepted, all code and datasets must meet specific requirements and be deposited prior to peer review. The ideas of this chapter build on the work done to form this track.


Containers
-----------

Containers a provide support for a "virtual environment". Containers can be particularly helpful toward building reproducibility packages for machine learning and computer vision research, since the container scripts themselves are assets that can be maintained under version control  and included with the reproducibility package. There is no limit on how many scripts can be created.

Beyond software, in the case of machine learning and computer vision, it is crucial to support data artifacts. 
A key component of reproducibility is to integrate with scholarly archival. Acquiring and obtaining a DOI for the package assures that the materials are  discoverable and citable.
There is a growing trend toward software citation.

IEEE Computing in Science and Engineering's Reproducible Research track and the Journal of Open Source Software. %, which are both pioneering efforts in reproducible research, focused on computational science and research software, respectively.


Zenodo
--------

This book itself is an example of a Zenodo artifact.

.. figure:: zenodo/figures/zenodo-contents.png

   Zenodo landing page (release contents)


.. figure:: zenodo/figures/zenodo-git-tags.png

   Git tags show up as new Zenodo artifacts

.. figure:: zenodo/figures/zenodo-doi-and-citation.png

   Zenodo DOIs and Citation


Zenodo metadata for including author info:

.. literalinclude:: zenodo/code/.zenodo.json
   :language: javascript


.. [Barba-Praxis] Praxis of Reproducible Computational Science, https://doi.org/10.22541/au.153922477.77361922

.. [Barba-Thiruvathukal-RR] Reproducible Research for Computing in Science & Engineering, Computing in Science and Engineering, https://ieeexplore.ieee.org/document/8090467

