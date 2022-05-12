FROM rockylinux/rockylinux:latest
RUN dnf install 'dnf-command(config-manager)'
RUN dnf config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
RUN dnf install gh
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null
RUN apt update
RUN dnf update -y
RUN dnf install -y python3
RUN dnf install -y jq
RUN dnf install -y python3-pip python3-wheel
#RUN python3 --version
#RUN apt-get install python3
run python3 --version
run pip3 freeze
run python3 -m venv python3-virtualenv
