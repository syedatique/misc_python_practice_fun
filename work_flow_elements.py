import json
work_flow_data = {"type":"bpmn","cells":[{"type":"bpmn.Validator","size":{"width":70,"height":70},"activityType":"Length","activityType2":">","activityType3":"8","position":{"x":670,"y":970},"angle":0,"id":"9f7720a0-f5f1-46f2-a51a-a29d10b9d930","embeds":"","z":3,"attrs":{".label":{"text":"Length> 8"}}},{"type":"bpmn.Event","size":{"width":70,"height":70},"eventType":"start","position":{"x":320,"y":980},"angle":0,"id":"d68eef78-a8f6-40eb-9878-dbedaf501162","embeds":"","z":8,"attrs":{".inner":{"visibility":"hidden"}}},{"type":"bpmn.ImportExport","size":{"width":70,"height":46.66666666666667,"rx":8,"ry":8},"activityType":"Import","activityType2":"EbayPlugin","activityType3":"--","position":{"x":500,"y":980},"angle":0,"id":"0b9a9612-2eea-49af-8bd6-3a7ea71e49e9","embeds":"","z":10,"attrs":{".label":{"text":"Import EbayPlugin"},"image":{"xlink:href":""}}},{"type":"bpmn.Flow","label":"--","flowType":"normal","id":"9dc4cafc-37f2-4a2a-96cc-e5dfd1806fc3","labels":[{"position":0.2,"attrs":{"text":{"fill":"blue","text":""}}}],"embeds":"","source":{"id":"d68eef78-a8f6-40eb-9878-dbedaf501162"},"target":{"id":"0b9a9612-2eea-49af-8bd6-3a7ea71e49e9"},"z":11,"attrs":{}},{"type":"bpmn.Flow","label":"--","flowType":"normal","id":"e9b3be98-77cd-4c4f-b746-9121d2133002","labels":[{"position":0.2,"attrs":{"text":{"fill":"blue","text":""}}}],"embeds":"","source":{"id":"0b9a9612-2eea-49af-8bd6-3a7ea71e49e9"},"target":{"id":"9f7720a0-f5f1-46f2-a51a-a29d10b9d930"},"z":12,"attrs":{}},{"type":"bpmn.Operator","size":{"width":70,"height":70},"activityType":"Truncate","activityType2":"--","activityType3":"--","position":{"x":870,"y":770},"angle":0,"id":"ebb888e1-7d02-4019-84e2-829d7c020224","embeds":"","z":13,"attrs":{".label":{"text":"Truncation"}}},{"type":"bpmn.Flow","label":"False","flowType":"normal","id":"9200d073-c7dc-4b4c-87f1-8cd9b48229c0","labels":[{"position":0.2,"attrs":{"text":{"fill":"blue","text":"False"},"rect":{"fill":"white"}}}],"embeds":"","source":{"id":"9f7720a0-f5f1-46f2-a51a-a29d10b9d930"},"target":{"id":"ebb888e1-7d02-4019-84e2-829d7c020224"},"z":14,"vertices":[{"x":700,"y":810}],"attrs":{}},{"type":"bpmn.Validator","size":{"width":70,"height":70},"activityType":"Length","activityType2":"=","activityType3":"8","position":{"x":1060,"y":960},"angle":0,"id":"04cd2ab0-ef51-466a-b21e-8a0b07535fae","embeds":"","z":15,"attrs":{".label":{"text":"Length= 8"}}},{"type":"bpmn.Flow","label":"True","flowType":"normal","id":"35f4b42c-0f1f-4900-bd39-4d5c0a755a87","labels":[{"position":0.2,"attrs":{"text":{"fill":"blue","text":"True"},"rect":{"fill":"white"}}}],"embeds":"","source":{"id":"9f7720a0-f5f1-46f2-a51a-a29d10b9d930"},"target":{"id":"04cd2ab0-ef51-466a-b21e-8a0b07535fae"},"z":16,"vertices":[{"x":700,"y":1140},{"x":1100,"y":1140}],"attrs":{}},{"type":"bpmn.Flow","label":"--","flowType":"normal","id":"5e9da660-a955-4afc-9f05-bbda7b9e7a28","labels":[{"position":0.2,"attrs":{"text":{"fill":"blue","text":""}}}],"embeds":"","source":{"id":"ebb888e1-7d02-4019-84e2-829d7c020224"},"target":{"id":"04cd2ab0-ef51-466a-b21e-8a0b07535fae"},"z":17,"vertices":[{"x":1100,"y":810}],"attrs":{}},{"type":"bpmn.ImportExport","size":{"width":70,"height":46.66666666666667,"rx":8,"ry":8},"activityType":"Export","activityType2":"NetSuitePlugin","activityType3":"--","position":{"x":1260,"y":970},"angle":0,"id":"73cec919-5715-44d5-b09e-560daaad8fb6","embeds":"","z":20,"attrs":{".label":{"text":"Export NetSuitePlugin"},"image":{"xlink:href":""}}},{"type":"bpmn.Flow","label":"--","flowType":"normal","id":"9d80d25a-7dc9-4a48-81b5-736081e51ca9","labels":[{"position":0.2,"attrs":{"text":{"fill":"blue","text":""}}}],"embeds":"","source":{"id":"04cd2ab0-ef51-466a-b21e-8a0b07535fae"},"target":{"id":"73cec919-5715-44d5-b09e-560daaad8fb6"},"z":21,"attrs":{}}]};
# work_flow_data = json.loads(work_flow_data);

# len(j_data['cells']) --> 12

validator_list = []
operator_list = []
impexp_list = []
link_list = []

for item in work_flow_data['cells']:
	if item['type'] == 'bpmn.Validator':
		validator_dict = {}
		validator_dict['id'] = item['id']
		validator_dict['activityType'] = item['activityType']
		validator_dict['activityType2'] = item['activityType2']
		validator_dict['activityType3'] = item['activityType3']
		validator_list.append(validator_dict)
		# print ('validator: %s' %validator_list)
	elif item['type'] == 'bpmn.Operator':
		operator_dict = {}
		operator_dict['id'] = item['id']
		operator_dict['activityType'] = item['activityType']
		operator_list.append(operator_dict)
		# print operator_list
	elif item['type'] == 'bpmn.ImportExport':
		impexp_dict = {}
		impexp_dict['id'] = item['id']
		impexp_dict['activityType'] = item['activityType']
		impexp_dict['activityType2'] = item['activityType2']
		impexp_list.append(impexp_dict)
		# print impexp_list
	elif item['type'] == 'bpmn.Flow':
		link_dict = {}
		link_dict['id'] = item['id']
		link_dict['label'] = item['label']
		link_dict['source_id'] = item['source']['id']
		link_dict['target_id'] = item['target']['id']
		link_list.append(link_dict)
		# print link_list
	else:
		print 'test'

# print ('validator: %s' %validator_list)
# print ('operator: %s' %operator_list)
# print ('link: %s' %link_list)
# print ('impexp: %s' %impexp_list)

# Import data OR Export Data??
for item in impexp_list:
	if item['activityType']== 'Import':
		impexp_import = item
	else:
		impexp_export = item

print ('ImportExport: %s' %impexp_import)
# print impexp_export

# Check Validator
for item in link_list:
	if (item['source_id'] == validator_list[0]['id']) and (item['label']== 'True') and (item['target_id'] == validator_list[1]['id']):
		link_start_validator_operator = item
		print ('path between 1st validator and 2nd validator: %s' %link_start_validator_operator)
	elif (item['source_id'] == validator_list[1]['id']) and (item['label']== 'True') and (item['target_id'] == validator_list[1]['id']):
		link_start_validator_operator = item
		print ('path between 1st validator and 2nd validator: %s' %link_start_validator_operator)
	elif (item['source_id'] == operator_list[0]['id']) and (item['target_id']== validator_list[0]['id']) and (item['label']== '--'):
		link_end_operator_validator = item
		print ('path between operator and 2nd validator: %s' %link_end_operator_validator)
	elif (item['source_id'] == operator_list[0]['id']) and (item['target_id']== validator_list[1]['id']) and (item['label']== '--'):
		link_end_operator_validator = item
		print ('path between operator and 2nd validator: %s' %link_end_operator_validator)
	elif item['label'] == 'False':
		link_start_validator_operator = item
		print 'path between 1st validator and operator: ', link_start_validator_operator
	else:
		print 'testing'




