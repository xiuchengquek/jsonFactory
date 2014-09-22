__author__ = 'quek'

from collections import OrderedDict
import json


def generateProteinGeneMap(inputfile):
    protein_gene = {}

    with open(inputfile) as f:
        for line in f:
            line = line.strip()
            fields = line.split('\t')

            if len(fields) == 1:
                pass
            else:
                protein_gene[fields[1]] = fields[0]

    return protein_gene


def generatedArray(filename, lookupDict={}):
    missingGeneID = open('missingGeneID.txt', 'w+')
    return_dict = OrderedDict()

    with open(filename, 'r+') as f:
        for lines in f:
            lines = lines.rstrip()
            fields = lines.split('\t')
            ensp_id = fields[-1]

            try:
                ensg_id = lookupDict[ensp_id]
            except KeyError:
                ensg_id = ""
                missingGeneID.write("%s\n" % ensp_id)

            try:
                return_dict[ensp_id]['_id'] = ensp_id
                return_dict[ensp_id]['ensg_id'] = ensg_id
            except KeyError:
                return_dict[ensp_id] = OrderedDict()
                return_dict[ensp_id]['_id'] = ensp_id
                return_dict[ensp_id]['ensg_id'] = ensg_id

            try:
                return_dict[ensp_id]['pmid'].append(int(fields[0]))
            except KeyError:
                return_dict[ensp_id]['pmid'] = []
                return_dict[ensp_id]['pmid'].append(int(fields[0]))
    return return_dict


def toJsonArray(json_obj):
    return_array = []
    for key, value in json_obj.iteritems():
        return_array.append(value)
    return return_array

if __name__ == "__main__":
    protein_gene = generateProteinGeneMap('ensp_ensg_all.tsv')
    json_array = generatedArray('all_genes2.sorted', protein_gene)
    for key, value in json_array.iteritems():
        print json.dumps(value)
