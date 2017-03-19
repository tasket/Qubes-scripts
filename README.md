# Qubes-scripts
Scripts that help with administration and usage of Qubes OS

## qubes-multi-update
Usage: qubes-multi-update [options] [vms-to-be-included ...]

Options:
  -h, --help   show this help message and exit
  --available  Include templates known to have available updates
  --all        Include all templates
  --trim       Trim root volumes

Updates multiple template and standalone VMs (and dom0). Has options for TRIM-ing after update and selecting based on available update status. Dom0 is normally ignored unless specified on the command line, and unlike the others dom0 update currently runs in interactive mode (and last).

