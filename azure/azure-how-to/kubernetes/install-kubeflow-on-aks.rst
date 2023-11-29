Install Kubeflow on AKS
=======================

`Kubeflow`_ is a novel open-source end-to-end Machine Learning tool that runs on Kubernetes. It is composed of 30+ microservices, and can be challenging to deploy and operate. However, the process is greatly simplified using Juju and this guides describes:

* How to deploy Kubeflow on AKS
* How to observe the state of your deployment using Juju and
* How to access your Kubeflow dashboard from your local machine


Basic requirements
------------------

* Access to an AKS Kubernetes cluster via ``kubectl``
* A minimum of 4 CPUs, 16GB RAM and 50GB Disk space should be available in your cluster


Install the Juju client
-----------------------

Juju provides a simple installation of Kubeflow across Kubernetes platforms, with a good level of customisation, as well as easy maintenance. For further details check out `Charmed Kubeflow`_. To use the Juju CLI, install the Juju client. On Linux, install it via snap using:

.. code::

   sudo snap install juju --classic

Alternatively, `download the Windows installer`_ or use ``brew install juju`` on macOS


Connect Juju to your AKS cluster
--------------------------------

To operate workloads in your Kubernetes cluster with Juju, you have to add your cluster to the list of clouds in Juju via the add-k8s command. If your Kubernetes config file is in the standard location (``~/.kube/config`` on Linux), and you only have one cluster, you can simply run:

.. code::

   juju add-k8s myk8s

If your ``kubectl`` config file contains multiple clusters, you can specify the appropriate one by name:

.. code::

   juju add-k8s myk8s --cluster-name=foo

Finally, if your config file is in a different location, you can set the KUBECONFIG environment variable to point to the relevant file. For example:

.. code::

   KUBECONFIG=path/to/file juju add-k8s myk8s


Create a controller
-------------------

To operate workloads on your Kubernetes cluster, Juju uses controllers. You can create a controller with the bootstrap command:

.. code::

   juju bootstrap myk8s my-controller

This command creates a couple of pods under the my-controller namespace. You can see your controllers with the ``juju controllers`` command.


Create a model
--------------

A model in Juju is a blank canvas where your operators are deployed, and it holds a 1:1 relationship with a Kubernetes namespace. You can create a model and give it a name, e.g. ``kubeflow``, with the add-model command. In the process you are also creating a Kubernetes namespace of the same name:

.. code::

   juju add-model kubeflow

You can list your models with the ``juju models`` command.


Deploy Kubeflow
---------------

.. note::

   To deploy Kubeflow you need at least 50GB of disk space, 14GB of RAM and 2 CPUs on your cluster. If you have fewer resources, deploy ``kubeflow-lite`` or ``kubeflow-edge``.

Once you have a model, you can simply ``juju deploy`` any of the provided `Kubeflow bundles`_ into your cluster. For the full Kubeflow bundle, run:

.. code::

   juju deploy kubeflow --trust

You can observe your Kubeflow deployment process with the command:

.. code::

   watch -c juju status --color

To customise your deployment, use the `docs on customisation`_.


Final deployment steps
----------------------

There are currently a couple of additional steps required to effectively deploy Kubeflow.

Add an RBAC role for Istio
~~~~~~~~~~~~~~~~~~~~~~~~~~

To setup Kubeflow with Istio correctly, you need to provide the ``istio-ingressgateway`` operator access to Kubernetes resources. This is done by creating an appropriate Role Based Access Control (RBAC) role:

.. code::

   kubectl patch role -n kubeflow istio-ingressgateway-operator -p '{"apiVersion":"rbac.authorization.k8s.io/v1","kind":"Role","metadata":{"name":"istio-ingressgateway-operator"},"rules":[{"apiGroups":["*"],"resources":["*"],"verbs":["*"]}]}'

Find the external IP address of your Kubeflow dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get the IP address of your Kubeflow dashboard run:

.. code::

   kubectl get svc/istio-ingressgateway -n kubeflow

where ``kubeflow`` is the name that you specified for your Juju model, and is in turn the namespace of your Kubeflow deployment. Save the returned IP address as ``EXTERNAL-IP`` for use in the next step.

Provide the external IP to authentication services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable access to your dashboard, provide its public IP to ``dex-auth`` and ``oidc-gatekeeper``:

.. code::

   juju config dex-auth public-url=http://<EXTERNAL-IP>:80
   juju config oidc-gatekeeper public-url=http://<EXTERNAL-IP>:80


Access the Kubeflow dashboard
-----------------------------

To view your authentication credentials,run:

.. code::

   juju config dex-auth static-username
   juju config dex-auth static-password

By default, these are both empty. If you wish to set them, add the relevant string to the end of the command, e.g.

.. code::

   juju config dex-auth static-username=admin
   juju config dex-auth static-password=AxWiJjk2hu4fFga7

Assuming you have configured your virtual network’s firewall to allow you to connect, you should be able to access your Kubeflow dashboard URL. The AKS cluster’s ingress will take you to the login page of your Charmed Kubeflow MLOps platform.


.. _`Kubeflow`: https://ubuntu.com/ai/what-is-kubeflow
.. _`download the Windows installer`: https://launchpad.net/juju/2.8/2.8.5/+download/juju-setup-2.8.5-signed.exe
.. _`Charmed Kubeflow`: https://charmed-kubeflow.io/docs
.. _`Kubeflow bundles`: https://charmed-kubeflow.io/docs/operators-and-bundles
.. _`docs on customisation`: https://charmed-kubeflow.io/docs/customise
