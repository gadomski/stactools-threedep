from pystac import Item

from stactools.threedep.metadata import Metadata


def create_item(product: str, id: str, base: str = None) -> Item:
    """Creates a STAC item from a product (e.g. "1") and an ID (e.g. "n41w106")."""
    metadata = Metadata.from_product_and_id(product, id)
    return metadata.to_item(base)