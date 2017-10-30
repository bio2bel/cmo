# -*- coding: utf-8 -*-

from pybel.constants import ABUNDANCE, NAMESPACE_DOMAIN_OTHER
from pybel_tools.ols_utils import OlsNamespaceOntology

__all__ = [
    'MODULE_NAME',
    'MODULE_DOMAIN',
    'MODULE_FUNCTION',
    'write_belns',
    'deploy_to_arty',
]

MODULE_NAME = 'cmo'
MODULE_DOMAIN = NAMESPACE_DOMAIN_OTHER
MODULE_FUNCTION = ABUNDANCE

ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, MODULE_FUNCTION)

write_belns = ontology.write_namespace
deploy_to_arty = ontology.deploy_namespace
