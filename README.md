# Qubes-scripts
Scripts that help with administration and usage of Qubes OS

## qubes3-multi-update
## qubes4-multi-update
Updates multiple template and standalone VMs (and dom0).

    Usage: `qubes4-multi-update [options] [vms-to-be-included ...]`

    Options:
      -h, --help         Show this help message and exit
      -a, --all          Select all updateable VMs
      -l, --available    Select VMs known to have available updates
      -e, --exclude      Exclude from selection; repeat as needed
      -u, --unattended   Non-interactive, supress prompts
      -t, --templates    (Qubes 4) Exclude non-templates
      -t, --trim         (Qubes 3) Trim root volumes
      -s, --shutdown     Shutdown all VMs after updates

On Qubes 3.x the `--shutdown` option can be used with `--trim` to help ensure template trims are successful; Note that Trim is unneeded on Qubes 4. Dom0 is normally ignored unless specified on the command line, and unlike the others dom0 update currently runs in interactive mode (and last). Excludes may also be specified in '/etc/qubes/autoupdate-exclude'.

## configure-sudo-prompt

Restores internal VM security so that authorization is required to gain root access. Auth is in the form of a dom0 popup yes/no prompt requiring the user to hit 'Enter' or 'OK'. Based on Qubes vm-sudo howto. For Debian 9.

## do-snapshot.py
    Usage: cron.d entry in dom0 such as:
```
*/15 * * * * root /usr/local/bin/do-snapshot.py
```

Keeps a rotating collection of Btrfs snapshots for root fs in a /Snapshots folder. Default settings retain four snapshots over a period of about 18-24 hours. Qubes 3.x only.

## halt-vm-by-window
    Usage: add script path to desktop manager hotkey, press hotkey in window of target VM

A simple way to shutdown a Qubes VM associated with the currently active window. Before shutdown, any running instances of Firefox or Thunderbird in that VM will be told to quit; this allows the apps to save their open-tabs state.

