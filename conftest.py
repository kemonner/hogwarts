# import pytest
#
#
# def pytest_collection_modifyitems(session, config, items):
#     # print(items)
#     # print(type(items))
#     for item in items:
#         if 'add' in item.nodeid:
#             item.add_marker(add)
#
#         elif 'div' in item.nodeid:
#             item.add_marker(pytest.mark.div)
