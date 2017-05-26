# Qubes-scripts
Scripts that help with administration and usage of Qubes OS

## qubes-multi-update
    Usage: qubes-multi-update [options] [vms-to-be-included ...]

    Options:
      -h, --help     show this help message and exit
      -l, --available    Include templates known to have available updates
      -a, --all          Include all templates
      -e, --exclude      Exclude from selection; repeat as needed
      -u, --unattended   Non-interactive, supress prompts
      -t, --trim         Trim root volumes
      -s, --shutdown     Shutdown all VMs after updates

Updates multiple template and standalone VMs (and dom0). Has options for TRIM-ing after update and selecting based on available update status. The `--shutdown` option can be used with `--trim` to help ensure template trims are successful. Dom0 is normally ignored unless specified on the command line, and unlike the others dom0 update currently runs in interactive mode (and last).

