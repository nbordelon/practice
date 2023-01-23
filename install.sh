#
# install.sh last updated 1-22-23
#

# Fail on any command
set -eux pipefail

# Install ZSH
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Install plug-in manager
sh -c "$(curl -fsSL https://github.com/zsh-users/antigen.git/antigen.zsh)"

# Install plug-ins
(cd ~/.oh-my-zsh/custom/plugins && git clone https://github.com/agkozak/zsh-z.git)
(cd ~/.oh-my-zsh/custom/plugins && git clone https://github.com/zsh-users/zsh-syntax-highlighting)
(cd ~/.oh-my-zsh/custom/plugins && git clone https://github.com/zsh-users/zsh-autosuggestions)
(cd $HOME && git clone https://github.com/junegunn/fzf)
(cd $HOME && git clone https://github.com/junegunn/fzf-git.sh)

# Install theme
(mkdir -p "$HOME/.zsh" && cd "$HOME/.zsh" && git clone https://github.com/sindresorhus/pure.git "$HOME/.zsh/pure")

# Switch the shell
chsh -s $(which zsh)