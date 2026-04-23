`arm64` on Google Cloud
==========================

## `arm64` platforms
Google Cloud currently provides two different CPU platforms for `arm64`: Ampere Altra (via the "Tau" `T2A` machine type) 
and Google's own Axion (via the `N4A` and `C4A` machine types).

## `64k` page kernels

From Jammy Jellyfish 22.04 onwards, Ubuntu provides two variant kernels to run `arm64`: `linux-gcp` and `linux-gcp-64k`.
"Standard" Ubuntu images on Google Cloud come preinstalled with the default `linux-gcp` kernel (see `rmadison linux-gcp` for details) but
the "accelerator" Ubuntu image line has `linux-gcp-64k`. To see the latest accelerator-based images available, use `gcloud compute images list --project=ubuntu-os-accelerator-images --no-standard-images`.

**N.B:** The `linux-gcp` kernel will work on *both* CPU platforms, but `linux-gcp-64k` *will not* work on `T2A` machine types.

## Changing the installed kernel

Should you wish to swap from the default kernel to the `64k` page variant (or vice versa), run:

```
sudo apt update
sudo apt install linux-gcp-64k
```
after installation a pop-up courtesy of `needrestart` will appear recommending you reboot.
You must reboot the instance for the kernel to properly install:
```
sudo reboot
```

When you log back into the instance, run `uname -a` to confirm the new kernel has indeed installed.

## More information

For more information on the different use cases of these two kernels, see `these docs`_.


.. _`these docs`: https://documentation.ubuntu.com/server/explanation/installation/choosing-between-the-arm64-and-arm64-largemem-installer-options/index.html
