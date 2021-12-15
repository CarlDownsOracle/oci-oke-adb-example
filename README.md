# OKE Example Project

This repository contains simple examples that quickly get up you to speed with 
accessing Autonomous Database in Oracle Cloud Infrastructure resources.

## Docker Desktop

[For Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac)

[For Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

## OCI Autonomous Database

[Create your ATP Instance](https://oracle-base.com/articles/vm/oracle-cloud-autonomous-transaction-processing-atp-create-service)

### Database Wallet

[Connecting to an Autonomous Database on Shared Exadata Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Database/Tasks/adbconnecting.htm)

This is a zip file.  Drop it in the root of this project and unzip it.  The 
directory that you create becomes the $TNS_ADMIN environment variable.

## Oracle Instant Client

You will need Oracle instant client to use the cx_Oracle Python package.
Download and unzip the client libraries from the free Oracle Instant Client “Basic” or “Basic Light” package for your operating system architecture.

[Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client/downloads.html)

### Create developer.oracle.env

    # cx_Oracle has a dependency on instantclient
    ORACLE_HOME={directory where you located your instantclient}
    DYLD_LIBRARY_PATH=$ORACLE_HOME:$DYLD_LIBRARY_PATH
    LD_LIBRARY_PATH=$ORACLE_HOME:$LD_LIBRARY_PATH
    PATH=$ORACLE_HOME:$PATH

## Local Development Environment

### Create developer.env

    DB_USERNAME={ADMIN}
    DB_PASSWORD={password you created@}
    DB_TNS_SERVICE_NAME={see the tnsname.ora file, pick a serbice name}
    TNS_ADMIN={simple name of the wallet directory -- no prefix slash, dot ... nothing}


## Python Library Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install:

    pip install -r requirements.txt

The ox_Oracle package requires Oracle 'instantclient' libraries. 
Here is a detailed discussion around the Python library that uses 
the instant client:

[cx_Oracle](https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html#quick-start-cx-oracle-installation)


## Steps to Deploy Outside of Containers

The primary script to set up your local environment (assumes a virtualenv named 'venv' exists at project root):

    $ source setup-env.sh

Run App Directly:

    $ source start-server.sh

The app exposes port 5000, so hit http://localhost:5000

## Steps to Deploy in Docker

### Build Docker images:

    $ source docker_build.sh

### Run app container locally in Docker:

    $ docker-compose up

## Steps to Deploy in Local Kubernetes

### Deploy secrets Kubernetes cluster:

    $ source k8s-create-env-secret.sh
    $ source k8s-create-wallet-secret.sh

### Deploy app to Kubernetes cluster:

    $ source k8s-deploy-local-service.sh

### Forward the 5000 port:

    $ kubectl port-forward service/enghouse-svc 8080:6000

### Access the site http://localhost:5000

## Steps to Deploy in OKE Kubernetes Cluster

You will need to deploy the images in OCI Registry (OCIR) at this point.

[OCIR How To](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/registry/index.html)

[OCIR Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryprerequisites.htm#Availab)

Note that the docker image full path will change once they are in OCIR varies slightly.

### Deploy app to OCI OKE Kubernetes cluster:

    $ source k8s-deploy-oke-iad-service.sh
    $ source k8s-deploy-oke-phx-service.sh

* Note that the separate shell scripts + deployment manifests
  are there to show the nuanced differences when targeting a
  given region


## Resources

[Oracle Cloud Infrastructure (OCI)](https://www.oracle.com/cloud/)

[cx_Oracle to connect to Autonomous Database](https://www.oracle.com/database/technologies/appdev/python.html)

## Applications


