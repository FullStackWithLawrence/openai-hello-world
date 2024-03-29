# OpenAI API "Hello World"

[![FullStackWithLawrence](https://a11ybadges.com/badge?text=FullStackWithLawrence&badgeColor=orange&logo=youtube&logoColor=282828)](https://www.youtube.com/@FullStackWithLawrence)<br>
[![OpenAI](https://a11ybadges.com/badge?logo=openai)](https://platform.openai.com/)
[![Docker](https://a11ybadges.com/badge?logo=docker)](https://docs.docker.com/)
[![Python](https://a11ybadges.com/badge?logo=python)](https://www.python.org/)
![Unit Tests](https://github.com/FullStackWithLawrence/openai-hello-world/actions/workflows/testsPython.yml/badge.svg?branch=main)
![GHA pushMain Status](https://img.shields.io/github/actions/workflow/status/FullStackWithLawrence/openai-hello-world/pushMain.yml?branch=main)
![Auto Assign](https://github.com/FullStackwithLawrence/openai-hello-world/actions/workflows/auto-assign.yml/badge.svg)
[![Release Notes](https://img.shields.io/github/release/FullStackWithLawrence/openai-hello-world)](https://github.com/FullStackWithLawrence/openai-hello-world/releases)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![hack.d Lawrence McDaniel](https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)

A Python "Hello World" application that demonstrates the OpenAI API and usage of Docker Compose to containerize your project. This is a command line utility that returns the value "Hello World" in the written language of your choice.

Python code is [located here](./app/)

## Quick Start

1. Setup the application

```console
git clone https://github.com/FullStackWithLawrence/openai-hello-world.git
cd openai-hello-world
make init    # create a virtual environment
```

2. Configure OpenAI API. Find and open the file `.env` in the root folder of the project. Add your OpenAI API key, save and close the file. See [OpenAI API Getting Started](./doc/OPENAI_API_GETTING_STARTED_GUIDE.md) for detailed setup instructions.

3. Run the application

```console
source activate
python -m app.hello_world
```

## OPTIONAL: Docker

This application can also run as a Docker container.

```console
make                # initializes a .env file for OPENAI_API_KEY and DOCKERHUB_ACCESS_TOKEN 
make docker-build   # run Docker compose to containerize your application
make docker-run     # run the application as a Docker container
```

Other Docker commands

```console
make docker-push    # push your Docker container to DockerHub. A DockerHub account and DOCKERHUB_ACCESS_TOKEN is required.
make docker-prune   # prune (permanently delete) all existing data in Docker: containers, images, cache.
```

## Requirements

- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). _pre-installed on Linux and macOS_
- [make](https://gnuwin32.sourceforge.net/packages/make.htm). _pre-installed on Linux and macOS._
- [OpenAI platform API key](https://platform.openai.com/).
  _If you're new to OpenAI API then see [How to Get an OpenAI API Key](./doc/OPENAI_API_GETTING_STARTED_GUIDE.md)_
- [Python 3.11](https://www.python.org/downloads/): for creating virtual environment.
- [Docker](https://docs.docker.com/): the Docker run-time environment for your operating system. Can be installed as a desktop application or as a service (daemon)
- [Docker Compose](https://docs.docker.com/compose/install/): used to create your production container.

## Documentation

Documentation is available here: [Documentation](./doc/)

## Support

To get community support, go to the official [Issues Page](https://github.com/FullStackWithLawrence/openai-hello-world/issues) for this project.

## Good Coding Best Practices

This project demonstrates a wide variety of good coding best practices for managing mission-critical cloud-based micro services in a team environment. Please see this [Code Management Best Practices](./doc/GOOD_CODING_PRACTICE.md) for additional details.

We want to make this project more accessible to students and learners as an instructional tool while not adding undue code review workloads to anyone with merge authority for the project. To this end we've also added several pre-commit code linting and code style enforcement tools, as well as automated procedures for version maintenance of package dependencies, pull request evaluations, and semantic releases.

## Contributing

We welcome contributions! There are a variety of ways for you to get involved, regardless of your background. In addition to Pull requests, this project would benefit from contributors focused on documentation and how-to video content creation, testing, community engagement, and stewards to help us to ensure that we comply with evolving standards for the ethical use of AI.

For developers, please see:

- the [Developer Setup Guide](./doc/CONTRIBUTING.md)
- and these [commit comment guidelines](./doc/SEMANTIC_VERSIONING.md) 😬😬😬 for managing CI rules for automated semantic releases.

You can also contact [Lawrence McDaniel](https://lawrencemcdaniel.com/contact) directly.
