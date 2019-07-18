# Qubes-scripts
Scripts that help with administration and usage of Qubes OS


## qubes4-multi-update
Updates multiple template and standalone VMs (and dom0).

    Usage: `qubes4-multi-update [options] [vms-to-be-included ...]`

    Options:
      -h, --help         Show this help message and exit
      -a, --all          Select all updateable VMs
      -l, --available    Select VMs known to have available updates
      -e, --exclude      Exclude VM from selection; repeat as needed
      -t, --templates    Exclude non-templates
      -u, --unattended   Non-interactive, supress prompts
      -s, --shutdown     Shutdown all VMs after updates


Excludes may also be specified in '/etc/qubes/autoupdate-exclude'.

Updates will be run for each specified VM even if
some VM updates return an error. Any VMs with errors will be reported at the end.

Dom0 is always skipped unless it is specified on the command line.


## configure-sudo-prompt
Restores internal VM security so that authorization is required to gain root access. Auth is in the form of a dom0 popup yes/no prompt requiring the user to hit 'Enter' or 'OK'. Based on Qubes vm-sudo howto. For Debian 9 VMs. (Caution! Back up your template before using, just in case re-configuration fails.)


## findpref
Dom0: Find all VMs that match a pref value, optionally set new values for them. For example, its a handy way to switch all VMs that are using a particular netvm to a different netvm.

Update 12/20/18: The searchval parameter is now optional; without it all VMs with the pref will be printed.
Also, a 'None' searchval can now match an empty/absent value.

    Usage: `findpref -p prefname [searchval] [newval]`
    
    Options:
      -p, --pref        Specify pref name/key to match (required)
      -e, --exclude     Exclude VM(s) from search result
      -y, --yes         Set values without prompting
          --mtypes      Match VM type(s)

## kde-color.sh
Sets custom window border colors on Qubes KDE. The defaults are muted colors that look nice with both light and dark app color schemes.


## halt-vm-by-window
A simple way to shutdown a Qubes VM associated with the currently active window. Before shutdown, any running instances of Firefox or Thunderbird in that VM will be told to quit; this allows the apps to save their open-tabs state.

    Usage: add script path to dom0 desktop manager hotkey, press hotkey in window of target VM


## system-stats-xen
Displays lmsensors and xentop system stats including temperature, fan speed, VM CPU & memory use in a compact format.

    Usage: run script in a visible dom0 terminal. For example, `gnome-terminal -- system-stats-xen`

---

## Obsolete scripts:

## do-snapshot.py
Keeps a rotating collection of Btrfs snapshots for root fs in a /Snapshots folder. Default settings retain four snapshots over a period of about 18-24 hours. Qubes 3.x only.

    Usage: cron.d entry in dom0 such as:
```
*/15 * * * * root /usr/local/bin/do-snapshot.py
```

## qubes3-multi-update

Run with `--help` to see options. On Qubes 3.x the `--shutdown` option can be used with `--trim` to
help ensure template trims are successful.


---

### Caveat
These scripts come with no warranty expressed or implied... use at your own risk! Also note that downloading programs via https may not protect their integrity in every case, so its a good idea to download with `git clone` and use a `gpg`-based verification procedure like `git log --show-signature -1`.
