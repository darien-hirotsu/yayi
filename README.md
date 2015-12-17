# yayi: yet another yaml introduction
## Overview
This project is for users who are new to YAML and are looking to build some basic knowledge to start producing YAML files. The goal is to start leveraging cool tools such as [Ansible](http://docs.ansible.com/ansible/index.html) , [Salt](https://docs.saltstack.com/en/latest/), [Heat](https://wiki.openstack.org/wiki/Heat), and many more without having to learn the full suite of YAML syntax. This project highlights the basics to get up and running quickly!

The project includes some basic YAML files to illustrate the basic data structures. The YAML examples are accompanied by a simple Python script that allows the user to see how the relevant YAML is serialized to Python data types. Some basic Python knowledge will definitely help. :)

Note that most tools (such as Ansible and the others previously mentioned) only leverage a subset of the YAML syntax. Again, this project focuses on the useful items to get up and running fast!

## Installation
* git clone https://github.com/darien-hirotsu/yayi.git

## How to Use this Project
1. Start by reviewing a sample YAML file with an editor of your choice
	* Atom, Eclipse, and SublimeText all provide syntax highlighting
2. Run the Python script and pass the reviewed YAML file as an argument
3. See how YAML syntax maps to Python data types

## Running
* python show_me_the_yaml.py 1_mapping.yml

* python show_me_the_yaml.py 2_sequence.yml

* python show_me_the_yaml.py 3_mappings.yml

* python show_me_the_yaml.py 4_sequences.yml

* python show_me_the_yaml.py 5_scalars.yml

## Useful References
* [YAML Specification](https://wiki.openstack.org/wiki/Heat)#
