# Dotfiles

This repo contains my dotfiles and will be used to track and deploy my development environment across all various distros.

*If you are looking for some reliable and opensource alternatives lookup ansible by RedHat*

## How to use:

```
git clone git@github.com:CyberFlaw/.dotfiles.git && python3 setup.py
```

All the config parameters are controlled via *config.json*. Each json block represents a subdir in the repo, and it will have entries which contains the path to where the symlink is to be created (Default will be *.config*)

The default config will be in a way to suite my personal needs, feel free to modify this and take inspiration from this approach. 

After config is edited the python file should be executed which will parse the json and do the needful. 

```
python3 setup.py
```

In the json file there will be specific blocks for system configration, make sure to update those too. The python script will be made to service for this architecture
