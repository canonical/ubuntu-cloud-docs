EKS kubelet snap
================

EKS worker nodes run kubelet from the `kubelet-eks snap`_. The snap 
channel is set based on the Kubernetes version corresponding to the EKS worker node image. For
Kubernetes version `X.Y` the channel is set to `X.Y.P/stable` where `P` is the latest kubelet `X.Y`
patch version supported by the image. For example, a supported version of kubelet is 1.32.0
for Kubernetes 1.32. Therefore, the channel of the ``kubelet-eks`` snap
in the image corresponding to the Kubernetes version is set to `1.32.0/stable`.

Note that the `latest` channel track of the snap is unused.

See the `official snap documentation <https://snapcraft.io/docs/channels>`_ for more information
about the concept of channels and tracks.

Automatic snap updates
~~~~~~~~~~~~~~~~~~~~~~

In EKS worker node images, automatic background updates of ``kubelet-eks``, ``aws-cli``, and
**all** other installed snaps are disabled. To enable automatic background updates of **all**
installed snaps run the following command in the worker node:

.. code::

    sudo snap refresh --unhold

To enable automatic background updates of only the ``kubelet-eks`` snap, run the following command in
the worker node:

.. code::

    sudo snap refresh --unhold kubelet-eks

Updates of ``kubelet-eks`` snap shouldn't affect running workloads, but Kubernetes API access for the
node is expected to be unavailable for up to 30 seconds.

.. _`kubelet-eks snap`: https://snapcraft.io/kubelet-eks
