# sarcasm-formater

The sarcasm formatter provides JS, Python, and Bash support for formatting text sArCaStIcAlLy, meaning with alternating lower and upper-case letters, and provides optional parametrization such as choosing the starting case.
You can see the Bash interface (following the installation on Gentoo) in action, [here](http://chymera.eu/vid/sarcasm.mp4).

# Installation

## On Gentoo

After [enabling the Chymeric Overlay](https://github.com/TheChymera/overlay#install), sarcasm-formatter can be installed (and uninstalled) directly via the package manager:

```console
yourhost # emerge sarcasm-formatter
```

## Python Package Manager (Developers)

Installation via a distribution's package manager is recommended, as it provides better support for administration as well as dependency resolution.
However, for developers, live access to the code as it is being worked on can be very helpful.
This can be obtained via Python's `setuptools`:

```console
git clone git@github.com:Othyem86/sarcasm-formatter.git
cd sarcasm-formatter
echo "export PATH=\$HOME/.local/bin/:\$PATH" >> ~/.bashrc
source ~/.bashrc
python setup.py develop --user
```

If you are getting a `Permission denied (publickey)` error upon trying to clone, you can either:

* [Add an SSH key](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) to your GitHub account.
* Pull via the HTTPS link `git clone https://github.com/IBT-FMI/SAMRI.git`.
