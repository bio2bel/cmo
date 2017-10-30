# -*- coding: utf-8 -*-

from __future__ import print_function

import logging
import sys

import click


@click.group()
def main():
    """CMO to BEL"""
    logging.basicConfig(level=10, format="%(asctime)s - %(levelname)s - %(message)s")


@main.command()
@click.option('-b', '--ols-base', help="Custom OLS base url")
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout)
def write(ols_base, output):
    """Writes BEL namespace"""
    from pybel_tools.ols_utils import OlsNamespaceOntology
    from bio2bel_cmo.run import MODULE_FUNCTION, MODULE_DOMAIN, MODULE_NAME
    ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, MODULE_FUNCTION, ols_base=ols_base)
    ontology.write_namespace(output)


@main.command()
@click.option('-b', '--ols-base', help="Custom OLS base url")
@click.option('--no-hash-check', is_flag=True)
def deploy(ols_base=None, no_hash_check=False):
    """Deploy to Artifactory"""
    from pybel_tools.ols_utils import OlsNamespaceOntology
    from bio2bel_cmo.run import MODULE_FUNCTION, MODULE_DOMAIN, MODULE_NAME
    ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, MODULE_FUNCTION, ols_base=ols_base)
    success = ontology.deploy(hash_check=(not no_hash_check))
    click.echo('Deployed to {}'.format(success) if success else 'Duplicate not deployed')


if __name__ == '__main__':
    main()
