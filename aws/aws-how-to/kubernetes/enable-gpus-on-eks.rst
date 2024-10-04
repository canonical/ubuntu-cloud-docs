Enable GPUs on EKS worker nodes
===============================

GPU-based EKS worker nodes are needed for many applications, such as for the training of deep learning models.

Before enabling GPUs on your worker nodes, you'll have to create a cluster and node groups with `GPU based instances`_. You'll also need SSH access to the nodes.



Install a GPU driver on each node
---------------------------------
For the GPU based instances to work, you'll need to install the appropriate `NVIDIA drivers`_ on them. For general purpose GPU usage, we recommend using a Tesla driver and the installation instructions from `Option 2 - Public NVIDIA drivers`_.

After installation, use ``sudo nvidia-smi`` to verify that the driver is successfully installed.


Install and set up the 'NVIDIA Container Toolkit' on each node
--------------------------------------------------------------
To support containerised GPU-accelerated applications, the default runtime should be set to 'NVIDIA Container Toolkit' on all the nodes.

For this, first configure the source repository:

.. code-block:: bash

  curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | \
  sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
  sudo apt-get update

Next, install the NVIDIA Container Toolkit:

.. code-block:: bash

   sudo apt-get install -y nvidia-container-toolkit

Restart ``containerd`` and check whether the runtime has been set correctly:

.. code-block:: bash

   sudo systemctl restart containerd
   sudo /etc/eks/bootstrap.sh ${YOUR_CLUSTER_NAME} --container-runtime nvidia-container-runtime

The output should be similar to:

.. code-block:: bash

   Using nvidia-container-runtime as the container runtime
   Aliasing EKS k8s snap commands
   Stopping k8s daemons until configured
   Stopped.
   Cluster "kubernetes" set.
   Container runtime is nvidia-container-runtime
   Configuring kubelet snap
   Starting k8s kubelet daemon
   Started.
   nvidia-smi found
   Persistence mode is already Enabled for GPU 00000000:00:1E.0.
   All done.
   All done.
   GPU 0: Tesla M60 (UUID: GPU-632acfab-13c7-fcf3-a9d5-1833d921cf80)
   Applications clocks set to "(MEM 2505, SM 1177)" for GPU 00000000:00:1E.0
   All done.


Apply 'NVIDIA Device Plugin' to the cluster
-------------------------------------------
The 'NVIDIA Device Plugin' for Kubernetes is a DaemonSet that allows you to automatically expose and manage the GPUs in each of your nodes, and to run GPU enabled containers in your cluster.

Create the ``DaemonSet`` using:

.. code-block:: bash

    kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.16.1/deployments/static/nvidia-device-plugin.yml

.. note::

  These are 'quick-start' instructions that enable the basic features of the plugin. For production settings use the `instructions for deployment via helm`_.


To apply the plugin to your cluster, run the following command from your local machine:

.. code-block:: bash

   kubectl apply -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.16.1/deployments/static/nvidia-device-plugin.yml

Verify that there are allocatable GPUs:

.. code-block:: bash

   kubectl get nodes "-o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu"

Test the GPU nodes by deploying a pod
-------------------------------------
Create a file named ``nvidia-smi.yaml`` to act as a Kubernetes manifest for a pod. Include the following contents in it:

..  code-block:: yaml

    apiVersion: v1
    kind: Pod
    metadata:
      name: nvidia-smi
    spec:
      restartPolicy: OnFailure
      containers:
      - name: nvidia-smi
        image: nvidia/cuda:tag
        args:
        - "nvidia-smi"
        resources:
          limits:
            nvidia.com/gpu: 1

Apply the manifest to create a pod:

.. code-block:: bash

   kubectl apply -f nvidia-smi.yaml

Once the pod is up and running, check its log using:

.. code-block:: bash

   kubectl logs nvidia-smi.yaml

.. _`GPU based instances`: https://docs.aws.amazon.com/dlami/latest/devguide/gpu.html
.. _`NVIDIA drivers`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html
.. _`Option 2 - Public NVIDIA drivers`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html#nvidia-installation-options
.. _`instructions for deployment via helm`: https://github.com/NVIDIA/k8s-device-plugin?tab=readme-ov-file#deployment-via-helm



