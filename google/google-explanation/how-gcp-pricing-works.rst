How GCP pricing works
=====================

Estimating GCP costs solely based on the `listed price`_ of your compute resources might not result in a good estimate. This is because the GCP service itself is available in a variety of modes, and there are other components apart from compute resources, that add to the cost. Since this cost estimation process is not very easy, GCP provides dedicated tools to assist you with the calculations.

Service modes
-------------

GCP is available in various service modes. While some of them are suitable for micro workloads launched on-demand, others are more suitable for long-term production workloads.

Free trial
~~~~~~~~~~

`Free trial`_ is an option that's available to all new GCP users. It allows a billing credit of $300 that is valid for 90 days and can be spent on most GCP resources. It might be a good option for organisations preparing for a cloud migration, as well as for students and individuals who want to learn GCP.

Free tier
~~~~~~~~~

Unlike free trial, `Free tier`_ is available to all GCP users. It provides free but limited access to many common GCP resources. The limits are mostly in terms of number of units per month, e.g. 'x' GB of storage per month, 1 non-preemptible e2-micro VM instance per month etc. Like the free trial, the free tier might be sufficient for learning purposes but is not suitable for production environments.

On-demand
~~~~~~~~~

`On-demand`_ mode is usually the default and the most popular mode across all the leading public cloud providers. In this mode, users can launch instances on-demand and get charged for the exact amount of resources consumed over time. This is based on the `pay-as-you-go (PAYG)`_ approach with no upfront payments or long-term commitments.

Spot VMs
~~~~~~~~

`Spot VMs`_ make use of unused GCP resources. They are launched when extra resources are available and can be hibernated, stopped or terminated whenever the cloud needs those resources back. They allow significant cost savings when compared to on-demand pricing, but are not suitable for workloads that need to meet service-level agreements (SLAs).

Committed use discounts
~~~~~~~~~~~~~~~~~~~~~~~

`Committed use discounts`_ are a compelling option to save costs when you are running workloads for a long term. By committing to specific usage, measured in $/hour, for at least a year, you receive a discounted rate on the usage your commitment covers. For any usage over the committed amount, you are charged at the on-demand rate. Committed use discounts are suitable for production environments with pre-defined resource requirements.

Sole-tenant nodes
~~~~~~~~~~~~~~~~~

`Sole-tenant nodes`_ also help you to optimise costs when running workloads for a long term. In this case you get physical machines allocated to you permanently, along with exclusive availability of all resources. Sole-tenant nodes might be the best option in situations where access to bare metal is required for compliance or licensing.


Pricing ingredients
-------------------

Except for sole-tenant nodes, all the other service modes presented above work based on PAYG billing. You pay for the exact amount of resources consumed over time. However, the final amount that you pay depends on multiple factors:

* **Compute resources** - the number of vCPUs and the amount of RAM in the Google Compute Engine (GCE) machine type
* **Storage resources** - the amount of storage and IOPS in the persistent disk type
* **Network traffic** - the amount of intra-region, inter-region and region-internet network traffic, measured in GB of data transfer per month
* **Other resources** - any other resources, such as external IP addresses or Cloud Load Balancing, that create extra charges

Some of these resources are available for free up to certain limits. On exceeding those limits, charges become applicable. 


Pricing tools
-------------

Estimating the cost of each factor manually can be a nightmare, especially when you're dealing with large, multi-service workloads. To help its customers with this process, GCP provides dedicated tools.

`Google cloud pricing calculator`_ provides estimates for total cost of ownership (TCO) of cloud instances based on their number, configuration and additional storage and network requirements. More detailed estimates are available for various regions, guest operating systems and pricing models. The calculator estimates total monthly and yearly costs.

`Pricing assistance`_ is another option that involves reaching out to GCP' sales team for a personalised quote based on detailed workload resource requirements. This might be the most convenient option for big enterprises as underestimating costs can have a negative impact on the entire cloud migration process.


Further reading
---------------

If you are wondering how GCP pricing compares to other leading cloud providers, you can check out `Canonical's Cloud Pricing Report 2022`_. It provides an overview of cloud list prices from leading public and private cloud providers as of July 2022. By considering three sample cost scenarios and using official TCO calculators, we estimate the costs of running the same workload across leading cloud platforms. The report includes results from our Cloud Pricing Survey 2022 and commentary from industry experts. The survey's outcomes show the growing importance of hybrid multi-cloud architecture and confirm its advantages from a TCO stance.

The research also confirms that compute resources account for only a portion of overall spending on public cloud infrastructure. Many organisations claim that the most significant portion of their budget is spent on storage resources (TB) and network resources. 

Some related topics that might interest you:

* `A business guide to cloud migration`_ 
* `What is a hybrid cloud?`_
* `What is multi-cloud?`_ 


.. _`listed price`: https://cloud.google.com/compute/all-pricing
.. _`Free trial`: https://cloud.google.com/free/docs/free-cloud-features#free-trial
.. _`Free tier`: https://cloud.google.com/free/docs/free-cloud-features#free-tier
.. _`On-demand`: https://cloud.google.com/compute/all-pricing
.. _`pay-as-you-go (PAYG)`: https://www.techtarget.com/searchstorage/definition/pay-as-you-go-cloud-computing-PAYG-cloud-computing
.. _`Spot VMs`: https://cloud.google.com/spot-vms/
.. _`Committed use discounts`: https://cloud.google.com/docs/cuds
.. _`Sole-tenant nodes`: https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes
.. _`Google cloud pricing calculator`: https://cloud.google.com/products/calculator
.. _`Pricing assistance`: https://cloud.google.com/contact/?direct=true
.. _`Canonical's Cloud Pricing Report 2022`: https://ubuntu.com/engage/cloud-pricing-report
.. _`A business guide to cloud migration`: https://ubuntu.com/engage/a-business-guide-to-cloud-migration
.. _`What is a hybrid cloud?`: https://ubuntu.com/cloud/hybrid-cloud
.. _`What is multi-cloud?`: https://ubuntu.com/cloud/multi-cloud


