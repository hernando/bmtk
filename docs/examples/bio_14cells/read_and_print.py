from bmtk.utils.sonata import File

net = File(data_files='network/v1_nodes.h5',
           data_type_files='network/v1_node_types.csv')

nodes = net.nodes['v1']
node = nodes.get_node_id(0)
print(node['orientation'])
node = nodes.get_node_id(1)
print(node['orientation'])

