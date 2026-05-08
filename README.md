# sarcasm-formater

The sarcasm formatter provides JS, Python, and Bash support for formatting text sArCaStIcAlLy, meaning with alternating lower and upper-case letters, and provides optional parametrization such as choosing the starting case.

# Installation

The script can be run directly from its containing folder (and thus, can simply be installed by downloading or cloning it from here - and adding run permissions):

```bash
git clone https://github.com/TheChymera/sarcasm-formatter.git /your/sarcasm-formatter/directory
cd /your/sarcasm-formatter/directory/bin
chmod +x sarcasm.sh
```

For [Gentoo Linux](http://en.wikipedia.org/wiki/Gentoo_linux) and [Derivatives](http://en.wikipedia.org/wiki/Category:Gentoo_Linux_derivatives), mkstage4 is also available in [Portage](http://en.wikipedia.org/wiki/Portage_(software)) via [the Chymeric Overlay](https://github.com/TheChymera/overlay).
On any Gentoo system, after [having enabled the aforementioned overlay](https://github.com/TheChymera/overlay#install), just run the following command:

```bash
emerge app-backup/sarcasm-formatter
```

# Usage

*If you are running the script from the containing folder (first install method) please make sure you use the `./sarcasm.sh` command instead of just `sarcasm`!*

```bash
# sarcasm how do I use this
"hOw dO i uSe ThiS" written to clipboard.
```

The notification at the end indicates that in addition to presenting the text for manual copy, `sarcasm` will by default place it into your clipboard (xclip or wl-copy, auto-detected).
Though convenient, this also means your clipboard will be overwritten.
This can be disabled via the `-n` parameter.
