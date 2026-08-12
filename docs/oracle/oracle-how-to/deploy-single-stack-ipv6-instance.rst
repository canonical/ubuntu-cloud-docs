Deploy a single-stack IPv6 instance
=====================================

Ubuntu images on Oracle Cloud support IPv6-only (single-stack) networking from **Ubuntu 24.04 LTS (Noble) onwards**. Ubuntu 22.04 LTS (Jammy) and earlier releases do not support this configuration.

No special image variant is required, the standard Ubuntu 24.04 LTS (Noble) and later images work with IPv6-only subnets. IPv6 address assignment and routing are handled by the OCI network infrastructure (VCN, subnet, and route table); no manual network configuration inside the instance is needed.

.. note::
   OCI single-stack IPv6 support is currently rolling out progressively. During the initial rollout phase, the feature may be in Limited Availability (LA) in select regions (such as Ashburn) before reaching General Availability (GA) across all commercial regions (like Phoenix). If the IPv6-only subnet option is not yet visible in your region's OCI Console, you will need to wait for the GA release in your specific region.

Prerequisites
-------------

You'll need:

- A compartment to create the instance.

- A Virtual Cloud Network (VCN) with IPv6 addressing enabled. 
  
  .. warning::
     VCN IPv6 support can **only** be enabled at the time of VCN creation. You cannot retroactively enable IPv6 on an existing IPv4-only VCN. If you do not have an IPv6-enabled VCN, you must create a new one from scratch. Refer to Oracle's documentation on `Enabling IPv6 on a VCN`_.

- An IPv6-prefix-only subnet within that VCN, along with an IPv6-enabled route table (detailed in `Create an IPv6-only Subnet and Route Table`_).

- **Appropriate Security Rules:** Ensure your VCN's Security List or Network Security Group (NSG) allows ingress traffic on TCP port 22 (SSH) from your IPv6 source (e.g., ``::/0`` for anywhere). Default OCI rules often only allow IPv4 (``0.0.0.0/0``).

- A way to reach the instance over IPv6 after launch. Because single-stack IPv6 instances have no IPv4 address, you cannot SSH into them from an IPv4-only host. Options are:

  - A host or jump box that already has a public IPv6 address.
  - The OCI Bastion service (see :doc:`use-bastion-to-access-VM`).


Create an IPv6-only Subnet and Route Table
------------------------------------------

If you do not already have an IPv6-only subnet configured with outbound routing, follow these steps in the OCI Console:

1. Navigate to :guilabel:`Networking` > :guilabel:`Virtual Cloud Networks` and select your IPv6-enabled VCN.

2. **Create the Route Table:** On the menu list, select :guilabel:`Routing`, then click :guilabel:`Create Route Table`.

    .. image:: ipv6-single-stack/create-route-table.png
       :alt: Create Route Table

   - Name the route table (e.g., ``ipv6-only-rt``).
   - Click :guilabel:`+ Another Route Rule`.
   - Select IPv6 as protocol version.
   - For *Target Type*, choose your appropriate target based on your use case. **Internet Gateway** is used in this example for instances that should be publicly reachable over IPv6. For details regarding all supported target types, refer to Oracle's documentation on `Route rule targets`_.
   - For *Destination CIDR Block*, enter ``::/0`` to route all outbound IPv6 traffic.

    .. warning::
         Routing ``::/0`` to an Internet Gateway makes all instances in subnets associated with this route table globally routable via their public IPv6 addresses. Ensure your Security Lists or NSGs strictly limit inbound traffic to expected ports (like SSH).

   - Select the target from your available options (e.g., ``<your-internet-gateway>``).

    .. note::
      The selected target (Internet Gateway, NAT Gateway, Service Gateway, etc.) must already exist in your VCN before you can use it here. Refer to Oracle's documentation on `Route rule targets`_ for the full list of supported target types and their creation steps.

   - Once you fill out all the fields, it will look something like this:

    .. image:: ipv6-single-stack/route-table-example.png
       :alt: Example IPv6 Route Table

   - Click :guilabel:`Create`.

3. **Create the Subnet:**

   - On the menu list, select :guilabel:`Subnets`, then click :guilabel:`Create Subnet`.

    .. image:: ipv6-single-stack/create-subnet.png
       :alt: Create Subnet

   - Name your subnet (e.g., ``ipv6-only-subnet``)
   - In **CIDR blocks and prefixes**, choose the IP type as **Oracle-allocated IPv6 Prefix** and give an appropriate subnet prefix length.
   - Under *Route Table*, select the IPv6 route table you created in Step 2.
   - For Subnet access, DNS resolution and Security Lists, select the appropriate options for your use case to ensure the subnet is configured correctly. You can refer to Oracle's documentation on `Creating a subnet`_ for guidance.
   - Once all the fields are filled out correctly, it will look something like this:

    .. image:: ipv6-single-stack/subnet-data.png
       :alt: Example IPv6 Subnet

   - Click :guilabel:`Create Subnet`.


Create an IPv6-only instance
----------------------------

Create a new instance using :guilabel:`Compute` > :guilabel:`Instances` > :guilabel:`Create instance`.

1. Under *Image and shape*, select :guilabel:`Change image` > :guilabel:`Ubuntu`. Choose **Ubuntu 24.04 LTS** or a later release.

2. Under *Networking*, select the VCN that has IPv6 enabled, then select the IPv6-only subnet you created.

   .. note::
      The option to assign an IPv4 address will not appear since the IPv6-only subnet has no IPv4 CIDR.

3. Complete the remaining instance settings (SSH key, shape, boot volume, etc.). For more details, refer to Oracle's documentation on `Creating a Compute instance`_. Then click :guilabel:`Create`.

Once the instance is created, OCI assigns it an IPv6 address from the subnet prefix. 


Access the IPv6-only instance
-----------------------------

Because the instance has no IPv4 address, you must connect to it over IPv6. 

**From a host with IPv6 connectivity**, SSH directly using the assigned IPv6 address:

.. code::

   ssh -i <path-to-key> ubuntu@<ipv6-address>

where ``<ipv6-address>`` is the IPv6 address listed on the instance details page in the OCI console.

**Without an IPv6-capable host**, use the OCI Bastion service to reach the instance over its private IPv6 address. Refer to :doc:`use-bastion-to-access-VM` for step-by-step instructions.


Verify the IPv6 configuration
------------------------------

After logging in, confirm that the instance has a working IPv6 address and default route:

.. code::

   ip -6 addr show
   ip -6 route show

You should see the assigned IPv6 address on the primary network interface and a default route via the subnet gateway. You can also confirm outbound IPv6 connectivity by running:

.. code::

   ping -6 -c 4 ipv6.google.com

Ubuntu’s primary archive mirrors are IPv6-enabled, so standard ``apt update`` and ``apt upgrade`` commands will function normally over your IPv6 gateway.


Further references
------------------

For more information about IPv6 networking on Oracle Cloud, refer to the Oracle Cloud documentation:

* `IPv6 Addresses`_
* `Enabling IPv6 on a VCN`_
* `Creating a subnet`_
* `Creating a VCN Route Table`_
* `Route rule targets`_
* `Creating an Internet Gateway`_
* `Creating a NAT Gateway`_
* `Creating a Compute instance`_

.. _`IPv6 Addresses`: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm
.. _`Enabling IPv6 on a VCN`: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm
.. _`Creating a subnet`: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm
.. _`Creating a VCN Route Table`: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-routetable.htm
.. _`Route rule targets`: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN
.. _`Creating an Internet Gateway`: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm
.. _`Creating a NAT Gateway`: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm
.. _`Creating a Compute instance`: https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm