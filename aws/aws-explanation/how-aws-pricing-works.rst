How AWS pricing works
=====================

Estimating AWS costs solely based on the listed price of your compute resources might not result in a good estimate. This is because the AWS service itself is available in a variety of modes, and there are other components apart from compute resources, that add to the cost. Since this cost estimation process is not very easy, AWS provides dedicated tools to assist you with the calculations.

Service modes
-------------

AWS is available in various service modes. While some of them are suitable for micro workloads launched on-demand, others are more suitable for long-term production workloads.

Free tier
~~~~~~~~~

`Free Tier`_ allows for free usage of AWS resources up to a specific limit. This might be a good option for organisations preparing for a cloud migration as well as students and individuals willing to learn AWS.

On-demand
~~~~~~~~~

`On-demand`_ mode is usually the default and the most popular mode across all leading public cloud providers. Users can launch instances on-demand and get charged for the exact amount of resources consumed over time. This approach is based on the `pay-as-you-go (PAYG)`_ approach with no upfront payments and long-term commitments.

Spot instances
~~~~~~~~~~~~~~

`Spot instances`_  make use of unused AWS resources. They are launched when extra resources are available and are hibernated, stopped or terminated whenever the cloud needs those resources back. They allow significant cost savings when compared to On-Demand pricing but are not suitable for workloads that need to meet service-level agreements (SLAs).


Saving plans
~~~~~~~~~~~~

`Saving plans`_ are a compelling option to save costs when you are running workloads in the long term. By committing to specific usage, measured in $/hour, for at least one year, organisations can benefit from competitive pricing compared to the On-demand mode. Saving plans are suitable for production environments with pre-defined resource requirements.


Dedicated hosts
~~~~~~~~~~~~~~~

`Dedicated hosts`_  also help organisations optimise costs when running workloads on AWS in the long term. As its name indicates, with Dedicated hosts, organisations get physical machines allocated to them permanently; all resources are available exclusively for them. Dedicated hosts might be the best option in situations where access to bare metal is required.


Pricing ingredients
-------------------

Except for dedicated hosts, all the other service modes presented above work based on PAYG billing. You pay for the exact amount of resources consumed over time. However, the final amount that you pay depends on multiple factors:

* **Compute resources** - the number of vCPUs and the amount of RAM as defined in the Elastic Compute Cloud (EC2) instance type,
* **Storage resources** - the amount of storage, IOPS, throughput and snapshots as defined in the Elastic Block Storage (EBS) volume type,
* **Network traffic** - the amount of intra-region, inter-region and region-internet network traffic, measured in GB of data transfer per month
* **Other resources** - any other resources, such as Elastic IP addresses or Elastic Load Balancers, that create extra charges.

Some of these resources are available for free up to certain limits. On exceeding those limits, charges become applicable. 


Pricing calculator
------------------

Estimating the cost of each factor manually can be a nightmare, especially when you're dealing with large, multi-service workloads. To help its customers with this process, AWS provides dedicated tools.

`AWS' pricing calculator`_ provides estimates for total cost of ownership (TCO) of cloud instances based on their number, configuration and additional storage and network requirements. More detailed estimates are available for various regions, guest operating systems and pricing models. The calculator estimates total monthly and yearly costs.

`Pricing assistance`_ is another option that involves reaching out to AWS' sales team for a personalised quote based on detailed workload resource requirements. This might be the most convenient option for big enterprises as underestimating costs can have a negative impact on the entire cloud migration process.


Further reading
---------------

If you are wondering how AWS pricing compares to other leading cloud providers, you can check out `Canonical's Cloud Pricing Report 2022`_. It provides an overview of cloud list prices from leading public and private cloud providers as of July 2022. By considering three sample cost scenarios and using official TCO calculators, we estimate the costs of running the same workload across leading cloud platforms. The report includes results from our Cloud Pricing Survey 2022 and commentary from industry experts. The survey's outcomes show the growing importance of hybrid multi-cloud architecture and confirm its advantages from a TCO stance.

The research also confirms that compute resources account for only a portion of overall spending on public cloud infrastructure. Many organisations claim that the most significant portion of their budget is spent on storage resources (TB) and network resources. 

Some related topics that might interest you:

* `A business guide to cloud migration`_ 
* `What is a hybrid cloud?`_
* `What is multi-cloud?`_ 

.. _`Free tier`: https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all
.. _`On-demand`: https://aws.amazon.com/ec2/pricing/on-demand/
.. _`pay-as-you-go (PAYG)`: https://www.techtarget.com/searchstorage/definition/pay-as-you-go-cloud-computing-PAYG-cloud-computing
.. _`Spot instances`: https://aws.amazon.com/ec2/spot/
.. _`Saving plans`: https://aws.amazon.com/savingsplans/
.. _`Dedicated hosts`: https://aws.amazon.com/ec2/dedicated-hosts/
.. _`AWS' pricing calculator`: https://calculator.aws/#/
.. _`Pricing assistance`: https://aws.amazon.com/contact-us/sales-support-pricing/
.. _`Canonical's Cloud Pricing Report 2022`: https://ubuntu.com/engage/cloud-pricing-report
.. _`A business guide to cloud migration`: https://ubuntu.com/engage/a-business-guide-to-cloud-migration
.. _`What is a hybrid cloud?`: https://ubuntu.com/cloud/hybrid-cloud
.. _`What is multi-cloud?`: https://ubuntu.com/cloud/multi-cloud


