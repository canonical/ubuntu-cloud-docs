Use Full Disk Encryption
========================

When an instance is launched on Oracle cloud, its disk (“Boot Volume”) is encrypted by default
using an Oracle managed key. Disk encryption is enabled by default and cannot be turned off.

Any other disks added to expand an instance’s storage are also encrypted by default.
You can use your own key to encrypt the disks if needed.

For more information about encryption on Oracle Cloud refer to the Oracle Cloud documentation:

* `Encrypting Data`_
* `OCI Vault overview`_
* `Block volume encryption`_

.. _`Encrypting Data`: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/encryption.htm
.. _`OCI Vault overview`: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm
.. _`Block volume encryption`: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption


Prerequisites
-------------

You will need

- a compartment to create the instance in.

- (Optional) a Virtual Cloud Network to create the instance in.
  Alternatively, you can create a new VCN while you create the instance.

- (Optional) a Vault with encryption keys to use for Boot Volume encryption.
  This is only necessary if you wish to use your own encryption key for FDE.
  Otherwise an Oracle managed key will be used.


Create an Ubuntu instance using FDE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
While creating a new instance from :guilabel:`Compute` > :guilabel:`Instances` >
:guilabel:`Create Instance`: , under :guilabel:`Image and Shape` > :guilabel:`Image`
> :guilabel:`Select Image` > :guilabel:`Ubuntu` select the desired Ubuntu release
and image build.

An Oracle managed key is used by default to encrypt the boot volume.
If you want to use your own key, select :guilabel:`Encrypt this volume with a key that you manage`
and follow the instructions described in `Using Your Own Keys for Server-Side Encryption`_
from the Oracle Cloud documentation.

.. _`Using Your Own Keys for Server-Side Encryption`: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/encryption.htm#Using_Your_Own_Keys_for_ServerSide_Encryption

If :guilabel:`Boot Volume` > :guilabel:`Advanced options` > :guilabel:`Use in-transit encryption`
is selected, the data moving between the instance and the block volume will also be encrypted.

The encryption key for a Boot Volume can also be changed after it has been created.
This can be done by following the steps described in `Editing a Key to a Block Volume`_
from the Oracle Cloud documentation.

.. _`Editing a Key to a Block Volume`: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Block_Volume.htm#assignkeyexistingblockvolume

