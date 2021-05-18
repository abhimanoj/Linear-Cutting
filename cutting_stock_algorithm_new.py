import itertools

class ApplyLinearCut(object):
    def __init__(self,  length: int, cuts:list):
            
        #input..
        self.length = length
        self.cuts = sorted(cuts, reverse=True)
        self.final_reult = ApplyLinearCut.run(self)
     
    def core_operation(self, res:list):
        data_list=[]

        for index, items in enumerate(res):
            sum=0

            index_list = {}
            for x in items:
                sum = sum + x

            sub = self.length - sum
            index_list['index'] = index
            index_list['reminder'] = sub
            data_list.append(index_list)

        ascending_order_list = sorted(data_list, key = lambda x: x['reminder'])

        #remove used elements..
        if len(ascending_order_list) > 0:
            for row in res[(ascending_order_list[0])['index']]:
                self.cuts.remove(row)

            return (res[(ascending_order_list[0])['index']])

    def run(self):
        final_reult = []
        """
        -apply sort on cuts 
        Step:1
            -You need to perform p&c on length of cuts
            -example:-len(cuts)--> 20 
                -we need to get all p&c of 0 to 19 elements.
                
        Step:2
            -once you have all p&c you need to perform sum of index values and subtract with length.
            -store the result and print in accending order.. 
            
            
        above steps we need to repeat for row 1 ,2 , 3 so on..

        """
        count = 1
        cut_len = len(self.cuts) 
        
        while(cut_len > 0):
        
            combinations_of_sum=[]
            for i in range(len(self.cuts), 0, -1):
                
                for seq in itertools.combinations(self.cuts, i):
                    if sum(seq) <= self.length:
                        combinations_of_sum.append(seq)
                
            
            no_duplicate=[t for t in (set(tuple(i) for i in combinations_of_sum))]
            res = [list(ele) for ele in no_duplicate]
            res.sort(key = len)
            
        
            if(len(res) <= 0):
                cut_len = -1
            else:
                final_reult.append(ApplyLinearCut.core_operation(self,res))
                cut_len = len(self.cuts)
                
            count += 1

        return final_reult

    def get_data(self):
        self.html = "<table><tbody><tr>Profile<td></td>Size<td></td></tr>"
        index = 0
        for col in self.final_reult:
            index += 1
            for row in col: 
                self.html += "<tr><td>"+str(index)+"</td><td>"+str(row)+"</td></tr>"

        self.html += "</tbody></table>"
        return str(self.html)

    def __str__(self):
        """
        -print final result..
        """ 

        return str(self.final_reult)
 
 
cuts_ = [7,8,6,7,2,3,3,3,4,2,9,5,1]
data = ApplyLinearCut(15, cuts_).final_reult
print(data)

