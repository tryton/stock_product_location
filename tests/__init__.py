# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.stock_product_location.tests.test_stock_product_location import suite  # noqa: E501
except ImportError:
    from .test_stock_product_location import suite

__all__ = ['suite']
