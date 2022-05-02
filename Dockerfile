FROM ubuntu:latest

# Adding server directory to make absolute filepaths consistent across services
WORKDIR /appsentinel

# Copy our code from the current folder to /server inside the container
COPY . /appsentinel

# Install system dependencies
RUN apt-get update
#RUN apt-get upgrade -y
#RUN apt-get install -y python2-minimal python-pip curl python3.6 python3-pip git aapt default-jre mariadb-server
#RUN apt-get install -y python2-minimal
#RUN apt-get install -y curl
#RUN apt-get install -y python3.9
#RUN apt-get install -y python3-pip
#RUN apt-get install -y git
#RUN apt-get install -y aapt
#-RUN apt-get install -y default-jre
RUN apt-get install -y mariadb-server

#RUN mysqld --user=root

# TODO !!! It needs user interaction, automate-it 
# RUN mysql_secure_installation

# Cloning the external tools and install python dependencies
#RUN git clone https://github.com/AndroBugs/AndroBugs_Framework.git ./tools/AndroBugs && \
#git clone https://github.com/clviper/droidstatx.git ./tools/droidstatx && \
#git clone https://github.com/SUPERAndroidAnalyzer/super.git ./tools/super && \
#pip3 install --trusted-host pypi.python.org -r requirements.txt

# Setup tools
#RUN rm ./tools/AndroBugs/androbugs.py && \
#cp extra/androbugs/androbugs.py tools/AndroBugs/androbugs.py && \
#cd tools/droidstatx; python3 install.py; cd ../.. && \
#curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
#ENV PATH="/root/.cargo/bin:${PATH}"
#- RUN (cd tools/super; cargo build --release) IT FREEZES DURING THIS BUILD



#CMD ["python3", "server.py"]

# This is just for testing... no clue if it works or not... needs testing!!!
# ---- START OF TEST
# Install mysql/mariadb database server
# RUN apt install mariadb

# Install the database on the mysql/mariadb server
# RUN mysql -u root -p < sql/scanner.sql
# ---- END OF TEST
# https://stackoverflow.com/questions/47252273/unable-to-build-a-mariadb-base-in-a-dockerfile
# https://github.com/dockerfile/mariadb
# https://linoxide.com/containers/setup-use-mariadb-docker-container/
# https://stackoverflow.com/questions/29420870/install-mysql-in-dockerfile (this seems to be what we want!!!)