from ..data.rooms import rooms_by_collection;

def fn_get_collection_by_location(location: str):
    for collection, locations in rooms_by_collection.items():
        if location in locations:
            selected_collection = collection
            return selected_collection;
    return None; 