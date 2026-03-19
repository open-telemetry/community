# How to provision an Oracle bare metal runner

## Overview

This document describes how to provision an Oracle bare metal instance on
Oracle Cloud Infrastructure (OCI).

1. Create the instance
2. Set up the instance
3. Set up GitHub self-hosted runner

## Step 1: Create the instance

1. Log in to the [Oracle Cloud Console](https://www.oracle.com/cloud/sign-in.html)
2. Click the **hamburger menu** (☰) in the top-left corner
3. Select **Compute → Instances**
4. Click **Create Instance**
5. Configure:
   - **Compartment**: Select **github-self-hosted-runners**
   - **Image**: Click **Change Image** → select **Ubuntu** →
     choose **Canonical Ubuntu 24.04**
   - **Shape**: Click **Change Shape** → select **Bare Metal Machine** →
     choose **BM.Standard3.64**
   - **Networking**: Under **Primary VNIC information**:
     1. Change the **VCN compartment** to **OpenTelemetry**
     2. Select VCN **vcn-20240506-1118**
     3. Change the **Subnet compartment** to **OpenTelemetry**
        (this is a separate dropdown from the VCN compartment)
     4. Select subnet **subnet-20240506-1118**
   - **SSH key**: Under **Add SSH keys**, select **Generate a key pair
     for me** and click **Download private key** to download it.
     Store the private key in the SIG Project Infrastructure 1Password vault.
6. Click **Create**

## Step 2: Set up the instance

### Increase the boot volume

The default boot volume (46.6 GB) is not large enough for runner workloads.
Increase it to at least 256 GB:

1. In the [Oracle Cloud Console](https://www.oracle.com/cloud/sign-in.html),
   navigate to the instance details page
2. Under **Resources** (left sidebar), click **Boot volume**
3. Click the boot volume name
4. Click **Edit**
5. Increase **Volume Size (in GB)** to **256** (or larger) and click
   **Save Changes**
6. SSH into the instance and run a rescan so the OS sees the new size:

   ```bash
   sudo dd iflag=direct if=/dev/oracleoci/oraclevda of=/dev/null count=1
   echo "1" | sudo tee /sys/block/sda/device/rescan
   ```

7. Extend the partition and filesystem:

   ```bash
   sudo growpart /dev/sda 1
   sudo resize2fs /dev/sda1
   ```

8. Verify the new size:

   ```bash
   df -h /
   ```

### Install required software

SSH into the instance and install required software:

```bash
ssh ubuntu@<instance-ip>

# Update packages
sudo apt-get update && sudo apt-get upgrade -y

# Install Docker and allow the runner to use it without sudo
sudo apt-get install -y docker.io
sudo usermod -aG docker $USER

# No other tools need to be installed on the host.
# Workloads should use container-based workflows to bring their own dependencies.
# See https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/running-jobs-in-a-container
```

## Step 3: Set up GitHub self-hosted runner

1. Go to the [org runner settings](https://github.com/organizations/open-telemetry/settings/actions/runners)
2. Click **New self-hosted runner**
3. Select **Linux** and **x64**
4. Follow the instructions shown on the page to download, configure, and start
   the runner on the instance
5. When prompted for runner group, enter
   **Oracle Cloud bare metal benchmark runners**
6. When prompted for runner name, enter the runner label
   (e.g., **oracle-bare-metal-64cpu-1024gb-x86-64-ubuntu-24**)
7. When prompted for additional labels, enter the same runner name
   (e.g., **oracle-bare-metal-64cpu-1024gb-x86-64-ubuntu-24**)
8. When prompted for work folder, press **Enter** to accept the default (`_work`)
9. Install and start the runner as a service (instead of using `./run.sh`):

   ```bash
   sudo ./svc.sh install
   sudo ./svc.sh start
   ```

   This ensures the runner starts automatically on reboot.
   See [configuring the self-hosted runner application as a service](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/configuring-the-self-hosted-runner-application-as-a-service).
10. Reboot the instance to verify everything starts automatically:

    ```bash
    sudo reboot
    ```
