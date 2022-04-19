#!/bin/sh
{{ if eq .chezmoi.os "linux" -}}
#!/bin/sh
sudo add-apt-repository ppa:jonathonf/vim -y
apt-get update
sudo apt-get install -y fzf cargo tmux zsh vim wget

# Install miniconda
if ! conda --version
then
    MINIFORGE_FILE=Miniforge3-Linux-x86_64.sh
    wget https://github.com/conda-forge/miniforge/releases/latest/download/$MINICONDA_FILE
    bash $MINIFORGE_FILE
fi

{{ else if eq .chezmoi.os "darwin" -}}
#!/bin/sh

# Install homebrew if it's not there already.
if ! brew --version
then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew install coreutils wget fzf cargo tmux zsh vim
fi


if ! conda --version
then
    MINIFORGE_FILE=Miniforge3-MacOSX-x86_64.sh
    wget https://github.com/conda-forge/miniforge/releases/latest/download/$MINICONDA_FILE
    bash $MINIFORGE_FILE
fi


{{ end -}}

cargo install bottom du-dust exa duf

sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting  && \
  git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions  && \
  git clone https://github.com/Aloxaf/fzf-tab ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/fzf-tab  && \
  git clone https://github.com/esc/conda-zsh-completion ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/conda-zsh-completion  && \
  mkdir -p "$HOME/.zsh" && git clone https://github.com/sindresorhus/pure.git "$HOME/.zsh/pure"  && \
  git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
