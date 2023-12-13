EC2 Credentials
===============

There are multiple different kinds of credential, Amazon uses slightly non-standard nomenclature, and it's not always clear which credential is required for a given application. 

Type of credentials
-------------------

* Signon credentials

These are the email address/password pair that you use when you sign up in `Amazon Web Services`_. You use these to sign on to the `AWS EC2 console`_, and can be considered the "account owner/root" credentials as they allow you to regenerate all other types of credentials. 

* Access Credentials

There are three types: access keys, X.509 certificates and key pairs. The first and second type allow you to connect to the Amazon APIs. Which type of credential depends on which API and tool you are using. Some APIs and tools support both options, whereas others support just one. The third type is SSH public/private key pairs that are used for initial logins to newly created instances.

  * access keys: Symmetric key encryption. These are for making requests to AWS product REST or Query APIs. Can be obtained/regenerated from the Access Keys tab on the AWS Security Credentials page.
  * X.509 certificates: Public key encryption. Use X.509 certificates to make secure SOAP protocol requests to AWS service APIs. These are the credentials you will use when using the command-line ec2 API tools. Can be obtained/regenerated from the X.509 Certificates tab on the AWS Security Credentials page.
  * key pairs: SSH key pairs. When you create an instance, Amazon inserts the public key of your SSH key pair into your new instance so that you can log in using your private key. You can add new SSH key pairs through the AWS management console by clicking on Key Pairs under Networking and Security in the Navigation pane and then the Create Key Pair button. After specifying a name you will be prompted to download and save your private key. EC2 stores the public portion of your key pair, and inserts it into :guilabel:`/home/ubuntu/.ssh/authorized_keys` when you instantiate your instance. If you lose this private key, it cannot be downloaded again; you will need to regenerate a new key pair.

Read `AWS security credentials`_ for more information about different credentials.

Create key pairs
----------------

You need to create key pairs for SSH connection to EC2 instances. Follow instructions at `Create key pairs`_ to create key pairs with using console, AWS CLI or CloudFormation.

Configure access keys
---------------------

To interact with AWS services, configure and set up access keys to access resources. See `Configuration and credential file settings`_ to create config file.

.. _`Amazon Web Services`: https://aws.amazon.com
.. _`AWS EC2 Console`: https://console.aws.amazon.com/ec2/home
.. _`AWS security credentials`: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html
.. _`Create key pairs`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html
.. _`Configuration and credential file settings`: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html