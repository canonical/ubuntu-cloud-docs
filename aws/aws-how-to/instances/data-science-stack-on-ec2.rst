Deploy Canonical Data Science Stack on EC2 using a GPU-enabled instance type
============================================================================


Canonical Data Science Stack (DSS) is a command line interface-based tool that bundles Jupyter Notebooks, MLflow and frameworks like PyTorch and TensorFlow on top of an orchestration layer, making this product excellent for rapid testing, prototyping and doing ML at a small scale. 

While this is a product intended for desktop machine learning users, you can also deploy it on EC2 following these instructions.

We are using a G4DN instance type to leverage the GPU, required for machine learning training and inference.

Learn more about Canonical Data Science Stack in our `press release post`_ and our `official documentation`_.

Launch a GPU-EC2 instance (G4DN instance family)
------------------------------------------------


Navigate to the EC2 Web console, select :guilabel:`Launch instance` and make sure you select either Ubuntu 22.04 or 24.04 LTS (free or Pro), and any G4DN instance type family.

For this example, we are using 22.04 on ``g4dn.xlarge``, which has 4 vCPUs and 16 GB of RAM. It is powered with an NVIDIA T4 GPU.

Make a note of the machine IP and the Key-Pair used. You’ll need it for connecting to the machine.

Log in and install GPU drivers
------------------------------

Connect to your machine. If you are using Linux (including WSL on Windows) or MacOS, open a terminal window and connect to your machine using:

.. code::

    ssh -i <<YOUR_KEYPAIR>> ubuntu@<<YOUR_MACHINE_IP>>


If you are connecting from Windows, you can use PuTTy.

Once you have connected, run a full upgrade:

.. code::

    sudo apt update && sudo apt upgrade -y


If you get a new kernel, it is advised to restart the machine before proceeding.

Now install the GPU drivers:

.. code::

    sudo apt install -y ubuntu-drivers-common
    sudo ubuntu-drivers install
    sudo reboot


After reboot, check if the drivers and CUDA have been installed properly and the GPU is detected correctly:

.. code::

    nvidia-smi


The output should be similar to:

.. code-block:: none

        +---------------------------------------------------------------------------------------+
        | NVIDIA-SMI 535.104.05             Driver Version: 535.104.05   CUDA Version: 12.2     |
        |-----------------------------------------+----------------------+----------------------+
        | GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
        | Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
        |                                         |                      |               MIG M. |
        |=========================================+======================+======================|
        |   0  Tesla T4                       On  | 00000000:00:1E.0 Off |                    0 |
        | N/A   26C    P8               9W /  70W |      2MiB / 15360MiB |      0%      Default |
        |                                         |                      |                  N/A |
        +-----------------------------------------+----------------------+----------------------+

        +---------------------------------------------------------------------------------------+
        | Processes:                                                                            |
        |  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
        |        ID   ID                                                             Usage      |
        |=======================================================================================|
        |  No running processes found                                                           |
        +---------------------------------------------------------------------------------------+

Note that the GPU is properly detected and CUDA has also been installed.

Install MicroK8s and DSS
------------------------

Install MicroK8s:


.. code::

    sudo snap install microk8s --channel 1.28/stable --classic
    sudo microk8s enable storage dns rbac
    sudo microk8s enable gpu

Install DSS:

.. code::

    sudo snap install data-science-stack --channel latest/stable
    dss initialize --kubeconfig="$(sudo microk8s config)"

Create your first Jupyter Notebook:

.. code::

    dss create my-tensorflow-notebook --image=kubeflownotebookswg/jupyter-tensorflow-cuda:v1.8.0


DSS will deploy Jupyter Notebooks with TensorFlow and with CUDA enabled. It’ll use a ``clusterIP`` from the MicroK8s cluster, which will only be accessible from inside the machine for the moment.

To allow outside access, change the deployment to use a ``Nodeport`` instead of a ``clusterIP`` and reconnect using an SSH tunnel:


.. code::

    sudo microk8s kubectl patch svc my-tensorflow-notebook --type='json' -p '[{"op":"replace","path":"/spec/type","value":"NodePort"}]' --namespace dss


Wait some seconds and it will get updated.


Create an SSH tunnel for accessing the deployment
--------------------------------------------------

Open a new connection to create the tunnel to the deployment port. You can close the previous connection as it won’t be used anymore.


.. code::

    ssh -i <<YOUR_KEYPAIR>> ubuntu@<<YOUR_MACHINE_IP>> -L 30633:localhost:30633


Open your browser with the address ``localhost:30633`` and start using your freshly deployed Jupyter Notebook with CUDA enabled.

.. note::
    If you want to create more Jupyter Notebook deployments, you'll have to create additional tunnels on new ports.



.. _`press release post`: https://canonical.com/blog/data-science-stack-release
.. _`official documentation`: https://documentation.ubuntu.com/data-science-stack/

