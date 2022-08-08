def create_filters(model, filters):
    filters_list = []
    for filter_name, filter_value in filters.items():
        filters_list.append(getattr(model, filter_name).ilike(f"%{filter_value}%"))
    return filters_list