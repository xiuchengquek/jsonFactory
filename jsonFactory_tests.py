__author__ = 'quek'


import unittest
from jsonFactory import generatedArray, generateProteinGeneMap

class TestDataFinder(unittest.TestCase):

    def setUp(self):
        self.mock_file ='test_resources/testcase.txt'
        self.obj_dict = generatedArray(self.mock_file)

    def testKeys(self):
        self.assertItemsEqual(self.obj_dict.keys(), ['geneA', 'geneB','geneC'], 'Keys are the same!')

    def testLen(self):
        self.assertEqual(len(self.obj_dict.keys()), 3,"Json len are the same")

    def testContentA(self):
        self.assertItemsEqual(self.obj_dict['geneA']['pmid'], [1000] )

    def testContentB(self):
        self.assertItemsEqual(self.obj_dict['geneB']['pmid'], [1000,1001,1002,1003,1004])

    def testContentC(self):
        self.assertItemsEqual(self.obj_dict['geneC']['pmid'], [1000,1001,1002,1003,1004,1005,1006,1007,1008,1009])

    #def testOutputA(self):


class TestGeneProteinLookup(unittest.TestCase):
    def setUp(self):
        self.mock_file = 'test_resources/testProteinGene.txt'
        self.protein_gene = generateProteinGeneMap(self.mock_file)

    def testKeys(self):
        self.assertItemsEqual(self.protein_gene.keys(), ['ENSP00000000001','ENSP00000000002','ENSP00000000003','ENSP00000000004'])

    def testKeyValue(self):
        keyvalue = []
        for kv in self.protein_gene.iteritems():
            keyvalue.append(kv)

        self.assertItemsEqual(keyvalue, [('ENSP00000000001', 'ENSG00000000001'),
                                         ('ENSP00000000002', 'ENSG00000000002'),
                                         ('ENSP00000000003', 'ENSG00000000003'),
                                         ('ENSP00000000004', 'ENSG00000000003')])

class TestGenePMIDwithLookup(unittest.TestCase):
    def setUp(self):
        self.mock_file ='test_resources/testLookup.txt'
        self.mock_map = 'test_resources/testProteinGene.txt'
        self.protein_gene = generateProteinGeneMap(self.mock_map)
        self.obj_dict = generatedArray(self.mock_file, lookupDict=self.protein_gene)

    def testKeys(self):
        self.assertItemsEqual(self.obj_dict.keys(), ['ENSP00000000001', 'ENSP00000000002','ENSP00000000003', 'ENSPNONOTEXISTS'])

    def testLen(self):
        self.assertEqual(len(self.obj_dict.keys()), 4,"Json len are the same")

    def testContentA(self):
        self.assertItemsEqual(self.obj_dict['ENSP00000000001']['pmid'], [1000])
        self.assertEqual(self.obj_dict['ENSP00000000001']['ensg_id'], 'ENSG00000000001')

    def testContentB(self):
        self.assertItemsEqual(self.obj_dict['ENSP00000000002']['pmid'], [1000,1001,1002,1003,1004])
        self.assertEqual(self.obj_dict['ENSP00000000002']['ensg_id'], 'ENSG00000000002')

    def testContentC(self):
        self.assertItemsEqual(self.obj_dict['ENSP00000000003']['pmid'], [1000,1001,1002,1003,1004,1005,1006,1007,1008,1009])
        self.assertEqual(self.obj_dict['ENSP00000000003']['ensg_id'], 'ENSG00000000003')


    def checkError(self):
        with open('missingGeneID.txt') as f:
            for line in f:
                self.assertEqual(line, 'ENSPNONOTEXISTS\n')




if __name__ == '__main__':
    unittest.main(verbosity=3)


