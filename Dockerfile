# Dockerfile

# FROM directive instructing base image to build upon
FROM django

# COPY startup script into known file location in container
ADD . /codetouch
WORKDIR /codetouch
# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]

# done!
